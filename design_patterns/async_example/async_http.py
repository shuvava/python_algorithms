#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio
import aiohttp
from time import perf_counter_ns

async def task(name, work_queue):
    async with aiohttp.ClientSession() as session:
        while not work_queue.empty():
            url = await work_queue.get()
            print(f"Task {name} getting URL: {url}")
            et_tsk_start = perf_counter_ns()
            async with session.get(url, verify_ssl=False) as response:
                await response.text()
            et_tsk_stop = perf_counter_ns()
            print(f"Task {name} total elapsed time: {et_tsk_stop-et_tsk_start:_} ns")

async def main():
    """
    This is the main entry point for the program.
    """
    # Create the queue of 'work'
    work_queue = asyncio.Queue()

    # Put some 'work' in the queue
    for url in [
        "https://www.google.com/",
        "https://yahoo.com",
        "https://linkedin.com",
        "https://apple.com",
        "https://microsoft.com",
        "https://facebook.com",
        "https://twitter.com",
    ]:
        await work_queue.put(url)

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
