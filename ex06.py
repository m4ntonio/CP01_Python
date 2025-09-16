preco = float(input("Digite o preço do produto: "))
if preco > 100:
    desconto = 0.10  # 10% de desconto
    preco_final = preco * (1 - desconto)
    print(f"Preço com desconto: R$ {preco_final:.2f}")
else:
    print(f"Preço sem desconto: R$ {preco:.2f}")