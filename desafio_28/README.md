# Desafio 28 — Coin Change

## Enunciado

Dado um array de denominações de moedas e um valor alvo, retornar o menor número de moedas necessário para formar exatamente o valor. Se não for possível, retornar -1. Cada denominação pode ser usada quantas vezes for necessário.

## Assinatura

```python
def coin_change(coins: list[int], amount: int) -> int
```

## Complexidade alvo

- **Tempo:** O(n × amount), onde n é o número de denominações
- **Memória:** O(amount)

## Principais casos de borda

- Valor zero (retornar 0)
- Nenhuma combinação possível
- Uma única moeda
- Valor igual a uma denominação
- Denominações não ordenadas

## Exemplos

1. **Entrada:** `coins = [1, 5, 10, 25], amount = 30`
   **Saída esperada:** `2`

2. **Entrada:** `coins = [2], amount = 3`
   **Saída esperada:** `-1`

3. **Entrada:** `coins = [1, 2, 3], amount = 0`
   **Saída esperada:** `0`
