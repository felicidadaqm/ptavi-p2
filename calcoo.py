#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


class Calculadora:

	def plus(self, operando1, operando2):
		return operando1 + operando2

	def minus(self, operando1, operando2):
		return operando1 - operando2

calc = Calculadora()
# instancio el objeto

if __name__ == "__main__":
    try:
        calc.operando1 = int(sys.argv[1])
        calc.operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    if sys.argv[2] == "suma":
        result = calc.plus(calc.operando1, calc.operando2)
    elif sys.argv[2] == "resta":
        result = calc.minus(calc.operando1, calc.operando2)
    else:
        sys.exit('Operación sólo puede ser sumar o restar.')

print(result)
