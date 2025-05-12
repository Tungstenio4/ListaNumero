from analise import analisar_lista

# Lista fornecida
numeros = [10, 23, 5, 8, 12, 33, 42, 7, 19, 28, 3, 16, 9, 50, 21]

# Executando a análise
resultado = analisar_lista(numeros)

# Exibindo os resultados
print(f"Maior número: {resultado['maior']}")
print(f"Menor número: {resultado['menor']}")
print(f"Soma: {resultado['soma']}")
print(f"Média: {resultado['media']:.2f}")
print(f"Números pares: {resultado['pares']}")