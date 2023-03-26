import json
from Customer import Customer
from Stock import Stock

if __name__ == '__main__':
    with open('input_files/customers.json', 'r') as inp:
        info = json.load(inp)  # См input_files, там видно как выглядит json
    for customer_attrs in info['customers']:
        customer = Customer(**customer_attrs)
        with open(f'output_files/{customer.get_id()}_result.json', 'w') as out:
            print(json.dumps(customer.restaurant_event()), file=out)
    stock = Stock()
