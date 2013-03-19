# -*- coding: utf-8 -*-
import requests
import sqlite3
import android
import time
droid = android.Android()
connection = sqlite3.connect('/mnt/sdcard/sl4a/scripts/server/sms.sqlite')
cursor = connection.cursor()
base = "http://sql.gerswin.com/delivery.php?"

def enviar_mensaje(numero,txt,id):
    cursore = connection.cursor()
    values = ('send', id, )
    cursore.execute("UPDATE smsout SET status=? WHERE id=?", values)
    connection.commit()
    cursore.close()    
	try:      
        result = droid.smsSend(numero, txt)
		userdata = {"status": "OK", "numero": numero, "mensaje": mensaje}
		resp = requests.post(base, params=userdata);			
    except:
		error = 1
    time.sleep(2)
	
    return True 


id = ('delivered', )
cursor.execute("SELECT * FROM smsout WHERE status=?", id)
for row in cursor:
    print row[0],row[1],row[2]
    enviar_mensaje(row[1],row[2],row[0])
    

cursor.close()
