import kociemba

# Example of a scrambled cube string
# Format: 9 chars for U, then 9 for R, F, D, L, B 
scrambled_cube = "DRLUUBFBRBLURRLRUBLRDDFDLFUFUFFDBRDUBRUFLLFDDBFLUBLRBD"

try:
    # Solve it
    solution = kociemba.solve(scrambled_cube)
    
    print("Purrr Purrr Purrr :#33333")
    print(f"Cube State: {scrambled_cube}")
    print(f"Solution:   {solution}")
    
    # Break it down for a human
    # Won't be needed in the future
    moves = solution.split(' ')
    print(f"Total Moves: {len(moves)}")
    
except Exception as e:
    print(f"Error: Invalid cube state! (Did you scan a face wrong?) \n{e}")