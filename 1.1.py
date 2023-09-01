#1.open the file
c1 = open('file_to_read.txt', 'r')
text = c1.read()

# 2.count the "terrible" num and print it.
count = text .count('terrible')
print("The number of occurrences of words' terrible ':", count)

# 3.Replace every even number time "terrible" for "pathetic",
#  Replace every odd number time "terrible" with "marvellous"
occurrence = 0
new_content = ''
for word in text.split():
    if word == 'terrible':
        occurrence += 1
        if occurrence % 2 == 0:
            new_content += 'pathetic '
        else:
            new_content += 'marvellous '
    else:
        new_content += word + ' '

# creat new file: result.txt
with open('result.txt', 'w') as file:
    file.write(new_content)