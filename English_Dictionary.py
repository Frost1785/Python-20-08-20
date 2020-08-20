d = {}
name = input ("Welcome to your new dictionary.""What would you like the name to be:")
print ("Welcome to", name,"!")

while True:
    print ("1. Make a new dictionary." )
    print ("2. List of all the words and translations.")
    print ("3. Translate from English to Traditional Chinese.")
    print ("4. Translate from Traditional Chinese to English.")
    print ("5. Test.")
    print ("6. Leave", name)

    option = input ("Where would you like to go:")
    if option == '6':
        break
    elif option == '1':
        while True:
            voc = input ("Input your new English vocabulary. (Press 0 to leave and go to main page.):")
            if voc == '0':
                break
            if voc not in d:
                voc_ch = input ("Input the Traditional Chinese translation for you new vocabulary:")
                d[voc] = voc_ch
            else:
                print ("This word is already in the dictionary.")
    elif option == '2':
        s = sorted(d)
        for i in s:
            print ("English:",i,"/Mandarin:",d[i])
    elif option == '3':
        print ("You are about to go to the Translation page. Yay!")
        while True:
            got = False
            voc1 = input("Which word would you like to translate from English to　Chinese.(Press 0 to go back):")
            if voc1 == '0':
                break
            for k,v in d.items():
                if voc1 == k :
                    print ('The Traditional Chinese translation is:', d[k])
                    got = True
            if got == False:
                a = input("This word does not exist in the dictionary. Would you like to add it? Press 1 if yes and 2 if not:")
                while True:
                    if a == '1':
                        voc2 = input("Input the new word.(Press 0 to go back):")
                        if voc2 == '0':
                            break
                        else:
                            voc3 = input("Input the Traditional Chinese Translation for this new word:")
                            d[voc2] = voc3
                    else:
                        break
    elif option == '4':
        print ("You are about to go to the Translation page. Yay!")
        while True:
            got = False
            voc4 = input("Which word would you like to translate from Chinese to English.(Press 0 to go back):")
            if voc4 == '0':
                break
            for k,v in d.items():
                if voc4 == v:
                    print ('The English translation to this word is:' , k)
                    got = True

            if got == False:
                a = input("This word does not exist in the dictionary. Would you like to add it? Press 1 if yes and 2 if not:")
                while True:
                    if a == '1':
                        voc2 = input("Input the new word.(Press 0 to go back):")
                        if voc2 == '0':
                            break
                        else:
                            voc3 = input("Input the Traditional Chinese Translation for this new word:")
                            d[voc2] = voc3
                    else:
                        break
    elif option == '5':
        score = 0
        for k,v in d.items():
            print ("The question is:", v)
            ans = input("The answer is:")
            if ans == k:
                print ("Correct!","Your score is:", score + 1)
                score += 1
            else:
                print ("Wrong!!")
        print ("Your total score is:", score)
        