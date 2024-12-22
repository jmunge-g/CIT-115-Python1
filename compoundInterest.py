"""


FV = PV(1+r/m)**mt
PV = 1000
R = 2.5
t = 2
m = 12
"""
fPrinciple = float(input(": ")) #PV -asks for input then converts it to a float and stores it in a variable
#R -does the same thing but with the interest rate but divide by 100 to get a decimal representing a percent 0.025
fInterestRate = float(input("Enter the annual interest rate: ")) / 100
#asks for how many times per year the interest is compounded, 
#cannot be a float because you cant compound the interest rate
#1.5 times a year, it is once a year, twice a year etc.
iTimesCompoundedPerYear = int(input("How many times per year is the interest compounded?: ")) #m
#again we cant have 1.5 years, it must be whole years like 2 years so its an int
iYears = int(input("For how many years will the account earn interest?: ")) #t
#plug in variables into formula on line 12
FV = fPrinciple * (1 + fInterestRate / iTimesCompoundedPerYear) ** (iTimesCompoundedPerYear*iYears)
print(f"At the end of {iYears} years you will have ${FV:,.2f}")