#Given three values - Start Fahrenheit Value (S), End Fahrenheit value (E) and Step Size (W), you need to convert all Fahrenheit values from Start to End at the gap of W, 
#into their corresponding Celsius values and print the table.
'''
Sample Input 1:
0 
100 
20
Sample Output 1:
0   -17
20  -6
40  4
60  15
80  26
100 37
'''

def printTable(start,end,step):

  for f in range(start,end+1,step):
    
    cellcius = int((f-32)*5/9)
    print(f,end=" ")
    print(cellcius)
    
    
s = int(input())
e = int(input())
step = int(input())
#cellcius = printTable(s,e,step)
#print(cellcius)
printTable(s,e,step)
