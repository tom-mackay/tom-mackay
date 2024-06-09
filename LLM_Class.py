import os
import json
from groq import Groq

class LLM_Manager:
    def __init__(self, relative_path=None):
        
        self.config = self.load_config(relative_path)
        # print(self.config)
        self.groq_key = self.load_api_key(self.config)
        self.client = Groq(api_key=self.groq_key)
        
    def make_ai_request(self, client, request_message):
        completion = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {
                    "role": "user",
                    "content": f"{request_message}"
                }
            ],
            temperature=1,
            max_tokens=1024,
            top_p=1,
            stream=True,
            stop=None,
        )
        return completion
            
    #& Might be worth moving this to Login_Main.py
    def load_config(self, file_path):
        with open(file_path, 'r') as file:
            config = json.load(file)
        return config
    
    def load_api_key(self, config):
        #! Create environment variable 
        os.environ['groq_api_key'] = config["groq_api_key"]
        #! Try to load API key from environment variable
        api_key = os.getenv('groq_api_key')
        if api_key:
            return api_key








if __name__ == '__main__':
    
    path_to_credentials = r"C:\Users\enjam\OD01\scye1_truths\environment_variables.json"
    llm_manager = LLM_Manager(path_to_credentials)
    completion = llm_manager.make_ai_request(llm_manager.client, "Can you help me?")
    #& This needs to be in a specific place
    for chunk in completion:
        print(chunk.choices[0].delta.content or "", end="")
