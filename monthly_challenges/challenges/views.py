from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    "january": "This works!",
    "february": "Walk for at least 20 minutes each day!",
    "march": "Learn Django for at least 20 minutes each day!",
    "april": "Learn Django for at least 20 minutes each day!",
    "may": "Learn Django for at least 20 minutes each in May!",
    "june": "Learn Django for at least 20 minutes each day in June!",
    "july": "Learn Django for at least 20 minutes each day in July!",
    "august": "Learn Django for at least 20 minutes each day in August!",
    "september": "Learn Django for at least 20 minutes each day in September!",
    "october": "Learn Django for at least 20 minutes each day in October!",
    "november": "Learn Django for at least 20 minutes each day in November!",
    "december": "Learn Django for at least 20 minutes each day in December!",
}

# Create your views here.


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month!")
    redirect_month = months[month - 1]
    reverse_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(reverse_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "month": month,
            "text": challenge_text,
        })
    except:
        return HttpResponseNotFound("This month is not supported!")
