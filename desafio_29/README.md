# Desafio 29 — Longest Increasing Subsequence

## Enunciado

Dado um array de inteiros, retornar o tamanho da maior subsequência estritamente crescente (não necessariamente contígua).

## Assinatura

```python
def length_of_lis(nums: list[int]) -> int
```

## Complexidade alvo

- **Tempo ideal:** O(n log n)
- **Memória:** O(n)

## Principais casos de borda

- Array vazio
- Array com um elemento
- Array totalmente crescente
- Array totalmente decrescente
- Todos os elementos iguais
- Elementos negativos
