class Triangulos:
    def __init__(self):
        pass

    def verificar(self, a, b, c):
        if a == b and a == c and b == c:
             return f"O triangulo é equilatero"
        elif a == b and a != c and b != c:
            return f"O triangulo é isoseles"

        elif a == c and a != b and b != c:
            return f"O triangulo é isoseles"

        elif b == c and b != a and a != c:
            return f"O triangulo é isoseles"

        elif a != b and a != c and b != c:
            return f"O triangulo é escaleno"
