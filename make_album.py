import sys
def make_album(name_1,title_1,tracks_1 = 0):
    """
    This function will store the  imformation in 
    the dictionary with key as 'name' and it's 
    associated value as 'title'
    """
    dict_n_a = {}
    dict_n_a[name_1.title()] = title_1.title()
    dict_n_a["Tracks"] = tracks_1
    return dict_n_a
# print(make_album("radhe","Krsna",3))
# print(make_album("radhe","Krsna"))
flag = True
while flag:
    name = input("Enter name of singer (Q to quit) : ").lower()
    if(name == "q"):
        break
    title = input("Enter title of song (Q to quit) : ").lower()
    if(title == "q"):
        break
    tracks = input('Enter number of tracks (if not, left empty) (Q to quit) : ').lower()
    if(tracks == "q"):
        break
    if(tracks.isnumeric() and name.isalpha() and title.isalpha()):
        print(make_album(name_1=name,title_1=title,tracks_1=int(tracks)))
    elif(not tracks and name.isalpha() or tracks.isalpha()):
        print(make_album(name_1=name,title_1=title))
    elif(not tracks.isnumeric()):
        print("...Enter the valid numeric input for the 'track'...")
    elif(not name.isalpha()):
        print("...Enter the valid alphabet input for the 'name'...")
    elif(not title.isalpha()):
        print("...Enter the valid numeric input for the 'title'...")
    print()
        
    
