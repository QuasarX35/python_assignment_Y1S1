## NAME: THEY KAI ZHE
## TP NUMBER: TP062802

### EXTRA FUNCTIONS ###

def insert_alt(list, term_to_insert, position): # replaces the built-in function "insert()"
    final_list = []                             # create a final list
    for element in list[0 : position]:          # loops through the specified list starting from the beginning to the specified position in the specified list
        final_list.append(element)              # adds the first part of the specified list into the final list

    final_list.append(term_to_insert)           # adds the term to insert into the final list

    for element in list[position : ]:           # loops through the specified list starting from specified position in the specified list to the end of the specified list
        final_list.append(element)              # adds the second part of the specified list into the final list

    return final_list                           # return the final list

# SAMPLE #
# random_list = ['apple', 'banana', 'orange', 'durian', 'grapes']
# new_list = insert_alt(random_list, 'watermelon', 2)
# print(new_list)

def del_alt(list, index):               # replaces the built-in function "del", but is only for deleting one element from a list"
    final_list = []                     # create a final list
    for element in list[0 : index]:     # loops through the specified list starting from the beginning to the specified position in the specified list
        final_list.append(element)      # adds the first part of the specified list into the final list

    for element in list[index + 1 : ]:  # loops through the specified list starting from after the specified position in the specified list to the end of the specified list
        final_list.append(element)      # adds the second part of the specified list except for the element indexed into the final list

    return final_list                   # return the final list

# SAMPLE #
# random_list = ['apple', 'banana', 'orange', 'durian', 'grapes']
# new_list = del_alt(random_list, 3)
# print(new_list)

def file_to_list(file):                         # converts a file to a list
    try:
        file_handler = open(file, 'r')          # attempts to open the file
    except:
        print(file + ' could not be opened.\n') # print failure if file cannot be opened
        return exit()                           # exit if file cannot be opened
    
    file_lines = file_handler.readlines()       # converts file into list

    count = 0
    for line in file_lines:                     
        file_lines[count] = line.strip().lower()# removes trailing or leading characters such as \n or \t from the list and also makes all letters lowercase
        count = count + 1

    return file_lines                           # returns the list from the file

# SAMPLE #
# test_file = 'sample_file.txt'
# new_list = file_to_list(test_file)
# print(new_list)

# wrong_file = 'unknown_file.txt'
# wrong_list = file_to_list(wrong_file)
# print(wrong_list)

def input_checker(input_type, input_message, error_message):    # checks the input
    while True:
        try:
            answer = input_type(input(input_message))           # input with specified type and specified input message
        except ValueError:                                      # checks if input type is correct
            print(error_message)
            continue
        if answer == '':                                        # checks if entered answer is blank
            print(error_message)
            continue
        else:
            return answer                                       # if none of the conditions above are met, function will return the input

# SAMPLE #
# type_of_input = str
# input_message = 'Please enter your word: '
# error_message = 'Invalid input'
# word = input_checker(type_of_input, input_message, error_message)
# print(word)

# type_of_input = int
# input_message = 'Please enter your number: '
# error_message = 'Invalid input'
# number = input_checker(type_of_input, input_message, error_message)
# print(number)

### PROGRAM FUNCTIONS ###

def login_page(user_type):                                                                          # login page function for the system
    login_page.username = input_checker(str, '\tUsername: ', invalid_input_message).lower()         # input username and checks it using input_checker() function and converts the whole input into lowercase
    print()

    username_line = 'username: ' + login_page.username                                              # adds 'username: ' to the username input so that the code can check with the file list

    if user_type == 'admin':
        retries = 3                                                                                 # number of retries, can be changed
        if username_line in admin_credentials_list:                                                 # if the username is found in the admin username and password list,
            admin_username_index = admin_credentials_list.index(username_line)                      # get the index of the line with the current admin username

            for tries in range(retries + 1):                                                        # for the number of retries + 1:
                password = input_checker(str, '\tPassword: ', invalid_input_message)                # input password and check with input_checker() function
                if 'password: ' + password == admin_credentials_list[admin_username_index + 1]:     # if password is the same as the line after the current admin's username line,
                    print()
                    print('Welcome back, admin ' + login_page.username + '.\n')                     # print admin welcome message and return
                    return
                    
                else:                                                                               # if password is wrong, display the number of retries left and continue the loop
                    if retries == 0:                                                                # if user has used up all of the retries, the program will exit.
                        print('\nYou have run out of retries. Exiting program now.\n')
                        return exit()
                    print('\nIncorrect password. You have ' + str(retries) + ' attempts left.\n')
                    retries = retries - 1
                    continue
        else: 
            print('Username not found.\n')                                                          # if username was not found in the admin username and password list, the user will be returned to the main page
            return False
            
    if user_type == 'customer':                                                                     # same process as admin check code block but checks in customer username and password list instead
        retries = 3
        if username_line in customer_credentials_list:
            customer_username_index = customer_credentials_list.index(username_line)

            for tries in range(retries + 1):
                password = input_checker(str, '\tPassword: ', invalid_input_message)
                if 'password: ' + password == customer_credentials_list[customer_username_index + 1]:
                    print()
                    print('Welcome back, customer ' + login_page.username + '.\n')
                    
                    return
                    
                else:
                    if retries == 0:
                        print('\nYou have run out of retries. Exiting program now.\n')
                        return exit()
                    print('\nIncorrect password. You have ' + str(retries) + ' attempts left.\n')
                    retries = retries - 1
                    continue
        else:
            print('Username not found.\n')
            return False

