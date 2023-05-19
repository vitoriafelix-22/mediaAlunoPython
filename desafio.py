notas_semestre1 = []
notas_semestre2 = []

# Preenchendo o vetor de notas do primeiro semestre
for i in range(4):
    nota = float(input("Digite a nota do semestre 1: "))
    notas_semestre1.append(nota)

# Preenchendo o vetor de notas do segundo semestre
for i in range(4):
    nota = float(input("Digite a nota do semestre 2: "))
    notas_semestre2.append(nota)

# Calculando a média final
media_semestre1 = sum(notas_semestre1) / 4
media_semestre2 = sum(notas_semestre2) / 4
media_final = (media_semestre1 + media_semestre2) / 2

print("A média final do estudante é:", media_final)