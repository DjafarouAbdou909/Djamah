  

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Notification

@login_required
def notification_list(request):
    notifications = Notification.objects.filter(receiver=request.user).order_by('-created_at')
    return render(request, 'notifications/list.html', {'notifications': notifications})

@login_required
def mark_as_read(request, pk):
    notification = get_object_or_404(Notification, pk=pk, receiver=request.user)
    notification.is_read = True
    notification.save()
    return redirect('notifications:list')


from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Notification

@login_required
def redirect_notification(request, pk):
    notification = get_object_or_404(Notification, pk=pk, receiver=request.user)

    notification.is_read = True
    notification.save()

    # Redirection vers home avec ancre
    return redirect(f"/#post-{notification.post.id}")



