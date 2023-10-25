#!/usr/bin/env python3
""" This script is a hello world multi lingual.

  Depends on the env LANG variabel this script show a "Hello, world" message
  in this language

 Usage:
    set LANG variabel
 Example:
    python3 hello.py
    or
    ./hello.py
 
"""
__version__ = "0.0.1"
__author__ = "Pedro Lucas"
__license__ = "GPLv2"

import os

current_language = os.getenv("LANG", "en_US")[:5]
msg="Hello, world!"

if current_language == "pt_BR":
   msg = "Olá, Mundo!"

elif current_language == "it_IT":
   msg = "Ciao, Mondo!"

elif current_language == "es_SP":
   msg = "Hola, Mundo!"

elif current_language == "de_DE":
   msg = "Hallo Welt!"

elif current_language == "fr_FR":
   msg = "Bonjour Monde!"

print(msg)
