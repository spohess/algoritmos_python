# Desafio 15 — Menor substring que contém todos caracteres

## Enunciado

Dadas duas strings `s` e `t`, encontrar a menor substring de `s` que contém todos os caracteres de `t` (incluindo duplicados). Se não existir, retornar uma string vazia.

## Assinatura

```python
def min_window_substring(s: str, t: str) -> str
```

## Complexidade alvo

- **Tempo:** O(n), onde n = len(s)
- **Memória:** O(k), onde k é o tamanho do alfabeto de t

## Principais casos de borda

- t vazio (retornar string vazia)
- s menor que t
- s igual a t
- Caracteres duplicados em t
- Múltiplas janelas mínimas de mesmo tamanho (retornar qualquer uma)
