import json


def write_order_to_json(item, quantity, price, buyer, date):
    order = dict()
    with open('orders.json', 'r') as json_file:
        order = json.load(json_file)
    order['orders'].append({
        'item': item,
        'quantity': quantity,
        'price': price,
        'buyer': buyer,
        'date': date
    })
    with open('orders.json', 'w') as json_file:
        json.dump(order, json_file, indent=4)


write_order_to_json('aser', 63, 9990, 'abc', '08.12.2020')
