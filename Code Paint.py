import math

def getFloatInput(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Error: Value must be a positive non-zero number.")
        except ValueError:
            print("Error: Please enter a valid number.")

def getGallonsOfPaint(fSquareFeet, fFeetPerGallon):
    return math.ceil(fSquareFeet / fFeetPerGallon)

def getLaborHours(fLaborHoursPerGallon, iTotalGallons):
    return fLaborHoursPerGallon * iTotalGallons

def getLaborCost(fLaborHours, fLaborChargePerHour):
    return fLaborHours * fLaborChargePerHour

def getPaintCost(iTotalGallons, fPaintPrice):
    return iTotalGallons * fPaintPrice

def getSalesTaxRate(sState):
    tax_rates = {
        "CT": 0.06,
        "MA": 0.0625,
        "ME": 0.085,
        "NH": 0.0,
        "RI": 0.07,
        "VT": 0.06
    }
    return tax_rates.get(sState.upper(), 0.0)

def showCostEstimate(sCustomerName, iTotalGallons, fLaborHours, fLaborCost, fPaintCost, fTotalCost, fTaxAmount):
    print(f"Customer Last Name: {sCustomerName}")
    print(f"Total Gallons of Paint: {iTotalGallons:,}")
    print(f"Total Labor Hours: {fLaborHours:,.1f}")
    print(f"Labor Cost: ${fLaborCost:,.2f}")
    print(f"Paint Cost: ${fPaintCost:,.2f}")
    print(f"Tax Amount: ${fTaxAmount:,.2f}")
    print(f"Total Cost (including tax): ${fTotalCost:,.2f}")

    filename = f"{sCustomerName}_PaintJobOutput.txt"
    with open(filename, 'w') as file:
        file.write("--- Cost Estimate ---\n")
        file.write(f"Customer: {sCustomerName}\n")
        file.write(f"Total Gallons of Paint: {iTotalGallons:,}\n")
        file.write(f"Total Labor Hours: {fLaborHours:,.1f}\n")
        file.write(f"Labor Cost: ${fLaborCost:,.2f}\n")
        file.write(f"Paint Cost: ${fPaintCost:,.2f}\n")
        file.write(f"Tax Amount: ${fTaxAmount:,.2f}\n")
        file.write(f"Total Cost (including tax): ${fTotalCost:,.2f}\n")
    
    print(f"File: {filename} was created")

def main():
    fSquareFeet = getFloatInput("Enter Wall Space in Square Feet: ")
    fPaintPrice = getFloatInput("Enter Paint Price per gallon: ")
    fFeetPerGallon = getFloatInput("Enter Feet per Gallon: ")
    fLaborHoursPerGallon = getFloatInput("Enter Labor Hours per Gallon: ")
    fLaborChargePerHour = getFloatInput("Enter Labor Charge per Hour: ")
    
    sState = input("Enter the state: ").strip()
    sCustomerLastName = input("Enter the customer's last name: ").strip()

    iTotalGallons = getGallonsOfPaint(fSquareFeet, fFeetPerGallon)
    fLaborHours = getLaborHours(fLaborHoursPerGallon, iTotalGallons)
    fLaborCost = getLaborCost(fLaborHours, fLaborChargePerHour)
    fPaintCost = getPaintCost(iTotalGallons, fPaintPrice)
    
    fSalesTaxRate = getSalesTaxRate(sState)
    fTaxAmount = (fLaborCost + fPaintCost) * fSalesTaxRate
    fTotalCost = fLaborCost + fPaintCost + fTaxAmount

    showCostEstimate(sCustomerLastName, iTotalGallons, fLaborHours, fLaborCost, fPaintCost, fTotalCost, fTaxAmount)

main()
