# MCP (Model Context Protocol) Demo

This project demonstrates the implementation of Model Context Protocol (MCP) for both local and remote server configurations using stdio and HTTP protocols. The demonstration is built using the Agent Development Kit (ADK) web interface.

## Overview

This project showcases two main MCP implementation scenarios:
1. Local server communication using stdio protocol
2. Remote server communication using HTTP protocol

The demonstration utilizes the Agent Development Kit (ADK) web interface to visualize and interact with the MCP implementations.

## Features

- Local MCP server implementation using stdio protocol
- Remote MCP server implementation using HTTP protocol
- Integration with ADK web interface for testing and demonstration
- Example of MCP server configurations and usage patterns

## Project Structure

- `server.py` - Main server implementation
- `multiserver/` - Package containing MCP server components
  - `agent.py` - Agent implementation for MCP
  - `__init__.py` - Package initialization

## Prerequisites

- Python 3.x
- ADK web interface
- Required Python packages (listed in `pyproject.toml`)

## Getting Started

1. Clone the repository
2. Install dependencies
3. Run the MCP server and ADK web interface as described below

## Running the Application

### Starting the MCP Server

To run the MCP server in HTTP mode:
```bash
uv run server.py http
```

### Starting the ADK Web Interface

To launch the Agent Development Kit (ADK) web interface:
```bash
uv run adk web
```

Once both servers are running, you can use the ADK web interface to interact with the MCP server and test different protocols (stdio and HTTP).

