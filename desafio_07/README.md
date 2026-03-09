# Desafio 07 — Interseção de dois arrays

## Enunciado

Dados dois arrays de inteiros, retornar os elementos que estão presentes em ambos, sem repetição. A ordem dos elementos no resultado não é relevante.

## Assinatura

```python
def intersection(nums1: list[int], nums2: list[int]) -> list[int]
```

## Complexidade alvo

- **Tempo:** O(n + m)
- **Memória:** O(n + m)

## Principais casos de borda

- Um ou ambos os arrays vazios
- Nenhum elemento em comum
- Arrays idênticos
- Arrays com muitos duplicados

## Exemplos

1. **Entrada:** `nums1 = [1, 2, 2, 1], nums2 = [2, 2]`
   **Saída esperada:** `[2]`

2. **Entrada:** `nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4]`
   **Saída esperada:** `[4, 9] (ordem pode variar)`

3. **Entrada:** `nums1 = [1, 3], nums2 = [2, 4]`
   **Saída esperada:** `[]`
