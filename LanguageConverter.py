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
    translate = EnglishToJapanese()
    keylist = translate.keys()
    eng = 'mother'
    for keys in keylist:
        if keys == eng:
            print(eng, ' translates to: ', translate[keys])
        else:
            print(eng, 'not found')




    eng = input('Enter word you want to translate to japanese: ')
    eng = eng.lower()
    running = True


    while running:
        flag = False
        for keys in keylist:
            if keys == eng:
                print(eng, ' translates to: ', translate[keys])
                flag = True


        if flag == False:
            print(eng, ' not found could not translate sorry!')

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
