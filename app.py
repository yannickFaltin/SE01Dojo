#Mastermind Code challenge for SE_01 Dojo

import random

#function to generate random 4 digit number using import random with a range 1000 to 10,000
number = random.randrange(1000, 10000)

n = int(input('You are the the codebreaker, figure out the 4-digit number code to solve the puzzle: '))

#player guesses all numbers correct and solves puzzle

if (n == number):
    print('congratulations, you have solved the puzzle on the first try!')

else:
    #ctr is the counter, which increases as user tries increase ctr
    ctr = 0
    while (n != number):
        ctr += 1
        count = 0
        n = str(n)
        number = str(number)

        #list to store correct numbers, X will be used as placeholder for unknown numbers
        correct = ['X']*4

        #loop to check all 4 digits
        for i in range(0, 4):
            if (n[i] == number[i]):

                count += 1
                correct[i] = n[i]
            else:
                continue

        #not all numbers guessed right, use count
        if (count < 4) and (count != 0):
            print("not the right numbers, but you managed to solve", count,"numbers of the code. keep trying!")
            print("the following numbers you guessed were right ")
            for c in correct:
                print(c, end=' ')
            print('\n')
            n = int(input("Please guess another number: "))

        elif (count == 0):
            print("you did not guess any numbers correctly")
            n = int(input("try again and guess another number: "))


       # second hint, check if any numbers match the random number (check for index of random number and compare to input number)
       # while n != number:
        #    right = 0
         #   index = 0
          #  for char in str(n):
           #     if char == str(number)[index]:
            #        index += 1
             #       right += 1
            #print(f'{right} were right')
            #n = int(input("That was incorrect! Enter your guess: "))
        #if n in number:
            #print("you got a number right but wrong position")


#solved puzzle
    if n == number:

        print("you have solved the puzzle!")
        print("it took you", ctr, "attempts to solve it.")

   #  First attempt at ex.2 using any() to see if input number matches random number
    #if any(n == number):
     #   print("you have gotten X digites right at the wrong place")


