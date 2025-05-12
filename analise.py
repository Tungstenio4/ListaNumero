def analisar_lista(numeros):
    """
    Analisa uma lista de números inteiros e retorna um dicionário com:
    maior número, menor número, soma, média e números pares.
    
    Args:
        numeros (list): Lista de números inteiros
        
    Returns:
        dict: Dicionário com as análises solicitadas
    """
    if not numeros:
        return {
            "maior": None,
            "menor": None,
            "soma": 0,
            "media": 0,
            "pares": []
        }
        
    maior = max(numeros)
    menor = min(numeros)
    soma = sum(numeros)
    media = soma / len(numeros)
    pares = [num for num in numeros if num % 2 == 0]
    
    return {
        "maior": maior,
        "menor": menor,
        "soma": soma,
        "media": media,
        "pares": pares
    }