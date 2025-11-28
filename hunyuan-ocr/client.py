from openai import OpenAI

client = OpenAI(
    api_key="EMPTY",
    base_url="http://localhost:8000/v1",
    timeout=3600
)

messages = [
    {"role": "system", "content": ""},
    {
        "role": "user",
        "content": [
            {
                "type": "image_url",
                "image_url": {
                    "url": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/chat-ui/tools-dark.png"
                }
            },
            {
                "type": "text",
                "text": (
                    "Extract all information from the main body of the document image "
                )
            }
        ]
    }
]

response = client.chat.completions.create(
    # model="tencent/HunyuanOCR",
    model="/models/HunyuanOCR",
    messages=messages,
    temperature=0.0,
    extra_body={
        "top_k": 1,
        "repetition_penalty": 1.0
    },
)
print(f"Generated text: {response.choices[0].message.content}")