word=input("Enter a word\n")
#print(word)
l=len(word)
if((word[-2:]=="AM") and (word[0:2]=="12")):
    time="00"+word[2:l-2]
elif((word[-2:]=="PM") and (word[0:2]!="12")):
    time=str((int)(word[0:2])+12)+word[2:l-2]
else:
    time=word[0:l-2]


print(time)
