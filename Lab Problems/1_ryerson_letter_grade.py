# As an example, here is an implementation of
# the first problem "Ryerson Letter Grade":

#1
def ryerson_letter_grade(n):
    if n < 50:
        return 'F'
    elif n > 89:
        return 'A+'
    elif n > 84:
        return 'A'
    elif n > 79:
        return 'A-'
    tens = n // 10
    ones = n % 10
    if ones < 3:
        adjust = "-"
    elif ones > 6:
        adjust = "+"
    else:
        adjust = ""
    return "DCB"[tens - 5] + adjust


print(ryerson_letter_grade(45))
print(ryerson_letter_grade(62))
print(ryerson_letter_grade(89))
print(ryerson_letter_grade(107))

#Expected:
    #F
    #C-
    #A
    #A+