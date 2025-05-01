# MCP Agent Demo

This is a simple demo project created for learning and experimenting with **MCP (Model Control Protocol)** and its integration with OpenAI agents. The goal is to understand how agents can interact with tools via MCP, both locally and remotely.

## 📦 Project Structure

This repository consists of two main components:

1. **`main.py`** – Acts as the MCP client.

   - Creates and runs an openai-agent.
   - Connects to a tool server via MCP (using either stdio or SSE).
   - Sends input messages and receives tool-generated responses.

2. **`server.py`** – Acts as a local MCP server (optional, if not using remote).

   - Built with [`fastmcp`](https://github.com/jlowin/fastmcp).
   - Defines a simple tool (`sum`) to compute a modified sum of two numbers.

## 🚀 How to Run MCP Agent

1. **Install dependencies**

   ```
   pip install -r requirements.txt
   ```

2. **Set environment variables** (use .env.example as reference)

   ```
   cp .env.example .env
   ```

3. **Start the MCP server** (optional, if not using remote):
   For the local MCP server there are 2 transport methods:

   - **SSE transport**:
     ```
     fastmcp run server.py:mcp --transport sse --port 8080 --host 0.0.0.0
     ```

   - **Stdio transport**:
     ```
     python server.py
     ```

4. **Run the OpenAI Agent**:
   ```
    python main.py
   ```
