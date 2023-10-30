from conta_corrente import Corrente

conta = Corrente()

conta.criar_conta(nome='João Pedro',email='JoaoPedro@gmail.com',limite=1000)

conta.sacar(100)
print()
conta.depositar(100)
print()


print(conta)

conta.criar_conta(nome='João Pedro',email='JoaoPedro@gmail.com',limite=1000)

print(conta)


