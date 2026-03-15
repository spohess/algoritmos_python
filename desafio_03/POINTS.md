# Pontuação — Desafio 03

## 2026-03-15 15:00

### Resultado: 73 / 100 *(corrigido)*

| Critério         | Peso | Nota | Justificativa |
|------------------|------|------|---------------|
| Corretude        | 50   | 50   | Todos os casos testados passaram (básicos, borda, negativos, aleatórios) |
| Tempo            | 25   | 0    | Varredura linear em `result` para cada elemento → O(n²); alvo é O(n). Não é questão de idioma da linguagem — em qualquer linguagem a escolha de verificar existência por varredura é O(n) por elemento. Alcançar O(n) exige uma estrutura de lookup O(1) (hash table, bitmap etc.) |
| Memória          | 15   | 15   | Apenas a lista `result` como estrutura extra → O(n) ✓ |
| Clareza          | 10   | 8    | Lógica clara e dentro do limite de linhas. Único ponto fraco algorítmico: `find = True` sem `break`, o que faz a varredura continuar após encontrar o elemento — desperdício de iterações em qualquer linguagem |

### Diagnóstico

A solução está **correta**, mas falha no critério de tempo. A decisão algorítmica de varrer `result` inteiro para checar existência é O(n) por elemento → O(n²) total. Para atingir O(n), a escolha correta é uma estrutura de lookup O(1) — em Python isso é um `set`, mas em C seria uma hash table, em outra linguagem seria um bitmap ou similar. O problema é a escolha de algoritmo, não o idioma.

O ponto sobre `find = True` sem `break` também é independente de linguagem: após confirmar que o elemento já existe, continuar varrendo é trabalho desnecessário.

**Aprovação:** ❌ Abaixo de 80 (aceitável)
