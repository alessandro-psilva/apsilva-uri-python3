# https://www.urionlinejudge.com.br/judge/pt/problems/view/1009
nvendedor = input()
vsalario = float(input())
vtot_vendas = float(input())

vtot_receber = vsalario + (vtot_vendas * 0.15)
print("TOTAL = R$ {:.2f}".format(vtot_receber))