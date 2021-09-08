class Person:
  def __initialize__(self, name, age, sex):
    self.name = name
    self.age = age
    self.sex = sex   

def SetAnnual():
  global annual
  annual=1000

def PrintMonthly():
    print("Your monthly payment is " + str(annual/12)+" USD.")
    SetAnnual()
    PrintMonthly()