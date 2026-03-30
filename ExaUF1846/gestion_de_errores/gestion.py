def escribe(numero):
    try:
        n = int(numero)

        print(f"el número es {n}")
    except ValueError:
        print("Número no valido", ValueError)
    except ZeroDivisionError:
        print("No se puede dividir entre cero")
    except Exception as z:
        print("No se puede dividir entre cero: ", z)
    except Exception as e:
        print("Se produjo el error", e)

escribe("0")

def lista_err():
    try:
        lista = [1,2,3]
        print(lista[6])
    except (IndexError, TypeError) as e:
        print("Error: ", e)
    finally:
        print("Tírate por el barranco")

lista_err()