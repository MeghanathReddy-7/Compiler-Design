def generate_tac(expression):
    tokens = expression.split()
    tac = []
    temp_count = 0
    def generate_temp():
        nonlocal temp_count
        temp_count += 1
        return f"t{temp_count}"
    for i in range(0, len(tokens), 2):
        if i >= len(tokens) - 2:  
            break
        if i == 0:
            left_operand = tokens[i]
        else:
            left_operand = tac[-1][-1]
        operator = tokens[i + 1]
        right_operand = tokens[i + 2]
        temp = generate_temp()
        tac.append((operator, left_operand, right_operand, temp))
    return tac
def main():
    expression = input("Enter an expression : ")
    tac = generate_tac(expression)
    print("\nThree Address Code:")
    for op, left, right, result in tac:
        print(f"{result} = {left} {op} {right}")
if __name__ == "__main__":
    main()