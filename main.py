import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from config import system_prompt
from call_function import available_functions

load_dotenv()

verbose = "--verbose" in sys.argv
args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]
if not args:
    print("Error, no prompt provided")
    print('Usage: python3 main.py "Prompt" [--verbose]')
    print('Example: python3 main.py "How do i finish this?"')
    sys.exit(1)

api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

prompt = " ".join(args)
messages = [types.Content(role="user", parts=[types.Part(text=prompt)])]
response = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages, config=types.GenerateContentConfig(system_instruction=system_prompt, tools=[available_functions]))

if not response.function_calls:
    print(response.text)
    
else:
    for function_call_part in response.function_calls:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")

if verbose:
    print(f"User prompt: {prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")