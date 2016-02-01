import sys, os
from django.core.wsgi import get_wsgi_application
os.environ['DJANGO_SETTINGS_MODULE'] = 'catear.settings'
application = get_wsgi_application()

from django.conf import settings
from django.contrib.auth import authenticate as django_auth
from notebox.models import *
import numpy as np

import csv

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('[usage] '+sys.argv[0]+' <data.csv>')
        sys.exit(1)

    # Load data
    filename = sys.argv[1]
    with open(filename, 'r') as fin:
        rows = [i for i in csv.reader(fin)]

    # Pop out the header
    print(rows.pop(0))

    # Conver to Numpy array
    nrows = np.array(rows)

    # Insert style
    styles = set(nrows[:,3])
    cur_styles = [i.name for i in Style.objects.all()]
    for s in styles:
        if s not in cur_styles:
            new_style = Style(name=s)
            new_style.save()

    # Get test user
    user = django_auth(username='test@test.com', password='testfortest')

    # Insert songs
    cur_songs = [i.title for i in Song.objects.all()]
    for s in rows:
        title = s[0]
        artist = s[1]
        composer = s[2]
        style = s[3]
        level = s[4]
        chord = s[5]
        yt_url = s[6]
        note_url = s[7]

        yt_id = yt_url.split('v=')[-1]

        style_obj = Style.objects.get(name=style)

        if title not in cur_songs:
            new_song = Song(title=title, artist=artist, note=chord, url=yt_url, song_yt_id=yt_id, 
                song_img_url='http://img.youtube.com/vi/{id}/0.jpg'.format(id=yt_id),
                level=level, desc='test', tab_url=note_url, time_length=0, song_style=style_obj, upload_user=user)
            new_song.save()





