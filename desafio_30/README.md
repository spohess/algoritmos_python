# Desafio 30 — Edit Distance

## Enunciado

Dadas duas strings `word1` e `word2`, retornar a distância de Levenshtein (número mínimo de operações para transformar `word1` em `word2`). As operações permitidas são: inserir um caractere, deletar um caractere, substituir um caractere.

## Assinatura

```python
def edit_distance(word1: str, word2: str) -> int
```

## Complexidade alvo

- **Tempo:** O(n × m)
- **Memória:** O(min(n, m)) ideal, O(n × m) aceitável

## Principais casos de borda

- Uma ou ambas as strings vazias
- Strings iguais
- Uma string é prefixo da outra
- Strings completamente diferentes
- Strings de um único caractere

## Exemplos

1. **Entrada:** `word1 = "horse", word2 = "ros"`
   **Saída esperada:** `3`

2. **Entrada:** `word1 = "intention", word2 = "execution"`
   **Saída esperada:** `5`

3. **Entrada:** `word1 = "abc", word2 = "abc"`
   **Saída esperada:** `0`
