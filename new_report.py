

def parselogs(path):
    delivery_log = open(path)
    for line in delivery_log:
        line = line.rstrip()
        words = line.split('|')
    
        customerid = words[0]
        customer_name = words[1]
        melons = words[2]
        amount_paid = words[3]
        overpaid_underpaid = float(melons) - float(amount_paid)

        if overpaid_underpaid > 0:
            print(f"{customerid} | {customer_name} underpaid by ${overpaid_underpaid:.2f}.")
        else:
            ""
            
parselogs('customer-orders.txt')