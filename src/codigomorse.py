# -*- coding: utf-8 -*-
# Codificador/Decodificador Morse

class Morse:
    """ Codificador/Decodificador Morse """
    
    MORSE = {'A':   '.-',
             'B':   '-...',
             'C':   '-.-.',
             'CH':  '----',
             'D':   '-..',
             'E':   '.',
             'F':   '..-.',
             'G':   '--.',
             'H':   '....',
             'I':   '..',
             'J':   '.---',
             'K':   '-.-',
             'L':   '.-..',
             'M':   '--',
             'N':   '-.',
             'Ñ':   '--.--',
             'O':   '---',
             'P':   '.--.',
             'Q':   '--.-',
             'R':   '.-.',
             'S':   '...',
             'T':   '-',
             'U':   '..-',
             'V':   '...-',
             'W':   '.--',
             'X':   '-..-',
             'Y':   '-.--',
             'Z':   '--..',
             '0':   '-----',
             '1':   '.----',
             '2':   '..---',
             '3':   '...--',
             '4':   '....-',
             '5':   '.....',
             '6':   '-....',
             '7':   '--...',
             '8':   '---..',
             '9':   '----.',
             '.':   '.-.-.-',
             ',':   '--..--',
             '?':   '..--..',
             '"':   '.-..-.',
             "'":   '.----.',
             '!':   '-.-.--',
             '/':   '-..-.',
             '(':   '-.--.',
             ')':   '-.--.-',
             '&':   '.-...',
             ':':   '---...',
             ';':   '-.-.-.',
             '=':   '-...-',
             '+':   '.-.-.',
             '-':   '-....-',
             '_':   '..--.-',
             '$':   '...-..-',
             '@':   '.--.-.',
             'AR':'.-.-.',
             'AS':'.-...',
             'BK':'-...-.-',
             'BT':'-...-',
             'CL':'-.-..-..',
             'CT':'-.-.-',
             'DO':'-..---',
             'K':'-.-',
             'KN':'-.--.',
             'SK':'...-.-',
             'SN':'...-.',
             'SOS':'...---...',
             'ERROR':'........'
             }

    def __init__(self, wpm=5):
        self.PALABRAS_POR_MINUTO = wpm
        self.UNIDAD_TIEMPO = 1200.0 / wpm
        self.PUNTO = self.UNIDAD_TIEMPO
        self.RAYA = self.PUNTO * 3
        self.ESPACIO_INTER_ELEMENTOS = self.PUNTO
        self.ESPACIO_ENTRE_LETRAS = self.PUNTO * 3
        self.ESPACIO_ENTRE_PALABRAS = self.PUNTO * 7

    def getPalabrasPorMinuto(self):
        return self.__PALABRAS_POR_MINUTO

    def getUnidadTiempo(self):
        return self.__UNIDAD_TIEMPO

    def getTiempoPunto(self):
        return self.__PUNTO

    def getTiempoRaya(self):
        return self.__RAYA

    def getTiempoEspacioInterElementos(self):
        return self.__ESPACIO_INTER_ELEMENTOS

    def getTiempoEspacioEntreLetras(self):
        return self.__ESPACIO_ENTRE_LETRAS

    def getTiempoEspacioEntrePalabras(self):
        return self.__ESPACIO_ENTRE_PALABRAS

    def charToMorse(self, caracter):
        """ Devuelve la representación en código Morse de un caracter
        Si el caracter es válido y distinto de Espacio -> Representación Morse
        Si el caracter es el Espacio -> ' '
        Si el caracter no es válido -> '_'
        """
        if caracter.upper() in self.__MORSE.keys(): return self.__MORSE.get(caracter.upper())
        elif caracter == ' ': return ' '
    
    def cadToMorse(self, cadena):
        """ Devuelve la representación en código Morse de una cadena """
        convertido = ''
        for i in cadena:
            convertido += self.charToMorse(i) + ' '
        return convertido.strip()
        
    def letraMorseToChar(self, letra):
        """ Devuelve la representación alfabética de una letra en código Morse """
        for clave, valor in self.MORSE.iteritems():
            if letra == valor: return clave
            
    def cadMorseToCad(self, cadena):
        """ Devuelve una cadena convertida desde un mensaje en código Morse """
        palabras = cadena.split('  ')
        convertida = ''
        for palabra in palabras:
            letras = palabra.split()
            for letra in letras:
                convertida += self.letraMorseToChar(letra)
            convertida += ' '
        return convertida.strip().lower()
    
    PALABRAS_POR_MINUTO = property(getPalabrasPorMinuto, None, None, None)
    UNIDAD_TIEMPO = property(getUnidadTiempo, None, None, None)
    PUNTO = property(getTiempoPunto, None, None, None)
    RAYA = property(getTiempoRaya, None, None, None)
    ESPACIO_INTER_ELEMENTOS = property(getTiempoEspacioInterElementos, None, None, None)
    ESPACIO_ENTRE_LETRAS = property(getTiempoEspacioEntreLetras, None, None, None)
    ESPACIO_ENTRE_PALABRAS = property(getTiempoEspacioEntrePalabras, None, None, None)
