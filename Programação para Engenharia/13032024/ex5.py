'''
Elabore um programa que solicite uma frase ao usuário e 
escreva a frase toda em maiúscula. 
No mesmo programa exiba a frase sem espaços em branco. 
'''

msg = input("Digite a sua frase: ")
print(msg.upper())
print(msg.replace(' ', ''))