import random
import string
import socket
import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        host='',
        user='root',
        password='root',
        database='meubanco'
    )

    if connection.is_connected():
        print('conexão estabelecida com sucesso.')
except Error as e:
    print(f"error: {e}")