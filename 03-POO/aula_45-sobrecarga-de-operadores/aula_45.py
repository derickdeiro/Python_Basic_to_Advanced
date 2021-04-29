class Retangulo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):  # com esse operador, é possível imprimir o r3 sem mostrar apenas o local da memória
        return f"<class 'Retangulo({self.x}, {self.y})'>"

    def __add__(self, other):  # Com isso o pycharm consegue fazer a soma do X e Y dos Retangulos**
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Retangulo(novo_x, novo_y)


r1 = Retangulo(10, 20)
r2 = Retangulo(10, 20)
r3 = r1 + r2  # **
print(r3)
