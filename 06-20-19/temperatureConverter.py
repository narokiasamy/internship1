# temperature must be typed with corresponding temperature scale unit! (ex: 32F or 68C)
temperature = str(input("temperature reading: "))

# temperature conversions
if "C" in temperature:
  removeLetter = int(temperature.rstrip("C"))
  fahrenheitCalculation = (int((removeLetter * 1.8) + 32))
  print (str(fahrenheitCalculation) + "F")
  print (temperature)
elif "F" in temperature:
  removeLetter = int(temperature.rstrip("F"))
  celsiusCalculation = (int((removeLetter - 32) / 1.8))
  print (str(celsiusCalculation) + "C")
  print (temperature)

