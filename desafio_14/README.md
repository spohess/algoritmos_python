# Desafio 14 — Janela deslizante com soma máxima tamanho k

## Enunciado

Dado um array de inteiros e um inteiro `k`, retornar a maior soma entre todos os subarrays contíguos de tamanho exatamente `k`. Garantido que `k <= len(nums)` e `k >= 1`.

## Assinatura

```python
def max_sum_window(nums: list[int], k: int) -> int
```

## Complexidade alvo

- **Tempo:** O(n)
- **Memória:** O(1)

## Principais casos de borda

- k igual ao tamanho do array
- k igual a 1
- Todos os elementos iguais
- Elementos negativos

## Exemplos

1. **Entrada:** `nums = [1, 3, -1, 2, 5, 1], k = 3`
   **Saída esperada:** `8`

2. **Entrada:** `nums = [1, 2, 3], k = 3`
   **Saída esperada:** `6`

3. **Entrada:** `nums = [-1, -2, -3, -4], k = 2`
   **Saída esperada:** `-3`
