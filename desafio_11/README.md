# Desafio 11 — Buscar intervalo que contém ponto

## Enunciado

Dada uma lista de intervalos não sobrepostos ordenados por início e um ponto, retornar o índice do intervalo que contém o ponto. Se nenhum intervalo contiver o ponto, retornar -1.

## Assinatura

```python
def find_interval(intervals: list[list[int]], point: int) -> int
```

## Complexidade alvo

- **Tempo:** O(log n)
- **Memória:** O(1)

## Principais casos de borda

- Lista vazia
- Ponto antes de todos os intervalos
- Ponto depois de todos os intervalos
- Ponto entre dois intervalos (em nenhum)
- Ponto exatamente no início ou fim de um intervalo
