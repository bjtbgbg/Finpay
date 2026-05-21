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
        "chat_template_kwargs": {"enable_thinking": False}
    }
)

print(completion.choices[0].message.content)
