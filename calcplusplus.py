#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoo
import calcoohija
import csv


class CalculadoraPlus(calcoohija.CalculadoraHija):
    operando1 = ""
    operando2 = ""


if __name__ == "__main__":

    calc = CalculadoraPlus()

    try:
        fichero = sys.argv[1]
        fich = open(fichero)
    except (FileNotFoundError, IndexError):
        sys.exit("Introduzca correctamente el nombre de fichero")

    with open(fichero) as File:
        reader = csv.reader(File)
        for row in reader:

            operacion = row[0]

            try:
                calc.operando1 = int(row[1])
                calc.operando2 = int(row[2])
            except ValueError:
                sys.exit("El fichero está vacío")

            if operacion == "suma":
                result = calc.plus()
                for numeros in row[3:]:
                    result = result + int(numeros)

            elif operacion == "resta":
                result = calc.minus()
                for numeros in row[3:]:
                    result = result - int(numeros)

            elif operacion == "multiplica":
                result = calc.multiply()
                for numeros in row[3:]:
                    result = result * int(numeros)

            elif operacion == "divide":
                result = calc.division()
                for numeros in row[3:]:
                    try:
                        result = result / int(numeros)
                    except ZeroDivisionError:
                        sys.exit("Division by zero is not allowed")

            else:
                sys.exit("Operación inválida")

            print(result)
