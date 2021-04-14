import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      "learning_log.settings")  #must be set before django

import django

django.setup()

from MainApp.models import Topic, Entry

topics = Topic.objects.all()

t = Topic.objects.get(id=1)

print(t)

entries = t.entry_set.all()

for entry in entries:
    print(entry)
"""
for t in topics:
    print(f"Topic_id: {t.id} Topic: {t}")

entries = Entry.objects.all()


for e in entries:
    print(f"Topic: {e.topic}")
    print(f"Topic: {e.topic}")
    print(f"Topic: {e.topic}")
"""