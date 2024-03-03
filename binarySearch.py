import random
datacuy = [148, 91, 89, 59, 149, 95, 5, 149, 21, 83, 138, 33, 137, 148, 36, 56, 24, 69, 90, 132, 149, 96, 81, 12,
           14, 22, 147, 56, 51, 58, 74, 128, 67, 148, 11, 27, 24, 7, 61, 17, 70, 81, 28, 15, 144, 109, 29, 127, 57, 111]
# binary search function


def binary_search(datacuy, target):
    low = 0
    high = len(datacuy) - 1

    while low <= high:
        mid = (low+high) // 2

        if datacuy[mid] == target:
            return mid
        elif datacuy[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# data yang acak diurutkan terlebih dahulu bisa menggunakan .sort() atau
# membuat algorithm sort sendiri
# contoh jika memakai insertion sort
    # def insertSort(datacuy):
    #     for i in range(1, len(datacuy)):
    #         j = i
    #         while j > 0 and datacuy[j-1] > datacuy[j]:
    #             datacuy[j-1], datacuy[j] = datacuy[j], datacuy[j-1]
    #             j -= 1
    #     return datacuy


# contoh jika memakai .sort()
datacuy.sort()
print(datacuy)
target = int(input("target bilangan yang ingin dicari?"))
hasil = binary_search(datacuy, target)
if hasil != -1:
    print("Bilangan", target, " ditemukan pada indeks ke", hasil)
else:
    print("Bilangan ", target, " tidak ditemukan")
