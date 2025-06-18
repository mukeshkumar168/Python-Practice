# Main function to generate a bill
def bill_generator(item, price, quantity):

    # Calculate the subtotal 
    subtotal = price * quantity

    # calculate GST 18 percent of the subtotal
    gst = subtotal * 0.18
    discount = subtotal * 0.10 

    # calculate the total amount
    total = (subtotal + gst ) - discount

    # Print the bill summary
    print("--Bill Summary--")
    print('Item: ', item)
    print('Price: ', price)
    print('Quantity:', quantity)
    print('Subtotal:', subtotal)
    print('GST (18%):', gst)
    print('Discount(10%)', discount)
    print('Total:', total)
    print('Thank you for your purchase!')

if __name__== '__main__':

    # User input for item details
    item = input("Enter the item name: ")
    price = float(input("Enter the price of the item: "))
    quantity = int(input("Enter the quantity of the item: "))

    # Call the bill generator function with user inputs
    bill_generator(item, price, quantity)

    