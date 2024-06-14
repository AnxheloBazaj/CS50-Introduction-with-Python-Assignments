def main():

    capacity= fuel_gauge()
    print(capacity)
def fuel_gauge():

    while True:

        try:
            get_fraction = input('Fraction: ')
            x, y = get_fraction.split('/')
            x =int(x)
            y = int(y)
            percentage = (100//y) * x

            if y <=100 and y >= x or y==x:
                if percentage >= 99: return 'F'
                elif percentage<= 1: return 'E'
                return f'{percentage}%'


        except (ValueError, ZeroDivisionError):
            pass


main()
def main():

    fuel_gauge()

def fuel_gauge():

    while True:

        try:
            get_fraction = input('Fraction: ')
            x, y = get_fraction.split('/')
            x =int(x)
            y = int(y)
            percentage = (100//y) * x

            if y <=100 and y >= x or y==x:
                if percentage >= 99: print('F');break
                elif percentage<= 1: print('E');break
                print(f'{percentage}%')
                break

        except (ValueError, ZeroDivisionError):
            pass


main()
