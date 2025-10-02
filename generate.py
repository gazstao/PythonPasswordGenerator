from itertools import combinations

# Lista de elementos (mesma do código anterior)
elementos = ['nome', 'nomedocachorro', 'mesdenascimento', 'nomedamae', 'simbolo']

# Dicionário para armazenar as combinações (opcional, só para referência)
dicionario = {}

# Gerar combinações
indice = 1
for r in range(1, len(elementos) + 1):
    for combinacao in combinations(elementos, r):
        chave = ''.join(combinacao)
        dicionario[chave] = f'Combinação {indice}'
        indice += 1

# Extrair apenas as chaves e gravar no arquivo de wordlist (uma por linha)
with open('wordlist_combinacoes.txt', 'w', encoding='utf-8') as arquivo:
    for chave in dicionario.keys():
        arquivo.write(chave + '\n')  # Cada chave em uma linha

print("Arquivo 'wordlist_combinacoes.txt' gerado com sucesso!")
print("Previa do conteúdo:")
for chave in list(dicionario.keys())[:5]:  # Mostra as primeiras 5
    print(chave)