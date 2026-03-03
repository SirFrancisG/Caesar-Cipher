# Caesar-Cipher
Encrypt and decrypt text using Julius Caesar's original cipher (Python)
# Caesar Cipher

A Python program that encrypts and decrypts text using **Julius Caesar's Cipher**, one of the oldest known encryption methods.

## How it works

The Caesar Cipher shifts each letter in the alphabet by a fixed number of positions. This implementation uses a key of **3** (the original one used by Julius Caesar), so:

```
a → d,  b → e,  c → f,  ...  w → z,  x → a
```

When a letter is near the end of the alphabet, the count wraps around to the beginning (circular behavior).

## Features

- **Bilingual support**: interface in Italian and English
- **Two alphabets**: Italian (21 letters) and English (26 letters)
- **Encryption**: converts plain text → encrypted text
- **Decryption**: converts encrypted text → plain text
- **Formatting**: readable output with 50-character margins

## Requirements

- Python 3.x

No external libraries needed (only uses `textwrap` from the standard library).

## Usage

```bash
python caesar_cipher.py
```

The program will guide you step by step:

1. Choose the language (Italian / English)
2. Enter the text to encrypt
3. View the encrypted result
4. Option to see the original text
5. Option to decrypt a message

## Example

```
Scegli l'alfabeto tra Italiano e Inglese:
inglese
Enter the text to be translated:
hello world
==================================================
TRANSLATED TEXT:
khoor zruog
==================================================
```

## Author

Francesco Giordano
