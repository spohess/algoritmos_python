# Desafio 13 — Subarray com soma máxima

## Enunciado

Dado um array de inteiros, encontrar o subarray contíguo com a maior soma e retornar essa soma. O array contém pelo menos um elemento.

## Assinatura

```python
def max_subarray_sum(nums: list[int]) -> int
```

## Complexidade alvo

- **Tempo:** O(n)
- **Memória:** O(1)

## Principais casos de borda

- Array com um único elemento
- Todos os elementos negativos
- Todos os elementos positivos
- Array com zeros
- Soma máxima no meio, início ou fim

## Exemplos

1. **Entrada:** `nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]`
   **Saída esperada:** `6`

2. **Entrada:** `nums = [-3, -2, -5, -1]`
   **Saída esperada:** `-1`

3. **Entrada:** `nums = [1, 2, 3, 4]`
   **Saída esperada:** `10`
