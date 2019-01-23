theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

### print the board
def print_board():
    print(theBoard['top-L'] + '|' + theBoard['top-M'] + '|' + theBoard['top-R'])
    print(theBoard['mid-L'] + '|' + theBoard['mid-M'] + '|' + theBoard['mid-R'])
    print(theBoard['low-L'] + '|' + theBoard['low-M'] + '|' + theBoard['low-R'])
    print("-------")

### --- Person 1(X) and person 2(O) alternate
# Pick an empty spot, randomly (for example) from 0-9
import random
random.seed()
Board_list = [0,1,2,3,4,5,6,7,8]
n=0
while True:
    pick=random.choice(Board_list)
    n=n+1
    if n%2==0:
        mark='O'
    else:
        mark='X'
    if pick==0:
        theBoard['top-L'] = mark
    elif pick==1:
        theBoard['top-M'] = mark
    elif pick==2:
        theBoard['top-R'] = mark
    elif pick==3:
        theBoard['mid-L'] = mark
    elif pick==4:
        theBoard['mid-M'] = mark
    elif pick==5:
        theBoard['mid-R'] = mark
    elif pick==6:
        theBoard['low-L'] = mark
    elif pick==7:
        theBoard['low-M'] = mark
    else:
        theBoard['low-R'] = mark
    Board_list.remove(pick)
    print_board()

### define winning and tie situations
    if  (theBoard['top-L']==theBoard['top-M'] and theBoard['top-L']==theBoard['top-R'] and theBoard['top-L']!=' ') or \
        (theBoard['mid-L']==theBoard['mid-M'] and theBoard['mid-L']==theBoard['mid-R'] and theBoard['mid-L']!=' ') or \
        (theBoard['low-L']==theBoard['low-M'] and theBoard['low-L']==theBoard['low-R'] and theBoard['low-L']!=' ') or \
        (theBoard['top-L']==theBoard['mid-L'] and theBoard['mid-L']==theBoard['low-L'] and theBoard['top-L']!=' ') or \
        (theBoard['top-M']==theBoard['mid-M'] and theBoard['mid-M']==theBoard['low-M'] and theBoard['top-M']!=' ') or \
        (theBoard['top-R']==theBoard['mid-R'] and theBoard['mid-R']==theBoard['low-R'] and theBoard['top-R']!=' ') or \
        (theBoard['top-L']==theBoard['mid-M'] and theBoard['mid-M']==theBoard['low-R'] and theBoard['top-L']!=' ') or \
        (theBoard['low-L']==theBoard['mid-M'] and theBoard['mid-M']==theBoard['top-R'] and theBoard['low-L']!=' '):
        if n%2==0:
            print("Person 2 won!")
            break
        else:
            print("Person 1 won!")
            break
    elif len(Board_list)==0:
        print("It's a tie.")
        break
