# Desafio 01 — Soma de pares

## Enunciado

Dado um array de inteiros e um valor alvo `k`, determinar se existe um par de elementos no array cuja soma é exatamente `k`.

## Assinatura

```python
def has_pair_with_sum(nums: list[int], target: int) -> bool
```

## Complexidade alvo

- **Tempo:** O(n)
- **Memória:** O(n)

## Principais casos de borda

- Array vazio
- Array com um único elemento
- Múltiplos pares válidos
- Elementos negativos
- Alvo zero com elementos positivos e negativos
- Elementos duplicados (e.g., `[3, 3]` com alvo `6`)
