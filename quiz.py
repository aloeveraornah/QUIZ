from PIL import Image #this allows for images to be imported from files
cat = Image.open("cat.jpeg") #this line and below it derives the jpeg image from my files
meow = Image.open("meow.jpeg")

#the list below is a dictionary where I will use indexes corresponding to the keys and values
questions_list = { 
    "What color is this cat?": "ORANGE",
    "What color is this other cat?": "BLACK",
    "What is 99/3": "33",
    "What is 2 x (1+3)": "8",
    "What is 2^2": "4",
    "What is 8(3+2)": "40",
    "What is 6 x 4/2": "12",
    "What is (8/4) + 2(2+1)": "8",
    "What is 12-2 x 12-2": "-14",
    "What is (6 x 4)/(2 x 3)": "4",
}

#this function is for the actual quiz
def questions_game():
    counter = 0 
    cat.show() #this displays the first image of a cat
    for i in range(10): #this for loop makes sure to print out all the 10 questions
        if i == 1: #this if statement assures the second image of the cat matches the second question
            meow.show() #this displays the second image of a cat
        game = input(list(questions_list.keys())[i] + ": ").upper() #this makes sure to print the key variable in the dictionary as an index matching the step of the loop
        if game == list(questions_list.values())[i]: #this makes sure to print the value variable in the dictionary as an index matching the step of the loop
            print("Correct")
            counter+=1 #this adds one to the counter every time user guesses correctly
        else:
            print("Incorrect")
    print("Score is " + str(counter) + " out of 10") #this prints out the score
    print("Percentage is " + str((counter/10)*100) + "%") #this prints out the percentage
    play_again() #this calls the function to replay the game

def play_again():
    while True:
        replay = input("Would you like to replay the quiz? Type 'YES' to play or type 'NO' to quit: ").upper() #this assures that the input is always capitalized
        if replay == "YES":
            questions_game()
            break
        elif replay == "NO":
            print("No game for you")
            quit()
        else:
            print("Please enter a valid response")

def select(): 
    while True:
        press_play = input("Want to answer 10 questions? Type 'YES' to play or type 'NO' to quit: ").upper()
        if press_play == "YES":
            questions_game()
            break
        elif press_play == "NO":
            print("No game for you")
            quit()
        else:
            print("Please enter a valid response")
select()
