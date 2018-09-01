#Defines the object expenses
class expenses (object):
	"""docstring for expenses """
	def __init__(self, rent, phone, gym, utilities, transportation, music,):
		super(expenses , self).__init__()
		self.rent = rent
		self.phone = phone
		self.gym = gym
		self.utilities = utilities
		self.transportation = transportation
		self.music = music

#Allows the user to input data into the object
rent = float(input("How much is your monthly rent?  "))
phone = float(input("How much is your phone bill?  "))
gym = float(input("How much is your gym membership?  "))
utilities = float(input("How much is your monthly utility bill?  "))
transportation = float(input("How much does it cost for transportation monthly?  "))
music = float(input("How much do you spend on music a month?  "))
incomeWeekly = float(input("How much did you make this week?  "))

#Inputs user data into object
myExpenses = expenses(rent, phone, gym, utilities, transportation, music)

#Gets the Budget
def getBudget():
	totalMonthly = myExpenses.rent + myExpenses.phone + myExpenses.gym + myExpenses.utilities + myExpenses.transportation + myExpenses.music
	totalWeekly = (myExpenses.rent + myExpenses.phone + myExpenses.gym + myExpenses.utilities + myExpenses.transportation + myExpenses.music)/4
	weeklyBudget = incomeWeekly - totalWeekly
	monthlyBudget = (incomeWeekly * 4) - totalMonthly
	print(monthlyBudget)
	print(weeklyBudget)

getBudget()
print(myExpenses.rent)
