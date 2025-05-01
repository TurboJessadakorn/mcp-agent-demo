import asyncio

from agents import Agent, Runner
from agents.mcp import MCPServerStdio, MCPServerSse
from dotenv import load_dotenv
import os

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

def connect_github():
    return MCPServerStdio(
        name="GitHub MCP",
        params={
            "command": "npx",
            "args": [
                "-y",
                "@modelcontextprotocol/server-github"
            ],
            "env": {
                "GITHUB_PERSONAL_ACCESS_TOKEN": os.environ.get("GITHUB_TOKEN")
            }
        }
    )

async def agent(message: str):
    print("Connecting to mcp server!")
    async with connect_github() as mcp_server:
        print("Initializing agent")
        agent = Agent(
            name="Assistant",
            instructions="""
            You are a Github helper. Your task is to answer user question about GitHub with the information you retieve from the tools.
            """,
            mcp_servers=[mcp_server],
            model="gpt-4o-mini"
        )

        print(f"Running: {message}")
        result = await Runner.run(starting_agent=agent, input=message)
        return result.final_output
    
async def run():
    message = "Detail of the repo mcp-agent-demo"
    result = await agent(message)
    print(result)

async def main():
    while True:
        user_input = input("USER: ")
        
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Exiting the conversation.")
            break
        
        try:
            bot_message = await agent(user_input)
            print(f"AGENT: {bot_message}")
        except Exception as e:
            print(f"AGENT: An error occurred: {e}")


if __name__ == "__main__":
    asyncio.run(main())