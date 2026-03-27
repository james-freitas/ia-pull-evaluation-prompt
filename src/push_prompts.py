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
    Faz push do prompt para o LangSmith usando Client (com metadata).
    """
    try:
        print_section_header(f"🚀 Enviando prompt: {prompt_name}")

        client = Client()

        # 1. Criar prompt template
        prompt = ChatPromptTemplate.from_messages([
            ("system", prompt_data["system_prompt"]),
            ("human", prompt_data["user_prompt"]),
        ])

        # 2. Nome com versionamento
        repo_name = f"{prompt_name}:{prompt_data.get('version', 'v1')}"

        # 3. Preparar metadata
        metadata = {
            "description": prompt_data.get("description", ""),
            "tags": prompt_data.get("tags", []),
            "created_at": prompt_data.get("created_at"),
        }

        # 4. Push usando Client
        response = client.push_prompt(
            repo_name,
            object=prompt,
            tags=[
                prompt_data.get("version", "v1.0.0"),
            ],
            description=metadata["description"],
        )

        print("✅ Prompt enviado com sucesso!")
        print(f"🔗 URL: {response.url if hasattr(response, 'url') else response}")

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

    print_section_header("📦 Iniciando push de prompts...")
    
    prompts = load_yaml("prompts/bug_to_user_story_v2.yml")

    for name, data in prompts.items():
        is_valid, errors = validate_prompt(data)

        if not is_valid:
            print(f"❌ Prompt inválido: {name}")
            for err in errors:
                print(f"  - {err}")
            continue

        push_prompt_to_langsmith(name, data)


if __name__ == "__main__":
    sys.exit(main())