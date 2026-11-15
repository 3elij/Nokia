c = {'chibuzo': '+234 703 103 8346', 'ebuka': '+234 903 248 9848', 'eob': '+234 809 414 4853',  'chiamaka': '+234 810 123 5568', 'evans': '+234 816 388 3558'}
balance = 0.00
def add_name_and_number():
    while True:
        name = input("Name: ").lower().strip()
        number = input("NUmber: ").strip()
        c[name] = number
        print("You have succesfully saved ths number")
        choice = int(input("0 to exit. 1 to continue: "))
        if choice == 0:
            break

def search():
    while True:
        name = input("Who are you searching for: ").lower().strip()
        if name in c:
            print(c[name])
        else:
            print("That person isnt saved in your phone")
        choice = int(input("0 to exit. 1 to continue: "))
        if choice ==0:
            break
def edit():
    while True:
        name =input("Input the name of the contact to be changed: ").lower().strip()
        if name in c:
            new_name = input("What will you be changing the name to: ").lower().strip()
            if new_name in c:
                print("That name has already been saved")
            else:
                c[new_name] = c[name]
                print("The name has been succesfuly changed")
        else: 
            print("That name isnt in your contacts")
        choice = int(input("0 to exit. 1 to continue: "))
        if choice ==0:
            break
def erase():
    while True:
        removed_name = input("What name are we removing").lower().strip()
        if removed_name in c:
            del c[removed_name]
            print("Removed")
        else:
            print("That name isnt in your contacts")
        choice = int(input("0 to exit. 1 to continue: "))
        if choice ==0:
            break
m ={}
def write_and_send():
    while True:
        messages = input("Write a message: ")
        recipient = input("Who is this message going to: ").lower().strip()
        print("Message sent")
        m[recipient] = messages
        choice = int(input("Input 0 to exit. Input 1 to continue: "))
        if choice == 0:
            break
def outbox():
    while True:
        if len(m) == 0:
            print("Your outbox is empty")
            choice = int(input("Input 0 to exit. Input 1 to continue: "))
            if choice == 0:
                break

        else:
            name = input("Whose message do you want to see: ").lower().strip()
            if name not in m:
                print("You have not sent such a message to anyone")
                choice = int(input("Input 0 to exit. Input 1 to continue: "))
                if choice == 0:
                    break
            else:
                print(f"Message to {name}: ")
                print(m[name])
                choice = int(input("Input 0 to exit. Input 1 to continue: "))
                if choice == 0:
                    break
def balance_changer():
    global balance
    while True:
        adder = int(input("How much money are you adding to your balance: $"))
        if adder > 0.0:
            balance+=adder
            choice = int(input("Input 0 to exit. Input 1 to continue: "))
            if choice == 0:
                break
        else:
            print("Invalid input")
            choice = int(input("Input 0 to exit. Input 1 to continue: "))
            if choice == 0:
                break
def balance_display():
    while True:
        print(f"You have ${balance} left")
        choice = int(input("Input 0 to exit. Input 1 to continue: "))
        if choice == 0:
            break
calls_made=[]
def call_maker():
    while True:
        name = input("Who do you want to call: ").lower().strip()
        if name in c:
            print(c[name])
            calls_made.append(name)
            print(f"Calling....")
            print(f"Calling....")
            print(f"Calling....")
            print(f"Calling....")
            print(f"Calling....")
            print(f"Calling....")
            print("No internet access")
            choice = int(input("Input 0 to exit. Input 1 to continue: "))
            if choice == 0:
                break
            
        else:
            print("This name isn't in your contact list")
            choice = int(input("Input 0 to exit. Input 1 to continue: "))
            if choice == 0:
                break
def call_log():
    while True:
        if len(calls_made) ==0:
            print("You hve no calls")
            break
        else:
            for item in calls_made:
                print(item)
            break
def erase_call_log():
    while True:
        calls_made.clear()
        break

