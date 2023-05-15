import random
import string
strPlayers=open('players.txt', 'r').read()
listPlayers=strPlayers.split('%\n')
listUsers=[]
for x in listPlayers:
    x=x.split(', ')
    listUsers.append(x)
blnValidUser=False
blnHardcore=False
intCreate=0
while not blnValidUser:
    strA=input('Please enter your username:')
    strB=input('Please enter your password:')
    for x in range(0, len(listUsers), 1):
        if listUsers[x][0]==strA and listUsers[x][1]==strB:
            blnValidUser=True
            print('Welcome back, '+strA+'.')
            break
    if not blnValidUser:
        if strB=='hardcore':
            print('')
            print('Welcome to hardcore mode.')
            print('')
            blnValidUser=True
            blnHardcore=True
        else:
            intCreate=intCreate+1
            if intCreate>2:
                strAns=input('Type "yes" if you wish to make a new account.')
                print('')
                if strAns=='yes':
                    strNew=input('Please enter your username:')
                    strNews=input('Please enter your password:')
                    strNewz=input('Please re-enter your password:')
                    print('')
                    intMatch=1
                    while intMatch==1:
                        if strNews!=strNewz:
                            print('Passwords do not match.')
                            print('')
                            strNews=input('Please enter your password:')
                            strNewz=input('Please re-enter your password:')
                        else:
                            intMatch=0
                    append2=open('players.txt', 'a').write('%\n'+str(strNew)+', '+str(strNews))
                    print('Your account has been created.')
                    print('')
                    print('Welcome, '+strNew+'.')
                    blnValidUser=True
            else:
                print("Incorrect username or password entered. Please try again.")
                print('')
strSongs=open('song for nea.txt', 'r+').read()
listSongs=strSongs.split('!\n')
listArray=[]
for x in listSongs:
    x=x.split(', ')
    listArray.append(x)
print('')
print("Welcome to 'What's The Song', the original song guessing game!")
if not blnHardcore:
    print("There are 5 rounds.")
print("You will be told the initials of a random song, and the name of the artist.")
print("You will be given 2 chances to guess what each inilitalism represents.")
print("If you get it correct the 1st time, you will gain 3 points.")
print("If you get it correct the 2nd time, you will gain 1 point.")
print("If you get it wrong on your 2nd try, the game will end.")
if blnHardcore:
    print('The game will continue until you make a mistake, or correctly answer every song in our database.')
print("Incorrectly spelt answers will not be accepted.")
print("That includes incorrect capitalisation, and punctuation.")
print("Good luck, "+strA+'.')
print('')
intScore=0
listBanned=[0, 1]
if not blnHardcore: 
    intLives=5
else:
    intLives=len(listArray)
    intAnswered=0
while intLives>0:
    blnBan=False
    intN=random.randint(0,len(listArray) - 1)
    while not blnBan:
        blnOut=False
        for x in listBanned:
            if x==intN:
                intN=random.randint(0,len(listArray))
                blnOut=False
            else:
                blnOut=True
        if blnOut:
            blnBan=True
    listBanned.append(intN)
    strAns=input(listArray[intN][0]+" by "+listArray[intN][1]+': ')
    if len(listArray)+2==len(listBanned):
        break
    else:
        if strAns==listArray[intN][2]:
            print('Correct!')
            intScore=intScore+3
            if blnHardcore:
                intAnswered=intAnswered+1
        else:
            print("That's incorrect.")
            strAns=input('Try again: ')
            if strAns==listArray[intN][2]:
                print('Correct!')
                intScore=intScore+1
            else:
                print('Wrong again!')
                print('The correct answer is '+listArray[intN][2]+'.')
                ('')
                break
    print('')
    intLives=intLives-1
print('')
print('You have '+str(intScore)+' points.')
if blnHardcore:
    print('You named '+str(intAnswered)+'songs.')
    if intAnswered==len(listArray):
        print("That's all the songs on the database, which means that you beat the game!")
print('Well done!')
if not blnHardcore:
    Highscore=open('highscore.txt', 'r+').read()
    listScore=Highscore.split('$\n')
    listHigh=[]
    for x in listScore:
        listHold=x.split(', ')
        listHigh.append(listHold)
    if intScore>=int(listHigh[4][1]):
        if intScore>=int(listHigh[3][1]):
            if intScore>=int(listHigh[2][1]):
                if intScore>=int(listHigh[1][1]):
                    if intScore>=int(listHigh[0][1]):
                        listHigh.insert(0,[strA, intScore])
                    else:
                        listHigh.insert(1,[strA, intScore])
                else:
                    listHigh.insert(2,[strA, intScore])
            else:
                listHigh.insert(3,[strA, intScore])
        else:
            listHigh.insert(4,[strA, intScore])
        print('Congratulations on making the leaderboard.')
    else:
        print('')
        print('You did not make the leadboard, unfortunately')
    listHigh.pop(5)
    print('')
    open('highscore.txt', 'w').write('')
    intPlace=1
    for x in listHigh:
        if intPlace==1:
            if x[1]==1:
                print('In 1st place, '+str(x[0])+ ' has 1 point.')
            else:
                print('In 1st place, '+str(x[0])+ ' has '+str(x[1])+ ' points.')
        elif intPlace==2:
            if x[1]==1:
                print('In 2nd place, '+str(x[0])+ ' has 1 point.')
            else:
                print('In 2nd place, '+str(x[0])+ ' has '+str(x[1])+ ' points.')
        elif intPlace==3:
            if x[1]==1:
                print('In 3rd place, '+str(x[0])+ ' has 1 point.')
            else:
                print('In 3rd place, '+str(x[0])+ ' has '+str(x[1])+ ' points.')
        else:
            if x[1]:
                print('In '+str(intPlace)+' place, '+str(x[0])+ ' has 1 point.')
            else:
                print('In '+str(intPlace)+'th place, '+str(x[0])+ ' has '+str(x[1])+ ' points.')
        append1=open('highscore.txt', 'a').write(str(x[0])+', '+str(x[1])+'$\n')
        intPlace=intPlace+1
        if intPlace==6:
            break
