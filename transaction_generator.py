import random
import pymysql

#setup
products = {1:'headphones',2:'phone_case',3:'phone_charger',4:'blazer',5:'jeans'}
prices = {1:135, 2:40,3:20,4:65,5:40}

number_of_days = 10


def store_order_details(order_id,product_id,quantity):
    cur.execute('insert into order_details (order_id,product_id,quantity) values (%s,%s,%s)',
                (order_id,product_id,quantity))
    cur.connection.commit()

def store_orders(order_id,customer_id,total_amount,date):
    cur.execute('insert into orders (order_id,customer_id,total_amount,date) values (%s,%s,%s,%s)',
                (order_id,customer_id,total_amount,date))
    cur.connection.commit()

def choix_client(ids_to_exclude):
    number = random.choice([x for x in range(1,51) if x not in ids_to_exclude])
    ids_to_exclude.append(number)
    return number

    
conn = pymysql.connect(host='******',user='root',passwd='*******',db='mysql')

cur = conn.cursor()
cur.execute('use shop2')

order_details = []
orders = []

order_id = 1



for day in range(1,number_of_days+1):
    total_transactions = random.randint(5,50)

    day_month_year = str(day)+'-01-2024'
    print('Today is day number: ',day_month_year)
    print('Number of transactions today: ',total_transactions)
    transaction_number = 0
    ids_to_exclude = []
    while transaction_number < total_transactions:
        customer_id = choix_client(ids_to_exclude)
        num_items = random.randint(1,5)
        total_amount = 0
    
        product_selected = random.sample(sorted(products.keys()), num_items)
        for product_id in product_selected:
            quantity = random.randint(1,5)
            store_order_details(order_id,product_id,quantity)
            order_details.append((order_id,product_id,quantity))
            total_amount += prices[product_id]*quantity
        store_orders(order_id,customer_id,total_amount,day_month_year)
        orders.append((order_id,customer_id,total_amount,day_month_year))
        order_id += 1
        transaction_number += 1
    i = 1
    while i < 6:
        print(orders[-i])
        i+=1
    
    print('Number of transactions to date: ',len(orders),'\n')
    
