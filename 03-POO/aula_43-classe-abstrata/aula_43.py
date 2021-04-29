from banco.contapoupanca import ContaPoupanca
from banco.contacorrente import ContaCorrente

cp = ContaPoupanca(1111, 2222, 0)
cp.depositar(10)
cp.sacar(5)
cp.sacar(5)
cp.sacar(1)

print('#' * 45)

cc = ContaCorrente(agencia=2222, conta=33333, saldo=0, limite=150)
cc.depositar(1500)
cc.sacar(1600)
cc.sacar(100)
