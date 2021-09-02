def arithmetic_arranger(problems, ans = False):

  first_line = ''
  second_line = ''
  
  dashes = ''
  sums = ''
  arranged_problems = []

  # return error if len of the number > 5
  if len(problems)>5:
    return 'Error: Too many problems.'

  #split int three parts
  for p in problems:
    line1 = p.split()[0]
    line2 = p.split()[2]
    operator = p.split()[1]
    

    #check only 4 digits
    if len(line1) > 4 or len(line2) > 4:
      return 'Error: Numbers cannot be more than four digits.'
    #check if each line contains numbers. Then perform the operation
    if not line1.isdigit() or not line2.isdigit():
      return 'Error: Numbers must only contain digits.'
    else:

      if operator == '+':
        total = int(line1) + int(line2)
      elif operator == '-':
        total = int(line1) - int(line2)
      else:
        return "Error: Operator must be '+' or '-'."
      # max length per line are 4 nums
      max_len = max(len(line1),len(line2)) + 2
      
      # adjust each line to the right
      first_line += str(line1.rjust(max_len))
      second_line += str(operator + line2.rjust(max_len-1)) 
      dashes += str('-'* max_len)
      sums += str(total).rjust(max_len)

      #there are 4 spaces for every operation
      if len(problems)-1 :
        first_line += ' '*4
        second_line += ' '*4
        dashes += ' '*4
        sums += ' '*4
    
      if ans == True:
        arranged_problems = first_line.rstrip() + '\n' + second_line.rstrip() + '\n' + dashes.rstrip() + '\n' +sums.rstrip()
      else: 
        arranged_problems = first_line.rstrip() + '\n' + second_line.rstrip() + '\n' + dashes.rstrip()
        
  return arranged_problems
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))