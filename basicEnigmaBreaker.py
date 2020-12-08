import string


enigma_file = open("enigma_output", 'r')
results = list(enigma_file.readlines())
enigma_file.close()
message = ""
for i in range(17):
    letter = string.ascii_uppercase
    count = [0] * 26
    for result in results:
        reading = result[i]
        readingNumber = ord(reading) - 65
        count[readingNumber] += 1
    report = list(zip(letter, count))
    for result in report:
        if result[1] == 0:
            message += result[0]
print(message)
