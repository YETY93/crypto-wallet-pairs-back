import mysql.connector

# Connect to server
# TODO: automatizar la coneccion por parametros y realizar un pool de ser necesario
cnx = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="crypto_wallet",
    user="root",
    password="",
    charset='utf8mb4',
    collation='utf8mb4_general_ci'  # Reemplaza por una colección soportada
)



def ejecutar_sentencia(query: str, valores: tuple)-> bool:
    try:
        cursor = cnx.cursor()
        cursor.execute(query, valores)
        cnx.commit()
        affected_rows = cursor.rowcount  # Número de filas afectadas
        cursor.close()
        print(f"Consulta ejecutada exitosamente. Filas afectadas: {affected_rows}")
        return True
    except mysql.connector.Error as err:
        cnx.rollback()  # Deshacer cambios en caso de error
        print(f"Error al ejecutar la consulta. Se realizó un rollback: {err}")
        return False