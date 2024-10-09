import random 
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 10
ROWS = 3
COLS = 3

symbol_count = {
    "$": 2,
    "@": 4,
    "&": 6,
    "%": 8
}

symbol_value = {
    "$": 5,
    "@": 4,
    "&": 3,
    "%": 2
}

def check_win(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], "|", end=" | ")
            else:
                print(column[row], end="")
        print()

def addCredit():
    while True:
        amount = input("Add credits to play: ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0 :
                break
            else:
                print("Credit amount must be greater than 0")
        else:
            print("Please enter a number")
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter number of lines to bet on (1 - " + str(MAX_LINES) + "): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES :
                break
            else:
                print(" Enter valid number of lines")
        else:
            print("Please enter a number")
    return lines

def get_bet():
    while True:
        bet_amount = input("Enter bet amount: ")
        if bet_amount.isdigit():
            bet_amount = int(bet_amount)
            if MIN_BET <= bet_amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} and ${MAX_BET}")
        else:
            print("Please enter a number")
    return bet_amount

def start(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total = bet * lines
        if total > balance:
            print(f"You do not have enough balance to bet that amount. You balance is ${balance}")
            addCredit()
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet is: ${total}")
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_win(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total

def main():
    balance = addCredit()
    while True:
        print(f"Current balance is ${balance}")
        if balance < 10:
            print("Insufficient balance")
            balance = addCredit()
        answer = input("Press enter to play (q to quit)")
        if answer == "q":
            break
        balance += start(balance)

    print(f"You left with ${balance}")    
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)

main()