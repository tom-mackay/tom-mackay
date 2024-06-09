import pandas as pd
import pathlib
import textwrap
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown
import os
#from google.cloud import aiplatform

class LLM_Manager:
    def __init__(self, relative_path = None):
        
        print(relative_path)
        if relative_path:
            os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = relative_path
            # Initialize the API client
            self.client = genai.Client()
        else:
            print("Google AI API Credential Validation Failed")
            return False
            
    def generate_text(self, model, prompt, max_tokens):
        # Generate text
        response = self.client.generate(
            model=model,
            prompt=prompt,
            max_tokens=max_tokens
        )
        # Print the generated text
        print(response['choices'][0]['text'])

        




if __name__ =='__main__':
    path_to_credentials = r"C:\Users\enjam\OD01\scye1_truths\root-truth-425919-k5-a1fb467be1e8.json"
    LLM_Manager(path_to_credentials)
    LLM_Manager.generate_text(
        model="text-davinci-003",
        prompt="Once upon a time in a magical forest,",
        max_tokens=50
    )