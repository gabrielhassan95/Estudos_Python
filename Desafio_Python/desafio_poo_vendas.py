class Venda:
    def __init__(self, produto, quantidade, valor):
        self.produto = produto
        self.quantidade = quantidade
        self.valor = valor

class Relatorio:
    def __init__(self):
        self.vendas = []

    def adicionar_venda(self, venda):
        # TODOS: Verifique se o objeto passado é uma instância da classe Venda.
        # Isso ajuda a garantir que apenas vendas válidas sejam adicionadas ao relatório.
        if isinstance(venda,Venda):
            self.vendas.append(venda)
        else:
            print("Erro: O obejto não é uma instância da classe Venda")    
        

    def calcular_total_vendas(self):
        total = 0
        for venda in self.vendas:
            # TODOS: Calcule o total de vendas baseado nas vendas adicionadas:
             # O cálculo deve multiplicar a quantidade pelo valor de cada venda e somar ao total.
            total += venda.quantidade*venda.valor 
            
        return total


def main():
    relatorio = Relatorio()
    
    for i in range(3):
        produto = input("Digite o nome do Produto: ")
        quantidade = int(input("Digite a quantidade: "))
        valor = float(input("Digite o valor unitário: "))
        venda = Venda(produto, quantidade, valor)
        relatorio.adicionar_venda(venda)
    
    # TODOS: Exiba o total de vendas usando o método calcular_total_vendas.
    # Utilize o método `calcular_total_vendas` da classe `Relatorio` para mostrar o total acumulado das vendas.
    total_vendas = relatorio.calcular_total_vendas()
    print(f"Total de vendas: R$ {total_vendas:.2f}")


if __name__ == "__main__":
    main()