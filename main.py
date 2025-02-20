class Member: #creating the class know as member
    def __init__(self, m_ID): #making the constuctor method for this class
        self.m_ID=m_ID #setting up self member ID variables
class SocialNetwork(Member): #creating a subcalss that inheits Members attrivutes
    def __init__(self, m_ID): #making the constuctor method for this class
        self.m_ID=m_ID #setting up self member ID variables
    def GetFriends(self, social_NW): #creating a method for outputting friends in the network
        self.FriendsList = [] #creating a self list for the curent self members friends in the network
        for i in range(1,  len(social_NW)): #setting up the loop extract data line by line
            if str(social_NW[i])[2] == " " or str(social_NW[i])[2] == "": #selecting to define if this part of the file is blank
                pass #passing the rest of the selction
            elif int(str(social_NW[i])[2]) == int(self.m_ID): #selection defining if this file position is the same as the self Id
                self.FriendsList.append(str(social_NW[i])[0]) #adding a friend ID to a list 
            elif int(str(social_NW[i])[0]) == int(self.m_ID): #selection defining if this file position is the same as the self Id
                self.FriendsList.append(str(social_NW[i])[2]) #adding a friend ID to a list 
            else: #if none of the above then
                pass #passing the rest of the selction
            self.FriendsList.sort() #sorting the friendlist into order
        CurrentFriendList = str(self.FriendsList) #creating a string variable of the list
        CurrentFriendList = CurrentFriendList.replace("[", "") #removing and formatting the excess from the list
        CurrentFriendList = CurrentFriendList.replace("'", "") #removing and formatting the excess from the list
        CurrentFriendList = CurrentFriendList.replace("]", "") #removing and formatting the excess from the list
        print("    ", self.m_ID, "->", CurrentFriendList) #the final output for a self ID and their friends
    def FriendRecommendation(self, social_NW): #creating a method for recommending friends fo an ID
        global MemberInit
        FriendsList = [] #predefning the list for input values friends
        FoFList = [] #predefning the list for comparions friends
        for i in range(1, len(social_NW)): #setting up the loop extract data line by line
            if str(social_NW[i])[2] == " " or str(social_NW[i])[2] == "": #selecting to define if this part of the file is blank
                pass #passing the rest of the selction 
            elif int(str(social_NW[i])[2]) == int(self.m_ID): #selection defining if this file position is the same as the friend Id
                FriendsList.append(str(social_NW[i])[0]) #adding a friend ID to a list 
            elif int(str(social_NW[i])[0]) == int(self.m_ID): #selection defining if this file position is the same as the friend Id
                FriendsList.append(str(social_NW[i])[2]) #adding a friend ID to a list
            else: #if none of the above then
                pass #passing the rest of the selction
            FriendsList.sort() #sorting the list into numerical order
        for y in range(len(FriendsList)): #creating a for loop for the length of the friends list of a user
            for i in range(1, len(social_NW)): #setting up the loop extract data line by line
                if str(social_NW[i])[2] == " " or str(social_NW[i])[2] == "" or str(social_NW[i])[0] == str(int(self.m_ID)) or str(social_NW[i])[2] == str(int(self.m_ID)) or FriendsList == []: #selecting to define if this part of the file is blank, the same as the input or empty
                    pass #sorting the list into numerical order
                elif int(str(social_NW[i])[2]) == int(FriendsList[y]): #selection defining if this file position is the same as the friend Id
                    FoFList.append(str(social_NW[i])[0]) #adding a friend ID to a list 
                elif int(str(social_NW[i])[0]) == int(FriendsList[y]): #selection defining if this file position is the same as the friend Id
                    FoFList.append(str(social_NW[i])[2]) #adding a friend ID to a list 
                else: #if none of the above then
                    pass #passing the rest of the selction
        for x in range(len(FriendsList)): #creating a for loop for the length of the friends list of a user
            if FriendsList[x] in FoFList: #selection cheaking if IDs in friendslist is in the friend of friends list
                FoFList.remove(FriendsList[x]) #remove friend id from friend of friend list
            if int(len(FriendsList)) == int(len(MemberInit)-1):
                FoFList = []
        try: #try function for a potential error code
            print("    The recommended friend for", int(self.m_ID), "is", FoFList[0]) #output for friend recommendations
        except: #if errors then
            print("    The recommended friend for", int(self.m_ID), "is none") #output for failed friend recommendations
    def FriendDisplay(self, social_NW): #creatinbg a method for displaying an IDs friends
        ListFriends = [] #predefning the list for input values friends
        for i in range(1, len(social_NW)): #setting up the loop extract data line by line
            if str(social_NW[i])[2] == " " or str(social_NW[i])[2] == "": #selecting to define if this part of the file is blank
                pass #using the while loop for invalid inputs
            elif int(str(social_NW[i])[2]) == int(self.m_ID):  #selection defining if this file position is the same as the friend Id
                ListFriends.append(str(social_NW[i])[0]) #adding a friend ID to a list 
            elif int(str(social_NW[i])[0]) == int(self.m_ID):  #selection defining if this file position is the same as the friend Id
                ListFriends.append(str(social_NW[i])[2]) #adding a friend ID to a list 
            else: #if none of the above then
                pass #passing the rest of the selction
        print("    User", str(self.m_ID), "has", len(ListFriends), "friends") #output for the friend count
    def FriendOfFriend(self, social_NW): #creating a method to display friends of frineds for an ID
        FriendsList = [] #predefning the list for input values friends
        for i in range(1, len(social_NW)): #setting up the loop extract data line by line
            if str(social_NW[i])[2] == " " or str(social_NW[i])[2] == "": #selecting to define if this part of the file is blank:
                pass #passing the rest of the selction
            elif int(str(social_NW[i])[2]) == int(self.m_ID): #selection defining if this file position is the same as the friend Id
                FriendsList.append(str(social_NW[i])[0]) #adding a friend ID to a list
            elif int(str(social_NW[i])[0]) == int(self.m_ID): #selection defining if this file position is the same as the friend Id
                FriendsList.append(str(social_NW[i])[2]) #adding a friend ID to a list
            else: #if none of the above then
                    pass #passing the rest of the selction
        FriendsList.sort() #sorting the list into order
        for x in range(len(FriendsList)): #for loop for each friend of an ID
            FriendsList2 = [] #defing a list of the friend of friends friend list
            for y in range(1, len(social_NW)): #setting up the loop extract data line by line
                if str(social_NW[y])[2] == " " or str(social_NW[y])[2] == "" or str(social_NW[y])[2] == self.m_ID or str(social_NW[y])[0] == self.m_ID: #selection defnfing if the postion is blank or the user input ID
                    pass  #passing the rest of the selction
                elif int(str(social_NW[y])[2]) == int(FriendsList[x]):  #selection defining if this file position is the same as the friend Id
                    FriendsList2.append(str(social_NW[y])[0]) #adding a friend ID to a list
                elif int(str(social_NW[y])[0]) == int(FriendsList[x]):  #selection defining if this file position is the same as the friend Id
                    FriendsList2.append(str(social_NW[y])[2]) #adding a friend ID to a list
                else: #if none of the above then
                    pass #passing the rest of the selction
                FriendsList2.sort() #sorting the list into order
            if FriendsList2 == []: #se;ection defnfing if the list is empty
                FriendsList2.append("none") #adding a null value to the empty list
            else: #if none of the above then
                pass #passing the rest of the selction     
            indirect_friends = str(FriendsList2) #converting the list into a string
            indirect_friends = indirect_friends.replace("[", "") #removing exess from the string
            indirect_friends = indirect_friends.replace("'", "") #removing exess from the string
            indirect_friends = indirect_friends.replace("]", "") #removing exess from the string       
            print("    ", FriendsList[x], "->", indirect_friends) #final output for friend of friend
