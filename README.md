
# 🏠 Consulta de Endereço por CEP — Projeto de Aprendizado

## 🧠 Objetivo de Aprendizado

Este projeto tem como objetivo **ensinar o consumo de uma API pública** para consultar **endereços a partir do CEP**, utilizando a biblioteca `requests` em Python.
Com este exercício, o aluno desenvolve competências práticas em:

* Envio de **requisições HTTP** (`GET`);
* Tratamento de **respostas JSON**;
* Manipulação de **dados retornados por uma API**;
* Estruturação de **condições lógicas** para verificar erros;
* Interação com o usuário via **entrada de dados (`input`)**.

---

## 🧩 Descrição do Projeto

O código realiza a **consulta de um CEP digitado pelo usuário** na **API pública ViaCEP**, retornando as seguintes informações:

* 📬 CEP
* 🏙️ Logradouro
* 🏘️ Bairro
* 🌆 Cidade
* 🗺️ Estado (UF)

Se o CEP não existir ou estiver incorreto, o programa informa que o CEP **não foi encontrado**.

---

## ⚙️ Funcionamento do Código

1. Importa a biblioteca `requests`;
2. Recebe o CEP digitado pelo usuário (apenas números);
3. Monta a URL de requisição para a **API ViaCEP**;
4. Envia a requisição HTTP (`GET`) para obter os dados do endereço;
5. Verifica se a resposta foi bem-sucedida (`status_code == 200`);
6. Exibe os dados formatados no terminal.

---

## 🧾 Exemplo de Saída

```
Digite o CEP (somente números): 01001000
CEP: 01001-000
Logradouro: Praça da Sé
Bairro: Sé
Cidade: São Paulo
Estado: SP
```

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**
* **Biblioteca requests**
* **API pública do [ViaCEP](https://viacep.com.br/)**

---

## 📦 Instalação

Antes de rodar o código, instale a biblioteca necessária:

```bash
pip install requests
```

---

## ▶️ Como Executar

1. Baixe ou clone este repositório:

   ```bash
   git clone https://github.com/SEU_USUARIO/nome-do-repositorio.git
   ```
2. Acesse a pasta do projeto:

   ```bash
   cd nome-do-repositorio
   ```
3. Execute o código:

   ```bash
   python consulta_cep.py
   ```

---

## 🧰 Aprendizado Recomendado

Para compreender completamente este projeto, recomenda-se estudar:

* Funcionamento das **APIs REST**;
* Estrutura e leitura de **respostas JSON**;
* Métodos de requisição (`GET`, `POST`, etc.);
* Boas práticas de **tratamento de erros** em requisições.

---

## 💡 Desafio Extra

Como exercício, tente:

* Tratar CEPs inválidos (com menos de 8 dígitos);
* Salvar o resultado em um **arquivo `.txt`**;
* Criar uma **interface gráfica (Tkinter)** para a busca de CEP;
* Exibir a **data e hora da consulta** junto ao resultado.

---


