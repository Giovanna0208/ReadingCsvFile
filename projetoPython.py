import csv

#Input da escolha do usuario
print("Digite 1 para mostrar a lista com todos os dados do arquivo")
print("Digite 2 para mostrar a lista com os dados de precipitação que ocorreu em determinado período")
escolha = int(input("Digite 3 para mostrar a lista com a temperatura máxima que ocorreu nos primeiros 7 dias de cada mês de determinado ano: "))
print()

#se o usuario escolhe uma opção não listada
while escolha > 3 or escolha < 1:
	print("Digite uma opção válida: ")
	print()
	print("Digite 1 para mostrar a lista com todos os dados do arquivo")
	print("Digite 2 para mostrar a lista com os dados de precipitação que ocorreu em determinado período")
	escolha = int(input("Digite 3 para mostrar a lista com a temperatura máxima que ocorreu nos primeiros 7 dias de cada mês de determinado ano: "))

#le o arquivo csv
with open("ArquivoDadosProjeto.csv", "r") as arq:
	arquivo = csv.reader(arq, delimiter=";")

	# Mostra lista com todos os dados do arquivo
	if escolha == 1:
		lista = []
		for linha in arquivo:
			lista.append(linha)
		print(lista)

	#Mostra dados de precipitação de um determinado periodo
	elif escolha == 2:
		mes = str(input("Informe o mês: "))
		ano = str(input("Informe o ano: "))
		print()
		
		for linha in arquivo:
			dataLista = linha[0]
			if dataLista[3:5] == mes and dataLista[6:] == ano:
				print(f"Precipitação do dia {linha[0]}: {linha[1]}" )

	#Mostra temperatura maxima dos 7 primeiros dias de determinado ano
	elif escolha == 3:
		ano = str(input("Informe o ano: "))
		print()
		tempsAno = []
		maiorTemp = -1000
		mes = "01"
		countMes = 1
		countIndex = 0

		#Pega os itens do ano informado
		for linha in arquivo:
			dataLista = linha[0]
			contaMes = 0
			if dataLista[6:] == ano:
				tempsAno.append(linha)
		
		while countMes <= 12:
			#reseta a maior temperatura
			maiorTemp = -1000

			for i, item in enumerate(tempsAno):
				dataLista = item[0]

				#checa se o mes do item é o mesmo da contagem
				if dataLista[3:5] == mes:
					temp = float(item[2])
					countIndex = i

					#checa se a temperatura é maior
					if temp > maiorTemp:
						maiorTemp = float(temp)

			print(f"A maior temperatura do mês {mes}: {maiorTemp}" )

			#configura o próximo mês
			countMes = countMes + 1
			if mes != "12": mes = tempsAno[countIndex + 1][0][3:5]