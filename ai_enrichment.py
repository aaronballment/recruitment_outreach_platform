import config
from google import genai
from google.genai import types

class AI():
    '''
    A class representing an AI connection.
    '''
    def __init__(self):
        '''
        Initialises the Gemini configuration.
        '''
        
        self._client = genai.Client(api_key=config.AI_API_KEY)
        
        self._model_id = 'gemini-3.1-flash-lite'
        
    def web_search(self, prompt: str) -> str:
        '''
        web search using a given prompt
        '''
        
        try:
            response = self._client.models.generate_content(
                model=self._model_id, 
                contents=prompt,
                config=types.GenerateContentConfig(
                    tools=[{'google_search': {}}],
                    temperature=0.2
                )
            )
            if response.text:
                return response.text.strip()
            else:
                return ''
        
        except Exception as e:
            print(f"Search API Error: {e}")
            return ""
        
    def generate_content(self, prompt: str) -> str:
        '''
        generate output with a given prompt.
        '''
        
        try:
            response = self._client.models.generate_content(
                model=self._model_id, 
                contents=prompt,
                config=types.GenerateContentConfig(
                    temperature=0.2
                )
            )
            if response.text:
                return response.text.strip()
            else:
                return ''
        
        except Exception as e:
            print(f"Generation API Error: {e}")
            return ""