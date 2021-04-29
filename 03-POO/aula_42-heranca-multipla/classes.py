from log import LogMixin

class Eletronico:
    def __init__(self, nome):
        self._nome = nome  # protegido
        self._ligado = False

    def ligar(self):
        if self._ligado:  # se for True, retorna
            return
        self._ligado = True  # Recebe True
        print(f'{self._nome} agora está ligado.')

    def desligar(self):
        if not self._ligado:  # se _ligado == False, retorna
            return
        self._ligado = False  # rebebe False
        print(f'{self._nome} foi desligado...')


class Smartphone(Eletronico, LogMixin):  # herança múltipla
    def __init__(self, nome):  # precisa receber o mesmo atributo da mãe.
        super().__init__(nome)
        self._conectado = False

    def conectar(self):
        if not self._ligado:
            info = f'{self._nome} não está ligado.'
            print(info)
            self.log_error(info)
            return

        if self._conectado:
            error = f'{self._nome} JÁ ESTÁ CONECTADO.'
            print(error)
            self.log_error(error)
            return

        info = f'{self._nome} agora está conectado.'
        print(info)
        self.log_info(info)
        self._conectado = True

    def desconectar(self):
        if not self._conectado:
            error = f'{self._nome} não está conectado.'
            print(error)
            self.log_error(error)
            return

        info = f'{self._nome} foi desconectado.'
        print(info)
        self.log_info(info)
        self._conectado = False
