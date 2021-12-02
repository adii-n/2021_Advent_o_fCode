n = 0 
result = 0
fileContents = open("day1index.txt")
stringed_txt = fileContents.read().split('\n')
int_text = [int(i) for i in stringed_txt]

for i in range(1, len(int_text)):
    difference = int_text[i] - int_text[i-1]
    if difference > 0:
        result +=1
print(result)
