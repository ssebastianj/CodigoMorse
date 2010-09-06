# -*- coding: utf-8 -*-

class Morse:
    """Codificador/Decodificador Morse."""
    
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
        """Constructor de la clase Morse.
        
        Argumentos:
        wpm -- Words Per Minute (Palabras Por Minuto) default=5 
        """
        self.PALABRAS_POR_MINUTO = wpm
        self.UNIDAD_TIEMPO = 1200.0 / wpm
        self.TMP_PUNTO = self.UNIDAD_TIEMPO
        self.TMP_RAYA = self.TMP_PUNTO * 3
        self.TMP_ESPACIO_INTER_ELEMENTOS = self.TMP_PUNTO
        self.TMP_ESPACIO_ENTRE_LETRAS = self.TMP_PUNTO * 3
        self.TMP_ESPACIO_ENTRE_PALABRAS = self.TMP_PUNTO * 7

    def get_palabras_por_minuto(self):
        """Devuelve la cantidad de palabras por minuto."""
        return self.__PALABRAS_POR_MINUTO

    def get_unidad_tiempo(self):
        u"""Devuelve la duración en milisegundos de una unidad de tiempo."""
        return self.__UNIDAD_TIEMPO

    def get_tmp_punto(self):
        u"""Devuelva la duración en milisegundos de un punto (dit)."""
        return self.__TMP_PUNTO

    def get_tmp_raya(self):
        u"""Devuelve la duración en milisegundos de una raya (dash)."""
        return self.__TMP_RAYA

    def get_tmp_espacio_inter_elementos(self):
        u"""Devuelve la duración en milisegundos de un espacio entre elementos."""
        return self.__TMP_ESPACIO_INTER_ELEMENTOS

    def get_tmp_espacio_entre_letras(self):
        u"""Devuelve la duración en milisegundos de un espacio entre letras."""
        return self.__TMP_ESPACIO_ENTRE_LETRAS

    def get_tmp_espacio_entre_palabras(self):
        u"""Devuelve la duración en milisegundos de un espacio entre palabras."""
        return self.__TMP_ESPACIO_ENTRE_PALABRAS

    def charToMorse(self, caracter):
        u"""Devuelve la representación en código Morse de un caracter.
        
        Si el caracter es válido y distinto de Espacio -> Representación Morse
        Si el caracter es el Espacio -> ' '
        Si el caracter no es válido -> '_'
        """
        if caracter.upper() in self.__MORSE.keys(): return self.__MORSE.get(caracter.upper())
        elif caracter == ' ': return ' '
    
    def cadToMorse(self, cadena):
        u"""Devuelve la representación en código Morse de una cadena."""
        convertido = ''
        for i in cadena:
            convertido += self.charToMorse(i) + ' '
        return convertido.strip()
        
    def letraMorseToChar(self, letra):
        u"""Devuelve la representación alfabética de una letra en código Morse."""
        for clave, valor in self.MORSE.iteritems():
            if letra == valor: return clave
            
    def cadMorseToCad(self, cadena):
        u"""Devuelve una cadena alfabética a partir de una cadena en código Morse."""
        palabras = cadena.split('  ')
        convertida = ''
        for palabra in palabras:
            letras = palabra.split()
            for letra in letras:
                convertida += self.letraMorseToChar(letra)
            convertida += ' '
        return convertida.strip().lower()
    
    #Seteo de las propiedades
    PALABRAS_POR_MINUTO = property(get_palabras_por_minuto, None, None, None)
    UNIDAD_TIEMPO = property(get_unidad_tiempo, None, None, None)
    TMP_PUNTO = property(get_tmp_punto, None, None, None)
    TMP_RAYA = property(get_tmp_raya, None, None, None)
    TMP_ESPACIO_INTER_ELEMENTOS = property(get_tmp_espacio_inter_elementos, None, None, None)
    TMP_ESPACIO_ENTRE_LETRAS = property(get_tmp_espacio_entre_letras, None, None, None)
    TMP_ESPACIO_ENTRE_PALABRAS = property(get_tmp_espacio_entre_palabras, None, None, None)
