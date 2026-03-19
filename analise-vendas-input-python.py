🧠 Sistema simples de vendas com input (entrada do usuário)

#Peça ao usuário:

#Digite o faturamento da loja:
faturamento = float(input("Digite o valor: ").replace("R$", "").replace(",", ".").strip())

custo = 800

lucro = faturamento - custo

if lucro >=0:
    print(f"Lucro da loja: R${lucro:,.2f}")
    print("Deu lucro")
else:
    print(f"Prejuizo de: R${lucro:,.2f}")
    print("Deu prejuizo")


vendas_segunda = float(input("Vendas segunda: ").replace("R$", "").replace(",", ".").strip())
vendas_terca = float(input("Vendas terça: ").replace("R$", "").replace(",", ".").strip())
vendas_quarta = float(input("Digite o Quarta: ").replace("R$", "").replace(",", ".").strip())
#print(f"Vendas de segunda: R${vendas_segunda:,.2f}")
#print(f"Vendas de terça: R${vendas_terca:,.2f}")
#print(f"Vendas de quarta R${vendas_quarta:,.2f}") 

total_vendas = vendas_segunda + vendas_terca + vendas_quarta
print(f"Total de Vendas: R${total_vendas:,.2f}")

meta_loja = 5000

if total_vendas >=5000:
    print("Meta atingida.")
else:
    print("Meta não atingida.")
