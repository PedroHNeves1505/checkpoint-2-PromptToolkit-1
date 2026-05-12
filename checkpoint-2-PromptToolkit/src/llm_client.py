import requests
import os
import time
from dotenv import load_dotenv 

load_dotenv()

class LLMClient:
    def __init__(self):
        self.host = os.getenv("OLLAMA_HOST", "http://localhost:11434")
        self.url = f"{self.host}/api/chat"

    def chat(self, prompt, system=None, temp=0.7, max_tokens=500, retries=3):
        payload = {
            "model": "gpt-oss-safeguard",
            "messages": [
                {"role": "system", "content": system} if system else None,
                {"role": "user", "content": prompt}
            ],
            "options": {
                "temperature": temp,
                "num_predict": max_tokens
            },
            "stream": False
        }
        
        payload["messages"] = [m for m in payload["messages"] if m]
        for attempt in range(retries):
            try:
                start_time = time.time()
                response = requests.post(self.url, json=payload, timeout=30)
            
                if response.status_code == 429:
                    print("Rate limit atingido. Aguardando...")
                    time.sleep(2)
                    continue
                
                response.raise_for_status()
                data = response.json()
                end_time = time.time()

                return {
                    "resposta": data["message"]["content"],
                    "tokens_prompt": data.get("prompt_eval_count", 0),
                    "tokens_resposta": data.get("eval_count", 0),
                    "tempo_ms": int((end_time - start_time) * 1000)
                }

            except (requests.exceptions.RequestException, requests.exceptions.Timeout) as e:
                print(f"Tentativa {attempt + 1} falhou: {e}")
                if attempt < retries - 1:
                    time.sleep(1)
                else:
                    print("Todas as tentativas falharam.")
                    return None