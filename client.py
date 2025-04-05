from dotenv import load_dotenv
from agents import Agent, Runner
from agents.mcp import MCPServerStdio, MCPServer

load_dotenv(override=True)


async def run(mcp_server: MCPServer):
    agent = Agent(name="agent", instructions="Use the tools to get linkedin profile", mcp_servers=[mcp_server])
    result = await Runner.run(agent, "Summarize me profile of pauliusztin, and then give me his email address",)
    print(result.final_output)

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