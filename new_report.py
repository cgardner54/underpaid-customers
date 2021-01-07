

def parselogs(path):
    delivery_log = open(path)
    for line in delivery_log:
        line = line.rstrip()
        words = line.split('|')
    
        customerid = words[0]
        customer_name = words[1]
        melons = words[2]
        amount_paid = words[3]
        overpaid_underpaid = float(amount_paid) - float(melons)

        print()

customer1_expected = customer1_melons * melon_cost
if customer1_expected != customer1_paid:
    print(f"{customer1_name} paid ${customer1_paid:.2f},",
          f"expected ${customer1_expected:.2f}"
          )

parselogs('customer-orders.txt')