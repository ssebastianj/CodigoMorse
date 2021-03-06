#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
         'ERROR':'........'
        }
    
def encode_to_morse(alfstring):
    u"""Convierte una cadena alfabética a código Morse. Devuelve una cadena con
        su representación.
    """
    morsestring = []
    
    for i in alfstring: 
        element = i.upper()                    # Normalizar caracter de entrada a mayúsculas.
        if element in MORSE.keys(): 
            morsekey = MORSE.get(element)
        elif element == ' ': 
            morsekey = ''   
        else:
            # Caracter a insertar en la cadena si el elemento no es válido en el código Morse.
            # Por cuestiones de compatibilidad futura, debería ser un caracter poco probable
            # de ser incluido en agregados futuros al código.
            morsekey = ''
        morsestring.append(morsekey)
    return ' '.join(morsestring)    
     
def decode_morse(morsestring):
    u"""Convierte una cadena en código Morse a una cadena alfabética. Devuelve una
        cadena con su representación.
       
        Argumentos:
        morsestring -- Cadena que contiene una combinación de rayas (-), puntos (.)
                       y espacios. 
                      
                       Convención de espacios:
                       - Entre símbolos de la misma letra: Sin espaciado
                       - Entre letras: 1 espacio
                       - Entre palabras: 2 espacios
                      
                       Si la cadena tiene uno o más espacios iniciales o finales,
                       éstos son eliminados a la salida.
                       
    """
    alfstring = []
    words = morsestring.split('  ')               # Separar la cadena de entrada en palabras.
    
    for word in words:
        letters = word.split()                    # Separar una palabra en sus letras.
        for letter in letters:
            for key, value in MORSE.iteritems():
                if letter == value:
                    alfstring.append(key.lower())   # Normalizar caracter de salida a minúsculas.
        alfstring.append(' ')
    return ''.join(alfstring).strip()

# La sintaxis para utilizar el módulo desde consola es la siguiente:
# python codigomorse.py [-e|-d] cadena
#
# cadena  Cadena encerrada entre comillas dobles.
# -e      Encode. Codificar cadena a código Morse.
# -d      Decode. Decodificar cadena desde código Morse. 
if __name__ == '__main__':
    import sys
    if len(sys.argv) == 3:
        # Verificar argumento pasado por consola.
        if sys.argv[1] == '-e':                   # Encode
            print encode_to_morse(sys.argv[2])    
        elif sys.argv[1] == '-d':                 # Decode
            print decode_morse(sys.argv[2])      
