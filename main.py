from fastapi import FastAPI
from fastapi_mcp import add_mcp_server
from linkedin_api import Linkedin
from dotenv import load_dotenv
import os
load_dotenv(override=True)

LINKEDIN_USERNAME = os.getenv("LINKEDIN_USERNAME")
LINKEDIN_PASSWORD = os.getenv("LINKEDIN_PASSWORD")

api = Linkedin(LINKEDIN_USERNAME, LINKEDIN_PASSWORD)

app = FastAPI()

mcp_server = add_mcp_server(
    app,
    mount_path="/mcp",
    name="My API MCP",
)

@mcp_server.tool()
async def get_profile(username:str) -> str:
    profile = api.get_profile(username)
    return profile