def add_med():                                                                              # upload medicine function for admin
    while True:                                                                             # keep looping if the medicine name is already in the list and all 4 inputs are not blank
        med_name = input_checker(str, '\tName of Medicine: ', invalid_input_message)        # use the function input_checker() to get the proper input
        if ('name: ' + med_name) in medicine_list:
            print('\n\t***This medicine is already in the medicine list.***\n')
            continue

        exp_date = input_checker(str, '\tExpiry Date (DD/MM/YYYY): ', invalid_input_message)
        price = input_checker(float, '\tPrice (RM): ', invalid_input_message)
        desc = input_checker(str, '\tDescription: ', invalid_input_message)

        break
    
    try:                                                                                    # try to open medicine file, append mode. If medicine file cannot be opened, error message will display and program will be exited
        medicine_file = open('medicine_list.txt', 'a')
    except:
        print("\nmedicine_list.txt could not be opened.\n")
        return exit()

    medicine_file.write('name: ' + med_name.lower() + '\n')                                 # append all inputs into medicine file
    medicine_file.write('expiry date: ' + exp_date.lower() + '\n')
    medicine_file.write('price: rm' + str(price) + '\n')
    medicine_file.write('description: ' + desc.lower() + '\n')
    medicine_file.write('\n')

    medicine_file.close()
    print('\nDetails recorded.\n')                                                          # will display success message if all medicine are recorded into medicine file
    return

def view_med():                                         # displays all medicine details in medicine file
    medicine_list = file_to_list('medicine_list.txt')
    
    for line in medicine_list:
        print(line)
    print()
    return

def del_med():                                                                                              # removes the specified medicine from the medicine file
    medicine_list = file_to_list('medicine_list.txt')
    view_med()                                                                                              # display all available medicine
    
    while True:
        search = input_checker(str, 'Enter the medicine name to delete: ', invalid_input_message).lower()   # input medicine name to delete
        print()
        search_line = 'name: ' + search

        if search_line in medicine_list:
            searched_line_index = medicine_list.index(search_line)                                          # if specified medicine name is found in medicine list,

            new_list = []
            for line in medicine_list[0 : searched_line_index]:                                             # add the first part of the medicine list before the specified medicine name into another list
                new_list.append(line)
            
            for line in medicine_list[searched_line_index + 5 : ]:                                          # add the second part of the medicine list after the medicine and its details to the other list
                new_list.append(line)

            try:
                medicine_file = open('medicine_list.txt', 'w')
            except:
                print("File could not be opened.\n")
                return exit()

            for line in new_list:                                                                           # overwrite the contents of the other list into the medicine text file
                medicine_file.write(line)
                medicine_file.write('\n')

            print('Medicine deleted.\n')

            medicine_file.close()
            return

        else:                                                                                               # if the specified medicine name is not found, display error message and let user try again
            print('\t***Medicine not found***\n')
            continue

