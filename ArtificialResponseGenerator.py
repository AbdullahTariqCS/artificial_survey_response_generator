from random import randint, seed
from time import sleep, process_time
numQ = 34
seed(randint(1,100))

file = open('Data.txt', 'w')
filestr = open('dataText.txt','w')

Option = [[0 for c in range(0,numQ)]for r in range(0,100)]
OptionStr = [['' for c in range(0,numQ)]for r in range(0,100)]


def normalGenerator(a, b, c, d, e,Q, pRange):
    global Option
    global OptionStr
    ch = randint(1,a+b+c+d+e-1)
    if ch > 0 and ch <= a: 
        print('Strongly Agree ', end = '')
        Option[pRange][Q] = 1
        OptionStr[pRange][Q] = 'Strongly Agree; '        
        
    elif ch > a and ch <= a+b:
        print('Agree', end = '')
        Option[pRange][Q] = 2
        OptionStr[pRange][Q] = 'Agree; '

    elif ch > a+b and ch <= a+b+c: 
        print('Netrual', end = '')
        Option[pRange][Q] = 3
        OptionStr[pRange][Q] = 'Neutral; '

    elif ch > a+b+c and ch <= a+b+c+d: 
        print('Disagree ', end = '')
        Option[pRange][Q] = 4
        OptionStr[pRange][Q] = 'Disagree; '

    elif ch > a+b+c+d and ch <= a+b+c+d+e: 
        print('Strongly Disagree ', end = '')
        Option[pRange][Q] = 5
        OptionStr[pRange][Q] = 'Strongly Disagree; '

    
def fileGenerator():
    global Option
    for r in range(0,100):
        for c in range(0,numQ):
            print(Option[r][c], end = '')
            if Option[r][c] == 0:
                file.write('  ')
            else:
                file.write(f'{Option[r][c]} ')
            filestr.write(f'{OptionStr[r][c]}')
        file.write('\n')
        filestr.write('\n')
        print()
    print(f'Compile Time: {process_time()}')
            
    

        
for Q in range (0, numQ):
    print(f'Q{Q+1})-')
    for pRange in range (0, 100):
    
        print(f'{pRange+1})-', end = '')
        

        frequency = randint(1,100)
        
        
        middle = randint(50,60)
        middleSide = randint(20,int((100-middle)/2))
        Side = int((100-middle-2*middleSide)/2)
        
        
        # print(f'Frequency: {frequency}')
        if frequency < 50:
            normalGenerator(
                            Side + randint(0,3),
                            middleSide + randint(-3,3),
                            middle,
                            middleSide + randint(-3,3),
                            Side  + randint(6,9),
                            Q, pRange)
        elif frequency >= 50 and frequency < 75:
            normalGenerator(
                            Side + randint(0,3),
                            middle,
                            middleSide + randint(-3,3),
                            middleSide + randint(-3,3),
                            Side  + randint(6,9),
                            # randint(5,10),
                            Q, pRange)
        elif frequency >= 75 and frequency < 100:
            normalGenerator( 
                            Side + randint(0,2),
                            middleSide + randint(-3,3),
                            middleSide + randint(-3,3),
                            middle,
                            Side  + randint(6,9),
                            # randint(5,10),
                            Q, pRange)
        
      
    print('\n')
    

fileGenerator()
            
        
                    
                    
    