# -*- coding: utf-8 -*-
from bit_oprs_helper import get_table_size, get_mask, \
        is_shifted, is_continuation, is_occupied, \
        is_empty, isElementClusterStart, isElementRunStart, \
        is_shifted_set, is_occupied_set, is_continuation_set, \
        is_occupied_clear, is_shifted_clear, is_continuation_clear, \
        get_remainder, \
        numberOfTrailingZeros, highestOneBit, bit_count


class QuotientFilter:
    def __init__(self, quotient_bits, remainder_bits, hash_fn):
        self.QUOTIENT_BITS = quotient_bits
        self.REMAINDER_BITS = remainder_bits
        self.ELEMENT_BITS = self.REMAINDER_BITS + 3

        self.INDEX_MASK = get_mask(quotient_bits)
        self.REMAINDER_MASK = get_mask(remainder_bits)
        self.ELEMENT_MASK = get_mask(self.ELEMENT_BITS)

        self.MAX_SIZE = 1 << self.QUOTIENT_BITS
        self.MAX_INSERTIONS = int(self.MAX_SIZE * 0.75)
        self.entries = 0
        # iterator properties
        self.visited = 0
        self.index = 0
        self.quotient = 0

        self.hash_fn = hash_fn
        size = get_table_size(quotient_bits, remainder_bits)
        self.table = [0] * size # array of unsigned integers
        self.overflowed = False

    def __getitem__(self, key):
        '''Return QF[idx] in the lower bits.
        '''
        elt = 0
        bitpos = self.ELEMENT_BITS * key
        tabpos = bitpos // 64
        slotpos = bitpos % 64
        spillbits = (slotpos + self.ELEMENT_BITS) - 64
        elt = (self.table[tabpos] >> slotpos) & self.ELEMENT_MASK
        if spillbits > 0:
            tabpos += 1
            x = self.table[tabpos] & get_mask(spillbits)
            elt |= x << (self.ELEMENT_BITS - spillbits)
        return elt

    def __setitem__(self, key, elt):
        '''
        Store the lower bits of elt into QF[idx].
        '''
        bitpos = self.ELEMENT_BITS * key
        tabpos = bitpos // 64
        slotpos = bitpos % 64
        spillbits = (slotpos + self.ELEMENT_BITS) - 64
        elt &= self.ELEMENT_MASK
        self.table[tabpos] &= ~(self.ELEMENT_MASK << slotpos)
        self.table[tabpos] |= elt << slotpos
        if (spillbits > 0):
            tabpos += 1
            self.table[tabpos] &= ~get_mask(spillbits)
            self.table[tabpos] |= elt >> (self.ELEMENT_BITS - spillbits)

    def __iter__(self):
        # Mark the iterator as done.
        self.visited = self.entries
        if self.entries == 0:
            return self
        for start in range(self.MAX_SIZE):
            if isElementClusterStart(self[start]):
                break
        self.visited = 0
        self.index = start
        return self

    def __next__(self):
        while self.entries != self.visited:
            elt = self[self.index]
            #Keep track of the current run.
            if isElementClusterStart(elt):
                self.quotient = self.index
            elif isElementRunStart(elt):
                quot = self.quotient
                do = True
                while do:
                    quot = self.inc_index(quot)
                    do = not is_occupied(self[quot])
                self.quotient = quot
            self.index = self.inc_index(self.index)
            if not is_empty(elt):
                quot = self.quotient
                rem = get_remainder(elt)
                _hash = (quot << self.REMAINDER_BITS) | rem
                self.visited += 1
                return _hash
        raise StopIteration()



    def inc_index(self, inx):
        return (inx + 1) & self.INDEX_MASK

    def dec_index(self, inx):
        return (inx - 1) & self.INDEX_MASK

    def hash_to_quotient(self, val):
        return (val >> self.REMAINDER_BITS) & self.INDEX_MASK

    def hash_to_remainder(self, val):
        return val & self.REMAINDER_MASK

    def find_run_Index(self, fq):
        '''
        Find the start index of the run for fq (given that the run exists)
        '''
        # Find the start of the cluster.
        b= fq
        while is_shifted(self[b]):
            b= self.dec_index(b)
        # Find the start of the run for fq
        s = b
        while b != fq:
            s = self.inc_index(s)
            while is_continuation(self[s]):
                s = self.inc_index(s)
            b = self.inc_index(b)
            while not is_occupied(self[b]):
                b = self.inc_index(b)
        return s

    def insert_into(self, s, elt):
        curr = elt
        do = True
        while do:
            prev = self[s]
            empty = is_empty(prev)
            if not empty:# Fix up `is_shifted' and `is_occupied'.
                prev = is_shifted_set(prev)
                if is_occupied(prev):
                    curr = is_occupied_set(curr)
                    prev = is_occupied_clear(prev)
            self[s]=curr
            curr = prev
            s = self.inc_index(s)
            do = not empty

    def insert(self, val, hashed=False):
        if self.entries >= self.MAX_INSERTIONS or self.overflowed:
            # Can't safely process an after overflow
            # Only a buggy program would attempt it
            if self.overflowed:
                raise OverflowError
            #Can still resize if we have enough remainder bits
            if self.REMAINDER_BITS > 1:
                self.double_size()
            else:
                self.overflowed = True
                raise OverflowError
        if hashed:
            _hash = val
        else:
            _hash = self.hash_fn(val)
        fq = self.hash_to_quotient(_hash)
        fr = self.hash_to_remainder(_hash)
        T_fq = self[fq]
        entry = (fr << 3) & ~7
        #Special-case filling canonical slots to simplify insert_into()
        if is_empty(T_fq):
            entry = is_occupied_set(entry)
            self[fq] = entry
            self.entries += 1
            return
        if not is_occupied(T_fq):
            self[fq] = is_occupied_set(T_fq)

        start = self.find_run_Index(fq)
        s = start
        if is_occupied(T_fq):
            do = True
            while do:
                rem = get_remainder(self[s])
                if rem >= fr:
                    break
                s = self.inc_index(s)
                do = is_continuation(self[s])

            if s == start: # The old start-of-run becomes a continuation.
                old_head = self[start]
                old_head = is_continuation_set(old_head)
                self[start] = old_head
            else: # The new element becomes a continuation.
                entry = is_continuation_set(entry)
        #Set the shifted bit if we can't use the canonical slot.
        if s != fq:
            entry = is_shifted_set(entry)

        self.insert_into(s, entry)
        self.entries += 1

    def __contains__(self, val):
        if self.overflowed:
            # Can't check for existence after overflow occurred
            # and things are missing
            raise OverflowError
        _hash = self.hash_fn(val)
        fq = self.hash_to_quotient(_hash)
        fr = self.hash_to_remainder(_hash)
        T_fq = self[fq]
        # If this quotient has no run, give up.
        if is_empty(T_fq):
            return False
        # Scan the sorted run for the target remainder.
        s = self.find_run_Index(fq)
        do = True
        while do:
            rem = get_remainder(self[s])
            if rem == fr:
                return True
            if rem > fr:
                return False
            s = self.inc_index(s)
            do = is_continuation(self[s])
        return False

    def __len__(self):
        return self.entries

    def __del_entry(self, s, quot):
        '''
        Remove the entry in QF[s] and slide the rest of the cluster forward.
        '''
        orig = s
        curr = self[s]
        sp = self.inc_index(s)
        while True:
            _next = self[sp]
            curr_occupied = is_occupied(curr)
            if is_empty(_next) or isElementClusterStart(_next) or sp == orig:
                self[s] = 0
                return
            # Fix entries which slide into canonical slots.
            updated_next = _next
            if isElementRunStart(_next):
                do = True
                while do:
                    quot = self.inc_index(quot)
                    do = not is_occupied(self[quot])
                if curr_occupied and quot == s:
                    updated_next = is_shifted_clear(_next)
                self[s] = is_occupied_set(updated_next) if curr_occupied else is_occupied_clear(updated_next)
                s = sp
                sp = self.inc_index(sp)
                curr = _next

    def __delitem__(self, val):
        if self.overflowed:
            #Can't safely process a remove after overflow
            #Only a buggy program would attempt it
            raise OverflowError
        _hash = self.hash_fn(val)
        fq = self.hash_to_quotient(_hash)
        fr = self.hash_to_remainder(_hash)
        T_fq = self[fq]
        if self.entries == 0 or not is_occupied(T_fq  ):
            #If you remove things that don't exist it's possible you will clobber
            #somethign on a collision, your program is buggy
            raise KeyError('Element not exist')
        start = self.find_run_Index(fq)
        s = start
        #Find the offending table index (or give up)
        do = True
        while do:
            rem = get_remainder(self[s])
            if rem == fr:
                break
            elif rem > fr:
                return
            s = self.inc_index(s)
            do = is_continuation(self[s])
        if rem != fr:
            #If you remove things that don't exist it's possible you will clobber
            #somethign on a collision, your program is buggy
            raise KeyError('Element not exist')
        kill = T_fq if s == fq else self[s]
        replace_run_start = isElementRunStart(kill)
        #If we're deleting the last entry in a run, clear `is_occupied'.
        if replace_run_start:
            _next = self[self.inc_index(s)]
            if not is_continuation(_next):
                T_fq = is_occupied_clear(T_fq)
                self[fq] = T_fq
        self.__del_entry(s, fq)
        if replace_run_start:
            _next = self[s]
            updated_next = _next
            if is_continuation(_next):# The new start-of-run is no longer a continuation.
                updated_next = is_continuation_clear(updated_next)
            if s == fq and isElementRunStart(updated_next):
                # The new start-of-run is in the canonical slot.
                updated_next = is_shifted_clear(updated_next)
            if updated_next != _next:
                self[s] = updated_next
        self.entries -= 1

    def __bitsForNumElementsWithLoadFactor(self, numElements):
        if numElements == 0:
            return 1
        if bit_count(numElements) == 1:
            candidate_bits = max(1, numberOfTrailingZeros(numElements))
        else:
            candidate_bits = numberOfTrailingZeros(highestOneBit(numElements) << 1)
        # May need an extra bit due to load factor
        if 0.75*2**candidate_bits < candidate_bits:
            candidate_bits += 1
        return candidate_bits


    def __resize(self, minimumEntries):
        if minimumEntries<= self.MAX_INSERTIONS:
            return self
        newQuotientBits = self.__bitsForNumElementsWithLoadFactor(minimumEntries)
        newRemainderBits = self.QUOTIENT_BITS + self.REMAINDER_BITS - newQuotientBits
        if newRemainderBits < 1:
            raise ValueError("Not enough fingerprint bits to resize")
        qf = QuotientFilter(newQuotientBits, newRemainderBits, self.hash_fn)
        for elt in self:
            qf.insert(elt, hashed=True)
        return qf


    def double_size(self):
        qf = self.__resize(self.MAX_INSERTIONS*2)
        if qf.entries != self.entries:
            raise AssertionError()
        self.QUOTIENT_BITS = qf.QUOTIENT_BITS
        self.REMAINDER_BITS = qf.REMAINDER_BITS
        self.ELEMENT_BITS = qf.ELEMENT_BITS
        self.INDEX_MASK = qf.INDEX_MASK
        self.REMAINDER_MASK = qf.REMAINDER_MASK
        self.ELEMENT_MASK = qf.ELEMENT_MASK
        self.MAX_SIZE = qf.MAX_SIZE
        self.MAX_INSERTIONS = qf.MAX_INSERTIONS
        self.table = qf.table
        pass
