# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  Copyright (c) 2026 Vladimir Shurygin. All rights reserved.
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
The Leaky Bucket algorithm is a rate-limiting algorithm used to control traffic flow.
It processes requests at a fixed rate, regardless of incoming burst size.

Concept

The bucket has:
* Capacity (maximum number of requests it can hold)
* Leak rate (requests processed per second)

Incoming requests:
* Added if bucket is not full
* Dropped if bucket is full

Requests leave the bucket at a constant rate
"""

import threading
import time


class LeakyBucket:
    def __init__(self, capacity: int, leak_rate: float):
        """
        :param capacity: Maximum number of requests the bucket can hold
        :param leak_rate: Requests per second allowed to leak
        """
        self.capacity = capacity
        self.leak_rate = leak_rate
        self._water = 0.0
        self._last_check = time.monotonic()
        self._lock = threading.Lock()

    def _leak(self):
        now = time.monotonic()
        elapsed = now - self._last_check
        leaked = elapsed * self.leak_rate

        self._water = max(0.0, self._water - leaked)
        self._last_check = now

    def allow_request(self, tokens: int = 1) -> bool:
        with self._lock:
            self._leak()

            if self._water + tokens <= self.capacity:
                self._water += tokens
                return True

            return False
