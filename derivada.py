# TODO: Solucionar bug del asterisco 

alfabeto = []

def obtener_alfabeto(expresion_regular):
    for caracter in expresion_regular:
        if caracter != 'ε' and caracter != '∅' and caracter != '+' and caracter != '*' and caracter != '(' and caracter != ')':
            if caracter not in alfabeto:
                alfabeto.append(caracter)

def separar_caracteres(expresion_regular):
    temp = []
    for caracter in expresion_regular:
        if caracter != '*':
            temp.append(caracter)
        elif caracter == '*':
            temp_2 = temp.pop()
            temp_2 = temp_2 + '*'
            temp.append(temp_2)
    return temp

def v(expresion_regular):

    # Regla 1
    if expresion_regular == 'ε':
        return 'ε'

    # Regla 2
    if expresion_regular == '∅':
        return '∅'

    # Regla 3
    if expresion_regular in alfabeto:
        return '∅'

    # Regla 4
    if '+' in expresion_regular:
        temp = expresion_regular.split('+')
        temp_2 = list(map(v, temp))
        return 'ε' if 'ε' in temp_2 else '∅'

    # Regla 5
    if len(expresion_regular) > 1:
        if len(expresion_regular) == 2 and expresion_regular.endswith('*'):
            pass
        else:
            temp = separar_caracteres(expresion_regular)
            temp_2 = list(map(v, temp))
            return '∅' if '∅' in temp_2 else 'ε'

    # Regla 6
    if '*' in expresion_regular:
        return 'ε'

def derivar(expresion_regular, caracter):

    obtener_alfabeto(expresion_regular)
    
    # Regla 1
    if expresion_regular == 'ε' or expresion_regular == '∅':
        return '∅'

    # Regla 2
    if expresion_regular == caracter:
        return 'ε'

    # Regla 3
    if len(expresion_regular) == 1 and expresion_regular != caracter:
        return '∅'

    # Regla 4
    if '+' in expresion_regular:
        temp = expresion_regular.split('+')
        temp_2 = list(map(derivar, temp, caracter))
        return 'ε' if 'ε' in temp_2 else '∅'

    # Regla 5
    if len(expresion_regular) > 1:
        pass

