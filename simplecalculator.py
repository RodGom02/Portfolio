def add(x, y):
    return x + y

def substract(x, y):
    return x - y

def divide(x, y):
    return x / y

def multiply(x, y):
    return x * y

print("Select Operation")
print("1.Add")
print('2.Substract')
print('3.Divide')
print('4.Multiply')

while True:
    choice = input("Enter Choice 1/2/3/4: ")

    if choice in ('1','2','3','4'):
        try:
            num1= float(input('Enter first number: '))
            num2= float(input('Enter second number: '))
        except ValueError:
            print("Invalid number selected") 
            continue

    if choice == '1':
        print(num1,'+',num2,'=',add(num1,num2))

    if choice == '2':
        print(num1,'-',num2,'=',substract(num1,num2))

    if choice == '3':
        print(num1,'/',num2,'=',divide(num1,num2))

    if choice == '4':
        print(num1,'*',num2,'=',multiply(num1,num2))

    next_calculation= input('Do you want to do another calculation:(yes/no): ')
    if next_calculation== 'no':
        print('Thank You')
        break

else:
    print('Invalid Input')

    
    



