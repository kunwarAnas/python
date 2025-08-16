num = 1

# if num > 5:
#     print("Greater")
# elif num < 5:
#     print("lesser")
# else:
#     print("else case")


# Ternary Operator

age = 20
status = "notEligible" if age < 18 else "eligible"


# Switch case -> ( _ )is default 
day = 3

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case _:
        print("Other day")