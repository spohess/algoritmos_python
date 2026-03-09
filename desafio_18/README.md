# Desafio 18 — Simplificar caminho Unix

## Enunciado

Dado um caminho absoluto Unix (começando com `/`), simplificá-lo para o caminho canônico. Regras: `..` volta um nível, `.` permanece no diretório atual, barras múltiplas são tratadas como uma, e barras finais são removidas.

## Assinatura

```python
def simplify_path(path: str) -> str
```

## Complexidade alvo

- **Tempo:** O(n)
- **Memória:** O(n)

## Principais casos de borda

- Caminho raiz `/`
- Múltiplas barras consecutivas
- `..` no nível raiz (não pode subir além da raiz)
- Caminho com `.` e `..` intercalados
- Nomes de diretório contendo pontos (e.g., `...` é um nome válido)
