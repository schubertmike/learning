#we are calculating exchange rates of Colombian pesos, Peruvian sols, and Brazilian reals

#first 3 variables capture the inputs and convert to integers
co = int(input("how many pesos do you have?"))
pe = int(input("how many sols do you have?"))
br = int(input("how many reals do you have?"))
#math calculates the total currency they have between the 3 denominations
math = co + pe + br
#usd converts each currency based on the current exchange rate (not dynamic)
#it also adds them together to get the total amount in USD
usd = (co * .00025) + (pe * .28) + (br * .18)

#prints the USD variable
print(usd)
