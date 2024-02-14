# TRADUTOR DE CÓDIGO MORSE

from pysine import sine
import time

# DICIONÁRIO MORSE
MORSE_DICT = { 
  'A':'.-',      'B':'-...',   'C':'-.-.',   'D':'-..', 
  'E':'.',       'F':'..-.',   'G':'--.',    'H':'....',
  'I':'..',      'J':'.---',   'K':'-.-',    'L':'.-..', 
  'M':'--',      'N':'-.',     'O':'---',    'P':'.--.', 
  'Q':'--.-',    'R':'.-.',    'S':'...',    'T':'-',
  'U':'..-',     'V':'...-',   'W':'.--',    'X':'-..-', 
  'Y':'-.--',    'Z':'--..',   '1':'.----',  '2':'..---', 
  '3':'...--',   '4':'....-',  '5':'.....',  '6':'-....',
  '7':'--...',   '8':'---..',  '9':'----.',  '0':'-----', 
  ', ':'--..--', '.':'.-.-.-', '?':'..--..', '/':'-..-.', 
  '-':'-....-',  '(':'-.--.',  ')':'-.--.-'
}

# CONVERTE A MENSAGEM PARA MORSE
def translate(message):
  result = ''
  for letter in message:
    if letter != ' ':
      result = result+MORSE_DICT[letter.upper()]+' '
    else: 
      result += '   '
  return result

# CONVERTE O TEXTO PARA ÁUDIO
def read(morse):
  for i in morse:
    if i == '-':
      sine(frequency=440.0, duration=0.3)
      time.sleep(0.1)
    elif i == '.':
      sine(frequency=440.0, duration=0.15)
      time.sleep(0.1)
    else:
      time.sleep(0.3)

# PRINTA A MENSAGEM NO CONSOLE E TOCA O ÁUDIO
def main(x):
  print(translate(x))
  read(translate(x))

main('love is running wild on the diamond sea')