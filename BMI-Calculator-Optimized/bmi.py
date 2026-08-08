def isfloat(n):
  """ 
  If string can be converted to floating number 
  returns that number, otherwise returns false
  """
  try:
    n=float(n)
    return n;
  except ValueError:
     return False;

def inputfloat(hint):
  """ 
  Prints hint and asks to enter number.
  Repeats until decimal number is entered.
  """
  ret = False
  while ret is False:
    ret = isfloat(input(hint))
    if ret is False:
      print("Please enter number")
  return ret 

class BMIcalculator:
  def getdata( ):
    """
    Get weight in kgs and height in cms.
    Height is entered in cetimetres and stored in metres
    """

    w = inputfloat("Please enter your weight in kilograms:")
    h = inputfloat("Please enter your height in centimetres:")/100

  def calculate( ):
    """
    Calculate and return bmi
    """

    return getdata.w/(getdata.h ** 2)
    #return self.w/(self.h ** 2)


def main():
  print("Hello, let's calculate your BMI.");
  
  calc = BMIcalculator()
  calc.getdata()
  bmi=calc.calculate()

  # .2f means 2 decimal places max
  print(f"Your BMI is {bmi: .2f}")

if __name__ == "__main__":
    main()