def CommonFriends(social_NW):
    global MemberInit
    CurrentFriendsList = []
    FriendsList = []
    common_friends = []
    for y in range(len(MemberInit)):
        common_friends = []
        for l in range(len(MemberInit)):
            CurrentFriendsList = []
            for i in range(1,  len(social_NW)): #setting up the loop extract data line by line
                FriendsList = []
                if str(social_NW[i])[2] == " " or str(social_NW[i])[2] == "": #selecting to define if this part of the file is blank
                    pass #passing the rest of the selction
                elif int(str(social_NW[i])[2]) == int(l): #selection defining if this file position is the same as the self Id
                    CurrentFriendsList.append(str(social_NW[i])[0]) #adding a friend ID to a list 
                elif int(str(social_NW[i])[0]) == int(l): #selection defining if this file position is the same as the self Id
                    CurrentFriendsList.append(str(social_NW[i])[2]) #adding a friend ID to a list 
                else: #if none of the above then
                    pass #passing the rest of the selction
                for x in range(1,  len(social_NW)): #setting up the loop extract data line by line
                    if str(social_NW[x])[2] == " " or str(social_NW[x])[2] == "": #selecting to define if this part of the file is blank
                       pass #passing the rest of the selction
                    elif int(str(social_NW[x])[2]) == int(y): #selection defining if this file position is the same as the self Id
                        FriendsList.append(str(social_NW[x])[0]) #adding a friend ID to a list 
                    elif int(str(social_NW[x])[0]) == int(y): #selection defining if this file position is the same as the self Id
                        FriendsList.append(str(social_NW[x])[2]) #adding a friend ID to a list 
                    else: #if none of the above then
                        pass #passing the rest of the selction
            common_friends.append(sum(x == y for x, y in zip(FriendsList, CurrentFriendsList)))
        print("    ",y, "->", common_friends)
