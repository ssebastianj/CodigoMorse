#! /usr/bin/env python
# -*- coding: utf-8 -*-

import Tkinter
import tkSnack
import codigomorse
import time

class CodigoMorseSound:
        
    def __init__(self, wpm=5, frequency=150, noteshape='sine'):
        self.palabras_por_minuto = wpm
        self.unidad_tiempo = 1200.0 / wpm
        self.frecuencia = frequency
        self._configTimes()
        
        self._root = Tkinter.Tk()
        tkSnack.initializeSnack(self._root)
        self._noteshape = noteshape
    
    def _configTimes(self):
        self.tmp_punto = self.unidad_tiempo
        self.tmp_raya = self.tmp_punto * 3
        self.tmp_espacio_inter_elementos = self.tmp_punto
        self.tmp_espacio_entre_letras = self.tmp_punto * 3
        self.tmp_espacio_entre_palabras = self.tmp_punto * 7
        
    def setWordsPerMinute(self, wpm):
        if wpm > 0: 
            self.palabras_por_minuto = wpm
            self.unidad_tiempo = 1200.0 / wpm
            self._configTimes()
        else: 
            raise ValueError(u'wpm debe ser un número mayor a cero.')
        
    def setTimeUnit(self, duration):
        if duration > 0: 
            self.unidad_tiempo = duration
            self.palabras_por_minuto = 1200.0 / self.unidad_tiempo
            self._configTimes()
        else: 
            raise ValueError(u'duration debe ser un número mayor a cero.')
        
    def setFrequency(self, frequency):
        if frequency >= 1 and frequency <= 10000: 
            self.frecuencia = frequency
        else: 
            raise ValueError(u'frequency debe ser un número entre 1 y 10000.')

    def setVolume(self, volume):
        if volume > 100: 
            volume = 100
        elif volume < 0: 
            volume = 0
        tkSnack.audio.play_gain(volume)
    
    def playMorseString(self, morsestring):
        if morsestring != '':
            words = morsestring.split('  ')
            words_spaces = len(words) - 1
            
            for word in words:
                letters = word.split()
                letters_spaces = len(letters) - 1
                
                for letter in letters:
                    elements_spaces = len(letter) - 1
                    for element in letter:
                        if element == '-':
                            print 'Raya'
                            self._playNote(self.frecuencia, self.tmp_raya)
                        elif element == '.':
                            print 'Punto'
                            self._playNote(self.frecuencia, self.tmp_punto)
                        
                        if elements_spaces != 0:
                            print 'Espacio entre elementos'
                            time.sleep(self.tmp_espacio_inter_elementos / 1000.0)
                            elements_spaces -= 1
                    
                    if letters_spaces != 0:
                        print 'Espacio entre letras'
                        time.sleep(self.tmp_espacio_entre_letras / 1000.0)
                        letters_spaces -= 1
                if words_spaces != 0:
                    print 'Espacio entre palabras'
                    time.sleep(self.tmp_espacio_entre_palabras / 1000.0)
                    words_spaces -= 1
                    
    def playAlfString(self, alfstring):
        self.playMorseString(codigomorse.encodeToMorse(alfstring))               

    def _playNote(self, frequency, duration):
        snd = tkSnack.Sound()
        self._filt = tkSnack.Filter('generator', frequency, 30000, 0.0, self._noteshape, int(11500 * (duration / 1000)))
        snd.stop()
        snd.play(filter=self._filt, blocking=1)
        
    def soundStop(self):
        try:
            self._root = self._root.destroy()
            self._filt = None
        except:
            pass
        
    def setNoteShape(self, shape):
        SHAPES = ['sine', 'triangle', 'rectangle', 'sampled', 'noise']
        if shape.lower().strip() in SHAPES:
            self._noteshape = shape
        else:
            raise ValueError(u'El valor de shape no es válido.')
        
if __name__ == '__main__':
    pass
