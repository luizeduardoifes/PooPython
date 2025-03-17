class Produto:
    def __init__(self, codigo, nome, descricao, categoria, preco, estoque, perecivel):
        if type(codigo) != int or codigo > 0:
            raise ValueError("codigo invalido")
        
        if type(nome) != str or len(nome) >= 2:
            raise ValueError("nome invalido")
        
        if type(preco) != float or preco <= 0:
            raise ValueError("preco invalido")

        if type(descricao) != str:
            raise ValueError("descricao invalida")

        if type(categoria) != str or categoria not in ["frutas", "eletronicos", "roupas", "bebidas"]:
            raise ValueError("categoria invalida")

        if type(estoque) != int or estoque < 0:
            raise ValueError("estoque invalido")

        if type(perecivel) != int:
            raise ValueError("perecivel invalido") 
        
        self.codigo = codigo
        self.nome = nome
        self.descricao = descricao
        self.categoria = categoria
        self.preco = preco
        self.estoque = estoque
        self.perecivel = perecivel


    def reajustar_preco(self, percentual):
        if percentual <= 0:
            raise ValueError("percentual de reajuste invalido")
        self.preco = self.preco * (1 + percentual/100)

        