def edit_med():                                                                                             # This function removes the specified medicine from the medicine file then lets the user add the details back in to update it
    medicine_list = file_to_list('medicine_list.txt')
    view_med()                                                                                              # This section is similar to del_med function but input message has been changed and successfully deleted message has been removed

    while True:
        search = input_checker(str, 'Enter the medicine name to update: ', invalid_input_message).lower()
        print()
        search_line = 'name: ' + search

        if search_line in medicine_list:
            searched_line_index = medicine_list.index(search_line)

            new_list = []
            for line in medicine_list[0 : searched_line_index]:
                new_list.append(line)
            
            for line in medicine_list[searched_line_index + 5 : ]:
                new_list.append(line)

            try:
                medicine_file = open('medicine_list.txt', 'w')
            except:
                print("File could not be opened.\n")
                return exit()

            for line in new_list:
                medicine_file.write(line)
                medicine_file.write('\n')

            medicine_file.close()
            break

        else:
            print('\t***Medicine not found***\n')
            continue
    
    medicine_list = file_to_list('medicine_list.txt')                                                       # updates the medicine list for the code

    while True:                                                                                             # this section is the same as the add_med function
        med_name = input_checker(str, '\tName of Medicine: ', invalid_input_message)
        if ('name: ' + med_name) in medicine_list:
            print('\n\t***This medicine is already in the medicine list.***\n')
            continue

        exp_date = input_checker(str, '\tExpiry Date (DD/MM/YYYY): ', invalid_input_message)
        price = input_checker(float, '\tPrice (RM): ', invalid_input_message)
        desc = input_checker(str, '\tDescription: ', invalid_input_message)

        break
    
    try:
        medicine_file = open('medicine_list.txt', 'a')
    except:
        print("\nmedicine_list.txt could not be opened.\n")
        return exit()

    medicine_file.write('Name: ' + med_name.lower() + '\n')
    medicine_file.write('Expiry Date: ' + exp_date.lower() + '\n')
    medicine_file.write('Price: RM' + str(price) + '\n')
    medicine_file.write('Description: ' + desc.lower() + '\n')
    medicine_file.write('\n')

    medicine_file.close()
    print('\nDetails recorded.\n')
    return

def search_med():                                                                                       # searches for a specified medicine name in the medicine file
    medicine_list = file_to_list('medicine_list.txt')
    
    while True:
        search = input_checker(str, 'Enter the medicine name to search: ', invalid_input_message).lower()   # input search with input_checker function
        print()
        search_line = 'name: ' + search

        if search_line in medicine_list:                                                                    # if specified medicine is found in medicine list,
            searched_line_index = medicine_list.index(search_line)
            for line in medicine_list[searched_line_index : searched_line_index + 5]:                       # print all the order_list starting from the specified medicine index to the specified medicine index + 5
                print(line)
            return

        else:                                                                                               # print not found message if medicine is not found in medicine list
            print('***Medicine not found***\n')
            continue

