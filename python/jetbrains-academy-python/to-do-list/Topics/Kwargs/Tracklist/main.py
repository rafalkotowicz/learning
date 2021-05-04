def tracklist(**songlist):
    for author in songlist:
        print(author)
        for album, track in songlist[author].items():
            print(f'ALBUM: {album} TRACK: {track}')
