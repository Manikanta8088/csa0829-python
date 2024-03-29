def calculate_total_amount(denominations, notes):
    total_amount = 0
    for i in range(len(denominations)):
        total_amount += denominations[i] * notes[i]
    return total_amount

def main():
    # Denominations available in the ATM machine
    denominations = [2000, 500, 200, 100]

    # Get the number of notes for each denomination from the user
    notes = []
    for denomination in denominations:
        num_notes = int(input(f"Enter the number of {denomination} notes: "))
        notes.append(num_notes)

    # Calculate the total amount available in the ATM machine
    total_amount = calculate_total_amount(denominations, notes)

    # Display the total amount available
    print(f"Total amount available in the ATM machine: {total_amount}")

if __name__ == "__main__":
    main()
