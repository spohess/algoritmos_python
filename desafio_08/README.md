# Desafio 08 — Prefixo comum mais longo

## Enunciado

Dada uma lista de strings, encontrar o maior prefixo comum entre todas elas. Se não houver prefixo comum, retornar uma string vazia.

## Assinatura

```python
def longest_common_prefix(strs: list[str]) -> str
```

## Complexidade alvo

- **Tempo:** O(S), onde S é a soma dos comprimentos de todas as strings
- **Memória:** O(1) (além da saída)

## Principais casos de borda

- Lista vazia
- Lista com uma única string
- Strings sem nenhum prefixo em comum
- Todas as strings idênticas
- Uma string vazia na lista

## Exemplos

1. **Entrada:** `strs = ["flower", "flow", "flight"]`
   **Saída esperada:** `"fl"`

2. **Entrada:** `strs = ["dog", "car", "race"]`
   **Saída esperada:** `""`

3. **Entrada:** `strs = ["abc", "abc", "abc"]`
   **Saída esperada:** `"abc"`
