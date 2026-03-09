# Desafio 05 — Verificar anagrama

## Enunciado

Dadas duas strings, determinar se são anagramas uma da outra, ignorando espaços e diferenças de caixa (maiúsculas/minúsculas).

## Assinatura

```python
def is_anagram(s1: str, s2: str) -> bool
```

## Complexidade alvo

- **Tempo:** O(n)
- **Memória:** O(1) (alfabeto finito)

## Principais casos de borda

- Strings vazias
- Strings com apenas espaços
- Diferenças de caixa
- Strings de tamanhos diferentes (após remover espaços)
- Caracteres especiais e números

## Exemplos

1. **Entrada:** `s1 = "listen", s2 = "silent"`
   **Saída esperada:** `True`

2. **Entrada:** `s1 = "a gentleman", s2 = "elegant man"`
   **Saída esperada:** `True`

3. **Entrada:** `s1 = "hello", s2 = "world"`
   **Saída esperada:** `False`
