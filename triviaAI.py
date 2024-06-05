from openai import OpenAI
import csv
import base64

class TriviaAI:
    string = b'N3Q0RE1rWU9saWM4bndBOW1UMUpUM0JsYmtGSndjb1V4V1pHTXJPZWM5aklhS1Nm'

    def __init__(self):
        """
        Initialize the TriviaAI class.
        """
        self.client = None
        self.set_client()

    def set_client(self):
        """Decodes API Key and sets client"""
        try:
            decoded_key = base64.b64decode(TriviaAI.string).decode("utf-8")
            self.client = OpenAI(api_key='sk-proj-' + decoded_key)
        except Exception as e:
            print(f"Failed to set client: {e}")

    def get_raw(self):
        """
        Get raw trivia question and answer in CSV format from OpenAI.

        Returns:
        - response (str): The response from OpenAI containing the trivia question and answer.
        """
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": "Create a trivia question on the topic of programming, video games, or tech. The output should be in CSV format, with the question (including abc options) in one column and the single correct answer a, b, or c in the other. Example: What software development hosting company has an Octocat for the logo? A. Github B. AWS C. Google Cloud,A"},
                ],
                max_tokens=200,  # Maximum Length
                temperature=0.7  # Variety
            )
            return response.choices[0].message.content
        
        except Exception as e:
            print(f"An error occurred during API request: {e}")
            return None

    def generate_new(self):
        """
        Generate a new trivia question and answer by processing the raw response.

        Returns:
        - fields (list): List containing the question and the correct answer.
        """
        raw = self.get_raw()
        if raw:
            fields = raw.split(",")
            return fields  # Returns a list that can be converted to object
        return None

    def write_new(self):
        """
        Write a new trivia question and answer to the CSV file.
        """
        new_qa = self.generate_new()
        if new_qa:
            try:
                with open('questionsDatabase.csv', 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(new_qa)
            except Exception as e:
                print(f"Failed to write to CSV file: {e}")