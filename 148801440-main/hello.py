def main():
    amount = 50
    valid_coins = [25, 10 , 5]
    while True:
        input_coin = int(input('Insert Coin:'))
        if input_coin not in valid_coins :
            continue
        else:
            break
    print(input_coin)

main()
def main():

    fuel_gauge()
(100//y) * x
def fuel_gauge():

    while True:
        try:
            get_fraction = input('Fraction: ')
            match get_fraction:
                case '0/1':
                    print('F')
                    break
                case '1/4':
                    print('25%')
                    break
                case '1/2':
                    print('50%')
                    break
                case '3/4':
                    print('75%')
                    break
                case '4/4':
                    print('F')
                    break

        except :
            pass


main()
get_fraction = input('Fraction: ')
            x, y = get_fraction.split('/')
            x =int(x)
            y = int(y)
            match get_fraction:
                case '1/100':
                    print('E')
                    break
                #case '99/100':
                    #print('F')
                    #break
                case '0/100':
                    print('E')
                    break
                case '100/100':
                    print('F')
                    break

            if y >= x or y==x:
                percentage =
                print(str(percentage)+'%' )
                break

        except :
            pass

