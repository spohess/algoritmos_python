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

## Exemplos

1. **Entrada:** `nums = [10, 9, 2, 5, 3, 7, 101, 18]`
   **Saída esperada:** `4`

2. **Entrada:** `nums = [1, 2, 3, 4, 5]`
   **Saída esperada:** `5`

3. **Entrada:** `nums = [5, 4, 3, 2, 1]`
   **Saída esperada:** `1`
