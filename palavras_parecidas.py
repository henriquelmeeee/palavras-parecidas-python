from unidecode import unidecode

p1 = str(input("Digite a primeira palavra: "))
p2 = str(input("Digite a segunda palavra: "))
p1 = p1.split(' ')[0].lower(); p2 = p2.split(' ')[0].lower()

debug = False

def algorithm(p1, p2):
    print("Info | Checando palavras...")
    if debug:
        print("Warn | O Debug está habilitado.")
    pontos = 0; n = 0; pos_adicionar = 0; erros = 0
    if len(p2) < len(p1) and not len(p2) == len(p1):
        for value in p2:
            try:        
                if debug:
                    print("Info | " + value + " / " + p1[n + pos_adicionar])
                if value == p1[n + pos_adicionar]:
                    pontos += 1
                else:
                    pos_adicionar += 1
                    erros += 1
                n += 1
            except Exception as e:
                break
    else:
        for value in p1:
            if len(p2) == len(p1):
                pos_adicionar = 0
            try:        
                if debug:
                    print("Info | " + value + " / " + p2[n + pos_adicionar])
                if value == p2[n + pos_adicionar]:
                    pontos += 1
                else:
                    pos_adicionar += 1
                    erros += 1
                n += 1
            except Exception as e:
                break
    if debug:
        print(f"Pontos: {pontos}")
    if (pontos - erros) > 2 and len(p1) - len(p2) < 3 and len(p2) - len(p1) < 3:
        return True
    return False

if algorithm(unidecode(p1), unidecode(p2)):
    print("\n" + p1 + " // " + p2 + ":")
    print("As palavras SÃO parecidas.")
else:
    print("\n" + p1 + " // " + p2 + ":")
    print("As palavras NÃO SÃO parecidas.")
