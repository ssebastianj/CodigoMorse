#! /usr/bin/env python
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
    
def encodeToMorse(alfstring):
    morsestring = []
    
    for i in alfstring: 
        element = i.upper()
        if element in MORSE.keys(): 
            morsekey = MORSE.get(element)
        elif element == ' ': 
            morsekey = ''   
        else:
            morsekey = ''
        morsestring.append(morsekey)
    return ' '.join(morsestring)    
     
def decodeMorse(morsestring):
    alfstring = []
    words = morsestring.split('  ')
    
    for word in words:
        letters = word.split()
        for letter in letters:
            for k, v in MORSE.iteritems():
                if letter == v:
                    alfstring.append(k.lower())
        alfstring.append(' ')
    return ''.join(alfstring).strip()

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 3:
        if sys.argv[1] == '-e':
            print encodeToMorse(sys.argv[2])
        elif sys.argv[1] == '-d':
            print decodeMorse(sys.argv[2])
    