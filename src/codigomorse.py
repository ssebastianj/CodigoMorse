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
         '$':   '...-..-',
         '@':   '.--.-.',
         'AR':  '.-.-.',
         'AS':  '.-...',
         'BK':  '-...-.-',
         'BT':  '-...-',
         'CL':  '-.-..-..',
         'CT':  '-.-.-',
         'DO':  '-..---',
         'K':   '-.-',
         'KN':  '-.--.',
         'SK':  '...-.-',
         'SN':  '...-.',
         'SOS': '...---...',
         'ERROR':'........'
        }

def charToMorse(caracter):
    u"""Devuelve la representación en código Morse de un caracter.
        
    Si el caracter es válido y distinto de Espacio -> Representación Morse
    Si el caracter es el Espacio -> ' '
    Si el caracter no es válido -> None
    """
    char = caracter.upper()
    if char in MORSE.keys(): return MORSE.get(char)
    elif caracter == ' ': return ' '
    else: return None
    
def cadToMorse(cadena):
    u"""Devuelve la representación en código Morse de una cadena."""
    cadenamorse = []
    for i in cadena: cadenamorse.append(charToMorse(i))
    return ' '.join(cadenamorse)
        
def letraMorseToChar(letra):
    u"""Devuelve la representación alfabética de una letra en código Morse."""
    for clave, valor in MORSE.iteritems():
        if letra == valor: return clave
        else: return None
            
def cadMorseToCad(cadena):
    u"""Devuelve una cadena alfabética a partir de una cadena en código Morse."""
    palabras = cadena.split('  ')
    cadenaalf = []
    for palabra in palabras:
        letras = palabra.split()
        for letra in letras:
            cadenaalf.append(letraMorseToChar(letra).lower())
        cadenaalf.append(' ')
    return ''.join(cadenaalf).strip()
    