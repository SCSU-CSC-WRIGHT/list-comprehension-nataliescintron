#Lab1 Grade calculator

def lab_1(): 
    test_scores = []
    repeat = int(input("How many test scores would you like to input? "))
    yay = 0

    for i in range(repeat):
        grades = int(input("Enter in your test score: "))
        test_scores.append(grades)
        i +=1
        #yay+= grades
    summation =sum(test_scores)
    length = len(test_scores)
    average = summation//length #yay//length
    if average in range(90,101):
        print(f"The average is: {average}, and your letter grade is an A ")
    elif average in range(80,90):
        print(f"The average is: {average}, and your letter grade is a B ")
    elif average in range(70,80):
        print(f"The average is: {average}, and your letter grade is a C ")
    elif average in range(60,70):
        print(f"The average is: {average}, and your letter grade is a D ")
    else:
        print(f"The average is: {average}, and your letter grade is a F ")


lab_1()

def lab_2():

    #numbers = []
    odd = []
    even = []

    #amount = int(input("How many numbers would you like to input? "))
    # for i in range(amount):
    #     num = int(input("Enter a number: "))
        #numbers.append(num)  - WHAT I DID BEFORE SPLIT

    num = input("Enter some numbers: ")
    numbers = num.split()

    for number in numbers:
        number = int(number)
        if number%2 == 0:
            even.append(number)
        else:
            odd.append(number)
    oddcount = len(odd)
    evencount = len(even)
    print(f"There were {len(odd)} even numbers ")
    print(f"There were {len(even)} odd numbers")

lab_2()
      
def lab_3():

    user_input1 = input("Type in multiple numbers: ")
    list_1 = user_input1.split()
    user_input2 = input("Type in multiple numbers: ")
    list_2 = user_input2.split()
    
    
    for x in list_1:
        if x in list_2:
            list_2.remove(x)
    
    both = list_1 +list_2
    print(both)
    question = input("Would you like to repeat this process with different numbers: Y or N ")
    if question == "Y":
       lab_3()
    else:
        return
        
        
lab_3()

#return list(set(both)) sets dont have duplicates, 






        
