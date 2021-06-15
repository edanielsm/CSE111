from datetime import datetime

discount_amount = 0
current_day = datetime.now()
print(current_day)
week_day = current_day.isoweekday()
want_continue = ""

while want_continue != 'done':
  user_total = float(input("What is the total amount you purchase?\n> "))
  full_amount = user_total
  if user_total < 50 and ( week_day == 2 or week_day == 3):
    print(f'You need to spend ${(50-user_total):.2f} more to reach the discount.')

  if week_day == 2 or week_day == 3:
    if user_total >= 50:
      discount_amount = user_total * .1
      user_total = full_amount - discount_amount

      

  sale_tax = user_total *.06
    
  total_amount = sale_tax + user_total

  print(f'Sales Tax Amount: ${sale_tax:.2f} ')
  print(f'Discount: ${discount_amount:.2f}')
  print(f'Total: ${total_amount:.2f}')
  want_continue = input("Enter 'done' if you're finished. \n> ")
  want_continue = want_continue.lower()


