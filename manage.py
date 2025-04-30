def name_quotes(name):
    quotes = {
    'Darth Warder': 'Im your father',
    'Anna': 'Whats hepennig',
    'Lil nas x': 'Im gonna take my hourse',
    'Bella' : 'Im barbi gir'
    }

    return quotes.get(name, 'He is not viral')

assert name_quotes('Anna') == 'Whats hepennig',(
    'Its not workly corectly'
)
   
assert name_quotes('Bella') == 'Im barbi girl',(
    'Its not workly corectly'
)

print(name_quotes('Anna'))