def OneRelationship(social_NW):
    global MemberInit
    while True: #setting up a loop for incorrect inputs
        DisplayPrompt = input("\nDisplay the relationships of a given user (y/n)? ") #ghetting user input for friend of friends
        if DisplayPrompt == "y": #selection of the users input
            try: #trying code wiwth potential errors
                FriendNumber = int(input("Enter a user ID as an interger from 0 to " + str(len(MemberInit)-1) + ": ")) #user selection for an ID
                if int(FriendNumber) > len(MemberInit)-1:  #selection defining if user input is higher then the highest ID number
                    print("    User ID does not exist.") #output for an invlaid ID
                else:
                    MemberInit["{0}".format(FriendNumber)].GetFriends(social_NW)
                    Relationships(social_NW)
            except: #if error then
                OneRelationship(social_NW)
        elif DisplayPrompt == "n": #selection of the users input
            Relationships(social_NW)
        else: #if none of the above then
             pass #passing the rest of the selction
def Relationships(social_NW): #creating a function for friends of friends
    global MemberInit #getting the list of init IDs
    while True: #setting up a loop for incorrect inputs
        FriendDisplayPrompt = input("\nDisplay the friends of the friends of a given user (y/n)? ") #ghetting user input for friend of friends
        if FriendDisplayPrompt == "y": #selection of the users input
            try: #trying code wiwth potential errors
                FriendNumber = int(input("Enter a user ID as an interger from 0 to " + str(len(MemberInit)-1) + ": ")) #user selection for an ID
                if int(FriendNumber) > len(MemberInit)-1:  #selection defining if user input is higher then the highest ID number
                    print("    User ID does not exist.") #output for an invlaid ID
                    Relationships(social_NW) #recursion restarting the function
                    return False #ending a while loop
                else: #if none of the above then 
                    MemberInit[str(FriendNumber)].FriendOfFriend(social_NW) #calling the friend count method with self ID
                while True: #while loop for incorect inputs
                    RestartPrompt = input("\nDo you want to try another social network (y/n)? ") #user input for restarting the whole program
                    if RestartPrompt == "y": #selection of the users input
                        FileEntryPrompt() #calling apon the first function
                        return False #ending a while loop
                    elif RestartPrompt == "n": #selection of the users input
                        while True:
                            input() #ending the program
                    else: #if none of the above then
                        pass #passing the rest of the selction
            except: #if error then
                Relationships(social_NW) #recurson to restart the function
        elif FriendDisplayPrompt == "n": #selection of the users input
            while True: #setting up a loop for incorrect inputs
                RestartPrompt = input("\nDo you want to try another social network (y/n)? ") #user input for restarting the whole program
                if RestartPrompt == "y": #selection of the users input
                    FileEntryPrompt() #calling apon the first function
                    return False #ending a while loop
                elif RestartPrompt == "n": #selection of the users input
                    while True:
                        input() #ending the program
                else: #if none of the above then
                    pass #passing the rest of the selction
        else: #if none of the above then
            pass #passing the rest of the selction
