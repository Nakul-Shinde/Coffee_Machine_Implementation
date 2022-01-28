logo=''' 
  ______   ______    _______  _______  _______  _______                               
 /      | /  __  \  |   ____||   ____||   ____||   ____|                              
|  ,----'|  |  |  | |  |__   |  |__   |  |__   |  |__                                 
|  |     |  |  |  | |   __|  |   __|  |   __|  |   __|                                
|  `----.|  `--'  | |  |     |  |     |  |____ |  |____                               
 \______| \______/  |__|     |__|     |_______||_______|                              
                                                                                      
                  .___  ___.      ___       ______  __    __   __  .__   __.  _______ 
                  |   \/   |     /   \     /      ||  |  |  | |  | |  \ |  | |   ____|
                  |  \  /  |    /  ^  \   |  ,----'|  |__|  | |  | |   \|  | |  |__   
                  |  |\/|  |   /  /_\  \  |  |     |   __   | |  | |  . `  | |   __|  
                  |  |  |  |  /  _____  \ |  `----.|  |  |  | |  | |  |\   | |  |____ 
                  |__|  |__| /__/     \__\ \______||__|  |__| |__| |__| \__| |_______|
                                                                                      

'''


print ("Welcome ot the coffee Machine ")

print(logo)
coffee_products=[{'name':'expresso','price': 1.50,'water':50,'milk':0,'coffee':18},
                 {'name':'latte','price': 2.50,'water':200,'milk':150,'coffee':24},
                 {'name':'cappuccino','price': 3.0,'water':250,'milk':100,'coffee':24} ]

machine_storage=[{'water':300,'milk':200,'coffee':100,'money':0}]


def manage_resource(selected_product,machine_storage,user_input):
    machine_storage[0]['water']=machine_storage[0]['water']-selected_product['water']
    machine_storage[0]['milk']=machine_storage[0]['milk']-selected_product['milk']        
    machine_storage[0]['coffee']=machine_storage[0]['coffee']-selected_product['coffee']
       
    print("Please insert the coins")
    penny=int(input(f"Penny:"))
    total_penny=float(penny*0.01)
    nickel=int(input(f"nickel:"))
    total_nickel=float(nickel*0.05)
    quarter=int(input(f"quarter:"))
    total_quarter=float(quarter*0.25)
    dime=int(input(f"dime:"))
    total_dime=float(dime*0.10)
    
    total_sum=total_penny+total_nickel+total_quarter+total_dime
   # print(total_sum)
    if total_sum>= selected_product['price']:
        machine_storage[0]['money']=selected_product['price']
        print(F"Here is your Change: ${round(total_sum - selected_product['price'],2)}")
        print(f"Here is your {user_input} Enjoy!!")
    else:
        print(F"Sorry that's not enough money.Money refunded ${round(total_sum)}")
   
def check_stock(user_input):
    
    if selected_product['water']<= machine_storage[0]['water']and selected_product['milk']<= machine_storage[0]['milk']and selected_product['coffee']<= machine_storage[0]['coffee']:
        print(f"We have suffieint supplies for {user_input}")
        return 1
        
    else:
        print(f"Sorry! we don't have sufficient supplies")
        return 0

repeat='y'
while repeat=='y':
    user_input= input("What would you like? (expresso/latte/cappuccino):")
    
    for i in range(0,len(coffee_products)):
        if user_input==coffee_products[i]['name']:
            selected_product=coffee_products[i]
            print(f"\nYou selectoion:\nProduct:{user_input}\nPrice:{coffee_products[i]['price']}\n")
    check=check_stock(user_input)
    
    if check==1:
        total_amount=manage_resource(selected_product,machine_storage,user_input)
    
    user_repeat=input(f"\nDo you want to continue(y/n)")
    if user_repeat=='y':
        repeat=='y'
    else:
        repeat=='n'
    



        
        