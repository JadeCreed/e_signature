from django.shortcuts import render, redirect
from .models import *
from django.db.models import Sum, Count

def planting_form(request):
    if request.method == "POST":
        name = request.POST.get("name")
        brgy = request.POST.get("barangay")

        user, _ = User.objects.get_or_create(
            name=name,
            barangay=brgy,
            role='farmer'
        )

        Planting.objects.create(
            user=user,
            barangay=brgy,
            area_planted=request.POST.get("area"),
            signature=request.POST.get("signature")  # ✅ ADD
        )

        return redirect('planting')

    return render(request, "farmer/planting_form.html")


def harvesting_form(request):
    if request.method == "POST":
        name = request.POST.get("name")
        brgy = request.POST.get("barangay")

        user, _ = User.objects.get_or_create(
            name=name,
            barangay=brgy,
            role='farmer'
        )

        Harvesting.objects.create(
            user=user,
            barangay=brgy,
            area_harvested=request.POST.get("area"),
            ave_yield=request.POST.get("yield"),
            volume=request.POST.get("volume"),
            signature=request.POST.get("signature"),
        )

        return redirect('harvesting')

    return render(request, "farmer/harvesting_form.html")

def president_dashboard(request):

    harvesting = Harvesting.objects.values(
        'barangay'
    ).annotate(
        total_area=Sum('area_harvested'),
        avg_yield=Sum('ave_yield'),
        total_volume=Sum('volume')
    )

    planting = Planting.objects.select_related('user')

    return render(request, "president/dashboard.html", {
        'harvesting': harvesting,
        'planting': planting
    })