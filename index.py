import random
import string
import socket
import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        host='localhost',  # No need for 'http://'
        port=3307,
        user='root',
        password='my-secret-pw',
        database='teste'
    )

    if connection.is_connected():
        print('conexão estabelecida com sucesso.')
except Error as e:
    print(f"error: {e}")