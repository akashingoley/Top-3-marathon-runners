distances = []
while True:
    intake = input("Enter the distances covered in kms : ")
    if intake == "":
        break
    while float(intake) > 42 or float(intake) < 0:
         print("Invalid distance \nValue should be between 0 and 42")
         intake = input("Please enter the distance again : ")
         if intake == "":
             break
    if intake == "":
        break
    distances.append(float(intake))
    for i in distances:
        if i == 42.00:
            distances.remove(i)

distances.sort(reverse = True)

print ("Next top 3 distances ran are ", distances[:3])
