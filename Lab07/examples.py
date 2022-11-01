# 5.1

def average_gpa(gpas):  
    ''' Find the average GPA from the list '''

    

    # Add them up.
    sum = 0
    for gpa in gpas:
        sum += gpa

    # Compute the average and return.
    average = sum / len(gpas)
    return average

average_gpa()