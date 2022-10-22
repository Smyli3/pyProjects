print("\t\t\t\t\t\tMULTIPLICATION TABLES:\n")
endUnit = int(input("What number do you want to go until?:\n"))
for i in range(1,endUnit+1):
    print("\n")
    for n in range(1,endUnit+1):
        print(str(i) + " X " + str(n) + " = " + str(i*n), end="  ")
end = input("\n\nPRESS ENTER TO EXIT:\n")