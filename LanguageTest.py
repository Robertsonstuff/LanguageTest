
lst = []

with open("test_russian.txt", 'r',encoding="utf8") as file:
    with open("test_english.txt", 'r',encoding="utf8") as file2:
        for line in file: 
            line = line.strip()
            lst.append(line)        
            for line2 in file2:
                line2 = line2.strip()
                lst.append(line2)
                for b, x in zip(file, file2):
                    print(f"\nWhat does this mean? {b} ")
                    input()
                    print(f"The correct answer is: {x}")
                    ele = input("\nDid you get it right? y or n: ")
                    lst.append(ele)
                print(f"Your score is {lst.count('y')} out of {lst.count('n') + lst.count('y')}\nWell Done!!")
