class Text:
    pass

class Header(Text):
    pass

h1 = Header()

print(type(h1) is Header)
print(type(h1) is Text)

print(isinstance(h1, Header))
print(isinstance(h1, Text))
