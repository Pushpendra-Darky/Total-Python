speak_french = True
knows_python = False

if speak_french==True and knows_python==True:
    print("You meet the requirements to apply")

elif speak_french==False and knows_python==False:
    print("To apply, you need to know how to program in Python and speak French")

elif speak_french==False and knows_python==True:
    print("To apply, you need to speak French")

else:
    print("To apply, you need to know how to program in Python")
