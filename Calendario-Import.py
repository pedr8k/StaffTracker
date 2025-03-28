'''
IMPORTANDO CALENDARIO
'''
import datetime 
data_inicio = datetime.datetime(2024, 12, 1, 14, 0, 0)

import calendar

funcionarios = [nome.strip() for nome in  input("Insira os nomes dos funcionários separados por vírgula: ").split(",")]
# Definir o dia do plantão como sábado
dia_plantao = 5  # Sábado é representado pelo número 5
# percorrer a lista de funcionarios
indice_funcionario = 0
# Loop contínuo para os sábados (vai até o final da lista de funcionários)
while True:
    # Solicita a data do sábado (no formato dd/mm/aaaa)
    data = input("Informe a data do sábado (formato dd/mm/aaaa), ou 'sair' para encerrar: ")
    if data.lower() == "sair":
        break
    try:
        dia, mes, ano = map(int, data.split('/'))
        if calendar.weekday(ano, mes, dia) == dia_plantao:
            # Se for sábado, atribui o plantão ao funcionário
            print(f"O plantão do dia {data} será de {funcionarios[indice_funcionario]}.")
               # Avança para o próximo funcionário na lista (circular)
            indice_funcionario = (indice_funcionario + 1) % len(funcionarios)
        else:
            # Se não for sábado, exibe a mensagem
            print(f"{data} não é sábado.")
    
    except ValueError:
        print("Formato de data inválido! Por favor, insira a data no formato dd/mm/aaaa.")
