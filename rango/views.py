from django.shortcuts import render

from django.http import HttpResponse
def index(request):
    #edited in excercise 3.6<>
    #edited again in 4.1
    
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage matches to {{ boldmessage }} in the template!
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, 'rango/index.html', context=context_dict)
    
    

#below is the new method from excercise 3.6
def about(request):
    #edited in excercise 3.6<>
    #return HttpResponse("Rango says here is the about page. <a href='/rango/'>Index</a>")
    #edited in 4.4 
    
    return render(request, 'rango/about.html')