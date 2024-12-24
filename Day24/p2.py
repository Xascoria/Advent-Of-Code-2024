from graphviz import Digraph
from collections import defaultdict

from graphviz import Digraph

class OperationNode:
    def __init__(self, operation, input1=None, input2=None, output=None):
        self.operation = operation
        self.input1 = input1
        self.input2 = input2
        self.output = output

def visualize_operations(operations):
    def add_operation(dot, operation):
        # Create a unique label for the operation node
        op_label = f"{operation.operation}({operation.input1}, {operation.input2})"
        op_node_id = f"{operation.operation}_{operation.input1}_{operation.input2}"
        dot.node(op_node_id, operation.operation)

        # Add edges for inputs
        if operation.input1:
            dot.node(operation.input1, operation.input1)
            dot.edge(operation.input1, op_node_id)
        if operation.input2:
            dot.node(operation.input2, operation.input2)
            dot.edge(operation.input2, op_node_id)

        # Add edge for output
        if operation.output:
            dot.node(operation.output, operation.output)
            dot.edge(op_node_id, operation.output)

    dot = Digraph()
    for operation in operations:
        add_operation(dot, operation)

    return dot

# Define binary operations
operation1 = OperationNode("AND", input1="A", input2="B", output="C")
operation2 = OperationNode("OR", input1="A", input2="B", output="D")
operation3 = OperationNode("XOR", input1="C", input2="D", output="E")

# Visualize and save the operations to a text file
operations = [operation1, operation2, operation3]
operations_dot = visualize_operations(operations)
output_file = 'binary_operations.txt'

with open(output_file, 'w') as file:
    file.write(operations_dot.source)

print(f"Operations DOT representation saved as {output_file}")

# # Define binary operations
# operation1 = OperationNode("AND", input1="A", input2="B", output="C")
# operation2 = OperationNode("OR", input1="A", input2="B", output="D")
# operation3 = OperationNode("XOR", input1="C", input2="D", output="E")

# # Visualize and save the operations to a text file
# operations = [operation1, operation2, operation3]
# operations_dot = visualize_operations(operations)
# output_file = 'binary_operations_hierarchy.txt'

# with open(output_file, 'w') as file:
#     file.write(operations_dot.source)

# print(f"Hierarchical DOT representation saved as {output_file}")

op_arr = []


f = open("Day24\day24.txt", "r")
a,b = f.read().split("\n\n")

b = b.strip().split("\n")

d  ={}
for i in a.split("\n"):
    r,v = i.split(": ")
    d[r] = int(v)

solved = [False] * len(b)
while not all(solved):
    for j,i in enumerate(b):
        if solved[j]:
            continue

        left, right = i.split(" -> ")
        operations = left.split()

        if not (operations[0] in d and operations[2] in d):
            continue

        v1 = d[operations[0]]
        v2 = d[operations[2]]
        p = {"AND": v1 & v2, "XOR": v1 ^ v2, "OR": v1 | v2}
        d[right] = p[operations[1]]
        solved[j] = True

for j,i in enumerate(b):
    left, right = i.split(" -> ")
    operations = left.split()

    op_arr += [OperationNode(operations[1], input1=operations[0]+f"({d[operations[0]]})", 
                             input2=operations[2]+f"({d[operations[2]]})", output=right+f"({d[right]})")]

# Define binary operations
operation1 = OperationNode("AND", input1="A", input2="B", output="C")
operation2 = OperationNode("OR", input1="A", input2="B", output="D")

# Visualize and save the operations to a text file
operations = [operation1, operation2]
operations_dot = visualize_operations(op_arr)
output_file = 'Day24/graph.txt'

with open(output_file, 'w') as file:
    file.write(operations_dot.source)

print(f"Operations DOT representation saved as {output_file}")