def quickSort(data):
    if len(data) <= 1:
        return data
    else:
        pivot = data[0]
        greater = [x for x in data[1:] if x >= pivot]
        smaller = [x for x in data[1:] if x < pivot]
        return quickSort(greater) + [pivot] + quickSort(smaller)

data = [43,76,12,89,33,57,98,22,68,9]

sorted_data = quickSort(data)

print("Data setelah diurutkan (descending):")
print(sorted_data)

print("\n5 nilai tertinggi:")
print(sorted_data[:5])

#1) Jadi, skor lima kandidat yang lolos dari tertinggi hingga terendah adalah [98, 89, 76, 68, 57]
#2) Kandidat yang lolos adalah kandidat 2, 4, 6, 7, dan 9