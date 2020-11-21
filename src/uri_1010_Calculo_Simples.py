# https://www.urionlinejudge.com.br/judge/pt/problems/view/1010
cpeca_1, npeca_1, vpeca_1 = input().split()
cpeca_2, npeca_2, vpeca_2 = input().split()

vtotal = (int(npeca_1) * float(vpeca_1)) + (int(npeca_2) * float(vpeca_2))
print("VALOR A PAGAR: R$ {:.2f}".format(vtotal))