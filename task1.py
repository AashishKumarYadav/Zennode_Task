import hashlib

class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __hash__(self):
        hash1 = hashlib.md5(self.first.encode()).hexdigest()
        hash2 = hashlib.md5(str(self.second).encode()).hexdigest()
        return int(hash1, 16) ^ int(hash2, 16)

productPrices = {
    "Product A": 20,
    "Product B": 40,
    "Product C": 50
}

mp = {}
for product in ["Product A", "Product B", "Product C"]:
    quantity = int(input("Enter the quantity of " + product + ": "))
    mp[Pair(product, productPrices[product])] = quantity

giftWrap = bool(int(input("Enter 1 if You want giftWrap or Not Enter 0: ")))

print("Product Details:- ")
print("Product Name | Total Product Price | Quantity ")
for key, value in mp.items():
    print(key.first, key.second * value, value)

totalQuantity = 0
totalAmount = 0
higherQty = 0
higherQtyAmount = 0
for key, value in mp.items():
    totalQuantity += value
    totalAmount += key.second * value
    if value > 15:
        higherQty = value
        higherQtyAmount = key.second * value
    elif 10 < value < 16 or (10 < value and totalQuantity >= 30):
        higherQty = value
        higherQtyAmount = key.second * value

print("SubTotal Amount:", totalAmount)

discount = 0
amountAfterDiscount = 0
discount1 = 0
if totalQuantity > 30 and higherQty > 15:
    discount1 = (higherQtyAmount * 50) // 100

discount2 = 0
if totalQuantity > 20:
    discount2 = (totalAmount * 10) // 100

discount3 = 0
if higherQty > 10:
    discount3 = (higherQtyAmount * 5) // 100

discount4 = 0
if totalAmount > 200:
    discount4 = 10

if discount1 > 0 and discount1 >= discount2 and discount1 >= discount3 and discount1 >= discount4:
    totalAmount -= higherQtyAmount
    discount = discount1
    amountAfterDiscount = higherQtyAmount - discount
    amountAfterDiscount += totalAmount
    print("50% Discount: ")
elif discount2 > 0 and discount2 >= discount1 and discount2 >= discount3 and discount2 >= discount4:
    discount = discount2
    amountAfterDiscount = totalAmount - discount
    print("10% Discount: ")
elif discount3 > 0 and discount3 >= discount1 and discount3 >= discount2 and discount3 >= discount4:
    totalAmount -= higherQtyAmount
    discount = discount3
    amountAfterDiscount = higherQtyAmount - discount
    amountAfterDiscount += totalAmount
    print("5% Discount: ")
elif discount4 > 0 and discount4 >= discount1 and discount4 >= discount2 and discount4 >= discount3:
    discount = discount4
    amountAfterDiscount = totalAmount - discount
    print("$10 Discount: ")
else:
    print("No Discount: Sorry ")

print(discount)

totalPrice = amountAfterDiscount
if giftWrap:
    print("gift wrap fee:", totalQuantity)
    totalPrice += totalQuantity

shipingFees = True
packagesFee = 0
if shipingFees:
    if totalQuantity % 10 == 0:
        packagesFee = (totalQuantity // 10) * 5
    else:
        packagesFee = ((totalQuantity // 10) * 5) + 5
    print("Shiping fee:", packagesFee)
    totalPrice += packagesFee

print("Final Total:", totalPrice)

print("Note all amount in $")