from firecrawl import FirecrawlApp
from dotenv import load_dotenv
import os
import sys

load_dotenv()

api_key = os.getenv("FIRECRAWL_API_KEY")

if not api_key: 
    raise ValueError('Missing firecrawl API key')

firecrawl = FirecrawlApp(api_key=api_key)

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <url>")
        return

    url = sys.argv[1]

    res = firecrawl.scrape(url)
    markdown = res.markdown

    if not markdown:
        print("No markdown returned")
        return

    print("\n" + "=" * 80)
    print(markdown[:3000])


if __name__ == '__main__':
    main()