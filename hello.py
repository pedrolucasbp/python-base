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
__version__ = "0.1.3"
__author__ = "Pedro Lucas"
__license__ = "GPLv2"

import os
import sys

arguments = {
        "lang": None,
        "count": None,
}
for arg in sys.argv[1:]:
  # TODO: Fix ValeuError
  key, value = arg.split("=")
  key = key.lstrip("-")
  value = value.strip()
  if key not in arguments:
    print ("Invalid option `{key}`")
    sys.exit()
  arguments[key] = value


current_language = arguments["lang"]

if current_language is None:

  if "LANG" in os.environ:
    current_language = os.getenv("LANG")

  else :
    current_language = input("Choose a languge:")

current_language = current_language[:5]

msg = {
        "en_US": "Hello, world!",
        "pt_BR": "Olá, Mundo!",
        "it_IT": "Ciao, Mondo!",
        "es_SP": "Hola, Mundo!",
        "fr_FR": "Bonjour, Monde!",
        "de_DE": "Hallo, Welt!",
}

if arguments["count"] is not None:
  print(msg[current_language] * int(arguments["count"]))
else :
  print(msg[current_language])
