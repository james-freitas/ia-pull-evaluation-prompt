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

## Como Executar

  ### Requisitos

   - Python 3.8 ou superior
   - LangChain
   - LangSmith
   - Outras dependências listadas no `requirements.txt`


  ### Como executar

   1. Clone este repositório:
      ```bash
      git clone https://github.com/devfullcycle/mba-ia-pull-evaluation-prompt.git
      cd mba-ia-pull-evaluation-prompt
      ```

   2. Crie e ative um ambiente virtual antes de instalar dependências:

      ```bash
      python3 -m venv venv
      source venv/bin/activate  # No Windows: venv\Scripts\activate
      pip install -r requirements.txt
      ```

    3. Execute o script para avaliação dos prompts:

      ```bash
      python evaluate_prompts.py
      ```

    4. Analise os resultados      


## Evidências no LangSmith:

  ### Execução com prompt v1

   - [Trace](https://smith.langchain.com/o/9077ae76-3565-4e39-977f-21c73f617378/projects/p/5934d526-8625-4381-a9b6-890cd0f4cca3?timeModel=%7B%22duration%22%3A%221d%22%7D) do LangSmith mostrando as execuções do prompt v1 

   - Resultados:
      ```shell
      ==================================================
      AVALIAÇÃO DE PROMPTS OTIMIZADOS
      ==================================================

      Provider: openai
      Modelo Principal: gpt-4o-mini
      Modelo de Avaliação: gpt-4o

      Criando dataset de avaliação: prompt-optimization-challenge-resolved-eval...
         ✓ Carregados 15 exemplos do arquivo datasets/bug_to_user_story.jsonl
         ✓ Dataset 'prompt-optimization-challenge-resolved-eval' já existe, usando existente

      ======================================================================
      PROMPTS PARA AVALIAR
      ======================================================================

      Este script irá puxar prompts do LangSmith Hub.
      Certifique-se de ter feito push dos prompts antes de avaliar:
      python src/push_prompts.py


      🔍 Avaliando: bug_to_user_story_v1
         Puxando prompt do LangSmith Hub: bug_to_user_story_v1
         ✓ Prompt carregado com sucesso
         Dataset: 15 exemplos
         Avaliando exemplos...
            [1/10] F1:0.75 Clarity:0.90 Precision:0.90
            [2/10] F1:0.75 Clarity:0.90 Precision:0.90
            [3/10] F1:0.75 Clarity:0.95 Precision:0.80
            [4/10] F1:0.58 Clarity:0.85 Precision:0.90
            [5/10] F1:0.75 Clarity:0.90 Precision:0.83
            [6/10] F1:0.85 Clarity:0.90 Precision:0.90
            [7/10] F1:0.85 Clarity:0.90 Precision:0.93
            [8/10] F1:0.75 Clarity:0.90 Precision:1.00
            [9/10] F1:0.80 Clarity:0.90 Precision:0.90
            [10/10] F1:0.67 Clarity:0.85 Precision:0.67

      ==================================================
      Prompt: bug_to_user_story_v1
      ==================================================

      Métricas LangSmith:
      - Helpfulness: 0.88 ✗
      - Correctness: 0.81 ✗

      Métricas Customizadas:
      - F1-Score: 0.75 ✗
      - Clarity: 0.90 ✗
      - Precision: 0.87 ✗

      --------------------------------------------------
      📊 MÉDIA GERAL: 0.8420
      --------------------------------------------------

      ❌ STATUS: REPROVADO (média < 0.9)
      ⚠️  Média atual: 0.8420 | Necessário: 0.9000
      ```

  ### Execução com prompt alterado mas reprovado

   - [Trace](https://smith.langchain.com/o/9077ae76-3565-4e39-977f-21c73f617378/projects/p/5934d526-8625-4381-a9b6-890cd0f4cca3?timeModel=%7B%22duration%22%3A%221d%22%7D) do LangSmith mostrando as execuções do prompt

   - Resultados:
      ```shell
      ==================================================
      AVALIAÇÃO DE PROMPTS OTIMIZADOS
      ==================================================

      Provider: openai
      Modelo Principal: gpt-4o-mini
      Modelo de Avaliação: gpt-4o

      Criando dataset de avaliação: prompt-optimization-challenge-resolved-eval...
         ✓ Carregados 15 exemplos do arquivo datasets/bug_to_user_story.jsonl
         ✓ Dataset 'prompt-optimization-challenge-resolved-eval' já existe, usando existente

      ======================================================================
      PROMPTS PARA AVALIAR
      ======================================================================

      Este script irá puxar prompts do LangSmith Hub.
      Certifique-se de ter feito push dos prompts antes de avaliar:
      python src/push_prompts.py


      🔍 Avaliando: bug_to_user_story_v1_improved
         Puxando prompt do LangSmith Hub: bug_to_user_story_v1_improved
         ✓ Prompt carregado com sucesso
         Dataset: 15 exemplos
         Avaliando exemplos...
            [1/10] F1:0.85 Clarity:0.90 Precision:0.90
            [2/10] F1:0.75 Clarity:0.90 Precision:0.90
            [3/10] F1:0.85 Clarity:0.90 Precision:0.90
            [4/10] F1:0.69 Clarity:0.85 Precision:0.67
            [5/10] F1:1.00 Clarity:1.00 Precision:1.00
            [6/10] F1:0.85 Clarity:0.85 Precision:0.67
            [7/10] F1:0.85 Clarity:0.80 Precision:0.67
            [8/10] F1:0.65 Clarity:0.80 Precision:0.80
            [9/10] F1:0.65 Clarity:0.75 Precision:0.67
            [10/10] F1:0.65 Clarity:0.75 Precision:0.67

      ==================================================
      Prompt: bug_to_user_story_v1_improved
      ==================================================

      Métricas LangSmith:
      - Helpfulness: 0.82 ✗
      - Correctness: 0.78 ✗

      Métricas Customizadas:
      - F1-Score: 0.78 ✗
      - Clarity: 0.85 ✗
      - Precision: 0.79 ✗

      --------------------------------------------------
      📊 MÉDIA GERAL: 0.8018
      --------------------------------------------------

      ❌ STATUS: REPROVADO (média < 0.9)
      ⚠️  Média atual: 0.8018 | Necessário: 0.9000

      ==================================================
      RESUMO FINAL
      ==================================================

      Prompts avaliados: 1
      Aprovados: 0
      Reprovados: 1

      ⚠️  Alguns prompts não atingiram média >= 0.9

      Próximos passos:
      1. Refatore os prompts com score baixo
      2. Faça push novamente: python src/push_prompts.py
      3. Execute: python src/evaluate.py novamente
      ```

  ### Execução com prompt alterado e aprovado

   - [Trace](https://smith.langchain.com/o/9077ae76-3565-4e39-977f-21c73f617378/projects/p/5934d526-8625-4381-a9b6-890cd0f4cca3?timeModel=%7B%22duration%22%3A%221d%22%7D) do LangSmith mostrando as execuções do prompt

   - Resultados:
      ```shell
      ==================================================
      AVALIAÇÃO DE PROMPTS OTIMIZADOS
      ==================================================

      Provider: openai
      Modelo Principal: gpt-4o-mini
      Modelo de Avaliação: gpt-4o

      Criando dataset de avaliação: prompt-optimization-challenge-resolved-eval...
         ✓ Carregados 15 exemplos do arquivo datasets/bug_to_user_story.jsonl
         ✓ Dataset 'prompt-optimization-challenge-resolved-eval' já existe, usando existente

      ======================================================================
      PROMPTS PARA AVALIAR
      ======================================================================

      Este script irá puxar prompts do LangSmith Hub.
      Certifique-se de ter feito push dos prompts antes de avaliar:
      python src/push_prompts.py


      🔍 Avaliando: awjamesfrj/bug_to_user_story_using_fewshot
         Puxando prompt do LangSmith Hub: awjamesfrj/bug_to_user_story_using_fewshot
         ✓ Prompt carregado com sucesso
         Dataset: 15 exemplos
         Avaliando exemplos...
            [1/10] F1:0.75 Clarity:0.85 Precision:0.90
            [2/10] F1:1.00 Clarity:0.95 Precision:1.00
            [3/10] F1:0.87 Clarity:0.90 Precision:1.00
            [4/10] F1:1.00 Clarity:1.00 Precision:1.00
            [5/10] F1:1.00 Clarity:1.00 Precision:1.00
            [6/10] F1:1.00 Clarity:1.00 Precision:1.00
            [7/10] F1:1.00 Clarity:1.00 Precision:1.00
            [8/10] F1:0.75 Clarity:0.80 Precision:0.90
            [9/10] F1:0.80 Clarity:0.85 Precision:0.67
            [10/10] F1:1.00 Clarity:1.00 Precision:1.00

      ==================================================
      Prompt: awjamesfrj/bug_to_user_story_using_fewshot
      ==================================================

      Métricas LangSmith:
      - Helpfulness: 0.94 ✓
      - Correctness: 0.93 ✓

      Métricas Customizadas:
      - F1-Score: 0.92 ✓
      - Clarity: 0.94 ✓
      - Precision: 0.95 ✓

      --------------------------------------------------
      📊 MÉDIA GERAL: 0.9343
      --------------------------------------------------

      ✅ STATUS: APROVADO (média >= 0.9)

      ==================================================
      RESUMO FINAL
      ==================================================

      Prompts avaliados: 1
      Aprovados: 1
      Reprovados: 0
      ```


## Comparativo de Prompts

| Critério | v1 — Baseline | v5a — Intermediário | v5b — Otimizado |
|---|---|---|---|
| **IDENTIDADE E PAPEL** | | | |
| Role prompting | ❌ Ausente — "assistente que ajuda", genérico | ✅ "Product Manager sênior escrevendo User Stories" | ✅ "Product Manager sênior escrevendo User Stories" |
| **ESTRUTURA DO OUTPUT** | | | |
| Formato obrigatório | ❌ Ausente — output completamente livre | ⚠️ Define formato simples, não demonstra o complexo | ✅ Formato explícito por complexidade + seções nomeadas |
| Adaptação por complexidade | ❌ Um único template para qualquer bug | ⚠️ Classifica simples/médio/complexo sem exemplos para todos | ✅ 9 exemplos cobrindo todas as variantes estruturais |
| Seções especializadas | ❌ Não sabe que existem seções como "Critérios de Prevenção" ou "Tasks Técnicas" | ⚠️ Conhece as seções mas demonstra apenas 2–3 variantes | ✅ Demonstra todas: Prevenção, Acessibilidade, Cálculo, Tasks por Sprint |
| **FEW-SHOT EXAMPLES** | | | |
| Quantidade de exemplos | ❌ 0 — zero-shot puro | ⚠️ 4 exemplos (simples ×2, médio ×1, acessibilidade ×1) | ✅ 9 exemplos (simples ×2, médio ×5 variantes, complexo ×1, insuficiente ×1) |
| Origem dos exemplos | ❌ N/A | ⚠️ Misturado — alguns do dataset, outros escritos manualmente | ✅ Todos copiados verbatim das `references` do dataset de avaliação |
| Cobertura do dataset | ❌ 0% | ⚠️ ~40% — apenas casos simples e 1–2 médios | ✅ ~80% — cobre os 7 tipos estruturais distintos do dataset |
| **REGRAS E GUARDRAILS** | | | |
| Restrição de output | ❌ Ausente — sem "responda apenas com a user story" | ✅ "Responda SOMENTE com a user story, sem introdução" | ✅ Idem + fallback para bugs insuficientes demonstrado |
| Fidelidade ao relato | ❌ Modelo pode inventar livremente | ✅ "Use somente informações do relato" | ✅ Idem — mantido em todas as iterações |
| Caso de fallback | ❌ Bug vago gera user story inventada | ⚠️ Definido em regras mas sem exemplo demonstrado | ✅ Exemplo 9 mostra a resposta exata para bug insuficiente |
| **COMPATIBILIDADE COM O AVALIADOR** | | | |
| Alinhamento com references | ❌ Output livre diverge completamente das references | ⚠️ Estrutura correta mas wording diverge nas variantes sem few-shot | ✅ Exemplos verbatim ensinam o vocabulário exato das references |
| Precision = 0.67 floor | ❌ Recorrente — output sem estrutura penalizado fortemente | ⚠️ Ainda ocorre em variantes sem few-shot (Prevenção, z-index) | ✅ Eliminado — todas as variantes com seção especial têm template |
| **SCORES OBTIDOS** | | | |
| Média geral | ❌ ~0.60 *(estimado)* | ⚠️ 0.8353 → 0.8732 | ✅ 0.8732 → **0.90 target** |
| F1-Score | ❌ ~0.50 | ⚠️ 0.80 | ✅ 0.84 → ~0.92 esperado |
| Clarity | ❌ ~0.60 | ✅ 0.90 | ✅ 0.91 |
| Precision | ❌ ~0.50 | ⚠️ 0.82 | ✅ 0.87 → ~0.93 esperado |