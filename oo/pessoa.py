class Pessoa:
    def __init__(self, nome=None):
        self.nome = None
    def cumprimentar(self):
         return f'olá{id(self)}'


if __name__ == '__main__':
    p = Pessoa('Julia')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    p.nome = 'Julia'
    print(p.nome)
