if __name__ == "__main__":
    num1 = float(input("Enter the first number: ")) #This line prompts the user to input the first number
    num2 = float(input("Enter the second number: ")) #this line prompts the user to input the second number and stores the converted floating-point value in the variable num2
    num3 = float(input("Enter the third number: ")) #This line prompts the user to input the third number and stores the converted floating-point value in the variable num3
    num4 = float(input("Enter the fourth number: ")) #This line prompts the user to input the fourth number and stores the converted floating-point value in the variable num4

    average = (num1 + num2 + num3 + num4) / 4 #calculate average

    print(f"The average of {num1}, {num2}, {num3}, and {num4} is: {average:.2f}") #print average