def LeastDisplay(social_NW): #creating a function for displaying the least friends
    global MemberInit #getting the list of init members
    FriendNumber = {} #creating a dicinary of friendID and friendcount
    Final = [] #creating a list for the final output
    compare1 = (len(MemberInit)-2) #setting the first number to be compared by
    while True: #setting up a loop for incorrect inputs
        FriendDisplayPrompt = input("\nDisplay the user with the least number of or have 0 friends has (y/n)? ") #getting user input for least display
        if FriendDisplayPrompt == "y": #selection of the users input
            for x in range(len(MemberInit)): #setting a for loop for each ID
                counter = 0 #resting friend count for each ID
                for i in range(1, len(social_NW)): #setting up the loop extract data line by line
                    if str(social_NW[i])[2] == " " or str(social_NW[i])[2] == "": #selecting to define if this part of the file is blank
                        counter = counter + 0 #setting up the new value for friendcount 
                        FriendNumber["{0}".format(x)] = counter #putting friendcount into the dicnary 
                    elif int(str(social_NW[i])[2]) == int(x): #selection defining if this file position is the same as the friend Id
                        counter = counter + 1 #setting up the new value for friendcount 
                        FriendNumber["{0}".format(x)] = counter #putting friendcount into the dicnary 
                    elif int(str(social_NW[i])[0]) == int(x): #selection defining if this file position is the same as the friend Id
                        counter = counter + 1 #setting up the new value for friendcount 
                        FriendNumber["{0}".format(x)] = counter #putting friendcount into the dicnary 
                    else: #if none of the above then
                        pass #passing the rest of the selction
            for y in range(len(MemberInit)): #selection of the users input
                compare2 = str(y) #converting memeber ID in strings
                if int(FriendNumber[compare2]) > compare1 or int(FriendNumber[compare2]) == 0: #selection defining if the this friend count is the new lowest
                    pass #passing the rest of the selction
                else: #if none of the above then
                    compare1 = int(FriendNumber[compare2]) #updating the new lowest friend count
                    Final.append(y) #adding the ID to the final output             
            Final = list(dict.fromkeys(Final)) #removing duplications
            Final = str(Final) #converting to a string
            Final = Final.replace("[", "") #removing excess from the list
            Final = Final.replace("'", "") #removing excess from the list
            Final = Final.replace("]", "") #removing excess from the list
            print("    The user ID for the user with the least friends is:", Final) #the final output for the least friends
            if FriendNumber["{0}".format(x)] == 0: #selection defning the user with 0 friends
                print("    The user ID for the user with 0 friends is:", x) #final output for 0 friends
            else: #if none of the above then
                print("    The user ID for the user with 0 friends is: none") #final output for 0 friends          
            OneRelationship(social_NW) #calling on the next function    
            return False #ending a while loop
        elif FriendDisplayPrompt == "n": #selection of the users input
            OneRelationship(social_NW) #calling on the next function 
            return False #ending a while loop
        else: #if none of the above then
            pass #passing the rest of the selction
def DisplayFriend(social_NW): #creating a function for user friend count
    global MemberInit #getting the list of init IDs
    while True: #setting up a loop for incorrect inputs
        FriendDisplayPrompt = input("\nDisplay how many friends a user has (y/n)? ") #getting user input for friend display
        if FriendDisplayPrompt == "y": #selection of the users input
            try: #trying code with potential errors
                ListValue = int(input("Enter a user ID as an interger from 0 to " + str(len(MemberInit)-1) + ": ")) #getting a user input of the friend ID
                if int(ListValue) > len(MemberInit)-1: #selection defining if user input is higher then the highest ID number
                    print(     "User ID does not exist.") #output for if the user ID is invalid
                    DisplayFriend(social_NW) #recusion to restart the function
                    return False #ending a while loop
                else: #if none of the above then
                    MemberInit[str(ListValue)].FriendDisplay(social_NW) #calling the display friends method with self ID
                    LeastDisplay(social_NW) #calling on the next function
                    return False #ending a while loop
            except: #if errors then
                DisplayFriend(social_NW) #recurson to restart the function
        elif FriendDisplayPrompt == "n": #selection of the users input
            LeastDisplay(social_NW) #calling on the next function
            return False #ending a while loop
        else: #if none of the above then
            pass #passing the rest of the selction
