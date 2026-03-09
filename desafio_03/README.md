# Desafio 03 — Remover duplicados mantendo ordem

## Enunciado

Dado um array de inteiros, retornar um novo array sem elementos duplicados, preservando a ordem da primeira ocorrência de cada elemento.

## Assinatura

```python
def remove_duplicates(nums: list[int]) -> list[int]
```

## Complexidade alvo

- **Tempo:** O(n)
- **Memória:** O(n)

## Principais casos de borda

- Array vazio
- Array sem duplicados
- Todos os elementos iguais
- Duplicados intercalados

## Exemplos

1. **Entrada:** `nums = [1, 2, 2, 3, 1, 4]`
   **Saída esperada:** `[1, 2, 3, 4]`

2. **Entrada:** `nums = [5, 5, 5, 5]`
   **Saída esperada:** `[5]`

3. **Entrada:** `nums = []`
   **Saída esperada:** `[]`
