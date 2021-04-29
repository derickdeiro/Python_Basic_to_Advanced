class Meta(type):  # metaclass
    def __new__(mcs, name, bases, namespace):  # criando o que é preciso na função nova, caso não tenha sido criada.
        if name == 'A':
            return type.__new__(mcs, name, bases, namespace)

        if 'b_fala' not in namespace:
            print(f'Oi, você precisa criar o método "b_fala" em {name}.')
        else:
            if not callable(namespace['b_fala']):
                print(f'"b_fala" precisa ser um método, não atributo em {name}.')

        return type.__new__(mcs, name, bases, namespace)
class A:
    def fala(self):
        self.b_fala()


class B(A):  # B herda de A
    def b_fala(self):
        print('Oi')
    pass

b = B()  # b = class B()
b.fala()  # função "fala()" da class A sendo executada.
