class First_Follow():
    def __init__(self, grammar):
        self.grammar = grammar
        self.non_terminals = grammar.keys()
        self.rules = [(head, body) for head, bodies in grammar.items() for body in bodies]

    def compute_first(self, variable):
        first = set()
        productions = [rule[1] for rule in self.rules if rule[0] == variable]
        for production in productions:
            if not production[0].isupper():
                first.add(production[0])
            else:
                for x in production:
                    first |= self.compute_first(x)
                    if '@' not in first:
                        break
                else:
                    first.remove('@')
        return first
    def print_sets(self):
        print("First Sets:")
        for non_terminal in self.non_terminals:
            print(f"{non_terminal}: {self.compute_first(non_terminal)}")

example_grammar = {
    'E': ['TZ'],
    'Z': ['+TZ', '@'],
    'T': ['FY'],
    'Y': ['*FY', '@'],
    'F': ['(E)', 'i'],
}
ff = First_Follow(example_grammar)
print("epsilon is printed as @")
ff.print_sets()