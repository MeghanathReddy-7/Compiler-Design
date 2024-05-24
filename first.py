
def first(grammar, symbol):
    first_set = set()
    productions = grammar[symbol]

    for production in productions:
        if production:  # Check if production is not empty
            first_char = production[0]
            if not first_char.isupper():
                first_set.add(first_char)
            elif first_char in grammar:
                first_set |= first(grammar, first_char)

    return first_set

def compute_first_sets(grammar):
    first_sets = {'a':'a','b':'b','c':'c'}

    for symbol in grammar:
        first_sets[symbol] = first(grammar, symbol)

    return first_sets
grammar = {
    'S': ['A','B C'],
    'A': ['a','b'],
    'B': ['p','#'],
    'C': ['c']
}
first_sets = compute_first_sets(grammar)
for symbol, first_set in first_sets.items():
    if symbol != '#':
        print(f'First({symbol}) = {first_set}')

