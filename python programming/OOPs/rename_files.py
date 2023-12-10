import os
path = 'C:/Users/THE_SHADOW/Videos/Dare.Devil S02 720p Hindi Vegamovies.NL'
files = os.listdir(path)
i = 1

for i, file in enumerate(files):
    os.rename(os.path.join(path, file), os.path.join(path, ''.join([str(i), '.mkv'])))
    # os.rename(path+file, path +'file_' + str(i)+ '.jpg')