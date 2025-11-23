print("!! WELCOME TO KBC !!")
print(f"What does not grow on a tree according to a popular Hindi saying? \n [a: Money, b: Flower, c: Leaves, d: Fruits] ")
ans1 = str(input("choose correct option : "))
answer = "a"
count = 0
if answer == ans1:
    count += 1
    print("Correct Answer! Your Prize Money is : 1000")
else:
    print("Wrong Answer")
    
print(f"Which city is known as the Pink City in India? \n [a: Bangalore, b: Mysore, c: Jaipur, d: Kochi]")
ans2 = str(input("choose correct option : "))
answer2 = "c"
if answer2 == ans2 :
    count += 1
    print("Correct Answer! Your Prize Money is : 3000")
else:
    print("Wrong Answer")
    
print(f"How many states are there in India? \n [a: 28, b: 29, c: 31, d: 30]")
ans3 = str(input("choose correct option : "))
answer3 = "c"
if answer3 ==ans3 :
    count += 1
    print("Correct Answer! Your Prize Money is : 6000")
else:
    print("Wrong Answer")

if count == 3:
    print("---------Congratulations! You Won The KBC---------")
else:
    print("you lose all the money")