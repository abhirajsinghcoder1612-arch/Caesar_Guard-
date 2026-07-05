# Caesar_Guard

a simple encryption tool i built with a gui, made using python and tkinter.

it uses the caesar cipher (a classic shift-based encryption method) to encrypt and decrypt text and files. it also has a "shred" feature that securely deletes files so they can't be recovered. 
Image

<img width="1920" height="1031" alt="image" src="https://github.com/user-attachments/assets/10b8d566-22b9-4cf6-b042-f0c2178c3a32" />


## features

- open a .txt file and load it into the app
- encrypt or decrypt text using a shift number you choose
- save always encrypts automatically before writing the file, so you can't accidentally save unprotected data
- shred file permanently deletes a file by overwriting it with random data first, so it can't be recovered
- custom logo + taskbar icon

## why caesar cipher?

caesar cipher isn't actually secure by modern standards (it can be cracked in seconds), but i built this project to learn the fundamentals of encryption, gui development, and file handling in python. it's a starting point, not a production-grade security tool.

## how to run it

you'll need python installed. then just run:

```
python caesarguard.py
```

make sure caesarguard_logo.png and caesarguard_logo.ico are in the same folder.

## how to build it into an .exe (windows)

1. make sure caesarguard.py, caesarguard_logo.png, caesarguard_logo.ico, and build_windows.bat are all in the same folder
2. double-click build_windows.bat
3. your caesarguard.exe will show up inside a new dist folder

## what i learned building this

- basic python (loops, functions, if/else)
- tkinter for building a gui
- reading and writing files
- packaging a python app into a standalone .exe using pyinstaller
- why encryption matters, and the difference between "looks secure" and "is secure"

## notes

this is a personal learning project, not meant for real-world sensitive data. if you want actual secure encryption, look into libraries like cryptography (aes encryption) instead of caesar cipher. 

Copyright &copy; 2026 Abhiraj singh. All rights reserved.

