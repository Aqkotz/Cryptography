"""
cryptography.py
Author: Andy Kotz
Credit: <list sources used, if any>

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
again = "yes"
while again == "yes":
    onoff = "on"
    while onoff == "on":
        modechoice = input("Enter e to encrypt, d to decrypt, or q to quit: ")
        if modechoice not in ["e", "d", "q"]:
            print ("Did not understand command, try again.")
        else:
            onoff = "off"
    if modechoice == "q":
        again = "no"
        print ("Goodbye!")
    elif modechoice == "e":
        message = input("Message: ")
        key = input("Key: ")
        
        #convert message into index digits
        messagelist = list(message)
        messagelistnew = []
        keylist = list(key)
        keylistnew = []
        for i in messagelist:
            x = associations.find(i)
            messagelistnew.append(x)
        
        #convert key into index digits
        for b in keylist:
            j = associations.find(b)
            keylistnew.append(j)
        for l in range(10):
            keylistnew = keylistnew + keylistnew
            
        #add key and message together
        messagelistfinal = []
        mixgofor = len(messagelistnew)
        numberat = 0

        while numberat < mixgofor:
            i = messagelistnew[numberat]
            b = keylistnew[numberat]
            new = i+b
            messagelistfinal.append(new)
            numberat+=1
        newmessage = []
        
        #translate into letters
        for x in messagelistfinal:
            if x>len(associations):
                x = x-len(associations)
            newletter = associations[x]
            newmessage.append(newletter)
        final = ""
        for i in newmessage:
            final = final + i
        print (final)
        
        
    elif modechoice == "d":
        message = list(input("Message: "))
        key = list(input("Key: "))
        
        messagenew = []
        for i in message:
            x = associations.find(i)
            messagenew.append(x)
        
        keynew = []
        for b in key:
            j = associations.find(b)
            keynew.append(j)
        for l in range(10):
            keynew = keynew + keynew
            
        messagefinal = []
        mixgofor = len(messagenew)
        numberat = 0

        while numberat < mixgofor:
            i = messagenew[numberat]
            b = keynew[numberat]
            new = i-b
            messagefinal.append(new)
            numberat+=1
            
        newmessaged = []
        for x in messagefinal:
            if x>len(associations):
                x = x-len(associations)
            newletter = associations[x]
            newmessaged.append(newletter)
        finald = ""
        for i in newmessaged:
            finald = finald + i
        print (finald)