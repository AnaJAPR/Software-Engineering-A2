from tree_design import TreeBuilder, SplittingState, StoppingState, PruningState, PreOrderIterator, CountLeavesVisitor, DepthVisitor

builder = TreeBuilder()

#estado 1: construir a árvore
builder.set_state(SplittingState())
tree = builder.build()

#estado 2: “parar” construção (mock)
builder.set_state(StoppingState())
tree = builder.build()

#estado 3: simular poda (mock)
builder.set_state(PruningState())
tree = builder.build()

iterator = PreOrderIterator(tree)
print("#######"*8)

for node in iterator:
    if hasattr(node, "question"):
        print(f"[Iterator] Nó de decisão: {node.question}")
    else:
        print(f"[Iterator] Folha: {node.result}")

print("#########"*8)
leaf_counter = CountLeavesVisitor()

iterator = PreOrderIterator(tree)
for node in iterator:
    node.accept(leaf_counter)

print(f"Total de categorias finais: {leaf_counter.count}")

depth_visitor = DepthVisitor()

## Para calcular profundidade, percorremos manualmente simulando profundidade:
def traverse(node, visitor, depth=0):
    visitor.current_depth = depth
    node.accept(visitor)
    for child in node.get_children():
        traverse(child, visitor, depth + 1)

traverse(tree, depth_visitor)
print(f"Profundidade máxima da árvore: {depth_visitor.max_depth}")