def place_order():                                                  # This function lets the customer place one order with a quantity and adds the order to the cart, order list and then to the order file
    medicine_list = file_to_list('medicine_list.txt')
    view_med()                                                      # Part 1: Display medicine list, cart and menu for customer to choose from

    order_list = file_to_list('order_list.txt')
    cart = []
    
    customer_index = order_list.index(customer_username)
    for line in order_list[customer_index + 1 : ]:                  # adds all the logged in customer's order list into the cart
        cart.append(line)
        if line == '':                                              # breaks the loop at the next blank line
            break

    med_menu = []
    count = 1
    for line in medicine_list:                                      # adds all of the medicine names from the medicine list to a new list "med_menu"
        if ('name: ') in line:
            med_name = line.replace('name: ', (str(count) + '. '))
            med_menu.append(med_name)
            count = count + 1

    print('Cart: ')
    for line in cart:                                               # print out the items and quantities in the cart
        print(line)
            
    for line in med_menu:                                           # print out the med menu for the customer to choose from
        print(line)
    print()

    while True:                                                                                         # Part 2: user input
        choice = input_checker(int, 'Please enter the number of choice: ', invalid_input_message)       # input choice and check with input_checker

        if not 0 < choice <= count-1:                                                                   # if choice input is not within the numbers from the med menu,
            print(invalid_input_message)                                                                # display invalid input message and loop again until the input is within the given menu
            continue
        else:
            break
        
    input_quantity = input_checker(int, 'Please enter your desired quantity: ', invalid_input_message)  # input quantity and input with input_checker
    print()
        
    choice = str(choice)                                                        # Part 3: process user input and check for certain conditions in the cart:
                                                                                # 1. if chosen medicine is already in cart, 2. if cart is empty, and 3. if chosen medicine is not yet in the cart
    
    for line in med_menu:                                                       # gets the name of the medicine only as med_name from the user's chosen number
        if line.startswith(choice):
            med_name = line.replace((choice + '. '), 'name: ')
            break
        
    if med_name in cart:                                                        # if chosen medicine is already in cart,
        cart_quantity_index = cart.index(med_name) + 1
        cart_quantity = int(cart[cart_quantity_index].replace('quantity: ', ''))
        cart_quantity = cart_quantity + input_quantity                          # add the new quantity to the old quantity in the cart
        cart[cart_quantity_index] = ('quantity: ' + str(cart_quantity))         # replace the quantity in the cart with the new quantity
            
    elif cart[0] == 'no orders':                                                # if cart has no orders,
        cart = del_alt(cart, 0)                                                 # delete the "no orders" string from the cart using the del_alt function
        cart = insert_alt(cart, med_name, 0)                                    # insert the chosen medicine into the cart using the insert_alt function
        
        cart_quantity = 'quantity: ' + str(input_quantity)
        cart = insert_alt(cart, cart_quantity, 1)                               # insert the quantity into the cart
            
    else:                                                                       # if chosen medicine was not found in the cart,
        cart = insert_alt(cart, med_name, len(cart) - 1)                        # insert the chosen medicine into the line before the blank line
        
        cart_quantity = 'quantity: ' + str(input_quantity)
        cart = insert_alt(cart, cart_quantity, len(cart) - 1)                   # insert the chosen quantity into the line before the blank line
    
    print('Item added to cart.\n')
    
    customer_username_index = order_list.index(customer_username)                   # Part 4: updates the whole order list as well as the order file with the customer's new cart
    for line in order_list[customer_username_index + 1 : ]:                                  # deletes the current customer's orders in the order list
        if line == '':
            break
        order_list = del_alt(order_list, customer_username_index + 1)
    
    count = 1
    for item in cart:                                                               # inserts the customer's new cart into the customer's section in the order list
        if item == '':
            break
        order_list = insert_alt(order_list, item, (customer_username_index + count))
        count = count + 1
        
    try:
        order_file = open('order_list.txt', 'w')
    except:
        print('order_list.txt could not be opened.\n')
        return exit()
    
    for line in order_list:                                                         # overwrites the order file with the updated order list
        order_file.write(line + '\n')
    
    print('Order recorded.\n')
    return

def view_customer_order():                          # views all customer orders
    order_list = file_to_list('order_list.txt')

    for line in order_list:                         # displays all elements in the order list
        print(line)
    
    return

def search_customer_order():                                                                                # searches for a customer's name and prints out their orders
    order_list = file_to_list('order_list.txt')

    search = input_checker(str, 'Please enter customer name to search: ', invalid_input_message).lower()
    print()
    
    if search in order_list:
        customer_index = order_list.index(search)
        for line in order_list[customer_index + 1 : ]:                                                      # prints out the lines in the order list starting from the customer name index to the next empty line
            print(line)
            if line == '':                                                                                  # breaks the loop at the next blank line
                break
    return
    
def view_my_order():                                        # displays the logged in customer's orders
    order_list = file_to_list('order_list.txt')

    customer_index = order_list.index(customer_username)
    for line in order_list[customer_index : ]:              # loops through the order list, starting from the line with the customer name
        print(line)
        if line == '':                                      # prints the lines until it arrives at a blank line
            break
    
    return

def payment():                                                                      # lets the customer proceed to payment   
    medicine_list = file_to_list('medicine_list.txt')
    order_list = file_to_list('order_list.txt')                                     # Part 1: displays the logged in customer's cart and total payable
    
    print('Cart: ')                                                                 # displays the logged in customer's cart
    view_my_order()
    
    customer_index = order_list.index(customer_username)
    
    if order_list[customer_index + 1] == 'no orders':                               # checks if the customer has ordered anything yet
        print('You have no orders yet.')                                            # if not, print not ordered anything yet message
        return
    
    else:
        cart_quantity = 0
        total = 0.00
        for item in order_list[customer_index + 1 : ]:                              # loops through the order list, starting from the line after the customer name
            if item.startswith('name: '):
                price_index = medicine_list.index(item) + 2
                price = float(medicine_list[price_index].replace('price: rm', ''))  # obtains the price of the medicine from the medicine list

            elif item.startswith('quantity: '):
                cart_quantity = item.replace('quantity: ', '')                      # obtains the quantity of the medicine from the order list
                total = total + (price * float(cart_quantity))                      # adds the price and quantity to the total payable
                
            else:                                                                   # if the item is a blank line, the loop will be broken
                break
            
        print('The total amount payable is: RM' + str(total) + '.\n')
                                                                                        # Part 2: removing the customer's orders from the order list and then the order list text file
        for item in order_list[customer_index + 1 : ]:                                  # loops through the order list, starting from the line with the customer name
            if item == '':
                order_list = insert_alt(order_list, 'no orders', customer_index + 1)    # when everything is removed from the customer's order list, 'no orders' will be inserted in the line after the customer name
                break
            order_list = del_alt(order_list, customer_index + 1)                        # deletes the orders from the customer list using the del_alt function
        
        try:
            order_file = open('order_list.txt', 'w')
        except:
            print('order_list.txt could not be opened.')
            return exit()
        
        for line in order_list:                                                         # overwrites the order list text file with the updated order list
            order_file.write(line + '\n')
            
        order_file.close()
        
        print('Thank you for shopping with us.\n')
    return

