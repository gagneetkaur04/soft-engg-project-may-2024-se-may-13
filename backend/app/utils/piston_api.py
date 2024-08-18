import requests

PISTON_API_URL = "https://emkc.org/api/v2/piston/execute"

def execute_code(code, input_data):
    # Prepare the code to call the function with the given input
    # the function written by the user is always expected to be named 'main'
    # this main function takes the input_data as an argument
    full_code = f"""
{code}

# Test Case Execution
import json
input_data = json.loads('{input_data}')
result = main(input_data)
print(result)
"""

    payload = {
        "language": "python",
        "version": "3.10.0",
        "files": [
            {
                "name": "main.py",
                "content": full_code
            }
        ]
    }

    response = requests.post(PISTON_API_URL, json=payload)
    
    if response.status_code == 200:
        result = response.json()
        if result['run']['stderr']:
            return {"error": result['run']['stderr']}
        else:
            return {"output": result['run']['stdout']}
    else:
        return {"error": f"API Error: {response.status_code} - {response.text}"}