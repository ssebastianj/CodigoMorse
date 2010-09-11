#! /usr/bin/env python
# -*- coding: utf-8 -*-

import codigomorse
import serial
from time import sleep

class CodigoMorseSerial():
    
    serialport = None
    
    def __init__(self, wpm=10, sport=0, sbaudrate=9600, sbytesize=8, sparity='N', sstopbits=1,
                 stimeout=None, sxonxoff=False, srtscts=False, sdsrdtr=False):
        try:
            self.serialport = serial.Serial(port=sport, baudrate=sbaudrate,
                                             bytesize=sbytesize, parity=sparity,
                                             stopbits=sstopbits, timeout=stimeout,
                                             xonxoff=sxonxoff, rtscts=srtscts,
                                             dsrdtr=sdsrdtr)
        except serial.SerialException:
            print 'Se ha producido un error al intentar conectarse al' + \
                  ' puerto {0} ("{1}")'.format(sport, serial.device(sport))
        
        self.words_per_minute = wpm
        # Utilizar números flotantes debido a un problema en la división realizada 
        # por el intérprete de Python 2.x
        self.time_unit = 1200.0 / wpm       
        self._configTimes()                 # Reconfigurar tiempo de elementos
    
    def _configTimes(self):
        u"""(Re)configura los tiempos de cada elemento basándose en la duración de
            WPM y/o una unidad de tiempo.
        """
        self.tmp_dot = self.time_unit
        self.tmp_dash = self.tmp_dot * 3
        self.tmp_inter_elements_space = self.tmp_dot
        self.tmp_space_between_letters = self.tmp_dot * 3
        self.tmp_space_between_words = self.tmp_dot * 7
        
    def setWordsPerMinute(self, wpm):
        u"""Establece la cantidad de palabras por minuto a utilizar.
           
           Argumentos:
           wpm -- Words Per Minute (Palabras Por Minuto)
        
           Excepciones:
           ValueError
        """
        if wpm > 0: 
            self.words_per_minute = wpm
            # Utilizar números flotantes debido a un problema en la división realizada 
            # por el intérprete de Python 2.x
            self.time_unit = 1200.0 / wpm
            self._configTimes()             # Reconfigurar tiempo de elementos
        else: 
            raise ValueError(u'wpm debe ser un número mayor a cero.')
        
    def setTimeUnit(self, duration):
        u"""Establece la duración de una unidad de tiempo.
        
            Argumentos:
            duration -- Duración (en milisegundos)
            
            Excepciones:
            ValueError
        """
        if duration > 0: 
            self.time_unit = duration
            # Utilizar números flotantes debido a un problema en la división realizada 
            # por el intérprete de Python 2.x
            self.words_per_minute = 1200.0 / self.time_unit
            self._configTimes()             # Reconfigurar tiempo de elementos
        else: 
            raise ValueError(u'duration debe ser un número mayor a cero.')
    
    def openPort(self):
        if self.serialport is not None:
            if not self.serialport.isOpen():
                self.serialport.open()
                
    def closePort(self):
        if self.serialport is not None:
            if self.serialport.isOpen():
                self.serialport.close()
                
    