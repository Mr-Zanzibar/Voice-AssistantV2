import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import subprocess
import pyjokes
import time
import pyautogui
import psutil
import pyperclip
import ctypes
import winshell
import cv2
from googletrans import Translator
import datetime
import time
import winsound
import pyaudio

#speech to text
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) 

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def
