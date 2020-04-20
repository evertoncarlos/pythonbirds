class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'
    @staticmethod
    def estatico_metodo():
        return 42
    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls}- olhos {cls.olhos}'

if __name__ == '__main__':
    renzo = Pessoa(nome='Renzo')
    everton = Pessoa(nome='Everton')
    luciano = Pessoa(renzo, everton, nome='Luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)
    luciano.sobrenome = 'Ramalho'
    del luciano.filhos
    luciano.olhos= 1
    print(luciano.sobrenome)
    print(luciano.__dict__)
    print(everton.__dict__)
    print(Pessoa.olhos)
    print(luciano.olhos)
    print(everton.olhos)
    print(id(Pessoa.olhos), id(everton.olhos), id(luciano.olhos))
    print(Pessoa.estatico_metodo(), luciano.estatico_metodo())
    print(Pessoa.nome_e_atributos_de_classe() , luciano.nome_e_atributos_de_classe())



