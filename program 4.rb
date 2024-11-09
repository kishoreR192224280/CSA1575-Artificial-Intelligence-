import itertools

def solve_cryptarithmetic():
    # All the letters in the cryptarithmetic puzzle
    letters = 'SENDMORY'
    
    # Generate all possible assignments of digits to letters
    for perm in itertools.permutations(range(10), len(letters)):
        # Create a dictionary mapping letters to digits
        assignment = dict(zip(letters, perm))
        
        # Ensure that no leading digit is zero for the words SEND, MORE, or MONEY
        if assignment['S'] == 0 or assignment['M'] == 0:
            continue
        
        # Compute the values of SEND, MORE, and MONEY using the current assignment
        send = 1000 * assignment['S'] + 100 * assignment['E'] + 10 * assignment['N'] + assignment['D']
        more = 1000 * assignment['M'] + 100 * assignment['O'] + 10 * assignment['R'] + assignment['E']
        money = 10000 * assignment['M'] + 1000 * assignment['O'] + 100 * assignment['N'] + 10 * assignment['E'] + assignment['Y']
        
        # Check if SEND + MORE == MONEY
        if send + more == money:
            print("Solution found:")
            print(f" SEND = {send}")
            print(f" MORE = {more}")
            print(f"MONEY = {money}")
            print("Letter to digit mapping:", assignment)
            return

    print("No solution found.")

# Run the solver
solve_cryptarithmetic()
