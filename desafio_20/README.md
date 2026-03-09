# Desafio 20 — Número de ilhas

## Enunciado

Dada uma grade (matriz) binária onde `1` representa terra e `0` representa água, contar o número de ilhas. Uma ilha é formada por células de terra conectadas horizontalmente ou verticalmente.

## Assinatura

```python
def count_islands(grid: list[list[int]]) -> int
```

## Complexidade alvo

- **Tempo:** O(R × C)
- **Memória:** O(R × C)

## Principais casos de borda

- Grade vazia
- Grade sem terra (tudo água)
- Grade toda de terra (uma ilha)
- Ilhas diagonais (não são conectadas)
- Grade com uma única célula

## Exemplos

1. **Entrada:** `grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,1,0,0],[0,0,0,1,1]]`
   **Saída esperada:** `3`

2. **Entrada:** `grid = [[1,1,1],[0,1,0],[1,1,1]]`
   **Saída esperada:** `1`

3. **Entrada:** `grid = [[0,0],[0,0]]`
   **Saída esperada:** `0`
