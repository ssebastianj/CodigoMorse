#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Tkinter
import codigomorse
import tkSnack
from time import sleep

class CodigoMorseSound:
    """Clase CodigoMorseSound"""
        
    def __init__(self, wpm=10, frequency=500, noteshape='sine'):
        u"""Crea una nueva instancia de CodigoMorseSound.
        
            Argumentos:
            wpm        -- Words Per Minute (Palabras Por Minuto)(default: 10)
            frequency  -- Frecuencia de la nota en Hz (default: 500)
            noteshape  -- Forma de onda de la nota. Los valores admitidos son:
                         'sine', 'triangle', 'rectangle', 'noise' y 'sampled' (default: 'sine')
        """
        self.words_per_minute = wpm
        # Utilizar números flotantes debido a un problema en la división realizada 
        # por el intérprete de Python 2.x
        self.time_unit = 1200.0 / wpm       
        self.frequency = frequency
        self.tmp_dot = self.time_unit
        self.tmp_dash = self.tmp_dot * 3
        self.tmp_inter_elements_space = self.tmp_dot
        self.tmp_space_between_letters = self.tmp_dot * 3
        self.tmp_space_between_words = self.tmp_dot * 7
        self._noteshape = noteshape
        
        self._filt = None
        # Inicialización necesaria para que funcione tkSnack.
        self._root = Tkinter.Tk()
        tkSnack.initializeSnack(self._root)
                    
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
        
    def set_frequency(self, frequency):
        u"""Establece la frecuencia de las notas.
        
            Argumentos:
            frequency -- Frecuencia en Hz entre 1 y 10000 (1kHz = 1000Hz)
            
            Excepciones:
            ValueError
        """
        if frequency >= 1 and frequency <= 10000: 
            self.frequency = frequency
        else: 
            raise ValueError(u'frequency debe ser un número entre 1 y 10000.')

    def set_volume(self, volume=50):
        u""""Establece el volumen de las notas.
        
             Argumentos:
             volume -- Volumen de las notas entre 0 y 100 (default: 50)
        """
        if volume > 100: 
            volume = 100
        elif volume < 0: 
            volume = 0
        tkSnack.audio.play_gain(volume)
    
    def play_morse_string(self, morsestring):
        u"""Procesa una cadena en código Morse y la reproduce mediante la placa de sonido
           utilizando las configuraciones de tiempo y duración preestablecidas. 
        
           Argumentos:
           morsestring -- Cadena en formato código Morse válida.
        """
        if morsestring != '':
            words = morsestring.split('  ')                 # Separar cadena en palabras
            words_spaces = len(words) - 1
            
            for word in words:                              # Separar palabra en sus letras
                letters = word.split()
                letters_spaces = len(letters) - 1
                
                for letter in letters:
                    elements_spaces = len(letter) - 1
                    for element in letter:
                        if element == '-':
                            # Reproducir nota de una raya
                            self._play_note(self.frequency, self.tmp_dash)         
                        elif element == '.':
                            # Reproducir nota de un punto
                            self._play_note(self.frequency, self.tmp_dot)
                        
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
                    
    def play_alf_string(self, alfstring):
        u"""Convierte una cadena alfabética en una cadena de código Morse
            y luego la reproduce mediante la placa de sonido.
           
            Argumentos:
            alfstring -- Cadena alfabética.
         """
        self.play_morse_string(codigomorse.encode_to_morse(alfstring))               

    def _play_note(self, frequency, duration):
        u"""Reproduce una nota de frecuencia 'frequency' y duración 'duration'.
        
           Argumentos:
           frequency -- Frecuencia de una nota (en Hz)
           duration  -- Duración de una nota (en milisegundos)
        """
        snd = tkSnack.Sound()
        self._filt = tkSnack.Filter('generator', frequency, 30000, 0.0, self._noteshape,
                                    int(11500 * (duration / 1000)))
        snd.stop()
        snd.play(filter=self._filt, blocking=1)
        
    def sound_stop(self):
        u"""Detiene el sonido que se encuentra reproduciendo (de manera brusca)."""
        try:
            self._root = self._root.destroy()
            self._filt = None
        except Tkinter.EXCEPTION:
            pass
        except Exception:
            pass
        
    def set_note_shape(self, shape):
        u"""Establece la forma de onda de las notas.
           
            Argumentos:
            shape -- Cadena indicando forma de onda a utilizar.
                     Valores admitidos: 'sine','triangle', 'rectangle', 'noise' y 'sampled'
                     
            Excepciones:
            ValueError
        """
        SHAPES = ['sine', 'triangle', 'rectangle', 'sampled', 'noise']
        if shape.lower().strip() in SHAPES:
            self._noteshape = shape
        else:
            raise ValueError(u'El valor de shape no es válido.')
        
    def __del__(self):
        self.sound_stop()