def calculator():
    while True:
        first = input('First number (0 to go back): ')
        if first == '0':
            break
        operator = input('Operator (+, -, *, /): ').strip()
        second = float(input('Second number: '))
        first = float(first)

        match operator:
            case '+':
                print(f'= {first + second}')
            case '-':
                print(f'= {first - second}')
            case '*':
                print(f'= {first * second}')
            case '/':
                if second == 0:
                    print('Cannot divide by zero')
                else:
                    print(f'= {first / second}')
            case _:
                print('Unknown operator')

        



        


    


        









heading1 = '         ===NOKIA 5510==='
heading2 = '         ===PHONE BOOK==='
heading3 = '         ===MESSAGES==='
heading4 = '         ===CHAT==='
heading5 = '         ===CALL REGISTER==='
heading6 = '         ===TONES==='
heading7 = '         ===SETTINGS==='
heading8 = '         ===CALL DIVERT==='
heading9 = '         ===MUSIC==='
heading10 = '        ===GAMES==='
heading11 = '        ===CALCULATOR==='
heading12 = '        ===REMINDERS==='
heading13 = '        ===CLOCK==='
heading14 = '        ===PROFILES==='
heading15 = '        ===SERVICES==='
heading16 = '        ===SIM SERVICES==='
print(f"{heading1:^10}")
user_number = 0
while True:
    user_number = input("What is your number: ").strip()
    if len(user_number) == 11:
        print("Your number has been saved")
        break
    else:
        print("Invalid input please input the correct format")
menu = ['1. Phone book','2. Messages','3. Chat','4. Call register','5. Tones','6. Settings','7. Call divert','8. Music','9. Games','10. Calculator','11. Reminders','12. Clock','13. Profiles','14. Services','15. SIM services','0. Exit']
sub_menu1 = ['1. Search', '2. Service Nos', '3. Add name', '4. Erase', '5. Edit', '6. Copy', '7. Assign Tone', '8. Send b-card', '9. Options', '10. Speed Dials', '11. Voice tags','0. Exit']
sub_menu2 = ['1. Write messages', '2. Inbox', '3. Outbox', '4. Picture messages', '5. Templates', '6. Smileys', '7. Message settings', '8. Info service', '9. Voice mailbox number', '10. Service command editor','0. Exit']
sub_menu3 = ['1. Make calls','2. Call Log', '3. Erase Call log','4. Show call duration', '5. Show call costs','6. Airtime Balance','0. Exit']
sub_menu4 = ['1. Ringing tone','2. Incoming call alert', '3. Message alert tone', '4. Keypad tones', '5. Warning tones', '6. Vibrating alert','0. Exit']
sub_menu5 = ['1. Call settings', '2. Phone settings', '3. Security settings', '4. Restore factory settings','0. Exit']
sub_menu6 = ['1. Music player', '2. Radio', '3. Recorder', '4. Track list','0. Exit']
sub_menu7 = ['1. Snake II', '2. Space Impact', '3. Bumper', '4. Bantumi', '5. Pairs II','0. Exit']
sub_menu8 = ['1. Alarm clock', '2. Clock settings', '3. Date setting', '4. Stopwatch', '5. Countdown timer', '6. Auto update of date and time','0. Exit']

