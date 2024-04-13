from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm


def review_list(request):
    reviews = Review.objects.all()

    context = {
        'reviews': reviews
    }

    return render(request, 'review_list.html', context)

@login_required
def create_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user  # Встановлюємо автора відгуку
            review.save()
            return redirect('reviews-list')
    else:
        form = ReviewForm()
    return render(request, 'create_review.html', {'form': form})

def home(request):
    return render(request, 'index.html')