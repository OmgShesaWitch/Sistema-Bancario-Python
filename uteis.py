def verificanumero(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False