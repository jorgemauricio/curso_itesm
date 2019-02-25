#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#  Author: Jorge Mauricio
#  Email: jorge.ernesto.mauricio@gmail.com
#  Date: 2018-02-01
#  Version: 1.0
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

Info:
Script que permite la codificación y decoficación de una frase
por medio del método de Caeser Cipher https://cryptii.com/caesar-cipher

La transformación se puede representar mediante la alineación de dos secuencias
del alfabeto, el alfabeto de cifrado es el alfabeto simple firado hacia la
izquierda o hacia la derecha por un número determinado de posiciones.

Ejmplo:
Cifrado Caeser Cipher usando una rotación de tres posiciones a la izquierda, lo
cual equivale a un desplazamiento de 23 posiciones a la derecha, el parámetro
de cambio se utiliza como clave:

Normal:    ABCDEFGHIJKLMNOPQRSTUVWXYZ
Cifrado:   XYZABCDEFGHIJKLMNOPQRSTUVW

Al encriptar, una persona busca cada letra del mensaje en la línea "normal"
y anota la letra correspondiente en la línea de "Cifrado".


Texto Normal:  TALLER DE PROGRAMACION EN PYTHON
Texto Cifrado: QXIIBO AB MOLDOXJXZFLK BK MVQELK
"""
