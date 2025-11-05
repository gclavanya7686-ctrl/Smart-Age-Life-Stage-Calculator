
birth_year = int(input("Enter your birth year: "))
birth_month = int(input("Enter your birth month (1-12): "))
birth_day = int(input("Enter your birth day: "))

today = date.today()
age_years = today.year - birth_year
age_months = today.month - birth_month
age_days = today.day - birth_day


if age_days < 0:
    age_months -= 1
    age_days += 30
if age_months < 0:
    age_years -= 1
    age_months += 12

print(f"\nYou are {age_years} years, {age_months} months, and {age_days} days old.")


if age_years < 13:
    print("You are a Child.")
elif age_years < 20:
    print("You are a Teenager.")
elif age_years < 60:
    print("You are an Adult.")
else:
    print("You are a Senior Citizen.")


next_birthday = date(today.year, birth_month, birth_day)
if next_birthday < today:
    next_birthday = date(today.year + 1, birth_month, birth_day)

days_left = (next_birthday - today).days
print(f"{days_left} days left for your next birthday.")