def anag(s1,s2):
    if(len(s1)&len(s2)==0):
        return("enter valid strings")
    elif(sorted(s1)==sorted(s2)):
        return("The given strings are anagram")
    else:
        return("The given strings are not anagram")

j=input("Enter the string: ")
k=input("Enter the string to be checked: ")
print(anag(j,k))
