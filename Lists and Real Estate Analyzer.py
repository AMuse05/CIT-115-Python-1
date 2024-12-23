def getFloatInput(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))
            
            if value <= 0:
                print("Error: Please enter a positive, non-zero value.")
            else:
                return value
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")

def main():
    count = 0
    sum_sales = 0.0
    min_sales = float('inf')
    max_sales = float('-inf')
    sales_data = []

    while True:
        sales_price = getFloatInput("Enter property sales value: ")
        
        count += 1
        sum_sales += sales_price
        
        if sales_price < min_sales:
            min_sales = sales_price
        if sales_price > max_sales:
            max_sales = sales_price

        sales_data.append(sales_price)

        while True:
            another = input("Enter another value (Y or N): ").strip().lower()
            if another == 'y':
                break
            elif another == 'n':
                break
            else:
                print("Please enter 'Y' for yes or 'N' for no.")
        
        if another == 'n':
            break
    
    sales_data.sort()

    if count % 2 == 1:
        median = sales_data[count // 2]
    else:
        median = (sales_data[(count // 2) - 1] + sales_data[count // 2]) / 2

    print("\nSales Data:")
    property_number = 1
    for price in sales_data:
        print(f"Property {property_number} ${price:,.2f}")
        property_number += 1

    print(f"\nMinimum: ${min_sales:,.2f}")
    print(f"Maximum: ${max_sales:,.2f}")
    print(f"Total: ${sum_sales:,.2f}")
    print(f"Median: ${median:,.2f}")
    print(f"Commission: ${sum_sales * 0.03:,.2f}")

if __name__ == "__main__":
    main()
