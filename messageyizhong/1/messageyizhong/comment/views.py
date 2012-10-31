from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
import datetime

from comment.models import Comments
from comment.forms import CommentForm

def comment_add(request):

    comment=Comments.objects.all().order_by('-datetime')    



    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            name = cd['name']
            content = cd['content']
            subject = cd['subject']
            #datetime = cd['datetime']
            cmt=Comments(name=name,content=content,subject=subject,datetime=datetime.datetime.now())
            cmt.save()
            
            return HttpResponseRedirect('/comment/add/')
    else:
        form = CommentForm()
    return render_to_response('comment_add.html',
       {'form': form,'comment':comment}, context_instance=RequestContext(request))
