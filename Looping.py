#looping menggunakan For
Buah = ["Apel", "nanas", "Jambu", "Melo", "Pepaya"]
for fruits in Buah:
    print(fruits)

#while Loop
count = 1
while count < 10:
    print(count)
    count += 1

#Looping Use range()
for j in range(5):
    print(j)

#Loop Use enumerate()
fruits = ["Apel", "nanas", "Jambu", "Manggis", "Semangka"]
for index, buah1 in enumerate(fruits):
    print(f"Index {index}: {buah1}")

#nested loop
for j in range(2):
    for i in range(3):
        print(j)
        print(i)

