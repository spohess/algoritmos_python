# Desafio 22 — K-ésimo menor elemento

## Enunciado

Dado um array de inteiros e um inteiro `k` (1-indexed), retornar o k-ésimo menor elemento do array.

## Assinatura

```python
def kth_smallest(nums: list[int], k: int) -> int
```

## Complexidade alvo

- **Tempo:** O(n) caso médio
- **Memória:** O(1) auxiliar (in-place) ou O(n)

## Principais casos de borda

- k igual a 1 (menor elemento)
- k igual ao tamanho do array (maior elemento)
- Array com duplicados
- Array já ordenado
- Array em ordem decrescente
