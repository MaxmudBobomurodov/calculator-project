import csv
import os
from django.shortcuts import render
from django.http import HttpRequest


history_file = 'history.csv'


def calculator_view(request: HttpRequest):
    result = None
    if request.method == 'POST':
        try:
            num1 = float(request.POST['num1'])
            num2 = float(request.POST['num2'])
            operation = request.POST['operation']

            if operation == 'add':
                result = num1 + num2
                symbol = "+"
            elif operation == 'substract':
                result = num1 - num2
                symbol = "-"
            elif operation == 'multiply':
                result = num1 * num2
                symbol = "*"
            elif operation == 'divide':
                if num2 == 0:
                    result = "it is impossible to divide by zero"
                    symbol = "/"
                else:
                    result = num1 / num2
                    symbol = "/"
            else:
                result = "Wrong operation"
                symbol = "/"

            if isinstance(result, (int, float)):
                with open(history_file, "a") as f:
                    f.write(f"{num1} {symbol} {num2} = {result}\n")
        except Exception as e:
            result = f"error: {e}"
    print(result)
    return render(request, 'index.html', {'result': result})


def history_view(request: HttpRequest):
    history = []
    if os.path.exists(history_file):
        with open(history_file, 'r') as f:
            history = f.readlines()

    return render(request, 'history.html', {'history': history})