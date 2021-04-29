from datetime import date


# Para utilizar algo com objeto, é necessário criar uma Class.

# molde
class Pessoa:  # por convenção é nomeada com a primeira letra maiúscula.
    ano_atual = date.today().year

    def __init__(self, nome, idade, comendo=False, falando=False):  # chamado de Instância.
        self.nome = nome  # por convênção, self se referencia ao próprio método
        self.idade = idade  # todas os argumentos estão recebendo "elas" próprias como método.
        self.comendo = comendo
        self.falando = falando

    def falar(self, assunto):
        if self.comendo:  # verificando se um argumento estiver ativo, será exibido um "erro".
            print(f'{self.nome} não pode falar enquanto estiver comendo.')
            return  # se não utilizar o "return" ele executa o comando fora do if.
        if self.falando:
            print(f'{self.nome} já está falando.')
            return
        print(f'{self.nome} está falando sobre {assunto}.')
        self.falando = True

    def parar_falar(self):
        if not self.falando:  # se não estiver falando
            print(f'{self.nome} não está falando.')
            return
        print(f'{self.nome} parou de falar.')
        self.falando = False

    def comer(self, alimento):
        if self.comendo:  # se o método for True, exibe a frase abaixo.
            print(f'{self.nome} já está comendo...')
            return
        if self.falando:
            print(f'{self.nome} não pode comer falando.')
            return

        print(f'{self.nome} está comendo {alimento}')  # todo método está disponível dentro da mesma Class
        self.comendo = True  # o argumento recebe "True"

    def parar_comer(self):
        if not self.comendo:  # se self.comendo for False, apresenta o "erro"
            print(f'{self.nome} não está comendo.')
            return
        print(f'{self.nome} parou de comer.')
        self.comendo = False  # o argumento recebe "False"

    def get_ano_nascimento(self):  # utiliza um atributo da Classe e também da Instância.
        return self.ano_atual - self.idade
