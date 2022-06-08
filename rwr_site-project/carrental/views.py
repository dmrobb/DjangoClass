from django.shortcuts import render,redirect
from .forms import ReviewForm
from django.urls import reverse


# Create your views here.
def rental_review(request):
    #POST request
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ReviewForm(request.POST)
        # check whether it's valid:
        if form.is_valid():

            # Save Form to Models
            form.save()
            # redirect to a new URL:
            return redirect(reverse('carrental:thank_you'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ReviewForm()
        # context =

    return render(request,'carrental/rental_review.html',context={'form':form})

def thank_you(request):
    return render(request,'carrental/thank_you.html')
