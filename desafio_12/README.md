# Desafio 12 — Duas somas em array ordenado

## Enunciado

Dado um array de inteiros ordenado em ordem crescente e um valor alvo `target`, encontrar os índices (0-based) de dois elementos cuja soma é exatamente `target`. Retornar a tupla `(i, j)` com `i < j`. Se não existir, retornar `(-1, -1)`.

## Assinatura

```python
def two_sum_sorted(nums: list[int], target: int) -> tuple[int, int]
```

## Complexidade alvo

- **Tempo:** O(n)
- **Memória:** O(1)

## Principais casos de borda

- Array com dois elementos
- Nenhum par válido
- Múltiplos pares válidos (retornar qualquer um)
- Elementos negativos
- Elementos duplicados

## Exemplos

1. **Entrada:** `nums = [2, 7, 11, 15], target = 9`
   **Saída esperada:** `(0, 1)`

2. **Entrada:** `nums = [1, 2, 3, 4, 6], target = 10`
   **Saída esperada:** `(3, 4)`

3. **Entrada:** `nums = [1, 2, 3, 9], target = 20`
   **Saída esperada:** `(-1, -1)`
