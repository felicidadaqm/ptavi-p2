#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoo
import calcoohija


class CalculadoraPlus(calcoohija.CalculadoraHija):
    operando1 = ""
    operando2 = ""

if __name__ == "__main__":

    try:
        fichero = sys.argv[1]
        fich = open(fichero)
    except (FileNotFoundError, IndexError):
        sys.exit("Introduzca correctamente el nombre de fichero")

    for line in fich.readlines():

        line = line.replace("\n", "")
        elementos = line.split(",")
        operación = elementos[0]

        calc = CalculadoraPlus()

        try:
            calc.operando1 = int(elementos[1])
            calc.operando2 = int(elementos[2])
        except ValueError:
            sys.exit("Coloca valores enteros en tu fichero")

        if operación == "suma":
            result = calc.plus()
            for numeros in elementos[3:]:
                result = result + int(numeros)

        elif operación == "resta":
            result = calc.minus()
            for numeros in elementos[3:]:
                result = result - int(numeros)

        elif operación == "multiplica":
            result = calc.multiply()
            for numeros in elementos[3:]:
                result = result * int(numeros)

        elif operación == "divide":
            result = calc.division()
            for numeros in elementos[3:]:
                try:
                    result = result / int(numeros)
                except ZeroDivisionError:
                    sys.exit("Division by zero is not allowed")

        else:
            sys.exit("Operación inválida")

        print(result)
