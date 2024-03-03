
print("Ini adalah program sederhana untuk mengurutkan bilangan ascending")
print("Masukkan bilangan bulat ya bro, ketik 'stop' untuk berhenti")

data = []
while True:
    inputData = input()
    if inputData.lower() != "stop":     # .lower() biar bisa membaca huruf besar dan kecil
        # .append() memasukkan data kedalam list []
        data.append(int(inputData))
    else:
        break


# ini adalah fungsi insertion sort
def insertionSorting(data):
    for i in range(1, len(data)):
        j = i
        while j > 0 and data[j-1] > data[j]:
            data[j], data[j-1] = data[j-1], data[j]
            j -= 1
    return data


print("data sebelum diurutkan", data)
urut = insertionSorting(data)
print("data setelah diurutkan", urut)
