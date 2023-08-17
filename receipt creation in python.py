def generate_receipt(customer_name, payment_amount, payment_method):
    receipt = f"Receipt\n"
    receipt += f"Customer: {customer_name}\n"
    receipt += f"Payment Amount: ${payment_amount:.2f}\n"
    receipt += f"Payment Method: {payment_method}\n"
    receipt += f"Thank you for your payment!"
    return receipt

def save_receipt_to_file(receipt_content, file_name):
    with open(file_name, 'w') as file:
        file.write(receipt_content)

def main():
    customer_name = input("Enter customer name: ")
    payment_amount = float(input("Enter payment amount: "))
    payment_method = input("Enter payment method: ")

    receipt_content = generate_receipt(customer_name, payment_amount, payment_method)
    receipt_file_name = "payment_receipt.txt"
    save_receipt_to_file(receipt_content, receipt_file_name)

    print("Payment receipt generated and saved to", receipt_file_name)

if __name__ == "__main__":
    main()
