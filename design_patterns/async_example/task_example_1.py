#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
async example
"""
import asyncio
import queue
from time import perf_counter_ns


async def task(name, work_queue):
    while not work_queue.empty():
        delay = await work_queue.get()
        et_tsk_start = perf_counter_ns()
        print(f"Task {name} running")
        await asyncio.sleep(delay)
        et_tsk_stop = perf_counter_ns()
        print(f"Task {name} total elapsed time: {et_tsk_stop-et_tsk_start:_} ns")


async def main():
    """
    This is the main entry point for the program.
    """
    # Create the queue of 'work'
    work_queue = asyncio.Queue()

    # Put some 'work' in the queue
    for work in [15, 10, 5, 2]:
        await work_queue.put(work)

    # Run the tasks
    et_start = perf_counter_ns()
    await asyncio.gather(
        asyncio.create_task(task("One", work_queue)),
        asyncio.create_task(task("Two", work_queue)),
    )
    et_stop = perf_counter_ns()
    print(f"\nTotal elapsed time: {et_stop-et_start:_} ns")

if __name__ == "__main__":
    asyncio.run(main())
