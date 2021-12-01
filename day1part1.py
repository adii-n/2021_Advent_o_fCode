int_text = 0
result = 0
n=0

fileContents = open("day1index.txt")
stringed_txt = fileContents.read().split('\n')
stringed_txt = [int(i) for i in stringed_txt]

int_text=stringed_txt

for i in range(2, len(int_text)):
    difference = int_text[n+1] - int_text[n]
    if difference > 0:
        result +=1
        n +=1
    if difference < 0:
        n +=1
print(result)

result2 = 0 

firstint = int_text[0]
secondint = int_text[1]
thirdint = int_text[2]
sum_block_1 = firstint + secondint + thirdint


for i in range(2, len(int_text)):
    difference2 = sum_block_1 - int_text[i-3] + int_text[i]
    if difference2 > sum_block_1:
        result2 +=1
print(result2)