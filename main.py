

def importKeyboard():
	age = int(input("Enter your age: "))
	ageToRetire = int(input("Enter age to retire: "))
	totalInvestedBegin = float(input("Enter current total investments amount: "))
	investPerYear = float(input("Enter yearly addition to investments: "))
	return age,ageToRetire,totalInvestedBegin,investPerYear
	

	
def calculateFuture(age,ageToRetire,totalInvestedBegin,ipy,badRate=.01,goodRate=.05,greatRate=.08):
	years = ageToRetire - age
	
	totalBad = totalInvestedBegin
	totalGood = totalInvestedBegin
	totalGreat = totalInvestedBegin
	
	for x in range(1,years+1):
		totalBad += ipy
		totalBad *= 1+badRate
		totalGood += ipy
		totalGood *= 1+goodRate
		totalGreat += ipy
		totalGreat *= 1+greatRate
	return [totalBad,totalGood,totalGreat]
	
	
def printValues(bad,good,great):
	print ("\nWith a bad market and 1% yearly rate increase, you will have ${0:,.2f} when you retire.".format(round(bad,2)))
	print ("With a good market and 5% yearly rate increase, you will have ${0:,.2f} when you retire.".format(round(good,2)))
	print ("With a great market and 8% yearly rate increase, you will have ${0:,.2f} when you retire.".format(round(great,2)))
	
	
	
if __name__ == "__main__":
	age,ageToRetire,totalInvestedBegin,investPerYear=importKeyboard()
	bad,good,great = calculateFuture(age,ageToRetire,totalInvestedBegin,investPerYear)	
	printValues(bad,good,great)
	print "\n\nEnter new rates if you so please (ex: .05 is 5%)"
	badRate = float(input("Enter bad rate: "))
	goodRate = float(input("Enter good rate: "))
	greatRate = float(input("Enter great rate: "))
	bad,good,great = calculateFuture(age,ageToRetire,totalInvestedBegin,investPerYear,badRate,goodRate,greatRate)
	printValues(bad,good,great)	

	



