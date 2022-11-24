# Print vharacter present at even index and odd index seperately for the given string


def printEvenOddIndex(s):
    n=len(s)
    print("Even index...")
    i=0
    while(i<n):
        if i%2==0:
            print(s[i],end=" ")                 # R m y n 
            i=i+2
    print("\nOdd index...")
    i=1
    while(i<n):
        if i%2!=0:
            print(s[i],end=" ")                 # a a a
            i=i+2


s=input("Enter the string:\n")                                             # Ramayan
ans=printEvenOddIndex(s)