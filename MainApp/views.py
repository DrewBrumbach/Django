from django.shortcuts import render, redirect
from .models import Topic
from .forms import TopicForm, EntryForm

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


def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)

        if form.is_valid():
            form.save()

            return redirect('MainApp:topics')

    context = {'form': form}
    return render(request, 'MainApp/new_topic.html', context)


def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('MainApp:topic', topic_id=topic_id)

    context = {'form': form, 'topic': topic}
    return render(request, 'MainApp/new_entry.html', context)