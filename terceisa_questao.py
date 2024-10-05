import json

# Lendo o arquivo JSON
with open('faturamento.json', 'r') as file:
    dados = json.load(file)

faturamento_diario = dados['faturamento']

# Filtrando os dias com faturamento
faturamento_validos = [valor for valor in faturamento_diario.values() if valor > 0]

# Calculando menor e maior faturamento
menor_faturamento = min(faturamento_validos)
maior_faturamento = max(faturamento_validos)

# Calculando a média mensal
media_faturamento = sum(faturamento_validos) / len(faturamento_validos)

# Contando os dias acima da média
dias_acima_media = sum(1 for valor in faturamento_validos if valor > media_faturamento)

# Exibindo os resultados
print(f"Menor faturamento: {menor_faturamento}")
print(f"Maior faturamento: {maior_faturamento}")
print(f"Número de dias acima da média: {dias_acima_media}")

