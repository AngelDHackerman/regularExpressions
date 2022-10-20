#!/usr/bin/python3

import re

# pattern = re.compile(r'^([\d]{4,4})\-.*$')  # * Aqui buscamos el año de la pelicula

pattern = re.compile(r'^([\d]{4,4})\-\d\d\-\d\d\,(.*),Friendly,.*$')  # * Busca si fue un partido amistoso "Friendly"

f = open('./results.csv', 'r')

for line in f:
  res = re.match(pattern, line)  # ? Aqui hace el match de cada linea con el patron que creamos arriba.
  if res:
    print ("%s\n" % res.group(2))

f.close()