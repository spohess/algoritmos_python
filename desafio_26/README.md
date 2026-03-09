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
