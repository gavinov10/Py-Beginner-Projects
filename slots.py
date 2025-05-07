# Python Slot Machine
import random

def spin_row():
    symbols = ["🍒", "🍉", "🍍", "🔔", "⭐️"]

    return [random.choice(symbols)for _ in range(3)]

def print_row(row):
    print(" ".join(row))

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 3
        elif row[0] == '🍍':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 8
        elif row[0] == '⭐️':
            return (f"Mega Jack Pot!! {bet * 20}")
    return 0
def main():
    balance = 100

    print("***********************************")
    print("----- Welcome to Python Slots ----- \n")
    print("Symbols: 🍒 🍉 🍍 🔔 ⭐️")

    while balance > 0:
        print(f"Current balance ${balance:.2f}")

        bet = input("Place your bet amount: ")

        if not bet.isdigit():
            print("only enter numerical values")
            continue
        
        bet = int(bet)

        if bet > balance:
            print("Insufficient funds")
            continue
        if bet <= 0:
            print("Bet must be greater than 0")
            continue 
        
        balance -= bet

        row = spin_row()
        print("Spinning..\n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
             print(f"You won {payout}")
        else:
            print("Sorry, you lost this round")

        balance += payout
        
        play_again = input("Do you want to play again (Y/N): ").upper()

        if "Y" not in play_again:
            break

    print("Thank you for playing! ")
  
if __name__ == "__main__":
    main()