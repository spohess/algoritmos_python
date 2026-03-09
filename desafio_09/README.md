# Desafio 09 — Palíndromo ignorando símbolos

## Enunciado

Dada uma string, verificar se é um palíndromo considerando apenas caracteres alfanuméricos e ignorando diferenças de caixa.

## Assinatura

```python
def is_palindrome(s: str) -> bool
```

## Complexidade alvo

- **Tempo:** O(n)
- **Memória:** O(1)

## Principais casos de borda

- String vazia (considerada palíndromo)
- String com apenas símbolos
- String com um único caractere alfanumérico
- Palíndromo com números
- String com espaços e pontuação

## Exemplos

1. **Entrada:** `s = "A man, a plan, a canal: Panama"`
   **Saída esperada:** `True`

2. **Entrada:** `s = "race a car"`
   **Saída esperada:** `False`

3. **Entrada:** `s = "!@#$%"`
   **Saída esperada:** `True`
