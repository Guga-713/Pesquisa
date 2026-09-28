# Entrada
excelente = 0
ruim = 0
# Executando a pesquisa 10 vezes
for i in range(10):
    nome= input("Digite o seu nome: ")
    idade= int(input("Digite a sua idade: "))
    nota= int(input("Qual a sua avaliação para o atendimento? (1-Excelente, 2-Bom, 3-Ruim): " ))
    # Verificação da nota e contagem das respostas
    if nota == 1:
        excelente = excelente + 1
    elif nota == 3:
        ruim = ruim + 1
# Exibindo os resultados
print("Quantidade de respostas EXCELENTE:", excelente)
print("Quantidade de respostas RUIM:", ruim)
