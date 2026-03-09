# Desafio 25 — Menor ancestral comum

## Enunciado

Dada a raiz de uma árvore binária e dois nós `p` e `q`, encontrar o menor ancestral comum (LCA) dos dois nós. Garantido que ambos os nós existem na árvore.

## Assinatura

```python
def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode
```

## Complexidade alvo

- **Tempo:** O(n)
- **Memória:** O(h), onde h é a altura da árvore

## Principais casos de borda

- Um dos nós é a própria raiz
- Um nó é ancestral do outro
- Ambos os nós estão no mesmo lado da árvore
- Ambos os nós estão em lados opostos
- Árvore com apenas dois nós

## Exemplos

1. **Entrada:** `root = [3,5,1,6,2,0,8,None,None,7,4], p = 5, q = 1`
   **Saída esperada:** `3`

2. **Entrada:** `root = [3,5,1,6,2,0,8,None,None,7,4], p = 5, q = 4`
   **Saída esperada:** `5`

3. **Entrada:** `root = [1,2], p = 1, q = 2`
   **Saída esperada:** `1`
