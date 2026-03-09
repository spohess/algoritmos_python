# Desafio 21 — Top K elementos frequentes

## Enunciado

Dado um array de inteiros e um inteiro `k`, retornar os `k` elementos mais frequentes. A ordem dos elementos no resultado não é relevante.

## Assinatura

```python
def top_k_frequent(nums: list[int], k: int) -> list[int]
```

## Complexidade alvo

- **Tempo:** O(n log k) ou melhor
- **Memória:** O(n)

## Principais casos de borda

- k igual ao número de elementos distintos
- Todos os elementos iguais
- k igual a 1
- Empate de frequência (retornar quaisquer k com maior frequência)
