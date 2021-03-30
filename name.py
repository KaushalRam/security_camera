def countWords():
    fileName = input("Enter the filename: ")
    number = 0
    words = open(fileName,'r')
    for i in words:
        count = i.split()
        number = number+len(count)
        print('number of words= ')
        print(number)

countWords()