# Desafio 23 — Detectar ciclo em linked list

## Enunciado

Dada a cabeça de uma lista ligada, determinar se a lista contém um ciclo.

## Assinatura

```python
def has_cycle(head: ListNode | None) -> bool
```

## Complexidade alvo

- **Tempo:** O(n)
- **Memória:** O(1)

## Principais casos de borda

- Lista vazia
- Lista com um único nó sem ciclo
- Lista com um único nó apontando para si mesmo
- Ciclo no meio da lista
- Ciclo no final voltando para o início
