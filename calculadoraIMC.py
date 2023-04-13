#CALCULADORA IMC 
#testando conhecimento de manipulação de input e condicionais

height = float(input("Sua altura em M "))
weight = float(input("seu peso em Kg "))
bmi = round(weight / height**2)
if bmi < 18.5:
    print(f"Seu IMC é {bmi}, você esta abaixo do peso normal.")
elif bmi < 25:
    print(f"Seu IMC é {bmi}, você está com o peso normal.")
elif bmi < 30:
    print(f"Seu IMC é {bmi}, você está com sobrepeso.")
elif bmi < 35:
    print(f"Seu IMC é {bmi}, você está com obesidade classe I")
elif bmi < 40:
    print(f"Seu IMC é {bmi}, você está com obesidade classe II")
else:
    print(f"Seu IMC é {bmi}, você está com obesidade classe III")

