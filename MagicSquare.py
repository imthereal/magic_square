'''  
  File: MagicSquare.py

  Description:

  Student's Name: Audrey McNay

  Student's UT EID: alm5735
 
  Partner's Name:

  Partner's UT EID:

  Course Name: CS 313E 

  Unique Number: 51335

  Date Created: 1/23/18

  Date Last Modified:
'''
import math

#gives row/col value that is in bounds
def in_bounds (num_check, n):
  num_check += 1
  if num_check >= n:
    num_check = 0

  return num_check

#Populate a 2-D list with numbers from 1 to n^2
def make_square ( n ):
    matrix = [0] * n
    for i in range(n):
      matrix[i] = [0] * n

    square_list = list(range(1, (n**2)+1))
    row = n-1
    col = n//2

    for i in square_list:
      if matrix[row][col] == 0:
        matrix[row][col] = i
      else:
        row = row - 2
        col = col - 1
        matrix[row][col] = i
      row = in_bounds(row, n)
      col = in_bounds(col, n)
    return (matrix)
      

# Print the magic square in a neat format where the numbers
# are right justified
def print_square ( magic_square ):
    print()
    n = str(len(magic_square))
    print("Here is a " + n + " x " + n + " magic square: \n")

    col_width = max(len(str(col)) for row in magic_square for col in row) + 2 # width of col to justify
    for row in magic_square:
      print ("".join(str(col).rjust(col_width) for col in row))



      

# Check that the 2-D list generated is indeed a magic square
def check_square ( magic_square ):
    n = len(magic_square)
    magic_sum = n * (n**2 + 1) // 2

    #check rows
    row_check = True
    for row in magic_square:
      if sum(row) != magic_sum:
        row_check = False
    if row_check == True:
      print("\nSum of row = " + str(magic_sum))

    #check col
    col_check = True
    for col in range(n):
       if (sum(row[col] for row in magic_square)) != magic_sum:
        col_check = False
    if col_check == True:
      print("Sum of column = " + str(magic_sum))

    #check diagonal UL to LR
    diagonal1 = 0
    for i in range(n):
        diagonal1 += magic_square[i][i]
    if diagonal1 == magic_sum:
      print("Sum diagonal (UL to LR) = " + str(diagonal1))

    #check diagonal UL to LR
    diagonal2 = 0
    for i in range(n):
        diagonal2 += magic_square[i][n-1-i]
    if diagonal2 == magic_sum:
      print("Sum diagonal (UR to LL) = " + str(diagonal2))


def main():
    while True:
      n = int(input("Please enter an odd number: ")) # Prompt the user to enter an odd number 3 or greater 
      if (n < 3) and (n % 2 == 0):
        print("That number is less than 3 and not odd. Try again.")
      elif n < 3:
        print("That number is less than 3. Try again.")
      elif n % 2 == 0: # Check if user input is even
        print("That is not an odd number. Try again.")
      else:
        break
    # Create the magic square
    magic_square = make_square( n )
    # Print the magic square
    print_square( magic_square )
    # Verify that it is a magic square
    check_square( magic_square )
main()