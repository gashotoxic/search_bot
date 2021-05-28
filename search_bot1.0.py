import pywhatkit as pk


def searchMode():
    print('welcome to the search module\n what is it that you would like to search?\n')
    searches = input('enter you option here: \n')
    print(pk.search(searches))
    more = input('would you like to get more info or a new search?  ').lower()
    if more == 'yes':
        different_search = input('a) use the previous search \nb) use a new search? ')
        if different_search == 'a':
            pk.info(searches, 5)
        if different_search == 'b':
            searches2 = input('enter the search phrase:\n')
            pk.info(searches2,5)
        else:
            print('sorry I could not find any relevant value\n you need to start from the top')
            searchMode()
    if more == 'no':
        print('okey! thank you for using the search module')
    else:
        print('you either need to type yes or no for us to understand you\n'
              'keep that in mind while you continue')
        searchMode()

def playYTB():
    print('welcome to the visual and entertainment area\n all you have to do is say what you want'
          'to search on youtube and you are good to go')
    youtube_search = input('what is it that you would like to search? \n')
    pk.playonyt(youtube_search)


def handwritten():
    print('welcome o handwritten convertion system\n all yu have to do is type something'
          'and see us convert your text into handwriting ')
    text = input('enter your text here: \n')
    # location = \Users\gashoTech\Desktop\pywhatkitHandwritings/images.png
    pk.text_to_handwriting((text))


while True:
    print('welcome to GASHOTECH ARSENAL OF FUNCTIONALITIES\n WHAT WOULD YOU LIKE TO START FAST'
          '\n a) play or search something on youtube\nb) search for something or get info online'
          '\n c) convert your text to a handwriting\n d) quit')
    choice = input('enter your selection here:  ').lower()
    if choice == 'a':
        playYTB()
    elif choice == 'b':
        searchMode()
    elif choice == 'c':
        handwritten()
    elif choice == 'd':
        print('THANK YOU FOR USING GASHOTECH WE VALUE YOU ALWAYS\n BYE! BYE!')
        break
    else:
        print('you have to select a valid operation\n')