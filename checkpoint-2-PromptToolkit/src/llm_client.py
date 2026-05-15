import os
import time
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

class LLMClient:
    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")

        if not self.api_key:
            print("❌ ERRO: GROQ_API_KEY não encontrada no arquivo .env")
            print("Certifique-se de que o arquivo .env existe e contém a chave.")
            self.client = None
        else:
            self.client = Groq(api_key=self.api_key)

        self.model_name = "llama-3.3-70b-versatile"

    def chat(self, prompt, system, temp=0.1):
        if not self.client:
            return None

        try:
            start_time = time.time()
            
            completion = self.client.chat.completions.create(
                model=self.model_name,
                messages=[
                    {"role": "system", "content": system},
                    {"role": "user", "content": prompt}
                ],
                temperature=temp,
            )
            
            end_time = time.time()

            return {
                "resposta": completion.choices[0].message.content,
                "tempo_ms": int((end_time - start_time) * 1000),
                "tokens_prompt": completion.usage.prompt_tokens,
                "tokens_resposta": completion.usage.completion_tokens
            }
            
        except Exception as e:
            print(f"❌ Erro na chamada da Groq: {e}")
            return None