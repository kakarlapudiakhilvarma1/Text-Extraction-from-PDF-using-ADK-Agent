from google.adk.agents import Agent
from .tools import extract_pdf_text, get_simple_info

root_agent = Agent(
    name="simple_pdf_extractor",
    model="gemini-2.0-flash",
    description="Simple PDF text extractor",
    instruction="""
You extract text from PDF files.

Tools:
- extract_pdf_text(file_path): Extract text from PDF
- get_simple_info(file_path): Get basic file information

Just extract text and return it. No analysis or processing.
""",
    tools=[extract_pdf_text, get_simple_info]
)
