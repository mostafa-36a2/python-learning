#!/usr/bin/env python3
# countasync.py
# https://realpython.com/async-io-python/
import asyncio


async def for_loop():
    for i in range(1, 10, 2):
        print(i)


async def for_loop2():
    for i in range(0, 10, 2):
        print(i)


# async def count(arg):
#     print("One")
#     await asyncio.to_thread(print)


async def main():
    # await asyncio.gather(count(12), count(33), count(44))
    await asyncio.gather(for_loop(), for_loop2())
    # name = input("Please enter your name: ")
    # print(f"Hello {name}")


if __name__ == "__main__":
    # simport time

    # s = time.perf_counter()
    asyncio.run(main())
    # elapsed = time.perf_counter() - s
    # print(f"{__file__} executed in {elapsed:0.2f} seconds.")
