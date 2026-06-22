import os 
if os.path.exists("loss1.txt"):
    print("path exist")
else:
    print("path does not exist")

    with open("loss.txt",'r') as file:
        for f in file:
            print(f.strip())