def view_p_info():                                                              # This function prints out the personal information of the logged in customer.
    customer_details_list = file_to_list('customer_details_list.txt')
    
    customer_index = customer_details_list.index('name: ' + customer_username)
    for line in customer_details_list[customer_index : ]:                       # starts looping through the customer details list from the line with the customer name to the end of the list
        print(line)
        if line == '':                                                          # if the loop hits a blank line, the loop will be broken.
            break
        
    return

def register():                                                                                                             # This function registers a new customer
    customer_details_list = file_to_list('customer_details_list.txt')
    
    while True:                                                                                                             # Part 1: inputs
        name = input_checker(str, '\tName: ', invalid_input_message).lower()                                                # ask new customer to input all the necessary details with the function input(checker)
        address = input_checker(str, '\tAddress: ', invalid_input_message).lower()
        email_id = input_checker(str, '\tEmail ID: ', invalid_input_message).lower()
        contact_number = input_checker(str, '\tContact number: ', invalid_input_message).lower()
        gender = input_checker(str, '\tGender (male/female/other): ', invalid_input_message).lower()
        date_of_birth = input_checker(str, '\tDate of birth (DD/MM/YYYY): ', invalid_input_message).lower()
        username = input_checker(str, '\tUser ID: ', invalid_input_message).lower()
        password = input_checker(str, '\tPassword: ', invalid_input_message).lower()
        password_retry = input_checker(str, '\tConfirm Password: ', invalid_input_message).lower()
        print()
    
        gender_list = ['male', 'female', 'other']
    
        if ('name: ' + name) in customer_details_list:                                                                      # checks if name has already been taken
            print('\n\tThis name has been taken. Please try again.\n')
            continue
        
        elif not gender in gender_list:                                                                                     # checks if user has entered any of the genders in the gender list 
            print('\n\tInvalid gender. Please try again.\n')
            continue
        
        elif ('username: ' + username) in customer_credentials_list or ('username: ' + username) in admin_credentials_list: # checks if username has already been taken
            print('\n\tThis User ID has been taken. Please try again.\n')
            continue
        
        elif ('password: ' + password) in customer_credentials_list or ('password: ' + password) in admin_credentials_list: # checks if password has been taken
            print('\n\tThis password has been taken. Please try again.\n')
            continue
        
        elif password_retry != password:
            print('\n\tYour confirmed password does not match your password. Please try again.\n')                          # checks if confirmed password is the same as the first entered password
            continue
        
        else:
            break
    
    try:                                                                            # Part 2: adding inputs into file
        customer_details_file = open('customer_details_list.txt', 'a')
        customer_list_file = open('customer_list.txt', 'a')
        order_file = open('order_list.txt', 'a')
    except:
        print('customer_details_list.txt or customer_list.txt or order_list.txt could not be opened.')
        return exit()

    customer_details_file.write(                                                    # adds the user inputs into the customer details file
        'Name: ' + name + '\n'
        'Address: ' + address + '\n'
        'Email: ' + email_id + '\n'
        'Contact Number: ' + contact_number + '\n'
        'Gender: ' + gender + '\n'
        'Date of birth: ' + date_of_birth + '\n'
        '\n'
    )

    customer_list_file.write(                                                       # adds the user's specified username and password into the customer list file
        'username: ' + username + '\n'
        'password: ' + password + '\n'
        '\n'
    )
    
    order_file.write(
        username + '\n'
        'no orders\n'
        '\n'
    )

    customer_details_file.close()
    customer_list_file.close()
    order_file.close()
    print('Details recorded. Welcome to the Ocean OPMS.\n')
    return

