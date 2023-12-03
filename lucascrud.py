from pymongo import MongoClient
import random

#conexao mongodb e db
client = MongoClient("mongodb+srv://viniciusgsouto2:1IxppcHW0qPqFCjb@projetouni.qfygcju.mongodb.net/?retryWrites=true&w=majority")
db = client.get_database("LucasTrabalho2")

#conexao das collections
collection_cliente = db["cliente2"]
collection_conta = db["conta2"]
collection_transacao = db["transacao2"]

#documento para cliente
example_kim_cliente = [
{"nome": "Kim",
"cpf": '000.000.000.01',
"rg": '0000001',
"nacionalidade": "Brasileira",
"estado_civil": "Solteira",
"renda_mensal": 'R$20.000',
"titulo_ocupacao": "Jogadora de LOL",
"atendimento_especial": "Nao precisa.",
"data_nascimento": "26/07/1995",
"sexo": "Feminina",
"endereco": "CEP: XXX | Rua: XXX | Estado: SP | Cidade: XX",
"email_contato": "kim_kim@contato",
"numero_contato": "(XX)9XXXX-XXXX",}
]

#documento para conta
example_kim_conta = [
{"nome": "Kim",
"cpf": '000.000.000.01',
"rg": '0000001',
"numero_agencia": "00001",
"numero_conta": "000000001",
"numero_banco": "00001",
"nome_banco": "BancoKim",
"cartao_credito_num": "0001 0001 0001 0001",
"cartao_credito_num_segu": "666",
"cartao_credito_data_vali": "04/30",
"cartao_debito": "true",
"pix": "kim_kim@contato",
"numero_saldo": "20000"}
]

#documento para transacao
example_kim_transacao = [
{"nome": "Kim",
"cpf": "000.000.000.01",
"chave_compra": random.randint(100, 1000),
"nome_produto": "RTX 3060",
"data_compra": "17/10/2023",
"horario_compra": "18:35",
"valor_compra": "10000",
"metodo_compra": "Feminina",
"parcelado_vista": "vista",
"nome_local": "pichau",
"novo_saldo": "10000"}
]

def menu():
    print("Selecione uma opção:")
    print("1. Criar")
    print("2. Ler")
    print("3. Atualizar")
    print("4. Excluir")
    print("5. Sair")

while True:
    menu()
    escolha = input("Digite o número da opção desejada: ")

    if escolha == "1":
        # Inserir os 3 exemplos de documento
        print("Documento cliente adicionado.", collection_cliente.insert_many(example_kim_cliente))
        print("Documento conta adicionado.", collection_conta.insert_many(example_kim_conta))
        print("Documento transacao adicionado.", collection_transacao.insert_many(example_kim_transacao))

    elif escolha == "2":
      # Mostrar todos os clientes
      print("Todos os clientes:")
      for cliente in collection_cliente.find():
        print(cliente)

      # Mostrar todas as contas
      print("\nTodas as contas:")
      for conta in collection_conta.find():
        print(conta)

      # Mostrar todas as transações
      print("\nTodas as transações:")
      for transacao in collection_transacao.find():
        print(transacao)

    elif escolha == "3":
        # Documento onde estar o campo nome e que é Kim
        atualizacao = {"nome": "Kim"}

        # Alter o campo nome para Gabriel
        novo_valor = {"$set": {"nome": "Gabriel"}}

        # Atualizar todos os documentos
        resultado_atualizacao_cliente = collection_cliente.update_many(atualizacao, novo_valor)
        resultado_atualizacao_conta = collection_conta.update_many(atualizacao, novo_valor)
        resultado_atualizacao_transacao = collection_transacao.update_many(atualizacao, novo_valor)

        # Verificar os resultados da atualização
        print("Documento cliente atualizado:", resultado_atualizacao_cliente)
        print("Documento conta atualizado:", resultado_atualizacao_conta)
        print("Documento transacao atualizado:", resultado_atualizacao_transacao)

    elif escolha == "4":
        # Critério de exclusão (por exemplo, pelo nome "Kim" no seu caso)
        deleta_gabriel = {"nome": "Gabriel"}
        deleta_kim = {"nome": "Kim"}

        # Excluir documento em cada coleção que tenha o nome Kim ou Gabriel
        resultado_exclusao_cliente = collection_cliente.delete_one({"$or": [deleta_gabriel, deleta_kim]})
        resultado_exclusao_conta = collection_conta.delete_one({"$or": [deleta_gabriel, deleta_kim]})
        resultado_exclusao_transacao = collection_transacao.delete_one({"$or": [deleta_gabriel, deleta_kim]})

        # Resultados do delete
        print("Documento excluído em 'cliente':", resultado_exclusao_cliente.deleted_count)
        print("Documento excluído em 'conta':", resultado_exclusao_conta.deleted_count)
        print("Documento excluído em 'transacao':", resultado_exclusao_transacao.deleted_count)

    elif escolha == "5":
        print("Saindo do programa.")
        break

    else:
        print("Opção invalida. Tente novamente.")