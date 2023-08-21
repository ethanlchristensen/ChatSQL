import os
import openai


class OpenAIPrompter:
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def complete(self, prompt):
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a robot that is trained to only respond on SQL queries based"
                                              "on the query the user gives to you. The user needs assistance writing"
                                              "SQL queries. Generally these involve updating existing rows or adding"
                                              "now rows."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=400
        )
        try:
            return completion.choices[0].message.content
        except Exception as exception:
            print(f"[ERROR] OpenAIPrompter: {exception}")
