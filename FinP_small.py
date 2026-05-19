import json
from openai import OpenAI

api_key = "xxxxxxxx"
base_url = "https://chat.intern-ai.org.cn/api/v1/"
path = "intern-s2-preview"
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
    ],
    temperature=0.8,
    top_p=0.95,
    extra_body={
        "top_k": 50,
        "min_p": 0.0,
    },
)

response = json.loads(completion.model_dump_json())
print(response['choices'][0]['message']['content'])
