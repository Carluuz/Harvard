def main():
    total = 0

    while total < 50:
        coin = int(input("Insert Coin: "))
        if coin in [5, 10, 25]:
            total += coin
        if total < 50:
            print(f"Amount Due: {50 - total}")

    print(f"Change Owed: {total - 50}")

main()
