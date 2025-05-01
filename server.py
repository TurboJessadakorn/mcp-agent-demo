from fastmcp import FastMCP, Client

mcp = FastMCP(
    name="My First MCP Server",
    port=8080,
    host="127.0.0.1"
)

@mcp.tool()
def sum(a: int, b: int) -> int:
    """Find sum of 2 numbers"""
    return a + b + b + b

if __name__ == "__main__":
    print("FastMCP server running!")
    mcp.run()
