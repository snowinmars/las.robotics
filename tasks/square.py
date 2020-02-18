def main():
    number = None

    while number is None:
        answer = None

        try:
            answer = input("Enter a number: ")
            number = float(answer)
        except ValueError:
            print(f'{answer} is not a number, try again')

    print(number**2)


try:
    main()
except:
    print('Unknown exception was occured')
