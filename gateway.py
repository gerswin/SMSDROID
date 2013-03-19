from bottle import route, run, request
import sqlite3
import sys
import time

def guardardb(numero,txt,status):
    t = (numero,txt,status)
    connection = sqlite3.connect('sms.sqlite')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO smsout (numero,mensaje,status) VALUES (?,?,?)', t)
    connection.commit()
    cursor.close()
    connection.close()
    return "'status':'delivered'"
    
@route('/')
def enviar():
    
	numero = request.GET['numero']
	mensaje = request.GET['mensaje']
	status = "delivered"
	retorno = guardardb(numero,mensaje,status)
	return retorno

run(host='', port=9988, debug=True)
