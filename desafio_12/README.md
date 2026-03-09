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
