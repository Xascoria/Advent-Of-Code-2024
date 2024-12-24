import networkx as nx
import matplotlib.pyplot as plt

class OperationNode:
    def __init__(self, op, inputs, output):
        self.op = op
        self.inputs = inputs
        self.output = output

def visualize_with_networkx(operations):
    G = nx.DiGraph()

    # Add edges
    for op in operations:
        operation_label = f"{op.op} ({op.output})"
        for input_var in op.inputs:
            G.add_edge(input_var, operation_label)
        G.add_edge(operation_label, op.output)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=100 , node_color="lightblue", font_size=5, font_weight="bold")
    plt.show()

# Example binary operations graph
operations = [
    OperationNode("AND", ["A", "B"], "C"),
    OperationNode("OR", ["A", "D"], "E"),
    OperationNode("XOR", ["C", "E"], "F")
]


f = open("Day24\day24.txt", "r")
a,b = f.read().split("\n\n")

d = {}
for i in a.split("\n"):
    r,v = i.split(": ")
    d[r] = int(v)

ops_arr = []
b=b.strip().split("\n")
for j,i in enumerate(b):
    left, right = i.split(" -> ")
    operations = left.split()
    ops_arr += [ OperationNode(operations[1], [operations[0], operations[2]], right) ]
    if j == 50:
        break

visualize_with_networkx(ops_arr)