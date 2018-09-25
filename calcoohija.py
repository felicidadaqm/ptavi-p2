#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoo


class CalculadoraHija(calcoo.Calculadora):

    operando1 = ""
    operando2 = ""

    def multiply(self):
        return self.operando1 * self.operando2

    def division(self):
        try:
            return self.operando1 / self.operando2
        except ZeroDivisionError:
            sys.exit("Division by zero is not allowed")
            # levanto aquí la excepcion si operando2 es cero


if __name__ == "__main__":

    calc = CalculadoraHija()

    try:
        calc.operando1 = int(sys.argv[1])
        calc.operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    if sys.argv[2] == "suma":
        result = calc.plus()
    elif sys.argv[2] == "resta":
        result = calc.minus()
    elif sys.argv[2] == "multiplica":
        result = calc.multiply()
    elif sys.argv[2] == "divide":
        result = calc.division()
    else:
        sys.exit("Operación inválida.")

    try:
        print(result)
    except NameError:
        sys.exit("No se puede imprimir el resultado")
