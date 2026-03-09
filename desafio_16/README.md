# Desafio 16 — Produto do array exceto ele mesmo

## Enunciado

Dado um array de inteiros, retornar um array onde cada posição contém o produto de todos os elementos do array original exceto o elemento naquela posição. Resolver sem usar divisão.

## Assinatura

```python
def product_except_self(nums: list[int]) -> list[int]
```

## Complexidade alvo

- **Tempo:** O(n)
- **Memória:** O(n) para a saída (O(1) memória auxiliar além da saída)

## Principais casos de borda

- Array com um zero
- Array com múltiplos zeros
- Array com dois elementos
- Elementos negativos
- Array com todos os elementos iguais a 1
