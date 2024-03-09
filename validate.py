def validate_positive_float(a):
    try:
        float(a)
    except ValueError:
        a = validate_positive_float(input("Por favor, ingrese el valor nuevamente: "))
    else:
        if float(a) < 0: a = validate_positive_float(input("Por favor, ingrese el valor nuevamente: "))
        return float(a)
