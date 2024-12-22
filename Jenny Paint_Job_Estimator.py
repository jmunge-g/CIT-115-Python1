import math


def getFloatInput(prompt):
    while True:
        try:
            nVALUE = float(input(prompt))
            if nVALUE <= 0:
                # a user is expected to enter only positive value
                print("Value must be a positive, non-zero number. Please try again.")
            else:
                # return a positive value or a value greater than zero
                return nVALUE
        except ValueError:
            # inform the user that they have entered a wrong value
            print("Wrong input. Please enter a valid numeric value.")


def getGallonsOfPaint(nSQUARE_FEET, nFEET_PER_GALLON):
    return math.ceil(nSQUARE_FEET / nFEET_PER_GALLON)


def getLaborHours(nLaborHoursPerGallon, nTotalGallons):
    return nLaborHoursPerGallon * nTotalGallons


def getLaborCost(nLaborHours, nLaborChargePerHour):
    return nLaborHours * nLaborChargePerHour


# function calculate tax based on state specified by the user
def getSalesTax(nState):
    nState = nState.upper()
    if nState == "CT":
        return 0.06
    elif nState == "MA":
        return 0.0625
    elif nState == "ME":
        return 0.085
    elif nState == "NH":
        return 0.00
    elif nState == "RI":
        return 0.07
    elif nState == "VT":
        return 0.06
    else:
        # if no state in the list is supplied, tax is 0
        return 0.0

# showCostEstimate function takes four parameters
def showCostEstimate(PAINT_PRICE, GALLONS_NEEDED, LABOR_HOURS, LABOR_COST, SALES_TAX_RATE,
                     CUSTOMER_LAST_NAME):
    nPaintCost = GALLONS_NEEDED * PAINT_PRICE
    nTotalCost = nPaintCost + LABOR_COST
    nTax = nTotalCost * SALES_TAX_RATE
    nGrandTotal = nTotalCost + nTax

    # Create file name and concatenate user's last name with a
    # txt file
    file_name = f"{CUSTOMER_LAST_NAME}_PaintJobOutput.txt"

    # Formatted output
    nOutput = (
        f"Gallons of paint: {GALLONS_NEEDED}\n"
        f"Hours of labor: {LABOR_HOURS:.2f}\n"
        f"Paint charges: ${nPaintCost:.2f}\n"
        f"Labor charges: ${LABOR_COST:.2f}\n"
        f"Tax: ${nTax:.2f}\n"
        f"Total cost: ${nGrandTotal:.2f}\n"

    )

    # Print to screen
    print(nOutput)

    # Write to file
    with open(file_name, "w") as file:
        file.write(nOutput)

    print(f"File: {file_name} was created")


def main():

    # use getFloatInput to validate user's input
    # wrong input raise error as per getFloatInput function
    nSquareFeet = getFloatInput("Enter wall space in square feet: ")
    nPaintPrice = getFloatInput("Enter paint price per gallon: ")
    nFeetPerGallon = getFloatInput("Enter feet per gallon: ")
    nLaborHoursPerGallon = getFloatInput("How many labor hours per gallon: ")
    nLaborChargePerHour = getFloatInput("Labor charge per Hour: ")

    # States: MA, CT, ME, NH, RI, VT
    # strip to remove trailing spaces
    nState = input("State job is in: ").strip()

    # get the customer's last name: also strip trailing spaces
    nName = input("Customer Last Name: ").strip()


    # we can call the functions to get gallons, calculate labor hours
    # get labor cost and calculate sales tax
    nGallonsNeeded = getGallonsOfPaint(nSquareFeet, nFeetPerGallon)
    nLaborHours = getLaborHours(nLaborHoursPerGallon, nGallonsNeeded)
    nLaborCost = getLaborCost(nLaborHours, nLaborChargePerHour)
    nSalesTaxRate = getSalesTax(nState)

    # once we have everything, showCostEstimate function takes all calculated values and output the results
    # on screen: Also save the output on a txt file
    showCostEstimate(nPaintPrice, nGallonsNeeded, nLaborHours, nLaborCost, nSalesTaxRate,
                     nName)


# call the main function here
main()