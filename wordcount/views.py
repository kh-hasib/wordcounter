
from django.http import HttpResponse
from django.shortcuts import render

import operator


def home(request):
    return render(request, "home.html", {})
    #return HttpResponse("h1")
def countword(request):
    fulltext = request.POST['fulltext']
    words = fulltext.split()
    worddictionary = {}
    for word in words:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1
    context = {
        'text': fulltext,
        'totalwords': len(words),
        'wordcount': sorted(worddictionary.items(), key= operator.itemgetter(1), reverse=True),
    }

    return render(request, 'count.html', context)

def about(request):
    return render(request, 'about.html')
