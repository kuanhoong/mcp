from mcp.server.fastmcp import FastMCP
import os

#===========================
# Create a MCP server
#===========================

mcp = FastMCP("Space Notes")


NOTES_FILE = os.path.join(os.path.dirname(__file__), "notes.txt")
RESOURCES_FILE = os.path.join(os.path.dirname(__file__), "resources.txt")


def ensure_file():
    if not os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "w") as f:
            f.write("")

#===========================
# Create a MCP Tool 1
#===========================

@mcp.tool()
def add_note(message: str) -> str:
    """
    Append a new note to the sticky note file.

    Args:
        message (str): The note content to be added.

    Returns:
        str: Confirmation message indicating the note was saved.
    """
    ensure_file()
    with open(NOTES_FILE, "a") as f:
        f.write(message + "\n")
    return "Note saved!"

#===========================
# Create a MCP Tool 2
#===========================

@mcp.tool()
def read_notes() -> str:
    """
    Read and return all notes from the space note file.

    Returns:
        str: All notes as a single string separated by line breaks.
             If no notes exist, a default message is returned.
    """
    ensure_file()
    with open(NOTES_FILE, "r") as f:
        content = f.read().strip()
    return content or "No notes yet."

#===========================
# Create a MCP Resource
#===========================

@mcp.resource("notes://latest")
def get_latest_note() -> str:
    """
    Get the most recently added resource note from the space note file.

    Returns:
        str: The last note entry. If no notes exist, a default message is returned.
    """
    ensure_file()
    with open(RESOURCES_FILE, "r") as f:
        lines = f.readlines()
    return lines[-1].strip() if lines else "No notes yet."

#===========================
# Create a MCP Prompt
#===========================

@mcp.prompt()
def note_summary_prompt() -> str:
    """
    Generate a prompt asking the AI to summarize all current notes.

    Returns:
        str: A prompt string that includes all notes and asks for a summary.
             If no notes exist, a message will be shown indicating that.
    """
    ensure_file()
    with open(NOTES_FILE, "r") as f:
        content = f.read().strip()
    if not content:
        return "There are no notes yet."

    return f"Summarize the current notes: {content}"
