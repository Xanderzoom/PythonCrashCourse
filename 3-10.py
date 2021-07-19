video_games = ['Spider-man', 'Titanfall 2', 'Subnautica', 'Batman:Arkham Knight']

video_games.append('Horizon zero dawn')
print(video_games)
video_games.insert(0, 'Horizon zero dawn')
del video_games[0]
print(video_games)
popped_video_games = video_games.pop()
print(video_games)
last_owned = video_games.pop(1)
print("the last video game I played was " + last_owned.title() + ".")
video_games.remove('Horizon zero dawn')
print(video_games)
print(popped_video_games)
print("here is the original list")
print(video_games)
print("\nhere is the sorted list")
print(sorted(video_games))
print("\nHere is the original list again")
print(video_games)

video_games.reverse()
print(video_games)
len(video_games)