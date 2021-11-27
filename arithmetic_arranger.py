import re
def arithmetic_arranger(problems, solve=False):
  split_problems = [problem.split() for problem in problems]
  
  #Error Message 1:
  if len(split_problems) > 5:
    return "Error: Too many problems."

  a_list = []
  opp_and_b_list = []
  base_list = []
  result_list = []
  

  for problem in split_problems:
    a = problem[0]
    opp = problem[1]
    b = problem[2]

    a_is_digits = re.search('\D', a)  #used to look for
    b_is_digits = re.search('\D', b)  #non-digit strings
    
    a_len = len(a)
    b_len = len(b)
    max_len = max(a_len, b_len)
    base = '-' * (max_len+2)
    #Error Message 3 - non-digit strings
    if a_is_digits == None and b_is_digits == None:
      result = str(eval(f'{a} {opp} {b}'))
    else: 
      return "Error: Numbers must only contain digits."

    #Error Messages 2 & 4:
    if opp == "/" or opp == "*":
      return "Error: Operator must be '+' or '-'."
    
    elif a_len > 4 or b_len > 4:
      return "Error: Numbers cannot be more than four digits."
    
    else:
      a_list.append(a.rjust(max_len+2))
      opp_and_b_list.append(opp + " " + b.rjust(max_len))
      base_list.append(base.rjust(max_len))
      result_list.append(str(result.rjust(max_len+2)))
  
  first_vals = "    ".join(a_list)
  second_vals = "    ".join(opp_and_b_list)
  base_lines = "    ".join(base_list)
  results = "    ".join(result_list)
  
  arranged_result = first_vals + '\n' + second_vals + '\n' + base_lines

  if solve == False:
    return arranged_result
  else:
    return arranged_result + '\n' + results