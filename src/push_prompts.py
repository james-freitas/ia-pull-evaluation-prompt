"""
Script para fazer push de prompts otimizados ao LangSmith Prompt Hub.

Este script:
1. Lê os prompts otimizados de prompts/bug_to_user_story_v2.yml
2. Valida os prompts
3. Faz push PÚBLICO para o LangSmith Hub
4. Adiciona metadados (tags, descrição, técnicas utilizadas)

SIMPLIFICADO: Código mais limpo e direto ao ponto.
"""

import os
import sys
from dotenv import load_dotenv
from langsmith import Client
from langchain import hub
from langchain_core.prompts import ChatPromptTemplate
from utils import load_yaml, check_env_vars, print_section_header

load_dotenv()


def push_prompt_to_langsmith(prompt_name: str, prompt_data: dict) -> bool:

    """
    Faz push do prompt otimizado para o LangSmith Hub (PÚBLICO).

    Args:
        prompt_name: Nome do prompt
        prompt_data: Dados do prompt

    Returns:
        True se sucesso, False caso contrário
    """
    try:
        print_section_header(f"🚀 Enviando prompt: {prompt_name}")

        # 1. Criar template de chat
        prompt = ChatPromptTemplate.from_messages([
            ("system", prompt_data["system_prompt"]),
            ("human", prompt_data["user_prompt"]),
        ])

        # 2. Preparar metadados
        metadata = {
            "description": prompt_data.get("description", ""),
            "tags": prompt_data.get("tags", []),
            "version": prompt_data.get("version", "v1"),
        }

        # 3. Nome final no hub
        # Ex: "bug_to_user_story_with_chain_of_thought"
        repo_name = prompt_name

        # 4. Push para LangChain Hub (LangSmith Hub)
        url = hub.push(
            repo_name,
            prompt,
            description=metadata["description"],
            tags=metadata["tags"],
        )

        print(f"✅ Prompt enviado com sucesso!")
        print(f"🔗 URL: {url}")

        return True

    except Exception as e:
        print(f"❌ Erro ao enviar prompt '{prompt_name}': {str(e)}")
        return False


def validate_prompt(prompt_data: dict) -> tuple[bool, list]:
    """
    Valida estrutura básica de um prompt (versão simplificada).

    Args:
        prompt_data: Dados do prompt

    Returns:
        (is_valid, errors) - Tupla com status e lista de erros
    """
    errors = []

    required_fields = ["system_prompt", "user_prompt"]

    # Check required fields
    for field in required_fields:
        if field not in prompt_data:
            errors.append(f"Campo obrigatório ausente: '{field}'")
        elif not isinstance(prompt_data[field], str):
            errors.append(f"Campo '{field}' deve ser string")
        elif prompt_data[field].strip() == "":
            errors.append(f"Campo '{field}' não pode estar vazio")

    # Optional fields validation
    if "description" in prompt_data and not isinstance(prompt_data["description"], str):
        errors.append("Campo 'description' deve ser string")

    if "version" in prompt_data and not isinstance(prompt_data["version"], str):
        errors.append("Campo 'version' deve ser string")

    if "tags" in prompt_data:
        if not isinstance(prompt_data["tags"], list):
            errors.append("Campo 'tags' deve ser uma lista")
        else:
            for tag in prompt_data["tags"]:
                if not isinstance(tag, str):
                    errors.append("Todos os itens em 'tags' devem ser strings")
    return (len(errors) == 0, errors)

def main():
    """Função principal"""
    
    if __name__ == "__main__":
        prompts = load_yaml("prompts/bug_to_user_story_v2.yml")

    for name, data in prompts.items():
        is_valid, errors = validate_prompt(data)

        if not is_valid:
            print(f"❌ Prompt inválido: {name}")
            for err in errors:
                print(f"  - {err}")
            continue

        push_prompt_to_langsmith(name, data)
