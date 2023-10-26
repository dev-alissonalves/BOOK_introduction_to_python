cigarretes_smoked = int(input("Number of cigarettes smoked per day: "))
smokers_years = int(input("How many years are smokers: "))

days_of_life_lost = (cigarretes_smoked * smokers_years * 10) / 1440

print(f"You have lost approximately {days_of_life_lost:.1f} days of your life due to smoking.")