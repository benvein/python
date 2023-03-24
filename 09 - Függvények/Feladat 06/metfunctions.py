def convertToKelvin(unit: str, degree: float) -> float:
    convertedDegree: float = None
    if (unit=="K" or unit=="Kelvin"):
        convertedDegree = degree + 273.15
    elif (unit=="F" or unit=="Fahrenheit"):
        convertedDegree = 9/5*degree+32

    return convertedDegree