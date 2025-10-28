from fastmcp import FastMCP
import argparse

# Create two separate server instances
local_server = FastMCP(name="LocalServer")
remote_server = FastMCP(name="RemoteServer")

# Tools for local server (stdio)
@local_server.tool()
def add_numbers(a: int, b: int) -> int:
    """This function adds two numbers"""
    return a + b

@local_server.tool()
def subtract_numbers(a: int, b: int) -> int:
    """This function subtracts two numbers"""
    return a - b

@local_server.tool()
def multiply_numbers(a: int, b: int) -> int:
    """This function multiplies two numbers"""
    return a * b

# Tools for remote server (HTTP)
@remote_server.tool()
def say_hello(name: str) -> str:
    """This function says hello to a person"""
    return f"Hello, {name}!"

@remote_server.tool()
def say_goodbye(name: str) -> str:
    """This function says goodbye to a person"""
    return f"Goodbye, {name}!"

@remote_server.tool()
def say_welcome(name: str) -> str:
    """This function says welcome to a person"""
    return f"Welcome, {name}!"

def parse_args():
    parser = argparse.ArgumentParser(description="Run MCP servers.")
    parser.add_argument(
        "transport",
        nargs="?",
        choices=["stdio", "http"],
        default="stdio",
        help="Transport method for the local server (default: stdio)",
    )
    return parser.parse_args()

if __name__ == "__main__":

    args = parse_args()

    remote_server.run(transport="http", port=4200) if args.transport == "http" else local_server.run(transport="stdio")

