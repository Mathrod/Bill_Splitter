import random


def number_of_friends():
    number_friends = int(input("Enter the number of friends joining (including you):\n"))
    friends = []
    if number_friends < 1:
        print("No one is joining for the party")
        return False
    else:
        print("Enter the name of every friend (including you), each on a new line:")
        for _ in range(number_friends):
            friends.append(input())
    return friends


def lucky_one(names):
    lucky = input('Do you want to use the "Who is lucky?" feature? Write Yes/No\n')
    if lucky == "Yes":
        lucky_name = random.choice(names)
        print(f"{lucky_name} is the lucky one!")
        return lucky_name
    else:
        print(f"No one is going to be lucky")
        return False


def bill_pp(names, total_bill, lucky):
    if lucky:
        return round(total_bill / (len(names) - 1), 2)
    else:
        return round(total_bill / len(names), 2)


def final_bill(names, total_bill, lucky=False):
    bill = bill_pp(names, total_bill, lucky)
    return {name: (bill if name != lucky else 0) for name in names}


def main():
    friends = number_of_friends()
    if friends:
        total_bill = int(input("Enter the total bill value:\n"))
        lucky = lucky_one(friends)
        print(final_bill(friends, total_bill, lucky))


if __name__ == "__main__":
    main()

