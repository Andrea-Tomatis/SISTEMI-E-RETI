import random

def readLista():
    file = open("spotify.csv","r")
    playlist = []

    for line in file:
        riga_canzone = line.split(",")
        canzone = {"id" : riga_canzone[0], "title" : riga_canzone[1], "author" : riga_canzone[2][:-1]}
        playlist.append(canzone)
    file.close()
    return playlist    



def readDict():
    file = open("spotify.csv","r")
    playlist = {}

    for line in file:
        riga_canzone = line.split(",")
        canzone = {"title" : riga_canzone[1], "author" : riga_canzone[2][:-1]}
        playlist[riga_canzone[0]] = canzone
    file.close()
    return playlist



def riproduciRandom(playlist):
    random.shuffle(playlist)
    for element in playlist:
        print(element)


def main():
    playlist = readLista()
    playlist2 = readDict()

    '''
    for i,canzone in enumerate(playlist2):
        print(f"{i}: {playlist2[canzone]}")

    for canzone in playlist:
        print(canzone)
    '''

    riproduciRandom(playlist)


if __name__ == "__main__":
    main()

