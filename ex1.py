entrada = input().strip()
preco_str, codigo_promocao = entrada.split()

preco = float(preco_str)

if codigo_promocao == "S":
    desconto = preco * 0.1
    preco_final = preco - desconto

else:
    preco_final = preco

print(preco)
print(f"Preco final à pagar é: ", preco_final)

print(f"{preco_final:.2f}")