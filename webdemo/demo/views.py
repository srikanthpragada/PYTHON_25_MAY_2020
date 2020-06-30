from django.shortcuts import render
from django.http import HttpResponse
import sqlite3


def index(request):
    return HttpResponse("<h1>Demo Application </h1>")


def about(request):
    return render(request, 'about.html')


def list_employees(request):
    con = sqlite3.connect(r"c:\classroom\may25\hr.db")
    cur = con.cursor()
    cur.execute("select * from employees order by salary")
    rows = cur.fetchall()
    con.close()
    return render(request, 'list_employees.html', {'employees': rows})