def RecommendFriend(social_NW): #crating a function for friend recommendation
    global MemberInit #getting the list of init IDs
    while True: #setting up a loop for incorrect inputs
        try: #trying code with potental errors
            RecommendValue = int(input("\nEnter a user ID as an interger from 0 to " + str(len(MemberInit)-1) + ": ")) #getting userinput for the ID they want to find recommendations
            if RecommendValue > len(MemberInit)-1: #selection defining if user input is higher then the highest ID number
                print("    User ID does not exist.") #output for if the user ID is invalid
                while True: #setting up a loop for incorrect inputs
                    RetryPrompt = input("Do you want to recommend friends to another user (y/n)? ") #getting an input for is the user wants to try again
                    if RetryPrompt == "y": #selection defingning a users answer
                        RecommendFriend(social_NW)
                        return False #ending the while loop
                    elif RetryPrompt == "n": #selection defingning a users answer
                        DisplayFriend(social_NW) #calling the function for displaying a users friend count
                        return False #ending the while loop
                    else: #if none of the above then
                        pass #passing the rest of the selction
            else: #if none of the above then
                pass #passing the rest of the selction
            MemberInit[str(RecommendValue)].FriendRecommendation(social_NW) #calling the friend recommendation method with self ID
            while True: #setting up a loop for incorrect inputs
                RecommendPrompt = input("Do you want to recommend friends to another user (y/n)? ") #getting userinput to restart the process
                if RecommendPrompt == "y": #selection of the users input
                    RecommendFriend(social_NW) #using recursion to restart the process
                    return False #eneding the while loop
                elif RecommendPrompt == "n": #selection of the users inpu
                    DisplayFriend(social_NW) #calling on the next function
                    return False #eneding the while loop
                else: #if none of the above then
                    pass #passing the rest of the selction
        except: #if error then
            RecommendFriend(social_NW) #recurson to restart the function
            return False
def FileEntryPrompt(): #denfing the file entry and display function
    global MemberInit #setting global dicinary
    FileInputValue = str(input("Enter a file name for the social network data: ")) #user input for file name
    if FileInputValue == "n": #selection of users input
        print("Goodbye") #output for quicting the program
        quit() #ending the program
    else: #if none of the above then
        try: #try code with potental errors
            while True: #setting up a loop for incorrect inputs
                MemberList = [] #defning member list
                MemberInit = {} #defning the dicinary used to init IDs
                OpenFile = open(FileInputValue, "r") #reopening the network file from the paramter input
                social_NW = OpenFile.readlines() #rereading lines of the file and saving them indervidually
                for i in range(1, len(social_NW)): #setting up the loop extract data line by line
                    if social_NW[i][::-1] in social_NW:
                        pass
                    else:
                        inconsitency = 1
                    MemberList.append(str(social_NW[i])[0]) #adding all data to the list
                    try:
                        MemberList.append(str(social_NW[i])[2]) #adding all data to the list
                    except:
                        MemberList.append(" ")
                MemberList = list(dict.fromkeys(MemberList)) #removing duplicated IDs
                try:
                    MemberList.remove(' ') #removing blank data
                except:
                    pass
                MemberList.sort() #sorting list into numerical order
                try:
                    if inconsitency == 1:
                        print("This social network contains inconsistencies")
                except:
                    pass
                for x in range(len(MemberList)): #creating a for loop for each ID
                    MemberInit["{0}".format(x)] = SocialNetwork(MemberList[x]) #init each member ID in a class     
                DisplayPrompt = input("Display the social network (y/n)? ") #user input for displaying the network
                if DisplayPrompt == "y": #defining user selection
                    for x in range(len(MemberList)): #creating a for loop for each ID
                        MemberInit["{0}".format(x)].GetFriends(social_NW) #calling a method to output each users friends
                    print("")
                    CommonFriends(social_NW)
                    RecommendFriend(social_NW) #calling on the next function
                    return False #ending a while loop
                elif DisplayPrompt == "n": #defining user selection
                    RecommendFriend(social_NW) #calling on the next function
                    return False #ending a while loop
                else: #if none of the above then
                    pass #passing the rest of the selction
        except: #if errors then
            print("    The network is inconsistent, try another file.") #outpt for failed  input
            FileEntryPrompt() #recurson to restart the function
FileEntryPrompt() #starting the first function
