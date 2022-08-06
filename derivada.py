# TODO: Solucionar bug del asterisco en expresiones largas

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

def v(expresion_regular, parentesis=False):


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
        if len(expresion_regular) == 2 and expresion_regular.endswith('*') or parentesis:
            pass
        else:
            temp = separar_caracteres(expresion_regular)
            temp_2 = list(map(v, temp))
            return '∅' if '∅' in temp_2 else 'ε'

    # Regla 6
    if '*' in expresion_regular or parentesis:
        return 'ε'

def derivar(expresion_regular, caracter, parentesis=False):

    expresion_regular = expresion_regular.replace(' ', '')

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
        temp_2 = []

        for x in temp:
            temp_3 = derivar(x, caracter)
            temp_2.append(temp_3)

        if parentesis:
            return '+'.join(temp_2) + '(' + expresion_regular + ')*'
        else:
            return '+'.join(temp_2) 

    # Regla 5
    if len(expresion_regular) > 1 and not parentesis:
        if len(expresion_regular) == 2 and expresion_regular.endswith('*'):
            pass
        elif expresion_regular.startswith(caracter):
            return expresion_regular[1:]
        else:
            return '∅'

    # Regla 6
    if '*' in expresion_regular or parentesis:

        if parentesis:
            temp = derivar(expresion_regular, caracter)
            if temp == '∅':
                return '(' + expresion_regular + ')*'
            else:
                return temp + '(' + expresion_regular + ')*'

        elif len(expresion_regular) == 2:
            if expresion_regular.startswith(caracter):
                return expresion_regular
            else:
                return '∅'
            


def leer_expresion(expresion_regular):

    obtener_alfabeto(expresion_regular)


