# Registro de Pontuações

## Desafio 01 — Soma de pares

**Data/Hora:** 2026-03-09 00:00 UTC

| Critério | Pontos Obtidos | Pontos Máximos | Observação |
|---|---|---|---|
| Corretude | 50 | 50 | 11/11 testes passando (básicos, borda e aleatórios) |
| Tempo | 5 | 25 | O(n²) — meta era O(n). Usa dois loops aninhados em vez de hash set |
| Memória | 15 | 15 | O(1) — dentro do alvo O(n) |
| Clareza | 7 | 10 | 10 linhas, nomes razoáveis, docstring. Loop interno redundante (verifica pares duas vezes) |
| **Total** | **77** | **100** | **Abaixo do aceitável (< 80)** |

### Justificativa

A solução acerta todos os testes, mas usa força bruta O(n²) com dois loops aninhados percorrendo a lista inteira. A abordagem ideal seria usar um `set` para buscar o complemento (`target - num`) em O(1) por elemento, atingindo O(n) no total. O loop interno também é ineficiente pois percorre todos os índices (incluindo anteriores), verificando cada par duas vezes. A clareza é boa, mas perde pontos pela redundância na lógica.

### Melhor solução

```python
def has_pair_with_sum(nums: list[int], target: int) -> bool:
    vistos = set()

    for num in nums:
        complemento = target - num
        if complemento in vistos:
            return True
        vistos.add(num)

    return False
```