#! /usr/bin/env python
# -*- coding: utf-8 -*-

import codigomorse
import time
import Tkinter
import tkSnack

class CodigoMorseSound:
        
    def __init__(self, wpm=10, frequency=500, noteshape='sine'):
        self.words_per_minute = wpm
        self.time_unit = 1200.0 / wpm
        self.frequency = frequency
        self._configTimes()
        
        self._root = Tkinter.Tk()
        tkSnack.initializeSnack(self._root)
        self._noteshape = noteshape
    
    def _configTimes(self):
        self.tmp_dot = self.time_unit
        self.tmp_dash = self.tmp_dot * 3
        self.tmp_inter_elements_space = self.tmp_dot
        self.tmp_space_between_letters = self.tmp_dot * 3
        self.tmp_space_between_words = self.tmp_dot * 7
        
    def setWordsPerMinute(self, wpm):
        if wpm > 0: 
            self.words_per_minute = wpm
            self.time_unit = 1200.0 / wpm
            self._configTimes()
        else: 
            raise ValueError(u'wpm debe ser un número mayor a cero.')
        
    def setTimeUnit(self, duration):
        if duration > 0: 
            self.time_unit = duration
            self.words_per_minute = 1200.0 / self.time_unit
            self._configTimes()
        else: 
            raise ValueError(u'duration debe ser un número mayor a cero.')
        
    def setFrequency(self, frequency):
        if frequency >= 1 and frequency <= 10000: 
            self.frequency = frequency
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
                            self._playNote(self.frequency, self.tmp_dash)
                        elif element == '.':
                            self._playNote(self.frequency, self.tmp_dot)
                        
                        if elements_spaces != 0:
                            time.sleep(self.tmp_inter_elements_space / 1000.0)
                            elements_spaces -= 1
                    
                    if letters_spaces != 0:
                        time.sleep(self.tmp_space_between_letters / 1000.0)
                        letters_spaces -= 1
                if words_spaces != 0:
                    time.sleep(self.tmp_space_between_words / 1000.0)
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
