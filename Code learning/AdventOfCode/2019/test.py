import itertools

noun = []
verb = []
for x in range(100):
    print(x)
    noun.append(x)
    verb.append(x)
#combined = [(noun, verb) for n in noun for v in verb] 
#print(combined)
combined = list(itertools.product(noun, verb))
print(combined)
print(noun)
print(verb)