import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_story(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a friendly storyteller."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()
import logging

logging.basicConfig(level=logging.INFO)

def generate_story(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a friendly storyteller."},
                {"role": "user", "content": prompt}
            ]
        )
        logging.info("Story generated successfully")
        return response.choices[0].message.content.strip()
    except Exception as e:
        logging.error("Error generating story: " + str(e))
        return None