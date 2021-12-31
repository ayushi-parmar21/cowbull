import random

def game():
    list=[0,0,0,0,0]
    list4=[0,0,0,0,0]
    list2=[0,1,2,3,4,5,6,7,8,9]
    secret1=random.sample(list2,5)
    print(secret1)

    def count():
        k=0
        count1=0
        while k<len(list):
            count1+=1
            k+=1
        return count1       
                
    print("\nYOU CAN GUESS THE THE NUMBER IN A LIST: ",list2)
    print(" "*19+"****YOU HAVE ONLY 10 TURN****\n")

    i=1
    while i<=10:
        print(" "*19+"***","This is your",i,"attem","***")
        User=int(input("ENTER A GUESS NUMBER: "))
        posi=int(input("ENTER A POSSION OF NUMBER: "))
        j=0
        while j<len(secret1):
            cow=0
            bull=0
            if User==secret1[j]:
                if posi==j:
                    if User not in list:
                        list[j]=User
                        print(list)
                        print("Bull","\U0001F917")
                        bull+=1
                        break
                    else:
                        print("its allready you choose correct number: ")
                        break
                elif posi!=j:
                    list4[j]=User
                    print(list4)
                    print("Cow","\U0001F919",list4)
                    cow+=1
                    break
            elif User<0 or User>9:
                print("\nOnly enter between 0 to 9: ")
                break
            j+=1
        i+=1
        if list==secret1:
            break
    while True:
        if list==secret1:
            print("\n","."*35+"you win congratulation: "+"."*35)
            print("\n",list)
            break
        elif list!=secret1:
            print("\n you loss soo sorry: ")
            break
game()
print("\n # DO YOU WANT TO PLAY THIS GAME AGAIN(YES OR NO): ")
USER1=input("ENTER YOUR ANSWER HERE: ")
if USER1=="yes":
    game()
else:
    print("."*35+"GAME OVER THANYOU FOR PLAYING"+"."*35)
     