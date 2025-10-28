from google.adk.agents.llm_agent import Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StreamableHTTPConnectionParams, StdioServerParameters

#=====================
# Define Local MCP (stdio)
#=====================

local_mcp_params = StdioServerParameters(
    command="uv",
    args=["run", "/Users/kuanhoong/Downloads/mcp/server.py"]
)

local_mcp_toolset = MCPToolset(
    connection_params=local_mcp_params
)

#=====================
# Define MCP over HTTP
#=====================

http_mcp_params = StreamableHTTPConnectionParams(
    url="http://127.0.0.1:4200/mcp"  # Changed port to match your remote_server port
)

http_mcp_toolset = MCPToolset(
    connection_params=http_mcp_params
)

#=====================
# Define Root Agent
#=====================

root_agent = Agent(
    name = "Agent_MCP",
    model = "gemini-2.5-flash",
    description = "A helpful assistant for user questions.",
    instruction = "Answer user questions to the best of your knowledge",
    #tools=[local_mcp_toolset]
    #tools=[http_mcp_toolset]
    tools=[local_mcp_toolset, http_mcp_toolset]
)