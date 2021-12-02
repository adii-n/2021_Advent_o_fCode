n = 1
result = 0
result_f1 = 0
fileContents = open("day2index.txt")
stringed_txt = fileContents.read().split('\n')

forward = 0 
depth = 0 
for x in range(0, 998):
    n += 1
    if stringed_txt[n] == "forward 1":
        forward += 1
    if stringed_txt[n] == "forward 2":
        forward += 2
    if stringed_txt[n] == "forward 3":
        forward += 3
    if stringed_txt[n] == "forward 4":
        forward += 4
    if stringed_txt[n] == "forward 5":
        forward += 5
    if stringed_txt[n] == "forward 6":
        forward += 6
    if stringed_txt[n] == "forward 7":
        forward += 7
    if stringed_txt[n] == "forward 8":
        forward += 8
    if stringed_txt[n] == "forward 9":
        forward += 9
    if stringed_txt[n] == "up 1":
        depth -= 1
    if stringed_txt[n] == "up 2":
        depth -= 2 
    if stringed_txt[n] == "up 3":
        depth -= 3
    if stringed_txt[n] == "up 4":
        depth -= 4
    if stringed_txt[n] == "up 5":
        depth -= 5
    if stringed_txt[n] == "up 6":
        depth -= 6
    if stringed_txt[n] == "up 7":
        depth -= 7
    if stringed_txt[n] == "up 8":
        depth -= 8
    if stringed_txt[n] == "up 9":
        depth -= 9
    if stringed_txt[n] == "down 1":
        depth += 1
    if stringed_txt[n] == "down 2":
        depth += 2 
    if stringed_txt[n] == "down 3":
        depth += 3 
    if stringed_txt[n] == "down 4":
        depth += 4
    if stringed_txt[n] == "down 5":
        depth += 5 
    if stringed_txt[n] == "down 6":
        depth += 6 
    if stringed_txt[n] == "down 7":
        depth += 7
    if stringed_txt[n] == "down 8":
        depth += 8 
    if stringed_txt[n] == "down 9":
        depth += 9 

print(forward * depth)