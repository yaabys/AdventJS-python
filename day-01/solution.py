"""
Santa ha recibido una lista de regalos, pero algunos están defectuosos. Un regalo es defectuoso si su nombre contiene el carácter #.

Ayuda a Santa escribiendo una función que reciba una lista de nombres de regalos y devuelva una nueva lista que solo contenga los regalos sin defectos.
"""

def filter_gifts(gifts):
  
  finalGifts = []
  
  for i in range(0,len(gifts),1):
      if "#" not in gifts[i]:
          finalGifts.append(gifts[i])
  
  return finalGifts

gifts1 = ["car", "doll#arm", "ball", "#train"]
good1 = filter_gifts(gifts1)
print(good1)
