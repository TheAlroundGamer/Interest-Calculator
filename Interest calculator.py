# user input fields
money_in_account = float(input("Money in account:"))
amount_of_years = int(input("Amount of years:"))
yearly_interest = float(input("Amount of interest in a year in % (1.xx):"))

# Commented out for simplicity reasons
# half_yearly_interest = 1.005
# monthly_interest = 1.00085

total_yearly_money = round((money_in_account * yearly_interest ** amount_of_years), 2)

print("In %s years you'll have $%s of interest" % (amount_of_years, (total_yearly_money - money_in_account)))

if yearly_interest <= 1.01:
    print("With this interest its not worth the time")

if yearly_interest >= 1.01:
    print("Saving is worth it with this interest")

if yearly_interest == 1.01:
    print("You decide yourself if its worth it or not")

# Commented out for simplicity reasons
# total_half_yearly_money = money_in_account * half_yearly_interest ** half_yearly_interest
# print("In half a year you'll have $%s of interest" % (total_half_yearly_money - money_in_account))

# total_monthly_money = money_in_account * monthly_interest ** monthly_interest
# print("In a month you'll have $%s of interest" % (total_monthly_money - money_in_account))
