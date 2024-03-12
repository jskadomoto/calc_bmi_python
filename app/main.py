from helpers.bmi import calc_bmi, classify_bmi

def main():
  try:
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))
    
    bmi = calc_bmi(weight, height)
    classification = classify_bmi(bmi)
    
    print(f"Your BMI is: {bmi: .2f}")
    print(f"Your classification: {classification}")
    
  except ValueError:
    print("Please enter valid numeric values!")

if __name__ == "__main__":
  main()