while True:
    print(*menu, sep='\n')
    menu_option = int(input("Choose a main-menu option(Press 0 to exit): "))
    match menu_option:
        case 0:
            break
        case 1:
            print(f"{heading2:^10}")
            while True:
                print(*sub_menu1, sep='\n')
                sub_menu1_option = int(input("Choose a menu option(Press 0 to exit): "))
                match sub_menu1_option:
                    case 0:
                        break 
                    case 1:
                        search()
                    case 2:
                        print("Your Network Service Number is XXX-XXX-XXX")
                        print("You will be sent back to the main menu now")
                        break
                    case 3:
                        add_name_and_number()
                    case 4:
                        erase()
                    case 5: 
                        edit()
                    case 6:
                        print("Under progress")
                        print("You will be sent back to the main menu now")
                        break
                    case 7:
                        print("Only Default available at this time")
                        print("You will be sent back to the main menu now")
                        break
                    case 8:
                        print("This function is only available with internet access")
                        break
                    case 9:
                        memory = input("Which memory do you want to use(phone or SIM)").lower().strip()
                        if memory == 'phone' or memory == 'sim':
                            print(f"You are using {memory} memory")
                            print("You have 2GB of space left")
                            print(f"You have {len(c)} names in your contcts list")
                            print("You will be sent back to the main menu now")
                            break
                        else:
                            print("Invalid input")                           
                   
                    case 10:
                        name = input("Which name do you want to add to speed dial: ").lower().strip()
                        if name in c:
                            print(f"{name} is now on speed dial")
                        else:
                            print("That name is not in your contacts")
                            print("You will be sent back to the main menu now")
                            break   
                    case 11:
                        print("This function is under construction for now")  
                        break
        case 2:
            print(f"{heading3:^10}")            
            while True:
                print(*sub_menu2, sep='\n')
                sub_menu2_option = int(input("Choose a menu option(Press 0 to exit): "))
                match sub_menu2_option:
                    case 0:
                        break
                    case 1:
                        write_and_send()
                    case 2:
                        print("No one wants to talk to you")
                        break
                    case 3:
                        outbox()
                    case 4:
                        print("Nobody wants to send you pictures")
                        break
                    case 5:
                        print("Since nobody is texting you, you dont need these")
                        break
                    case 6:
                        print(":-), :-( , ;-), :-<, :-> ")
                        break
                    case 7:
                        print("Your network message centre number is +234803000000")
                        print("Message is sent as 'Text'")
                        print("The network will keep trying to deliver for the Maximum time")
                        choice = input("Do you want a note each time a text arrives(yes/no): ").lower().strip()
                        if choice == 'yes' or choice == 'no':
                            print("Your choice has been updated")
                            break
                        else:
                            print("Invalid input")
                            break
                    case 8:
                        print("The weather today is sunny")
                        break
                    case 9:
                        print(f"Call {user_number} to access your voicemail")
                    case 10:
                        codes = input("Input *123# to add to your balance. Input *456# to check your balance").strip()
                        if codes == '*123#':                            
                            balance_changer()
                        if codes == '*456#':
                            balance_display()
        case 3:
            print(f"{heading4:^10}")
            write_and_send()
        case 4: 
            print(f"{heading5:^10}")
            while True:
                print(*sub_menu3, sep='\n')
                sub_menu3_option = int(input("Choose a menu option(Press 0 to exit): "))
                match sub_menu3_option:
                    case 0:
                        break
                    case 1:
                        call_maker()
                    case 2:
                        call_log()
                    case 3:
                        erase_call_log()                       
                    case 4:
                        print("Your calls lasted an averge of 4 minutes")
                        break
                    case 5:
                        print("Your calls cost $1 per minute")
                        break
                    case 6:
                        balance_display()
        case 5:
            print(f"{heading6:^10}")
            while True:
                print(*sub_menu4, sep='\n')
                sub_menu4_option = int(input("Choose a menu option(Press 0 to exit): "))
                match sub_menu4_option:
                    case 0:
                        break
                    case 1:
                        ring_tone = input("Which ringtone do you want: ")
                        print(f"The chosen ringtone is {ring_tone}")
                        break
                    case 2:
                        choice = input("Do you want the phone to beep, ring or be on silent: ")
                        print("Your choice has been updated")
                        break
                    case 3:
                        print("The alert for a new message is a chime")
                        break
                    case 4:
                        choice = input("Do you want keypad sounds to be on or off(yes/no): ")
                        print("Your choice has been updated")
                        break
                    case 5:
                        choice = input("Do you want error beeps to be off?:  ")
                        print("Your choice has been updated")
                        break
                    case 6: 
                        choice = input("Do you want the vibrate to be on or off: ")
                        print("Your choice has been updated")
                        break
                    case 7:
                        print("This feature is under construction")
                        break
        case 6:
            print(f"{heading7:^10}")
            while True:
                print(*sub_menu5, sep='\n')
                sub_menu5_option = int(input("Choose a menu option(Press 0 to exit): "))
                match sub_menu5_option:
                    case 0:
                        break
                    case 1:
                        choice1 = input("Do you want automatic redial to be on or off: ").strip().lower()
                        if choice1 =='on' or choice1 == 'off':
                            print("Your choice has been updated")                            
                        else:
                            print("Invalid input")
                        choice2 = input("Do you want speed dialling to be on or off: ").lower().strip()
                        if choice2 =='on' or choice2 == 'off':
                            print("Your choice has been updated")
                            
                        else:
                            print("Invalid input")
                            
                        choice3 = input("Do you want your number to show to people you call: ").lower().strip()
                        if choice3 =='yes' or choice3 == 'no':
                            print("Your choice has been updated")
                            break
                        else:
                            print("Invalid input")
                            
                    case 2:
                        choice1 = input("What country are you in: ")
                        print(f"You are in {choice1}. Your language has been updted automatically")
                        break
                    case 3:
                        choice1 = input("Turn on PIN verification? ").lower().strip()
                        if choice1 =='yes' or choice1 == 'no':
                            print("Your choice has been updated")
                            break
                        else:
                            print("Invalid input")
                    case 4:
                        choice = input("Do you want to factory reset the phone: ").lower().strip()
                        if choice == 'yes':
                            choice1 = input("Are you sure?: ")
                            if choice1 == 'yes':
                                c.clear()
                                m.clear()
                                calls_made.clear()
                                print("All information has been cleared from the phone")
                                break
                            else:
                                print("You will be returned to the menu")
                                break
                        else:
                            print("You will be returned to the menu")
                            break
        case 7:
            print(f"{heading8:^10}")
            while True:
                print("Call divert isn't supported on this device")
                break
        case 8:
            print(f"{heading9:^10}")
            while True:
                print(*sub_menu6, sep='\n')
                sub_menu6_option = int(input("Choose a menu option(Press 0 to exit): "))
                match sub_menu6_option:
                    case 0:
                        break
                    case 1:
                        print("Music player isnt supported on this device")
                        break
                    case 2:
                        print("Radio isnt supported on this device")
                        break
                    case 3:
                        print("Recorder isn't supported on this device")
                        break
                    case 4:
                        print("This function isn't supported on this device")
                        break
        case 9:
            print(f"{heading10:^10}")
            while True:
                print(*sub_menu7, sep='\n')
                sub_menu7_option = int(input("Choose a menu option(Press 0 to exit): "))
                match sub_menu7_option:
                    case 0:
                        break
                    case 1:
                        print("Snake II needs to be donwloaded")
                        break
                    case 2:
                        print("Space Impact needs to be downloaded")
                        break
                    case 3:
                        print("Bumper needs to be downloaded")
                        break
                    case 4:
                        print("Bantumi needs to be downloaded")
                        break
                    case 5:
                        print("Pairs II needs to be downloaded")
                        break
        case 10:
            print(f"{heading11:^10}")
            
            calculator()
                
        case 11:
            print(f"{heading12:^10}")
            while True:
                print("You have no reminders")
                break
        case 12: 
             print(f"{heading13:^10}")
             while True:
                 print(*sub_menu8, sep='\n')
                 choice = int(input("Choose a menu option(Press 0 to exit): "))
                 print("Clock is still under construction")
                 break
        case 13:
            print(f"{heading14:^10}")
            while True:
                print("There is only one profile on this device")
                break
        case 14:
            print(f"{heading15:^10}")
            while True:
                print("You do not have access to the internet")
                break
        case 15:
            print(f"{heading16:^10}")
            while True:
                print("You need internet access to access this function")
                break
end = "          ===Thank you for using NOKIA 5510!==="
print(f"{end:^10}")             