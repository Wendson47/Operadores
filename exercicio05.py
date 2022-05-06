from __future__ import division


largura = input("Coloque a largura do seu comodo em metros: ")

comprimento = input("Coloque o comprimento do seu comodo em metros: ")

resultado = float(comprimento) * float(largura)

dividir = resultado / 2

mensagem = "Sera necessário " + str(dividir) + " litros de produto para realizar a limpeza. "

print(mensagem)  