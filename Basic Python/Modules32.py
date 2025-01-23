# def lbs_to_kg(weight):
#   return float(weight) * 0.45

# def kg_to_lbs(weight):
#   return float(weight) / 0.45


# Q
def find_max(numbers):
    max = numbers[0]

    for number in numbers:
        if number>max:
            max = number
    return max
