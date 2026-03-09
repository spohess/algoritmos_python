# Desafio 10 — Mesclar intervalos

## Enunciado

Dada uma lista de intervalos representados como pares `[início, fim]`, unir todos os intervalos sobrepostos e retornar a lista de intervalos resultante ordenada por início.

## Assinatura

```python
def merge_intervals(intervals: list[list[int]]) -> list[list[int]]
```

## Complexidade alvo

- **Tempo:** O(n log n)
- **Memória:** O(n)

## Principais casos de borda

- Lista vazia
- Um único intervalo
- Nenhum intervalo sobreposto
- Todos os intervalos sobrepostos
- Intervalos adjacentes (e.g., `[1,2]` e `[2,3]`)
- Intervalos não ordenados na entrada
