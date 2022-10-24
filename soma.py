#Criei um programa que possua as variáveis A, B e C.
#Imprima o resultado de A + B caso ele seja menor do que C, caso contrário imprima que o valor é menor. 
#Teste a aplicação com alguns valores nas variáveis sugeridas.

from ast import If
from xml.dom.minidom import ReadOnlySequentialNamedNodeMap


A = int(input("valor de A"))
B = int(input("Valor de B"))
C = int(input("Valor de C"))
soma = A + B 

if soma > C:
    print("C É MENOR QUE A + B")
else:
    print("C é maior que A + B")