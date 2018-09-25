#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


class Calculadora:

    operando1 = ""
    operando2 = ""

    def plus(self):
        return self.operando1 + self.operando2

    def minus(self):
        return self.operando1 - self.operando2

calc = Calculadora()

if __name__ == "__main__":

    calc = Calculadora()

    try:
        calc.operando1 = int(sys.argv[1])
        calc.operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    if sys.argv[2] == "suma":
        result = calc.plus()
    elif sys.argv[2] == "resta":
        result = calc.minus()
    else:
        sys.exit('Operación sólo puede ser sumar o restar.')

print(result)
