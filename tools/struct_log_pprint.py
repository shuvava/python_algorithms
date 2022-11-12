#!/usr/bin/env python3
# encoding: utf-8
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  Copyright (c) 2022 Vladimir Shurygin. All rights reserved.
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import fileinput
import json

if __name__ == '__main__':
    for line in fileinput.input(encoding="utf-8"):
        try:
            r = json.loads(line)
            if r is not None:
                print(json.dumps(r, indent=2, sort_keys=True))
        except Exception:
            continue
