from agents import Agent, Runner
from agents.mcp import MCPServer, MCPServerStdio
from dotenv import load_dotenv

load_dotenv(override=True)


async def run(mcp_server: MCPServer):
    messages = []
    agent = Agent(
        name="welcome",
        model="gpt-4o-mini",
        instructions="""
        You are a helpful assistant.
        Your job is to answer the user query.
        
        IMPORTANT :
        - You are only allowed to use tools when necessary.
        - Do not answer anything that is not related to the linkedin profile.
        - If user asking about something outside linkedin profile, say that you can not help.
        """,
        mcp_servers=[mcp_server],
    )

    is_run = True
    while is_run:
        query = input("Query: ")
        if query == "exit":
            is_run = False
            break

        messages.append({"role": "user", "content": query})
        response = await Runner.run(agent, input=messages)
        messages = response.to_input_list()

        print(f"Answer: {response.final_output}")


async def main():
    async with MCPServerStdio(
        params={
            "command": "mcp-proxy",
            "args": ["http://localhost:8000/mcp"],
        }
    ) as server:
        await run(server)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
