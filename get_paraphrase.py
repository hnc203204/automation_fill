from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("api_key"))

def get_paraphrase(content):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"Viết lại một câu nhận xét như  \'{content}\' sao cho ý nghĩa vẫn được giữ nguyên"}
        ]
    )
    print(response.choices[0].message.content)
    return response.choices[0].message.content