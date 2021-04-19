from django.shortcuts import render
from .models import Topic

# Create your views here.


def index(request):
    ''' the home page for learning log. '''
    return render(request, 'MainApp/index.html')


#pulled data from database, but still needs to be fed to site
def topics(request):
    topics = Topic.objects.order_by('date_added')

    context = {'topics': topics}
    return render(request, 'MainApp/topics.html', context)


def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')

    context = {'topic': topic, 'entries': entries}

    return render(request, 'MainApp/topic.html', context)