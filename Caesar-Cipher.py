# -*- coding: utf-8 -*-

import textwrap

print ("Scegli l'alfabeto tra Italiano e Inglese:", "Choose between Italian and English alphabet:")
x = input ()

ita = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "z"]
eng = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


if x == "Italiano" or x == "italiano" or x == "Italian" or x == "italian":
  y = ita
else:
  y = eng

chiave = 3
testo_cifrato = ""

if y == ita:
  print ("Inserisci il testo da tradurre:")
  testo = input ()
  testo = testo.lower()
else:
  print ("Enter the text to be translated:")
  testo = input ()
  testo = testo.lower()


for lettera in testo:
  if lettera in y:
    posizione = y.index(lettera)
    nuova_posizione = (posizione + chiave) % len(y)
    testo_cifrato = testo_cifrato + y[nuova_posizione]
  else:
    testo_cifrato = testo_cifrato + lettera


print("=" * 50)
if y == ita:
  print("TESTO CIFRATO:")
else:
  print("TRANSLATED TEXT:")
print(textwrap.fill(testo_cifrato, width=50))
print("=" * 50)

if y == ita:
  print("Vuoi vedere anche il testo originale?")
else:
  print("Would you like to see the original text as well?")
z = input()

if z == "si" or z == "Si":
  print("\n" + "=" * 50)
  print("TESTO ORIGINALE:")
  print(textwrap.fill(testo, width=50))
elif z == "Yes" or z == "yes":
  print("\n" + "=" * 50)
  print("Original Text:")
  print(textwrap.fill(testo, width=50))
else:
  print("\n" + "=" * 50)
  if y == ita:
    print("Arrivederci!")
  else:
    print("Goodbye!")

if y == ita:
  print("\n" + "=" * 50)
  print("Aspetta mi sono dimenticato di chiederti se vuoi tradurre messagio dal criptato all'italiano?")

else:
  print("\n" + "=" * 50)
  print("Wait, I forgot to ask you if you want to translate the message from encrypted to English?")

q = input()

if q == "si" or q =="SI":
  print("\n" + "=" * 50)
  print("Incolla il testo qui")
elif q == "Yes" or q == "yes":
  print("\n" + "=" * 50)
  print("Paste the text here:")

w = input()

if q == "si" or q =="SI":
  p = ita
else:
  p = eng


testo_decifrato = ""

nuovo_testo = w.lower()

for carattere in nuovo_testo:
  if carattere in p:
    position = p.index(carattere)
    new_position = (position - chiave) % len(y)
    testo_decifrato = testo_decifrato + y[new_position]
  else:
    testo_decifrato = testo_decifrato + carattere

print("=" * 50)
if p == ita:
  print("TESTO DECIFRATO:")
else:
  print("TRANSLATED TEXT:")
print(textwrap.fill(testo_decifrato, width=50))
print("=" * 50)
