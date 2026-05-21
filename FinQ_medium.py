import json
from openai import OpenAI

api_key = "xxxxxxxx"
base_url = "http://35.220.164.252:3888/v1/"
path = "qwen3.5-122b-a10b"
question = "你好"

client = OpenAI(
    api_key=api_key,
    base_url=base_url,
)

completion = client.chat.completions.create(
    model=path, 
    messages=[{'role': 'user', 'content': question}],
    temperature=0.7,
    top_p=0.8,
    presence_penalty=1.5,
    extra_body={
        "top_k": 20,
        "enable_thinking": False
    }
)
response = json.loads(completion.model_dump_json())
print(response['choices'][0]['message']['content'])
