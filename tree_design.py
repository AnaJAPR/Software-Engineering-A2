from abc import ABC, abstractmethod

## Composite
class Node(ABC):
    """Interface base para todos os nós."""
    @abstractmethod
    def accept(self, visitor):
        raise NotImplementedError()

    def get_children(self):
        return []

class DecisionNode(Node):
    """Nó representando um ponto de decisão como 'Dor intensa?' e seus ramos são as respostas (Sim/Não)."""
    def __init__(self, question):
        self.question = question
        self.children = []  ## Lista de pares (condição, nó)

    def add_child(self, condition, node):
        self.children.append((condition, node))

    def accept(self, visitor):
        visitor.visit_decision(self)

    def get_children(self):
        return [child for cond, child in self.children]


class LeafNode(Node):
    """Nó folha com resultado final (Emergência, Urgência ou Não urgente). Este nó não tem filhos."""
    def __init__(self, result):
        self.result = result

    def accept(self, visitor):
        visitor.visit_leaf(self)

## Iterator
class PreOrderIterator:
    """Percorre os nós em pré-ordem."""
    def __init__(self, root):
        self.stack = [root]

    def __iter__(self):
        return self

    def __next__(self):
        if not self.stack:
            raise StopIteration()
        current = self.stack.pop()
        ## Adiciona filhos ao stack (ordem reversa para a pré-ordem estar correta)
        children = current.get_children()
        for child in reversed(children):
            self.stack.append(child)
        return current

## Visitor
class Visitor(ABC):
    """Realiza operações que a árvore em si não sabe fazer, como contar folhas e calcular profundidade."""
    def visit_decision(self, node):
        pass
    
    @abstractmethod
    def visit_leaf(self, node):
        pass


class CountLeavesVisitor(Visitor):
    """Descobre quantos resultados finais existem na árvore."""
    def __init__(self):
        self.count = 0

    def visit_leaf(self, leaf):
        print(f"[Visitor] Visitando folha: {leaf.result}")
        self.count += 1


class DepthVisitor(Visitor):
    """Descobre a profundidade da árvore de decisão."""
    def __init__(self):
        self.max_depth = 0
        self.current_depth = 0

    def visit_decision(self, node):
        self.current_depth += 1
        self.max_depth = max(self.max_depth, self.current_depth)

    def visit_leaf(self, leaf):
        ## folha também conta como profundidade
        self.max_depth = max(self.max_depth, self.current_depth + 1)

