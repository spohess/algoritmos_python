# Desafio 17 — Validar parênteses

## Enunciado

Dada uma string contendo apenas os caracteres `(`, `)`, `{`, `}`, `[` e `]`, determinar se a sequência de parênteses é válida. Uma sequência é válida se cada abertura tem um fechamento correspondente na ordem correta.

## Assinatura

```python
def is_valid_parentheses(s: str) -> bool
```

## Complexidade alvo

- **Tempo:** O(n)
- **Memória:** O(n)

## Principais casos de borda

- String vazia (válida)
- Apenas aberturas
- Apenas fechamentos
- Tipos misturados e intercalados
- Fechamento sem abertura correspondente

## Exemplos

1. **Entrada:** `s = "()[]{}"`
   **Saída esperada:** `True`

2. **Entrada:** `s = "(]"`
   **Saída esperada:** `False`

3. **Entrada:** `s = "([{}])"`
   **Saída esperada:** `True`
