# Pull, Otimização e Avaliação de Prompts com LangChain e LangSmith

## Objetivo


O objetivo deste desafio é aplicar técnicas avançadas de prompt engineering para otimizar um prompt específico, utilizando o LangSmith para avaliação automática. Você irá iterar no processo de refatoração do prompt até atingir uma performance excelente, documentando todo o processo e os resultados obtidos.

---

## Técnicas Aplicadas

   - Neste desafio, foram usadas as técnicas  **Role Prompting** e o **Few-shot** 
   

   ### Role Prompting
   
   - O **Role Prompting** foi utilizado para definir uma persona clara para o modelo, de forma a controlar o tom, estilo e abordagem da resposta. 

   - Exemplo prático da técnica aplicada:

     ```
     Você é um Product Manager sênior escrevendo User Stories no padrão ágil.
     ```
   
   ### Few-shot Learning

   - O **Few-shot Learning** foi aplicado para fornecer exemplos claros de entrada / saída para ajudar o modelo a entender exatamente o formato e o tipo de resposta esperada.

   - Exemplo prático da técnica aplicada:
   
      ```
      ## EXEMPLO 1 — SIMPLES

      Relato de Bug:
      Botão de adicionar ao carrinho não funciona no produto ID 1234.

      User Story:

      Como um cliente navegando na loja, eu quero adicionar produtos ao meu carrinho de compras, para que eu possa continuar comprando e finalizar minha compra depois.

      Critérios de Aceitação:
      - Dado que estou visualizando um produto
      - Quando clico no botão "Adicionar ao Carrinho"
      - Então o produto deve ser adicionado ao carrinho
      - E devo ver uma confirmação visual
      - E o contador do carrinho deve ser atualizado

      ---

      ## EXEMPLO 2 — SIMPLES

      Relato de Bug:
      No iOS, ao girar o celular para landscape, o layout da tela de perfil fica quebrado.

      User Story:

      Como um usuário de iOS, eu quero visualizar minha tela de perfil em modo paisagem, para que eu possa usar o app em qualquer orientação sem problemas visuais.

      Critérios de Aceitação:
      - Dado que estou na tela de perfil no iOS
      - Quando giro o dispositivo para modo paisagem
      - Então o layout deve se adaptar corretamente
      - E todos os elementos devem permanecer visíveis e alinhados
      - E não deve haver sobreposição de componentes

      ---
      ```

## (WIP) Resultados Finais 

   - Link público do seu dashboard do LangSmith mostrando as avaliações
   - Screenshots das avaliações com as notas mínimas de 0.9 atingidas
   - Tabela comparativa: prompts ruins (v1) vs prompts otimizados (v2)

## (WIP) Como Executar

   - Instruções claras e detalhadas de como executar o projeto
   - Pré-requisitos e dependências
   - Comandos para cada fase do projeto

## (WIP) Evidências no LangSmith:
   - Link público (ou screenshots) do dashboard do LangSmith
   - Devem estar visíveis:

     - Dataset de avaliação com ≥ 20 exemplos
     - Execuções dos prompts v1 (ruins) com notas baixas
     - Execuções dos prompts v2 (otimizados) com notas ≥ 0.9
     - Tracing detalhado de pelo menos 3 exemplos

## VirtualEnv para Python

Crie e ative um ambiente virtual antes de instalar dependências:

```bash
python3 -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---


---

## Entregável

1. **Repositório público no GitHub** (fork do repositório base) contendo:

   - Todo o código-fonte implementado
   - Arquivo `prompts/bug_to_user_story_v2.yml` 100% preenchido e funcional
   - Arquivo `README.md` atualizado com:

2. **README.md deve conter:**

   A) **Seção "Técnicas Aplicadas (Fase 2)"**:

   - Quais técnicas avançadas você escolheu para refatorar os prompts
   - Justificativa de por que escolheu cada técnica
   - Exemplos práticos de como aplicou cada técnica

   B) **Seção "Resultados Finais"**:

   - Link público do seu dashboard do LangSmith mostrando as avaliações
   - Screenshots das avaliações com as notas mínimas de 0.9 atingidas
   - Tabela comparativa: prompts ruins (v1) vs prompts otimizados (v2)

   C) **Seção "Como Executar"**:

   - Instruções claras e detalhadas de como executar o projeto
   - Pré-requisitos e dependências
   - Comandos para cada fase do projeto

3. **Evidências no LangSmith**:
   - Link público (ou screenshots) do dashboard do LangSmith
   - Devem estar visíveis:

     - Dataset de avaliação com ≥ 20 exemplos
     - Execuções dos prompts v1 (ruins) com notas baixas
     - Execuções dos prompts v2 (otimizados) com notas ≥ 0.9
     - Tracing detalhado de pelo menos 3 exemplos

---

## Dicas Finais

- **Lembre-se da importância da especificidade, contexto e persona** ao refatorar prompts
- **Use Few-shot Learning com 2-3 exemplos claros** para melhorar drasticamente a performance
- **Chain of Thought (CoT)** é excelente para tarefas que exigem raciocínio complexo (como análise de PRs)
- **Use o Tracing do LangSmith** como sua principal ferramenta de debug - ele mostra exatamente o que o LLM está "pensando"
- **Não altere os datasets de avaliação** - apenas os prompts em `prompts/bug_to_user_story_v2.yml`
- **Itere, itere, itere** - é normal precisar de 3-5 iterações para atingir 0.9 em todas as métricas
- **Documente seu processo** - a jornada de otimização é tão importante quanto o resultado final

---



## How to run

python3 src/push_prompts.py

---
Link prompt acesso publico: https://smith.langchain.com/hub/bug-to-user-story-using-chain-of-thought/bug_to_user_story_with_chain_of_thought

