DFA = {'i': set('n'), 'n': set('t'), 't': None}
ip = input("enter identifier or int keyword")
c, n = 0, len(ip)
print(f"transitions for {ip}")
for lexeme in ip:
  c += 1
  if lexeme not in DFA.keys():
    print(ip[c - 1:], '->', 'identifier')
    break
  cur = DFA[lexeme]
  if cur is None and c == n:
    print(lexeme, '->', 'keyword')
  else:
    print(lexeme, '->', cur)
