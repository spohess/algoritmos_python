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
