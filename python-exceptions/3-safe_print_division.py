#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        resultado = None
    finally:
        if resultado is None:
            print("Inside result: None")
        else:
            print("Inside result: {:.2}".format(resultado))
        return resultado
