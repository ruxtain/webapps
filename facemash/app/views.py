from django.shortcuts import render, redirect
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from app.models import Girl
from app.rating import rating

import glob
import random
import os

def home(request):
    """
    直接用文件名作为图片的 id，就暂时不搞 hash 那么复杂了。
    """
    top100 = Girl.objects.all().order_by('-rating')[:1000]
    img1, img2 = random.sample(list(top100), 2)
    return render(request, 'app/home.html', {'img1': img1, 'img2': img2})


def vote(request):
    """
    处理用户的投票；为了让用户不停投票，就不显示投票结果，我做一个页面专门查看天梯
    """
    winner = request.POST['winner']
    loser = request.POST['loser']
    winner = Girl.objects.get(pk=winner)
    loser = Girl.objects.get(pk=loser)
    winner.rating, loser.rating = rating(winner.rating, loser.rating)
    winner.save()
    loser.save()
    return redirect('/')


def ladder(request):
    girls_list = Girl.objects.all().order_by('-rating') # 按照分数降序排列
    paginator = Paginator(girls_list, 20)
    page = request.GET.get('page')
    try:
        girls = paginator.page(page)
    except PageNotAnInteger:
        girls = paginator.page(1)
    except EmptyPage: # out of page's range
        girls = paginator.page(paginator.num_pages)

    return render(request, 'app/ladder.html', {'girls': girls})























