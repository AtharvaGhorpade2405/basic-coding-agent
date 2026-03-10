import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys

def main():
    
    load_dotenv()

    api_key=os.environ.get("GEMINI_API_KEY")
    
    if len(sys.argv)<2:
        print("I need a prompt")
        sys.exit(1)
    
    verbose_flag=False
    if len(sys.argv)==3 and sys.argv[2]=="--verbose":
        verbose_flag=True
    
    prompt=sys.argv[1]

    client = genai.Client(api_key=api_key)
    
    messages=[
        types.Content(role="user", parts=[types.Part(text=prompt)])
    ]

    response=client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=messages
    )

    print(response.text)
    if response is None or response.usage_metadata is None:
        print("Response is malformed.")
        return
    if verbose_flag:
        print(f"User prompt: {prompt}")
        print(f"Prompt Tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response Tokens: {response.usage_metadata.candidates_token_count}")
    
main()