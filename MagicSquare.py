import math

def in_bounds(num_check, n):
  """
  Gives row/col value that is in bounds
  """
  num_check += 1
  if num_check >= n:
    num_check = 0

  return num_check

def make_square(n):
  """
  Populate a 2-D list with numbers from 1 to n^2
  """
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
    
def print_square(magic_square):
  """
  Print the magic square in a neat format where the numbers are right justified
  """
  print()
  n = str(len(magic_square))
  print("Here is a " + n + " x " + n + " magic square: \n")

  col_width = max(len(str(col)) for row in magic_square for col in row) + 2 # width of col to justify
  for row in magic_square:
    print ("".join(str(col).rjust(col_width) for col in row))

def check_square(magic_square):
  """
  Check that the 2-D list generated is indeed a magic square
  """
  n = len(magic_square)
  magic_sum = n * (n**2 + 1) // 2

  #check rows
  for row in magic_square:
    if sum(row) != magic_sum:
      print("Incorrect sum in row", str(row) + ":", sum(row))
      return
  

  #check col
  for col in range(n):
    if (sum(row[col] for row in magic_square)) != magic_sum:
      print("Incorrect sum in column", str(col) + ":", sum(row[col]))
      return

  #check diagonal UL to LR
  main_diag_sum = sum(magic_square[i][i] for i in range(n))
  if main_diag_sum != magic_sum:
    print("Incorrect sum on main diagonal (UL to LR):", main_diag_sum)
    return

  #check diagonal UL to LR
  off_diagonal_sum = sum(magic_square[i][n-1-i] for i in range(n))
  if off_diagonal_sum != magic_sum:
    print("Incorrect sum on off diagonal (UR to LL):", off_diagonal_sum)
    return

  print("\nSum of row = " + str(magic_sum))
  print("Sum of column = " + str(magic_sum))
  print("Sum diagonal (UL to LR) = " + str(magic_sum))
  print("Sum diagonal (UR to LL) = " + str(magic_sum))


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
  magic_square = make_square(n)
  # Print the magic square
  print_square(magic_square)
  # Verify that it is a magic square
  check_square(magic_square)

main()