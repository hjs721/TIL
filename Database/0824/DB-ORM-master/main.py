import sys
import os
import django
sys.dont_write_bytecode = True
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from db.models import *

# # 1. Artist 생성
# artist = Artists()
# artist.name = '아이브'
# import datetime
# artist.debut = datetime.date(2021, 12, 1)
# artist.save()

# artist = Artists()
# artist.name = '아이유'
# artist.debut = '2008-12-26'
# artist.save()