
class Users():
    sFName = ' '
    sLname = ' '
    sUsername = ' '
    sPassword = ' '
    bAccess = False

    def __init__(self):
        self.sFName = 'john'
        self.sLName = 'doe'
        self.Username = 'user'
        self.sPassword = 'Pass'
        self.bAccess = False

def UserDetails(User):
        bUserLoop = True
        bPassLoop = True
        bLoop = True
        while bLoop ==  True:
            print('\n\n------------Input Details--------------\n\n')
            sFName = input('Enter Forename... ')
            sLName = input('Enter Surname... ')
            while bUserLoop == True:
                sUsername = input('Enter Username .. ')
                if ' ' in sUsername:
                    print('Your Username cannot contain any spaces')
                elif sUsername.isalpha() == False:
                    print('Your Username cannot contain any special charcaters')
                elif len(sUsername) < 5:
                    print('Username MUST be at least 5 characters long')
                else:
                    bUserLoop = False
            while bPassLoop == True:
                sPassword = input('Enter Password... ')
                if sPassword.islower() == True:
                    print('Must contain at least 1 capital letter')
                elif sPassword.isupper() == True:
                    print('Must contain at least 1 lower case letter')
                elif sPassword.isalpha() == True:
                    print('Must contain at least 1 special character')
                elif len(sPassword) < 6:
                    print('Must be at least 6 characters long')
                else:
                    bPassLoop = False



            iCorrect = int(input('\nAre these correct? [1 for yes, 2 for no] '))

            if iCorrect == 1:
                bLoop = False
            elif iCorrect == 2:
                bLoop = True
                print('\nOK, Please try again\n')
                print('\n[Press ENTER to continue]\n')
            else: 
                print('\nEnter Valid Option\n')
                input('\n[Press ENTER to continue]\n')


        User[0].sFName = sFName
        User[0].LName = sLName
        User[0].Username = sUsername
        User[0].Password = sPassword

        return User 

#-------------------------------------------Main Code-------------------------------------------

User = list()
User.append(Users())
bUserLoop = True
bPassLoop = True
bLoginLoop = True
while bLoginLoop == True:

    print('---------------Login---------------\n\n') 
    print('Welcome')
    input('[Press Enter to continue]')

    sUsername = input('\nEnter Username... ')
    sPassword = input('\nEnter password... ')





    if sUsername == 'User' and sPassword == 'Pass':

        User = UserDetails(User)

    else:
        bValid = False

        for x in User:
            if sUsername == x.Username or x.Username.lower() and sPassword == x.Password:
                bValid = True

        if bValid == True:
            bLoginLoop = False
            print('Logging in')
        else:
            print('FAILED TO LOGIN')

#-------------------------------------------End Main Code-------------------------------------------


print('\n\n---------------Main Menu---------------\n\n')
#hhh

