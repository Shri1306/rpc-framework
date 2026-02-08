from marshalling import validate_types

def calculate_grade_average(profile):
    validate_types(profile)
    return sum(profile.grades) / len(profile.grades)
