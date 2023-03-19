from calculator import StringCalculator


if __name__ == '__main__':
   calculator=StringCalculator()
   string = input("Enter a strings numbers :")
  
   response=calculator.add(string)
   print(response)

