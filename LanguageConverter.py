#!/usr/bin/env python
def EnglishToJapanese():
    translate = {}
    file = open("words.txt", "r")
    for line in file:
        x = line.split(",")
        a = x[0]
        b = x[1]
        c = len(b)
        b = b[0:c]
        translate[a] = b
    return translate

def main():
    #translate = {'mother: 'okaa-san', 'brother': 'onii-chan'}
    #create the dictionary
    translate = EnglishToJapanese()

    #get the user input for the word they want to translate
    eng = input('Enter word you want to translate to japanese: ')
    eng = eng.lower()
    keylist = translate.keys()
    running = True

    #while loop to key translating a word until you dont type yes
    while running:
        flag = False
        #use a for loop to iterate through the dictionary to match the word and translate it
        for keys in keylist:
            if keys == eng:
                print(eng, ' translates to: ', translate[keys])
                flag = True


        if flag == False:
            print(eng, ' not found could not translate sorry!')
            print('\n')

        #ask if they want to enter another word if yes get the user input again
        ans = input('Do you want translate another word enter Yes anything else will terminate the program: ')
        if ans == 'yes' or ans == 'YES' or ans == 'Yes':
            eng = input('Enter word you want to translate to japanese: ')
            eng = eng.lower()
            pass
        else:
            print('Program terminating...')
            running = False



if __name__ == '__main__':
    main()
