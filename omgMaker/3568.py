import sys

# ###########################
import io

str_1="""int& abc*[]&, b, cd*;"""

sys.stdin = io.StringIO(str_1)
# ###########################


arr = input().replace(';', '').split(' ')

basic = arr[0]
del arr[0]

for i in range(0, len(arr)):
    arr[i] = arr[i].replace(',', '')

for item in arr:
    term = ''
    for i in range(len(item)-1, 0, -1):
        
        if item[i].isalpha():
            item = item[:i+1]
            break
        else:
            if item[i] == ']':
                term += '['
            elif item[i] == '[':
                term += ']'
            else:
                term += item[i]

    print(basic + term + ' ' + item + ';')

