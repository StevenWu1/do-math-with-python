def print_menu():
    print('1. Kilograms to Pounds')
    print('2. Pounds to Kilograms')
    
def kilograms_pounds():
    kilograms = float(input('Enter weight in kilograms: '))
    pounds = kilograms * 2.2
    print('Weight in pounds: {0}'.format(pounds))

def pounds_kilograms():
    pounds = float(input('Enter weight in pounds: '))
    kilograms = pounds / 2.2
    print('weight in kilograms: {0}'.format(kilograms))

if __name__ == '__main__':
    print_menu()
    choice = input('Which conversion would you like to do?: ')
    if choice == '1':
        kilograms_pounds()
    if choice == '2':
        pounds_kilograms()
