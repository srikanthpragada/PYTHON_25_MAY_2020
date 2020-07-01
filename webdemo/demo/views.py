from django.shortcuts import render
from django.http import HttpResponse
import sqlite3
import requests


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


def list_countries(request):
    resp = requests.get("https://restcountries.eu/rest/v2/all")
    countries = resp.json()
    return render(request, 'list_countries.html', {'countries': countries})


def add_employee(request):
    if 'fullname' in request.GET:
        # read data from request parameters
        fullname = request.GET['fullname']
        job = request.GET['job']
        salary = request.GET['salary']
        con = sqlite3.connect(r"c:\classroom\may25\hr.db")
        cur = con.cursor()
        try:
           cur.execute("insert into employees(fullname,job,salary) values(?,?,?)",
                    (fullname,job,salary))
           con.commit()
           msg = "Added Employee Successfully!"
        except Exception as ex:
            print(ex)
            msg = "Sorry! Could not add employee!"

        con.close()
        return render(request,'add_employee.html', {'message' : msg})
    else:
        return render(request, 'add_employee.html')
