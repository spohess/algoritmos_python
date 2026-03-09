# Desafio 27 — Dijkstra

## Enunciado

Dado um grafo ponderado com pesos não negativos representado como lista de adjacência, um número de vértices `n` e um vértice de origem `src`, retornar uma lista de distâncias mínimas de `src` a cada vértice. Se um vértice não for alcançável, a distância deve ser -1.

## Assinatura

```python
def dijkstra(n: int, edges: list[list[int]], src: int) -> list[int]
```

## Complexidade alvo

- **Tempo:** O((V + E) log V)
- **Memória:** O(V + E)

## Principais casos de borda

- Grafo desconexo
- Vértice origem sem arestas
- Grafo com um único vértice
- Múltiplos caminhos para o mesmo destino
- Arestas com peso zero
