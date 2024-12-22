def getFloatInput(prompt):
    # this section uses while loop and try catch to
    # validate user input. The user is expected to enter only
    # positive values and a number greater than 0
    while True:
        try:
            nValue = float(input(prompt))
            if nValue <= 0:
                print("Wrong input!: The value must be positive and non-zero. keep trying.")
            else:
                # we only reach here if number entered is non-zero and positive
                return nValue
        except ValueError:
            # invalid values like strings or any non-numeric
            print("Error: Invalid input. Please enter a valid number.")

def getMedian(nVALUES):
    # Calculates the median
    # determine the number of values
    nNumber = len(nVALUES)
    # If the number of entries in the list is odd,
    # divide the count by 2 and use that entry as the median
    if nNumber % 2 == 1:
        return nVALUES[nNumber // 2]
    else:
        # for even list
        nMid = nNumber // 2
        return (nVALUES[nMid - 1] + nVALUES[nMid]) / 2

def main():

   # Main function to collect sales values to a list
   # perform analysis,
   # display the results.

  # List variable: will hold the entries of sales
    nSales = []
    while True:
        # Get sales value
        nSalesValue = getFloatInput("Enter property sales value: ")
        nSales.append(nSalesValue)

        # Ask if user wants to enter another value
        while True:
            nMoreInput = input("Enter another value Y or N: ").strip().lower()
            if nMoreInput in ('y', 'n'):
                break
            else:
                print("Error: Please enter Y or N.")
        # break out of the loop
        # if input is 'n'
        if nMoreInput == 'n':
            break



    # Output all the entries
    # we've used enumerate function to display sale and counter
    for i, sale in enumerate(nSales, start=1):
        print(f"Property {i}: ${sale:,.2f}")

    # Perform analytics
    nMinValue = min(nSales)
    nMaxValue = max(nSales)
    nTotalValue = sum(nSales)
    nVerageValue = nTotalValue / len(nSales)
    nMedianValue = getMedian(nSales)
    nCommission = nTotalValue * 0.03

    # Display all sale analysis
    # in 2 decimal places
    print(f"Minimum: ${nMinValue:,.2f}")
    print(f"Maximum: ${nMaxValue:,.2f}")
    print(f"Total: ${nTotalValue:,.2f}")
    print(f"Average: ${nVerageValue:,.2f}")
    print(f"Median: ${nMedianValue:,.2f}")
    print(f"Commission: ${nCommission:,.2f}")


# call the main function
main()
