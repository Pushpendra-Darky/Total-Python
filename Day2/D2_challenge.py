name = input("Enter Your Name: ")
total_sale = input("Enter Total Monthly Sale: ")

total_sale = int(total_sale)
commission = total_sale*13/100

commission = round(commission,2)

print(f"Hi {name}, your commission this month is ${commission} \nThank You,\nHave A Good Day.")