def generate_assembly_code(tac):
    assembly_code = []

    for op, left, right, result in tac:
        if op == '+':
            assembly_code.append(f"ADD {left}, {right}, {result}")
        elif op == '-':
            assembly_code.append(f"SUB {left}, {right}, {result}")
        elif op == '*':
            assembly_code.append(f"MUL {left}, {right}, {result}")
        elif op == '/':
            assembly_code.append(f"DIV {left}, {right}, {result}")
        elif op == '=':
            assembly_code.append(f"MOV {left}, {result}")

    return assembly_code

def main():
    tac = [
        ('+', 'a', 'b', 't1'),
        ('-', 't1', 'c', 't2'),
        ('=', 't2', '', 'd')
    ]

    assembly_code = generate_assembly_code(tac)

    print("Generated Assembly Language Code:")
    for instruction in assembly_code:
        print(instruction)

if __name__ == "__main__":
    main()