"""
La fábrica de Santa ha empezado a recibir la lista de producción de juguetes.
Cada línea indica qué juguete hay que fabricar y cuántas unidades.

Los elfos, como siempre, han metido la pata: han apuntado algunos juguetes con cantidades que no tienen sentido.

Tienes una lista de objetos con esta forma:

toy: el nombre del juguete (string)
quantity: cuántas unidades hay que fabricar (number)
Tu tarea es escribir una función que reciba esta lista y devuelva un array de strings con:

Cada juguete repetido tantas veces como indique quantity
En el mismo orden en el que aparecen en la lista original
Ignorando los juguetes con cantidades no válidas (menores o iguales a 0, o que no sean número)

const production1 = [
  { toy: 'car', quantity: 3 },
  { toy: 'doll', quantity: 1 },
  { toy: 'ball', quantity: 2 }
]

const result1 = manufactureGifts(production1)
console.log(result1)
// ['car', 'car', 'car', 'doll', 'ball', 'ball']

const production2 = [
  { toy: 'train', quantity: 0 }, // no se fabrica
  { toy: 'bear', quantity: -2 }, // tampoco
  { toy: 'puzzle', quantity: 1 }
]

const result2 = manufactureGifts(production2)
console.log(result2)
// ['puzzle']
"""

def manufacture_gifts(gifts_to_produce):

  gifts_produced = []
            
  for i in gifts_to_produce:
    for key, value in i.items():
        toy = key
        count = value
        if int(count) > 0:
          while int(count) >= 0:
            gifts_produced.append(toy)
            count = count - 1
    
  return gifts_produced

production = [
    { 'toy': 'car', 'quantity': 3 },
    { 'toy': 'doll', 'quantity': 1 },
    { 'toy': 'ball', 'quantity': 2 }
]

print(manufacture_gifts(productionn))