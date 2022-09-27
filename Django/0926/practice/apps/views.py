from multiprocessing import context
from django.shortcuts import render
import random

# Create your views here.


def num(request, id):

    if id % 2 == 0 and id != 0:
        res = "짝수"
    if id == 0:
        res = "0"
    else:
        res = "홀수"

    context = {"res": res, "id": id}

    return render(request, "num.html", context)


def calculator(request, num1, num2):
    if num2 == 0:
        return render(request, "zero.html")
    res_sum = num1 + num2
    res_min = num1 - num2
    res_mul = num1 * num2
    res_div = num1 // num2
    context = {
        "num1": num1,
        "num2": num2,
        "result_sum": res_sum,
        "result_min": res_min,
        "result_mul": res_mul,
        "result_div": res_div,
    }
    return render(request, "calculator.html", context)


def life(request):
    return render(request, "life.html")


def life_result(request):
    name = request.GET.get("name")
    results = ["왕", "귀족", "노비", "백정", "선비", "기생", "장군", "농민", "왜구"]
    result = random.choice(results)
    context = {"name": name, "result": result}
    return render(request, "life_result.html", context)
