"""
Testes automatizados para validação de prompts.
"""
import pytest
import yaml
import sys
from pathlib import Path

# Adicionar src ao path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from utils import validate_prompt_structure

def load_prompts(file_path: str):
    """Carrega prompts do arquivo YAML."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

class TestPrompts:
    def test_prompt_has_system_prompt(self):
        """Verifica se o campo 'system_prompt' existe e não está vazio."""
        prompts = load_prompts("prompts/bug_to_user_story_v2.yml")

        assert isinstance(prompts, dict), "O arquivo deve conter um dicionário de prompts"

        for prompt_name, prompt_data in prompts.items():
            assert "system_prompt" in prompt_data, f"{prompt_name} não possui 'system_prompt'"

            system_prompt = prompt_data["system_prompt"]

            assert isinstance(system_prompt, str), f"{prompt_name} 'system_prompt' deve ser string"
            assert system_prompt.strip() != "", f"{prompt_name} 'system_prompt' não pode estar vazio"

    def test_prompt_has_role_definition(self):
        """Verifica se o prompt define uma persona (ex: "Você é um Product Manager")."""
        pass

    def test_prompt_mentions_format(self):
        """Verifica se o prompt exige formato Markdown ou User Story padrão."""
        pass

    def test_prompt_has_few_shot_examples(self):
        """Verifica se o prompt contém exemplos de entrada/saída (técnica Few-shot)."""
        pass

    def test_prompt_no_todos(self):
        """Garante que você não esqueceu nenhum `[TODO]` no texto."""
        pass

    def test_minimum_techniques(self):
        """Verifica (através dos metadados do yaml) se pelo menos 2 técnicas foram listadas."""
        pass

if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])