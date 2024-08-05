
import time


def menu():
    while 1:
        print('Press 1 : For information about Cars')
        print('Press 2 : For information about Bike')
        print('Press 3 : For information about commercial vehicle')
        print('Press 4 : For information about Bicycle')
        print('Press 5 : For Exit')
        b=input(a+': ')
        match b:
            case '1':
                print('Wall-E: Welcome To The Car Section')
                print('Press 1 : I20')
                print('Press 2 : Swift Dzire')
                print('Press 3 : Creta')
                print('Press 4 : Venue')
                print('Press 5 : Menu')
                print('Please select the car you are looking for')
                c=input('You: ')
                match c:
                    case '1':
                        print('I20 selected')
                        import car1
                        break
                    case '2':
                        print('Swift Dzire Selected')
                        import car2   
                        break
                    case '3':
                        print('Creta Selected')  
                        import car3 
                        break 
                    case '4':
                        print('Venue Selected')   
                        import car4
                        break 
                    case '5':
                        menu()
                        break
                    case _:
                        print('Invalid Choice')  
                break
            case '2':
                print('Wall-E: Welcome To The Bike Section')
                print('Press 1 : Royal Enfield')
                print('Press 2 : Bajaj Pulsar-220')
                print('Press 3 : KTM')
                print('Press 4 : TVS Apache')
                print('Press 5 : Menu')
                print('Please select the car you are looking for')
                d=input(a+': ')
                match d:
                    case '1':
                        print('Royal Enfield Selected')   
                        import bike1
                        break
                    case '2':
                        print('Bajaj Pulsae-220 Selected')  
                        import bike2 
                        break
                    case '3':
                        print('KTM Selected')
                        import bike3   
                        break 
                    case '4':
                        print('TVS Apache Selected')   
                        import bike4
                        break 
                    case '5':
                        menu()
                        break
                    case _:
                        print('Invalid Choice')
                break
            case '3':
                print('Wall-E: Welcome To The Commercial Vehicle Section')
                import intra_v50
                break
            case '4':
                print('Wall-E: Welcome To The Bicycle Section')
                print('Press 1 : Hero Ranger')
                print('Press 2 : Hero DTB')
                print('Press 3 : Hero Sprint')
                print('Press 4 : Hero E-cycles')
                print('Press 5 : Menu')
                print('Please select the Bicycle you are looking for!')
                f=input(a+': ')
                match f:
                    case '1':
                        print('Hero Ranger Selected')   
                        import cycle1
                        break
                    case '2':
                        print('Hero DTB Selected')
                        import cycle2   
                        break
                    case '3':
                        print('Hero Sprint Selected')  
                        import cycle3 
                        break 
                    case '4':
                        print('Hero E-Cycle Selected') 
                        import cycle4  
                        break 
                    case '5':
                        menu()
                        
                        break
                    case _:
                        print('Invalid Choice')
                break

            case '5':
                print('Have a Great Day! Its Great interacting with you! ')
                exit()
                break     
            case _:
                print('invaild choice')
                time.sleep(1)



print('Hi! I\'m Wall-E I\'m here to help you')
time.sleep(.5)
print('Wall-E: May I Know your Name ?')
a=input('You: ')
print('Wall-E: Hello! '+a)
time.sleep(1)
print('Wall-E: How may I help you?')
menu()
