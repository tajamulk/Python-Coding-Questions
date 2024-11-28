theboard = {
'top-L' : 'O',
'top-M' : 'X',
'top-R' : 'O',
'mid-L' : 'O',
'mid-M' : 'X',
'mid-R' : 'X',
'low-L' : 'X',
'low-M' : 'O',
'low-R' : 'O'
}

def printboard(x):
    print(x['top-L'] + '|' + x['top-M'] + '|' + x['top-R'])
    print('-----')
    print(x['mid-L'] + '|' + x['mid-M'] + '|' + x['mid-R'])
    print('-----')
    print(x['low-L'] + '|' + x['low-M'] + '|' + x['low-R'])

printboard(theboard)
