foods ={}
prices = []
total = 0



while True :
    food = input("silahkan masukan paket makanan yang di beli (q to quit): ")
    if food.lower() == "q" :
        break
    else:
        price= float(input(f"silahkan masukan harga {food}: RP"))
        
        prices.append(price)
    

print("----- YOUR CARD-----")

for food in foods:
    print(food, end=" ")

for price in prices:
    total += price

print()
print(f"your total is: ${total}")