# Desafio 26 — Ordenação topológica

## Enunciado

Dado um número de vértices `n` (numerados de 0 a n-1) e uma lista de arestas direcionadas `[u, v]` (u → v), retornar uma ordenação topológica válida. Se o grafo contiver ciclo, retornar uma lista vazia.

## Assinatura

```python
def topological_sort(n: int, edges: list[list[int]]) -> list[int]
```

## Complexidade alvo

- **Tempo:** O(V + E)
- **Memória:** O(V + E)

## Principais casos de borda

- Grafo sem arestas
- Grafo com ciclo
- Grafo linear (cadeia)
- Vértice isolado
- Múltiplas ordenações válidas

## Exemplos

1. **Entrada:** `n = 4, edges = [[0,1],[0,2],[1,3],[2,3]]`
   **Saída esperada:** `Uma ordem válida, por exemplo [0, 1, 2, 3]`

2. **Entrada:** `n = 3, edges = [[0,1],[1,2]]`
   **Saída esperada:** `[0, 1, 2]`

3. **Entrada:** `n = 3, edges = [[0,1],[1,2],[2,0]]`
   **Saída esperada:** `[]`
