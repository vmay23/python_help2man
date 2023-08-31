'''
Text Type: string (str)
NUmber Types: Integer (int), Point Float Number (float), etc...
'''

print("200 is a great number")  #string
print(200)  #int
print(200.0)    #float

#Lets calculate how many minutes we have in 20 days
print(20 * 24 * 60)

number_of_days = 20
hours_on_day = 24
minutes_in_hour = 60

minutes_in_20days = number_of_days*hours_on_day*minutes_in_hour
print(minutes_in_20days)

'''
    String Concatenation
    |---> add string to another string
    use '+' for string and str() for !str
'''

print("In one hour we have " + str(60) + " minutes")    #used but not recomended
print(f"In one hour we have {60} minutes")              #most used form to concatenate not string with string (only python3.6 and so on)
print(f"In one day we have {60 * 24} minutes")          #by the way 'f' stands to 'Format'

print(f"In 22 days we have {22 * 24 * 60 * 60} seconds")

'''
V A R I A B L E S

RESERVED WORDS:

  and           except          lambda          with
  as            finally         nonlocal        while
  assert        false           None            yield
  break         for             not             
  class         from            or
  continue      global          pass
  def           if              raise
  del           import          return
  elif          in              True
  else          is              try
'''


seconds_in_x_day = 24*3600
print(f"In 22 days we have {22*seconds_in_x_day} seconds")

name_of_unit = "seconds"
print(f"In 25 days we have   {25*seconds_in_x_day} {name_of_unit}")
print(f"In 1 days we have     {1*seconds_in_x_day} {name_of_unit}")
print(f"In 110 days we have {110*seconds_in_x_day} {name_of_unit}")

