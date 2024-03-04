house_price = 1000000

buyer_credit = False

if buyer_credit:
    print("Good Credit! :)")
    print("Down Payment 10%")
    total = 0.1 * house_price
    print(total)
else:
    print("Bad Credit :(")
    print("Down Payment 20%")
    total = 0.2 * house_price
    print(total)


# How video solve
price = 1000000
has_good_credit = True
if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down Payment: ${down_payment}")