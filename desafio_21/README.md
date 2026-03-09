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

## Exemplos

1. **Entrada:** `nums = [1,1,1,2,2,3], k = 2`
   **Saída esperada:** `[1, 2] (ordem pode variar)`

2. **Entrada:** `nums = [1], k = 1`
   **Saída esperada:** `[1]`

3. **Entrada:** `nums = [4,4,4,5,5,6], k = 1`
   **Saída esperada:** `[4]`
