"""
Script para fazer pull de prompts do LangSmith Prompt Hub.

Este script:
1. Conecta ao LangSmith usando credenciais do .env
2. Faz pull dos prompts do Hub
3. Salva localmente em prompts/bug_to_user_story_v1.yml

SIMPLIFICADO: Usa serialização nativa do LangChain para extrair prompts.
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from langsmith import Client
from langchain_openai import ChatOpenAI
from langchain.load.dump import dumps
from utils import save_yaml, check_env_vars, print_section_header

load_dotenv()

def pull_prompts_from_langsmith():
    client = Client()
    prompt = client.pull_prompt("leonanluppi/bug_to_user_story_v1")

    prompt_data = dumps(prompt)

    save_path = Path("prompts/raw_prompts.yml")
    save_path.parent.mkdir(parents=True, exist_ok=True)

    with open(save_path, "w", encoding="utf-8") as f:
        f.write(prompt_data)

    print(f"✅ Prompt salvo com sucesso em {save_path}")    

def main():
    """Função principal"""
    pull_prompts_from_langsmith()

if __name__ == "__main__":
    sys.exit(main())
