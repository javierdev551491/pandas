def sonAnagramas(palabra1 , palabra2):
    if len(palabra1) != len(palabra2):
        return False
    
    letras1 = {}
    letras2 = {}
    
    for letra in palabra1:
        if letra in letras1:
            letras1[letra] += 1
        else:
            letras1[letra] = 1

    for letra in palabra2:
        if letra in letras2:
            letras2[letra] += 1
        else:
            letras2[letra] = 1

    if letras1 == letras2:
        return True
    else:
        return False    

print (sonAnagramas('amor', 'roma'))