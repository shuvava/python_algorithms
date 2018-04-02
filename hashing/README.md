# Hashing

## Common definitions

### Load factor

let n  = Number of keys stored in table
m = number slots in table
    => load factor (alfa) = n/m <=> average number keys per slot

## Hash Function division method

    h(k) = k mod m
* k1 and k2 collide when k1 = k2( mod m) i. e. when m divides | k1 − k2 |
* fine if keys you store are uniform random
* but if keys are x, 2x, 3x, . . . (regularity) and x and m have common divisor d then use only 1/d of table. This is likely if m has a small divisor e. g. 2.
* if m = 2r then only look at r bits of key

Good Practice: A good practice to avoid common regularities in keys is to make m a prime number that is not close to power of 2 or 10

## Hash Function Multiplication Method

    h(k) = [(a * k) mod 2^w] >> (w − r)
    where m = 2^r and w-bit machine words and a = odd integer between 2*(w − 1) and 2w

Good Practise: a not too close to 2^(w−1) or 2^w.

## Hash Function Universal Hashing

    h(k) = [(a*k+b) mod p] mod m
    where a and b are random ∈ {0, 1, . . . p−1}, and p is a large prime (> |U|).