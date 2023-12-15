first_number = int(input("Please enter your first number: "))
second_number = int(input("Please enter your second number: "))
operator_choice = str(input("Please enter either + or - : "))

if operator_choice == "+":
    print("The answer is: " + str(first_number) + " + " + str(second_number) + " = " + str(first_number + second_number))
elif operator_choice == "-":
    print("The answer is: " + str(first_number) + " - " + str(second_number) + " = " + str(first_number - second_number))
else:
    print("Unkonwn operator, please use either + or -, and try again")