"""
            VALIDATE USER INPUTS
    We want to avoid or handle values:
        |---> which doesn't make sense
        |---> that could crash our program
        |---> could even be a security risk

    by conditionals
        EQUALS:                     a == b
        NOT EQUALS:                 a != b
        LESS THAN:                  a < b
        GREATER THAN:               a > b
        LESS THAN OR EQUAL TO:      a <= b
        GREATER THAN OR EQUAL TO:   a >= b

"""



"""
------------------------------------------------------------------------------------------------------------
-----------------------------------          Global Variables       ----------------------------------------
------------------------------------------------------------------------------------------------------------
"""
seconds_in_x_day = 24*60*60
minutes_in_x_day = 24*60
name_of_unit = "minutes"
#------------------------------------------------------------------------------------------------------------


"""
------------------------------------------------------------------------------------------------------------
----------------------------------------        Functions           ----------------------------------------
------------------------------------------------------------------------------------------------------------
"""
def days_to_units_enhanced(n_days):
    return f"In {n_days} days we have {n_days * minutes_in_x_day} {name_of_unit}"


def days_to_units_user_check(n_days):
    if n_days >= 0:
        return f"In {n_days} days we have {n_days * minutes_in_x_day} {name_of_unit}"
    else:
        return "Please, enter with a positive value"
#------------------------------------------------------------------------------------------------------------


"""
------------------------------------------------------------------------------------------------------------
----------------------------------------       Main Function         ---------------------------------------
------------------------------------------------------------------------------------------------------------
"""
my_var = days_to_units_user_check(10)
print(my_var)

user_var = input("Enter with an valid number of days: \t")
my_var = days_to_units_user_check(int(user_var))
print(my_var)
#------------------------------------------------------------------------------------------------------------