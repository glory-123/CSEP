p=eval(input("enter the principal amount: "))
r=eval(input("enter the rate: "))
n=eval(input("enter the time in years: "))
def compound_interest(p,r,n):
	amount=p*(pow((1+r/100),n))
	return amount
amount=compound_interest(p,r,n)
ci=amount-p
print("compound interest is : ",ci)
