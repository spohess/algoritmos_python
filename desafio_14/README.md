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
