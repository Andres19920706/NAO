# -*- encoding: UTF-8 -*-
"""
Ejemplo 1:
    Hacer que NAO diga "hola mundo", a través de un código de python
"""

#Libreria
from naoqi import ALProxy

#Conexión
tts = ALProxy("ALTextToSpeech","127.0.0.1",9559)

#
tts.say ("Hola mundo! 2")