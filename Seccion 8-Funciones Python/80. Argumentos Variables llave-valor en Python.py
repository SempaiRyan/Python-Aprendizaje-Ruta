# 80. Argumentos Variables llave-valor en Python


def listarTerminos(**terminos):
    for llave,valor in terminos.items():
        print(f'{llave},{valor}')

listarTerminos(IDE='Integrate dev Enviroment',PK='P.Key')

listarTerminos(DBMS='Data M.System')