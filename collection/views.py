from django.shortcuts import render,redirect
from collection.forms import PrivateLabelForm
from collection.models import PrivateLabel

def index(request):
  privatelabels = PrivateLabel.objects.all()
  return render(request, 'index.html', {'privatelabels': privatelabels,})

def privatelabel_detail(request, slug):
    privatelabel = PrivateLabel.objects.get(slug=slug)
    return render(request, 'privatelabels/privatelabel_detail.html', {'privatelabel': privatelabel, })

def edit_privatelabel(request, slug):
    #grab the object
    privatelabel = PrivateLabel.objects.get(slug=slug)
    #set the form we're using
    form_class = PrivateLabelForm

    #if we are comong to this view from a submitted form, grab the data from the form and apply to the form.
    if request.method == 'POST':
        form = form_class(data=request.POST, instance=privatelabel)
        if form.is_valid():
            #save the data
            form.save()
            return redirect('privatelabel_detail', slug=privatelabel.slug)
    else:
            form = form_class(instance=privatelabel)
            #and render the template
            return render(request, 'privatelabels/edit_privatelabel.html', {
            'privatelabel': privatelabel,
            'form': form,
            })
