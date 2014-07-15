#!/usr/bin/env python
# -*- coding: utf-8 -*-

#==== Signal ========== Abbrev ==== Pin ========================================
# Common Ground           G          5
# Transmitted Data        TxD        3
# Received Data           RxD        2
# Data Terminal Ready     DTR        4
# Data Set Ready          DSR        6
# Request To Send         RTS        7 
# Clear To Send           CTS        8
# Carrier Detect          DCD        1
# Ring Indicator          RI         9
#===============================================================================

import codigomorse
import serial
from time import sleep

class CodigoMorseSerial():
    """Clase CodigoMorseSerial"""
    
    serialport = None
    
    def __init__(self, wpm=10, sport=0, sbaudrate=9600, sbytesize=8, sparity='N',
                 sstopbits=1, stimeout=None, sxonxoff=False, srtscts=False,
                 sdsrdtr=False):
        u"""Crea una nueva instacia de CodigomorseSerial.
        
           Argumentos:
           wpm        --  Words Per Minute (Palabras Por Minuto)(default: 10)
           sport      --  Puerto serie a utilizar (default: 0)
           sbaudrate  --  Ratio de baudios a utilizar (default: 9600)
           sbytesize  --  Tamaño de bytes (default: 8)
           sparity    --  Bit de paridad (default: 'N')
           sstopbits  --  Bits de parada (default: 1)
           stimeout   --  Timeout (default: None)
           
           
           Atención: poner a True solamente uno de los 3 argumentos siguientes:
           sxonxoff   --  Control de flujo por software (default: False)
           srtscts    --  Control de flujo por hardware RTS/CTS (default: False)
           sdsrdtr    --  Control de flujo por hardware DSR/DTR (default: False)
        """
        try:
            # Inicializar puerto serie
            self.serialport = serial.Serial(port=sport, baudrate=sbaudrate,
                                            bytesize=sbytesize, parity=sparity,
                                            stopbits=sstopbits, timeout=stimeout,
                                            xonxoff=sxonxoff, rtscts=srtscts,
                                            dsrdtr=sdsrdtr)
            self.serialport.setRTS(0)
            self.serialport.setDTR(0)
        except serial.SerialException:
            print 'Se ha producido un error al intentar conectarse al' + \
                  ' puerto {0} ("{1}")'.format(sport, serial.device(sport))
        
        self.words_per_minute = wpm
        # Utilizar números flotantes debido a un problema en la división realizada 
        # por el intérprete de Python 2.x
        self.time_unit = 1200.0 / wpm       
        self.tmp_dot = self.time_unit
        self.tmp_dash = self.tmp_dot * 3
        self.tmp_inter_elements_space = self.tmp_dot
        self.tmp_space_between_letters = self.tmp_dot * 3
        self.tmp_space_between_words = self.tmp_dot * 7
    
    def _config_times(self):
        u"""(Re)configura los tiempos de cada elemento basándose en la duración de
            WPM y/o una unidad de tiempo.
        """
        self.tmp_dot = self.time_unit
        self.tmp_dash = self.tmp_dot * 3
        self.tmp_inter_elements_space = self.tmp_dot
        self.tmp_space_between_letters = self.tmp_dot * 3
        self.tmp_space_between_words = self.tmp_dot * 7
        
    def set_words_per_minute(self, wpm):
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
            self._config_times()             # Reconfigurar tiempo de elementos
        else: 
            raise ValueError(u'wpm debe ser un número mayor a cero.')
        
    def set_time_unit(self, duration):
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
            self._config_times()             # Reconfigurar tiempo de elementos
        else: 
            raise ValueError(u'duration debe ser un número mayor a cero.')
    
    def open_port(self):
        """Abre el puerto serie configurado."""
        if self.serialport is not None:
            if not self.serialport.isOpen():
                self.serialport.open()
                
    def close_port(self):
        """Cierra el puerto serie configurado."""
        if self.serialport is not None:
            if self.serialport.isOpen():
                self.serialport.close()
                
    def write_morse_string(self, morsestring, newlines=False):
        u"""Escribe una cadena en código Morse al puerto serie configurado.
        
           Argumentos:
           morsestring -- Cadena en código Morse válida.
           newlines    -- Booleano que indica si al final de la cadena se
                          introduce el caracter de nueva línea (default: False)
        """
        if morsestring != '':
            if self.serialport.isOpen():
                if newlines:
                    # Escribir al puerto con caracter de nueva línea
                    self.serialport.writelines(morsestring)
                else:
                    # Escribir al puerto sin caracter de nueva línea
                    self.serialport.write(morsestring)
                    
    def write_alf_string(self, alfstring, newlines=False):
        u"""Convierte una cadena alfabética en una cadena en código Morse y la
           escribe en el puerto serie.
           
           Argumentos:
           alfstring -- Cadena alfabética
           newlines  -- Booleano que indica si al final de la cadena se introduce
                        el caracter de nueva línea.
        """
        self.write_morse_string(codigomorse.encode_to_morse(alfstring), newlines) 

    def set_RTS(self, morsestring):
        u"""Establece el nivel del pin RTS de acuerdo a los elementos de la cadena Morse.
        
           Argumentos:
           morsestring -- Cadena en código Morse válida.
        """
        self._set_pin_state(morsestring, 'RTS')
    
    def set_DTR(self, morsestring):
        u"""Establece el nivel del pin DTR de acuerdo a los elementos de la cadena Morse.
        
           Argumentos:
           morsestring -- Cadena en código Morse válida.
        """
        self._set_pin_state(morsestring, 'DTR')
        
    def _set_pin_state(self, morsestring, pin):
        u"""Establece el nivel de un pin dado en forma dinámica.
           
           Argumentos:
           morsestring -- Cadena en código Morse válida.
           pin         -- Nombre del pin (salida) del puerto serie válido.
        """
        # Obtener setter del pin de forma dinámica
        pin_control = getattr(self.serialport, 'set' + pin)

        if morsestring != '':
            words = morsestring.split('  ')                 # Separar cadena en palabras
            words_spaces = len(words) - 1
            
            for word in words:                              # Separar palabra en sus letras
                letters = word.split()
                letters_spaces = len(letters) - 1
                
                for letter in letters:
                    elements_spaces = len(letter) - 1
                    for element in letter:
                        # Poner a nivel alto el pin
                        pin_control(1)     
                        if element == '-':
                            # Dejar a nivel alto tanto como dure una raya
                            sleep(self.tmp_dash / 1000.0)
                        elif element == '.':
                            # Dejar a nivel alto tanto como dure un punto
                            sleep(self.tmp_dot / 1000.0)
                        
                        # Poner a nivel bajo el pin
                        pin_control(0)
                        
                        if elements_spaces != 0:
                            # Realizar pausa para emular un espacio entre elementos
                            sleep(self.tmp_inter_elements_space / 1000.0)
                            elements_spaces -= 1
                    
                    if letters_spaces != 0:
                        # Realizar pausa para emular un espacio entre letras
                        sleep(self.tmp_space_between_letters / 1000.0)
                        letters_spaces -= 1
                if words_spaces != 0:
                    # Realizar pausa para emular un espacio entre palabras
                    sleep(self.tmp_space_between_words / 1000.0)
                    words_spaces -= 1

    def __del__(self):
        self.close_port()
        self.serialport = None
