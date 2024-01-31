import random as rand 
FileAmount = int(input("How many files do you want to create here?: "))
Sure = input("Are you sure you want to continue?, press enter to continue, else exit the program. The files will be created at the root drive.")

for i in range(1, FileAmount+1):
    with open(f"{i}.txt", "w") as file:
        file.write(str(i))
        print(f"Wrote file {i}.")

print("Finished Program.")
input("Press enter to exit.")