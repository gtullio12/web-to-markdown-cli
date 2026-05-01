# Firecrawl Markdown Extractor

A lightweight CLI tool that takes a URL, scrapes it using Firecrawl, and prints clean markdown to the terminal.

The goal is to quickly turn web pages into readable or LLM-ready text without dealing with HTML or manual parsing.

---

## What it does

- Accepts a URL as input
- Uses Firecrawl to scrape the page
- Extracts markdown from the response
- Prints a preview to the terminal

---

## Setup

Install dependencies: `pip install -r requirements.txt`

Create a .env file in the project root with contents: 
`FIRECRAWL_API_KEY=your_api_key_here`


Run: `python firecrawl_scraper.py https://firecrawl.dev`

### Example Output
================================================================================

# Power AI agents with clean web data

The API to search, scrape, and interact with the web at scale.

Firecrawl converts any URL into structured, LLM-ready markdown with a single call.

...


## What I learned
- How to integrate a third-party API (Firecrawl)
- How to build a simple Python CLI tool
- How to manage environment variables securely using .env
- How to process and display API responses in a terminal


## Future improvements
- Support multiple URLs in one run
- Save output to a .md file
- Add JSON output mode for LLM pipelines
- Add basic content cleaning (remove nav/footer noise)