# Desafio 06 — Rotacionar array em k

## Enunciado

Dado um array de inteiros e um valor `k`, rotacionar o array `k` posições para a direita. O array deve ser retornado como um novo array.

## Assinatura

```python
def rotate_array(nums: list[int], k: int) -> list[int]
```

## Complexidade alvo

- **Tempo:** O(n)
- **Memória:** O(n)

## Principais casos de borda

- Array vazio
- k igual a zero
- k maior que o tamanho do array
- k igual ao tamanho do array
- Array com um único elemento

## Exemplos

1. **Entrada:** `nums = [1, 2, 3, 4, 5], k = 2`
   **Saída esperada:** `[4, 5, 1, 2, 3]`

2. **Entrada:** `nums = [1, 2, 3], k = 0`
   **Saída esperada:** `[1, 2, 3]`

3. **Entrada:** `nums = [1, 2, 3], k = 5`
   **Saída esperada:** `[2, 3, 1]`
