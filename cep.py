# Importação da biblioteca requests para fazer a requisição à API
import requests

# Solicita ao usuário que digite o CEP
cep = input("Digite o CEP (somente números): ")

# Criação da URL para fazer a consulta na API com o CEP informado
url = f'https://viacep.com.br/ws/{cep}/json/'

# Realiza a requisição à API
resposta = requests.get(url)

# Verifica se o código de status da resposta é 200 (sucesso)
if resposta.status_code == 200:
    # Converte a resposta para JSON
    dados = resposta.json()
    
    # Verifica se a chave 'erro' não está presente nos dados
    if 'erro' not in dados:
        # Exibe as informações de CEP, logradouro, bairro, cidade e estado
        print(f'CEP: {dados["cep"]}')
        print(f'Logradouro: {dados["logradouro"]}')
        print(f'Bairro: {dados["bairro"]}')
        print(f'Cidade: {dados["localidade"]}')
        print(f'Estado: {dados["uf"]}')
    else:
        # Exibe uma mensagem caso o CEP não tenha sido encontrado
        print('CEP não encontrado')
else:
    # Exibe uma mensagem de erro caso o status da resposta não seja 200
    print(f'Erro na requisição: {resposta.status_code}')
    print(resposta.content)
