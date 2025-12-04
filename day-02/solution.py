def manufacture_gifts(gifts_to_produce):

  gifts_produced = []
    
  for gift in gifts_to_produce:
    toyName = gift['toy']
    value = gift['quantity']
    
    while value > 0:
      gifts_produced.append(toyName)
      value -= 1
    
  return gifts_produced

production = [
    { 'toy': 'car', 'quantity': 3 },
    { 'toy': 'doll', 'quantity': 1 },
    { 'toy': 'ball', 'quantity': 2 }
]

print(manufacture_gifts(production))