def admin_menu():                                                                               # displays admin menu and asks user input for number of choice
    
    print(
        '\t1. Upload Medicine\n'
        '\t2. View All Medicine Details\n'
        '\t3. Update/Modify Medicine\n'
        '\t4. Delete Medicine\n'
        '\t5. Search Medicine\n'
        '\t6. View Orders\n' 
        '\t7. Search Customer Orders\n'
        '\t8. Exit\n'
        )
    
    option = input_checker(int, 'Please enter your number of choice: ', invalid_input_message)  # asks user input and returns a the corresponding function
    print()
    
    if option == 1:
        add_med()
        return admin_menu()
    elif option == 2:
        view_med()
        return admin_menu()
    elif option == 3:
        edit_med()
        return admin_menu()   
    elif option == 4:
        del_med()
        return admin_menu()    
    elif option == 5:
        search_med()
        return admin_menu()    
    elif option == 6:
        view_customer_order()
        return admin_menu()   
    elif option == 7:
        search_customer_order()
        return admin_menu()    
    elif option == 8:
        return
    else:
        print(invalid_input_message)
        return admin_menu()

def customer_menu():                                                                            # displays the functions that the customer can choose to do and ask for the customer input
    
    print(
        '\t1. View All Medicine Details\n'
        '\t2. Place An Order\n'
        '\t3. Proceed to Payment\n'
        '\t4. View My Orders\n' 
        '\t5. View Personal Information\n'
        '\t6. Exit\n'
        )
    option = input_checker(int, 'Please enter your number of choice: ', invalid_input_message)  # asks user input and returns a the corresponding function
    print()
    
    if option == 1:
        view_med()
        return customer_menu()
    elif option == 2:
        place_order()
        return customer_menu()
    elif option == 3:
        payment()
        return customer_menu()
    elif option == 4:
        view_my_order()
        return customer_menu()
    elif option == 5:
        view_p_info()
        return customer_menu()
    elif option == 6:
        return
    else:
        print(invalid_input_message)
        return customer_menu()

def new_customer_menu():                                                                        # displays the functions that a user that is not registered yet can and returns the corresponding function
    print(
        '\t1. View All Medicine Details\n'
        '\t2. Register\n'
        '\t3. Exit\n'
    )
    option = input_checker(int, 'Please enter your number of choice: ', invalid_input_message)  # asks user input and returns a the corresponding function
    print()

    if option == 1:
        view_med()
        return new_customer_menu()
    elif option == 2:
        register()
        return
    elif option == 3:
        return
    else:
        print(invalid_input_message)
        return new_customer_menu()

### NON-FUNCTION CODE ###
print('Welcome to The OCEAN OPMS.\n')                                                           # display welcome message
while True:
    admin_credentials_list = file_to_list('admin_list.txt')                                     # gets the admin username and passwords from the admin_list.txt file
    customer_credentials_list = file_to_list('customer_list.txt')                               # gets the customer username and passwords from the customer_list.txt file
    medicine_list = file_to_list('medicine_list.txt')                                           # gets the medicine details from the medicine_list.txt file
    order_list = file_to_list('order_list.txt')                                                 # gets the order list from the order_list.txt file
    customer_details_list = file_to_list('customer_details_list.txt')                           # gets the customer details from the customer_details.txt file
    invalid_input_message = '\n\t***Invalid input***\n'                                         # global invalid input message
    
    print(
        '\t1. Admin login\n'
        '\t2. Customer login\n'
        '\t3. Unregsitered customer\n'
        '\t4. Exit\n'
        )
    user = input_checker(int, 'Please enter your number of choice: ', invalid_input_message)
    print()
    
    if user == 1:                                                                               # if user is admin, bring user to admin page
        output = login_page('admin')
        if output == False:
            continue
        else:
            admin_menu()
            continue

    elif user == 2:                                                                             # if user is customer, bring user to customer page
        output = login_page('customer')
        if output == False:
            continue
        else:
            customer_username = login_page.username
            customer_menu()
            continue
        
    elif user == 3:                                                                             # if user is not registered in the database, bring user to new user menu
        new_customer_menu()
        continue
    
    elif user == 4:
        exit()

    else:
        print(invalid_input_message)
        continue
