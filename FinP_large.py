import json
from openai import OpenAI

api_key = "xxxxxxxxxxxxx"  
base_url = "https://chat.intern-ai.org.cn/api/v1/"
path = "intern-s1"  
question = "你好"

client = OpenAI(
    api_key=api_key,
    base_url=base_url,
)

completion = client.chat.completions.create(
    model=path,
    messages=[
        {
            "role": "user",
            "content": question
        }
    ]
)

response = json.loads(completion.model_dump_json())
content = response["choices"][0]["message"]["content"]

print(content)
