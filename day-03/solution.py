def draw_gift(size, symbol):
    if size < 2:
        return ""

    gift = ""

    if size == 2:
        for i in range(0,size,1): # relleno parte arriba
            gift += symbol

        gift += "\n"

        for i in range(0,size,1): # rellenar parte abajo
            gift += symbol
    else:
        for i in range(0,size,1): # relleno parte arriba
            gift += symbol

        gift += "\n"
        
        # ------------------------------------------------------
        stringLateral = symbol # se mete el simbolo al principio

        count = size

        for i in range(1,size-1,1): # los espacios entre los simbolos
            if count > 1:
                stringLateral += " "
                count -= 1
        
        stringLateral += symbol # ultimo simbolo del string

        for i in range(1,size-1,1): # rellenar laterales
            gift += stringLateral
            gift += "\n"
        #-------------------------------------------------------

        for i in range(0,size,1): # rellenar parte abajo
            gift += symbol

    return gift

print(draw_gift(4,"Ñ"))
