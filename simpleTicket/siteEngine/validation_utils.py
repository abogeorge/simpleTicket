# Checks if the provided char is at least 5 chars long
def validateMinCharLength(field):
    if len(field) >= 5:
        return True
    else:
        return False

# validates that the value provided by the user is a float value above 0
def validateValue(value):
    if isinstance(value, float):
        if value > 0.0:
            return True
    return False

# validates that the number of units provided by the user is an integer value above 0
def validateUnits(units):
    if isinstance(units, int):
        if units > 0:
            return True
    return False