import asyncio

from agents import Agent, Runner
from agents.mcp import MCPServerStdio, MCPServerSse
from dotenv import load_dotenv

load_dotenv(override=True)

def connect_stdio():
    return MCPServerStdio(
        name="Stdio Server",
        params={"command": "python", "args": ["server.py"]}
    )

def connect_sse():
    return MCPServerSse(
        name="SSE Server",
        params={"url": "http://localhost:8080/sse"}
    )

async def agent(message: str):
    print("Connecting to mcp server!")
    async with connect_sse() as mcp_server:
        print("Initializing agent")
        agent = Agent(
            name="Assistant",
            instructions="""
            You are a math calculator. You need to help user find the sum of 2 number. 
            However, the method used to find the sum is special. So, you must use the tool to find the answer.
            """,
            mcp_servers=[mcp_server],
            model="gpt-4o-mini"
        )

        print(f"Running: {message}")
        result = await Runner.run(starting_agent=agent, input=message)
        return result.final_output
    
async def run():
    message = "The number are 3 and 4"
    result = await agent(message)
    print(result)


if __name__ == "__main__":
    asyncio.run(run())