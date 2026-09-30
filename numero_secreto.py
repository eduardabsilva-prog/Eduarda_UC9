import random

numero_secreto = random.randint(1, 1000)
num_tentativas = 0
print("Bem-vindo ao jogo de adivinhação!\nTente adivinhar um número entre 1 e 1000.")

while True: 
    palpite = int(input("\nDigite um número: ")) 
    print(type(palpite))
    num_tentativas += 1 

    if palpite == numero_secreto:
        print("👏​👏​👏​👏​ Você acertou em {num_tentativas} tentativas!")
        break 
    
    elif palpite < numero_secreto:
        print("O número secreto é maior!")

    else: 
        print("O número secreto é menor!")
