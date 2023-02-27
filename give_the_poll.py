favorite_languages = {
                    'jen': 'python',
                    'sarah': 'c',
                    'edward': 'ruby',
                    'phil': 'python',
                    }
name = input("Enter your name : ")
if(name not in favorite_languages):
    fav_lang = input("Enter your favourite language : ")
    favorite_languages[name] = fav_lang
    print("...Thanks for giving the poll...")
else:
    print("Sorry !! Your name is already registered.")