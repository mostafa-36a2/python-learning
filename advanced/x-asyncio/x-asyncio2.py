import asyncio


async def get_user_input():
    # Use asyncio.to_thread to run synchronous code (input) in a separate thread
    user_input = await asyncio.to_thread(input, "Enter something: ")
    print(f"You entered: {user_input}")


async def main():
    print("Waiting for user input...")
    await get_user_input()
    print("Done!")


# Run the asynchronous event loop
if __name__ == "__main__":
    asyncio.run(main())
    print("Hi Aziz")
    print("Hi Zed")
