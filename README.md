# Gerador de Wordlist para Bruteforce

Programa Python Gerador de dicionário personalizado a partir de palavras chave

Este projeto contém um script Python que gera todas as combinações possíveis de palavras fornecidas pelo programador, relacionadas ao alvo, criando um dicionário que pode ser salvo como uma wordlist em formato `.txt` para uso em ferramentas de recuperação de senhas e ataques de força bruta (como **John the Ripper**, **Hashcat** ou **fcrackzip**). O objetivo é criar uma lista personalizada de senhas candidatas.

**Nota**: Este projeto é apenas para fins educacionais e éticos. Use apenas em arquivos que você possui ou tem permissão para testar.

## Funcionalidades
- Gera todas as combinações possíveis dos elementos fornecidos na lista de elementos.
- Salva as combinações em um arquivo de texto (`wordlist_combinacoes.txt`), com uma combinação por linha, compatível com ferramentas de cracking.
- Código modular e fácil de adaptar para outros elementos ou formatos de saída.

## Requisitos
- Python 3.x
- Módulo `itertools` (nativo no Python)
- Ferramentas opcionais para uso da wordlist:
  - [John the Ripper](https://www.openwall.com/john/)
  - [Hashcat](https://hashcat.net/)
  - [fcrackzip](http://oldhome.schmorp.de/marc/fcrackzip.html)

## Como Usar
1. Clone o repositório:
   ```bash
   git clone https://github.com/gazstao/PythonPasswordGenerator
   cd PythonPasswordGenerator
   (edite o arquivo generate.py e coloque os elementos interessantes na lista)
   python generate.py