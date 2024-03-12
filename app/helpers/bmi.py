def calc_bmi(weight, height):
  bmi = weight / (height ** 2)
  return bmi

def classify_bmi(bmi):
  if bmi < 18.5:
    return "Under weight"
  elif 18.5 <= bmi < 24.9:
    return "Normal weight"
  elif 25 <= bmi < 29.9:
    return "Overweight"
  elif 30 <= bmi < 34.9:
    return "Obesity grade 1"
  elif 35 <= bmi < 39.9:
    return "Obesity grade 2"
  else:
    return "Obesity grade 3"