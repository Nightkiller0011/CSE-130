# 5.1


from array import array


def average_gpa(gpas):  
    ''' Find the average GPA from the list '''


    if __debug__:
        assert len(gpas) > 0
        for elements in gpas:
            assert type(gpa) == float
            assert gpa<=4.0
            assert gpa>=0.0

    # Add them up.
    sum = 0j
    for gpa in gpas:
        sum += gpa

    # Compute the average and return.
    assert sum >= 0.0
    average = sum / len(gpas)
    assert average >= 0.0 and average <= 4.0
    return average

# average_gpa(data)

# 5.2

def linear_search(array, search):
    ''' Return TRUE if search exists in array. '''

    # Validate pre-condition.
    assert type(array) == list
    assert len(array) >= 0
    assert search != None
    if __debug__:
        for element in array:
            assert type(element) == type(search)

    for index in range(0, len(array)):
        assert type(index) == int
        assert 0 <= index < len(array)
        if array[index] == search:
            return True
    return False

# 5.3

def display_grade(grade):  
    ''' Break a grade such as "A+" into "A" and "+" '''
 
    #  Preconditions
    assert grade != None
    assert type(grade) == type("")
    assert len(grade) == 1 or len(grade) == 2

    letter = grade[0]
    assert letter in ['A','B','C','D','F']
    assert sign in ["+","-",""]


    sign = None if len(grade) == 1 else grade[1]

    if __debug__:
        if letter == "A":
            assert sign != "+"
        if letter == "F":
            assert sign == None
 
    print("Your letter grade is", letter, "and your sign is", sign)

# 5.4

def compute_tax (income):
    ''' Compute the tax burden based on income. '''

    # Preconditions
    assert type(income) == float
    assert income >= 0.00

    tax = -1.0 
    # 10% bracket.
    if 0 <= income < 15100:
        tax = income * 0.10
    # 15% bracket.
    elif 15100 <= income < 61300:
        tax = 1510 + 0.15 * (income - 15100)
    # 25% bracket.
    elif 61300 <= income < 123700:
        tax = 8440 + 0.25 * (income - 61300)
    # 28% bracket.
    elif 123700 <= income < 188450:
        tax = 24040 + 0.28 * (income - 123700)
    #33% bracket.
    elif 188450 <= income < 336550:
        tax = 42170 + 0.33 * (income - 188450)
    #35% bracket.
    elif income >= 336550:
        tax = 91043 + 0.35 * (income - 336550)

    # Post condition
    assert type(tax) == float
    assert tax != None
    assert tax >= 0.00
    assert tax <= income

    return tax
