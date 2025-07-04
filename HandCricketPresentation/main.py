"""this handcricket sourse code"""
import random

def hand_cricket():
    """the function for virtual gamplay"""
    score =0
    while True: 
        try:
            enemy=random.randint(1,6)
            ui=int(input("enter the numbber"))
            if ui>=7 or ui<0:
                print("give the number only between 0 to 6")
            elif ui!=enemy:
                score+=ui
                print("enemy guess",enemy)
                print("your current Score:",score)
            elif ui==enemy:
                print("enemy guess",enemy)
                print("------------you are out")
                print("------------final score",score)
                break

        except ValueError:
            print("You give the invalid input,Try Again")
            break
if __name__=="__main__":
    hand_cricket()
