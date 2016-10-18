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
        messagelist = list(message)
        messagelistnew = []
        keylist = list(key)
        keylistnew = []
        for i in messagelist:
            x = associations.find(i)
            messagelistnew.append(x)
        print (messagelistnew)
        for b in keylist:
            j = associations.find(b)
            keylistnew.append(j)
        for l in range(10):
            keylistnew = keylistnew + keylistnew
        messagelistfinal = []
        mixgofor = len(messagelistnew)
        numberat = 0
        print (keylistnew)
        while numberat < mixgofor:
            i = messagelistnew[numberat]
            b = keylistnew[numberat]
            new = i+b
            messagelistfinal.append(new)
            numberat+=1
        print (messagelistfinal)
    elif modechoice == "d":
        message = input("Message: ")
        key = input("Key: ")
    
    
    
    """
            messagelist = list(message)
        goforstay = len(messagelist)
        gofor = 0
        for i in messagelist:
            while gofor <= goforstay:
                letternow = associations[gofor]
                if letternow == i:
                    i = gofor
                gofor=gofor+1
        goforkey = 0
        goforkeystay = len(key)
        listkey = list(key)
        for b in listkey:
            while goforkey <= goforkeystay:
                keyletternow = associations[goforkey]
                if keyletternow == b:
                    b = goforkey
                goforkey = goforkey + 1
        for i in messagelist:
            for b in listkey:
                i = i + b
        for j in messagelist:
            j = associations[(int(j))]
        print (messagelist)
        """
        