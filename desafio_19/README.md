# Desafio 19 — BFS menor caminho em grade

## Enunciado

Dada uma grade (matriz) binária onde `0` representa célula livre e `1` representa bloqueio, encontrar o menor número de passos para ir da posição `(0, 0)` até `(linhas-1, colunas-1)`, movendo-se nas 4 direções cardinais. Se não houver caminho, retornar -1. A célula inicial e final são garantidamente `0`.

## Assinatura

```python
def shortest_path_grid(grid: list[list[int]]) -> int
```

## Complexidade alvo

- **Tempo:** O(R × C)
- **Memória:** O(R × C)

## Principais casos de borda

- Grade 1×1 (retornar 0)
- Sem caminho possível
- Grade sem bloqueios
- Caminho exige contornar bloqueios
