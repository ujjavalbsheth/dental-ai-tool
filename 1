import os
from openai import OpenAI

client = OpenAI()

def run_analysis(data):

    prompt = f"""
    You are a dental expert.

    Patient:
    Age: {data['age']}
    Complaint: {data['complaint']}
    OPG: {data['opg_description']}

    Suggest a treatment plan.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
