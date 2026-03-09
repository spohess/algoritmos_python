# Desafio 24 — Inverter árvore binária

## Enunciado

Dada a raiz de uma árvore binária, inverter a árvore (trocar os filhos esquerdo e direito de cada nó recursivamente) e retornar a raiz.

## Assinatura

```python
def invert_tree(root: TreeNode | None) -> TreeNode | None
```

## Complexidade alvo

- **Tempo:** O(n)
- **Memória:** O(h), onde h é a altura da árvore

## Principais casos de borda

- Árvore vazia
- Árvore com um único nó
- Árvore completamente desbalanceada (tipo lista)
- Árvore completa

## Exemplos

1. **Entrada:** `root = [4, 2, 7, 1, 3, 6, 9]`
   **Saída esperada:** `[4, 7, 2, 9, 6, 3, 1]`

2. **Entrada:** `root = [1, 2, 3]`
   **Saída esperada:** `[1, 3, 2]`

3. **Entrada:** `root = []`
   **Saída esperada:** `[]`
