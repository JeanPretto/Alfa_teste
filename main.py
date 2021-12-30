import requests
import psycopg2



# Banco de dados
host = 'localhost'
dbname = 'Alfa'
user = 'postgres'
password = 'ky$14gr@'

conn_string = 'host={0} user={1} dbname={2} password={3} '.format(host, user, dbname, password)
conn = psycopg2.connect(conn_string)
cursor = conn.cursor()



print('###################')
print('###Consulta CNPJ ###')
print('###################')
print()



# Abertura
cnpj = input('Digite o CNPJ para a consulta:')



# Verificar quantidade de caracteres
while (len (cnpj) != 14):
    cnpj = input('CNPJ Inválido digite novamente: ')
else:
    print("\nCNPJ Encontrado com sucesso!\n")     
    



# Site para consulta
address_data = requests.get('https://www.receitaws.com.br/v1/cnpj/' + cnpj)
address_data = address_data.json()
status = address_data['status']
#print(address_data)



if  status == 'OK': 
    
    cnpj = address_data['cnpj']
    nome = address_data['nome']
    cidade = address_data['municipio']
    estado = address_data['uf']
    
    print('CNPJ: ' + cnpj)
    print('Razão Social: ' + nome)
    print('Cidade: ' + cidade)
    print('UF: ' + estado)
    

    cursor.execute(
    "insert into cadastro_filiais (cnpj, nome, cidade, estado) values ('" + cnpj + "', '" + nome + "', '" + cidade + "', '" + estado + "')")
    conn.commit()
    cursor.close
    conn.close
    
    
    print("\nDados inseridos com sucesso!") 


elif status == '404' or 'ERROR':
    print("Erro na consulta!")

