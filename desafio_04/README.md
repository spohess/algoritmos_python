# Desafio 04 — Primeiro caractere não repetido

## Enunciado

Dada uma string, retornar o primeiro caractere que aparece exatamente uma vez. Caso não exista, retornar uma string vazia.

## Assinatura

```python
def first_unique_char(s: str) -> str
```

## Complexidade alvo

- **Tempo:** O(n)
- **Memória:** O(1) (alfabeto finito)

## Principais casos de borda

- String vazia
- Todos os caracteres repetidos
- Apenas um caractere
- Caractere único no final da string
