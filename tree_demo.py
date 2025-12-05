from tree_design import DecisionNode, LeafNode, PreOrderIterator, CountLeavesVisitor, DepthVisitor


# Nó raiz
root = DecisionNode("Dor intensa?")

# Árvore do lado "Sim"
node_breath = DecisionNode("Dificuldade de respirar?")
node_emerg = LeafNode("EMERGÊNCIA")
node_urg = LeafNode("URGÊNCIA")

node_breath.add_child("Sim", node_emerg)
node_breath.add_child("Não", node_urg)

# Árvore do lado "Não"
node_accident = DecisionNode("Acidente recente?")
node_non_urg = LeafNode("NÃO URGENTE")

node_accident.add_child("Sim", node_urg)
node_accident.add_child("Não", node_non_urg)

# Conectando ao root
root.add_child("Sim", node_breath)
root.add_child("Não", node_accident)


## Testando o Iterator
iterator = PreOrderIterator(root)

for node in iterator:
    if hasattr(node, "question"):
        print(f"[Iterator] Nó de decisão: {node.question}")
    else:
        print(f"[Iterator] Folha: {node.result}")


## Testando o Visitor de contagem de folhas

print("##############"*5)
counter = CountLeavesVisitor()

iterator = PreOrderIterator(root)
for node in iterator:
    node.accept(counter)

print(f"Total de folhas: {counter.count}")


## Testando visitor de pronfundidade

print("##############"*5)
depth_visitor = DepthVisitor()

def traverse(node, visitor, depth=0):
    visitor.current_depth = depth
    node.accept(visitor)
    for child in node.get_children():
        traverse(child, visitor, depth + 1)

traverse(root, depth_visitor)

print(f"Profundidade máxima da árvore: {depth_visitor.max_depth}")
