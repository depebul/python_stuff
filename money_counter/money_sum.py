def counting_money(money_list):
    money_sum = 0
    for money in money_list:
        money_sum += money
    return money_sum

def pop_last_value(money_list):
    if money_list:
        return money_list.pop()
    else:
        print("The list is empty.")
        return None

if __name__ == "__main__":
    money_list = list(map(float, input("Enter money values separated by spaces: ").split()))
    while True:
        action = input("Do you want to add more values or pop the last value? (add/pop/exit): ").strip().lower()
        if action == 'add':
            more_values = list(map(float, input("Enter more money values separated by spaces: ").split()))
            money_list.extend(more_values)
        elif action == 'pop':
            popped_value = pop_last_value(money_list)
            if popped_value is not None:
                print(f"Popped value: {popped_value}")
        elif action == 'exit':
            break
        else:
            print("Invalid option. Please enter 'add', 'pop', or 'exit'.")
    print("Total sum:", counting_money(money_list))