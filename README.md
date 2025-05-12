# Projeto de Análise de Lista de Números

## Descrição
Este projeto contém uma função em Python que analisa uma lista de números inteiros e retorna informações como maior número, menor número, soma, média e números pares. O projeto é composto por dois arquivos Python e este README.

## Estrutura do Projeto
- `analise.py`: Contém a função `analisar_lista` que realiza a análise da lista.
- `teste.py`: Importa e utiliza a função `analisar_lista` com a lista fornecida.
- `README.md`: Este arquivo com a documentação do projeto.

## Como Usar
1. Certifique-se de que ambos os arquivos (`analise.py` e `teste.py`) estão no mesmo diretório.
2. Execute o arquivo `teste.py` com Python:
   ```bash
   python teste.py
   ```
3. A saída mostrará:
   - O maior número da lista
   - O menor número da lista
   - A soma de todos os números
   - A média dos números
   - A lista de números pares

## Exemplo de Saída
Para a lista `[10, 23, 5, 8, 12, 33, 42, 7, 19, 28, 3, 16, 9, 50, 21]`, a saída será:
```
Maior número: 50
Menor número: 3
Soma: 286
Média: 19.07
Números pares: [10, 8, 12, 42, 28, 16, 50]
```

## Detalhes da Implementação
- A função `analisar_lista` verifica se a lista está vazia e retorna valores padrão se necessário.
- Usa funções nativas do Python como `max()`, `min()`, `sum()` e list comprehension para eficiência.
- Retorna um dicionário com todas as informações solicitadas.
