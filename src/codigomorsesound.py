# -*- coding: utf-8 -*-

import codigomorse
import winsound

class CodigoMorseSound:
        
    def __init__(self, wpm=5, frequency=150):
        self.palabras_por_minuto = wpm
        self.unidad_tiempo = 1200.0 / wpm
        self.frecuencia = frequency
        self._configTimes()
    
    def _configTimes(self):
        self.tmp_punto = self.unidad_tiempo
        self.tmp_raya = self.tmp_punto * 3
        self.tmp_espacio_inter_elementos = self.tmp_punto
        self.tmp_espacio_entre_letras = self.tmp_punto * 3
        self.tmp_espacio_entre_palabras = self.tmp_punto * 7
        
    def setWordsPerMinute(self, wpm=5):
        if wpm > 0: 
            self.palabras_por_minuto = wpm
            self.unidad_tiempo = 1200.0 / wpm
            self._configTimes()
        else: raise ValueError(u'wpm debe ser un número mayor a cero.')
        
    def setTimeUnit(self, duration):
        if duration > 0: 
            self.unidad_tiempo = duration
            self.palabras_por_minuto = 1200.0 / self.unidad_tiempo
            self._configTimes()
        else: raise ValueError(u'duration debe ser un número mayor a cero.')
        
    def setFrequency(self, frequency):
        if frequency >= 37 and frequency <= 32767: self.frecuencia = frequency
        else: raise ValueError(u'frequency debe ser un número entre 37 y 32767')

    def play(self):
        