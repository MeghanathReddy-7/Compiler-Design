class Operation:
    def __init__(self, left, right):
        self.left = left
        self.right = right 
n = int(input("Enter the Number of Values: "))
operations = []
for _ in range(n):
    left = input("left: ")
    right = input("right: ")
    operations.append(Operation(left, right))
print("Intermediate Code")
for op in operations:
    print(f"{op.left} = {op.right}")
pr = []
z = 0
# Dead Code Elimination
for op1 in operations:
    temp = op1.left
    for op2 in operations:
        if temp in op2.right:
            pr.append(Operation(op1.left, op1.right))
            z += 1
            break
print("\nAfter Dead Code Elimination")
for p in pr:
    print(f"{p.left} = {p.right}")
# Eliminate Common Expressions
for i in range(z):
    for j in range(i + 1, z):
        if pr[i].right == pr[j].right:
            pr[j].left = None
print("Optimized Code")
for p in pr:
    if p.left is not None:
      print(f"{p.left} = {p.right}")