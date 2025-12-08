def decode_santa_pin(code: str) -> str:
  
  # [], [], []
  finalCode = ""
  cont = 0
  
  for item in str:
      if item === "]": # Mirar primero si se acaba los corchetes
        cont = 0
      if item !== "[" # Mirar que no sea el corchete del inicio
        if item === "+":
            cont += 1
            if cont > 9:
                cont = 0
        elif item === "-":
            cont -= 1
            if cont ===:
                cont = 0
            
  
  return finalCode

print(decode_santa_pin('[1++][2-][3+][<]'))
# "3144"

print(decode_santa_pin('[9+][0-][4][<]'))
# "0944"

print(decode_santa_pin('[1+][2-]'))
# null (solo 2 dígitos)