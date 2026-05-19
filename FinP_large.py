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
    ],
    temperature=0.7,
    top_p=0.95,
    extra_body={
        "top_k": 50,
        "repetition_penalty": 1.0,
        "enable_thinking": True,
    },
)

response = json.loads(completion.model_dump_json())
content = response["choices"][0]["message"]["content"]

print(content)
