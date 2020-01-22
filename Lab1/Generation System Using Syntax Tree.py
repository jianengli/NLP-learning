import random

#A "receptionist" language can be defined as below
host = """
sentence = Greetings Introduction Ask Business Endind 
Greetings = title sayhi | sayhi
title = Person .
Person = Sir | Madam 
sayhi = Hello, | Hej,
Introduction = I am Name .
Name =  Firstname | Nickname 
Firstname = Mike | Tommy | Jessica
Nickname = Airplane | Bear 
Ask = Would you like | Do you need
Business = fika | other services
Specific business = a beer | to play card | to play video game 
Endind = ?
"""
# create the rule of grammer of "receptionist" language
def create_grammar(grammar_str, split='=>', line_split='\n'):
    grammar = {}
    for line in grammar_str.split(line_split):
        if not line.strip(): continue
        exp, stmt = line.split(split)
        grammar[exp.strip()] = [s.split() for s in stmt.split('|')]
    return grammar

choice = random.choice

# randomly create a sentence based on rule given in the specific grammer
def generate(gram, target):
        if target not in gram: return target # means target is a terminal expression
        expaned = [generate(gram, t) for t in choice(gram[target])]
        return ' '.join([e if e != '/n' else '\n' for e in expaned if e != 'null'])

# generate n times
def generate_n(counter):
    for i in range(counter):
        print(generate(gram=create_grammar(host, split='='), target='sentence'))

generate_n(20)