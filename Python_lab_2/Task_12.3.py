n = int(input())
purchase_list = []
purchase_amount_list = []
for i in range(n):
    purchase = input()
    purchase_list.append(purchase)
    purchase_amount = input()
    purchase_amount_list.append(purchase_amount)
for j in range(n - 1, -1, -1):
    print(purchase_list[j], purchase_amount_list[j])