import os
from dotenv import load_dotenv
from google import genai
import sys

def main():
    
    load_dotenv()

    api_key=os.environ.get("GEMINI_API_KEY")
    
    if len(sys.argv)<2:
        print("I need a prompt")
        sys.exit(1)
    
    prompt=sys.argv[1]

    client = genai.Client(api_key=api_key)

    response=client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt
    )

    print(response.text)
    
main()