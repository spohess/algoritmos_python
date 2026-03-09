# Algoritmos em Python — 30 Desafios

Repositório de estudo de algoritmos com 30 desafios organizados por dificuldade crescente. Cada desafio contém a assinatura da função a ser implementada, testes automatizados e um enunciado com metas de complexidade.

## Objetivo

Praticar algoritmos e estruturas de dados implementando soluções que passem em todos os testes e respeitem as metas de complexidade de tempo e memória definidas em cada desafio.

## Requisitos

- Python 3.12+
- pytest

## Configuração do ambiente

### Criar virtualenv

```bash
python3 -m venv .venv
```

### Ativar virtualenv

```bash
source .venv/bin/activate
```

### Instalar dependências

```bash
pip install -r requirements.txt
```

## Executando os testes

### Rodar todos os testes

```bash
pytest -q
```

### Rodar testes de um único desafio

```bash
pytest -q desafio_01/
```

## Métrica de avaliação por desafio

Use uma métrica em 4 eixos para cada desafio:

### Métrica

- Corretude: passar em casos básicos, borda e aleatórios.
- Complexidade alvo: tempo e memória máximos aceitáveis.
- Robustez: solução clara, sem depender de casos especiais escondidos.
- Qualidade de implementação: código legível, nomes bons, sem duplicação desnecessária.

### Score sugerido por desafio: 100 pontos

- 50 pts: corretude
- 25 pts: tempo
- 15 pts: memória
- 10 pts: clareza

### Regra prática de aprovação

- 80+: aceitável
- 90+: boa
- 100: solução de referência

### Como medir na prática

Para cada desafio, sua meta deve ser:

- Acertar todos os testes que você mesmo montar.
- Bater a complexidade alvo.
- Não usar mais do que a memória alvo.
- Explicar em 3 a 6 linhas por que sua solução atinge essa meta.

### Sugestão de limite de clareza

- Fácil: até 25 linhas
- Médio: até 40 linhas
- Difícil: até 60 linhas

Esse limite não entra como objetivo principal, só como freio contra código confuso.

## Lista de desafios

| #  | Desafio                                    | Complexidade alvo        |
|----|--------------------------------------------|--------------------------|
| 01 | Soma de pares                              | O(n)                     |
| 02 | Maior sequência crescente contínua         | O(n)                     |
| 03 | Remover duplicados mantendo ordem          | O(n)                     |
| 04 | Primeiro caractere não repetido            | O(n)                     |
| 05 | Verificar anagrama                         | O(n)                     |
| 06 | Rotacionar array em k                      | O(n)                     |
| 07 | Interseção de dois arrays                  | O(n + m)                 |
| 08 | Prefixo comum mais longo                   | O(S)                     |
| 09 | Palíndromo ignorando símbolos              | O(n)                     |
| 10 | Mesclar intervalos                         | O(n log n)               |
| 11 | Buscar intervalo que contém ponto          | O(log n)                 |
| 12 | Duas somas em array ordenado               | O(n)                     |
| 13 | Subarray com soma máxima                   | O(n)                     |
| 14 | Janela deslizante com soma máxima tamanho k| O(n)                     |
| 15 | Menor substring que contém todos caracteres| O(n)                     |
| 16 | Produto do array exceto ele mesmo          | O(n)                     |
| 17 | Validar parênteses                         | O(n)                     |
| 18 | Simplificar caminho Unix                   | O(n)                     |
| 19 | BFS menor caminho em grade                 | O(R×C)                   |
| 20 | Número de ilhas                            | O(R×C)                   |
| 21 | Top K elementos frequentes                 | O(n log k)               |
| 22 | K-ésimo menor elemento                     | O(n) médio               |
| 23 | Detectar ciclo em linked list              | O(n) tempo, O(1) memória |
| 24 | Inverter árvore binária                    | O(n)                     |
| 25 | Menor ancestral comum                      | O(n)                     |
| 26 | Ordenação topológica                       | O(V+E)                   |
| 27 | Dijkstra                                   | O((V+E) log V)           |
| 28 | Coin Change                                | O(n × valor)             |
| 29 | Longest Increasing Subsequence             | O(n log n)               |
| 30 | Edit Distance                              | O(n × m)                 |
