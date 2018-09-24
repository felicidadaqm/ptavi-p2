#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


class Calculadora:

    def plus(self, operando1, operando2):
        return operando1 + operando2

    def minus(self, operando1, operando2):
        return operando1 - operando2


class CalculadoraHija(Calculadora):

    def multiplication(self, operando1, operando2):
        return operando1 * operando2

    def division(self, operando1, operando2):
            return operando1 / operando2


calc = CalculadoraHija()
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
    elif sys.argv[2] == "multiplica":
        result = calc.multiplication(calc.operando1, calc.operando2)
    elif sys.argv[2] == "divide":
        if calc.operando2 == "0":
            sys.exit("Division by zero is not allowed")
        else:
            result = calc.division(calc.operando1, calc.operando2)
    else:
        sys.exit("Operación sólo puede ser sumar o restar.")

print(result)
