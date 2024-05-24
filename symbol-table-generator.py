import string
i = 0
j = 0
x = 0
n = 0
add = [None] * 5  
b = []
d = []
expression = input("Expression terminated by $:")
while expression[i] != '$':
    b.append(expression[i])
    i += 1
n = i - 1
print("Given Expression:")
i = 0
# Print the given expression
while i <= n:
    print(b[i], end="")
    i += 1
print("\nSymbol Table")
print("Symbol \t addr \t type")
while j <= n:
    c = b[j]
    if c in string.ascii_letters:
        p = id(c)
        add[x] = p
        d.append(c)
        print(f"\n{c} \t {p} \t identifier")
        x += 1
        j += 1
    else:
        if c in '+-*=':
            p = id(c)  
            add[x] = p
            d.append(c)
            print(f"\n{c} \t {p} \t operator")
            x += 1