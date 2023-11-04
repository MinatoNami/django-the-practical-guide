from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported!")
