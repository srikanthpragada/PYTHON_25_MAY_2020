from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import EmployeeForm
import sqlite3
import requests
import datetime


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
    if 'fullname' in request.POST:
        # read data from request parameters
        fullname = request.POST['fullname']
        job = request.POST['job']
        salary = request.POST['salary']
        con = sqlite3.connect(r"c:\classroom\may25\hr.db")
        cur = con.cursor()
        try:
            cur.execute("insert into employees(fullname,job,salary) values(?,?,?)",
                        (fullname, job, salary))
            con.commit()
            msg = "Added Employee Successfully!"
        except Exception as ex:
            print(ex)
            msg = "Sorry! Could not add employee!"

        con.close()
        return render(request, 'add_employee.html', {'message': msg})
    else:
        return render(request, 'add_employee.html')


def add_employee2(request):
    if request.method == "GET":
        f = EmployeeForm()
        return render(request, 'add_employee2.html', {'form': f})
    else:  # POST
        # read data from request parameters
        f = EmployeeForm(request.POST)
        if f.is_valid():
            fullname = f.cleaned_data['fullname']
            job = f.cleaned_data['job']
            salary = f.cleaned_data['salary']
            con = sqlite3.connect(r"c:\classroom\may25\hr.db")
            cur = con.cursor()
            try:
                cur.execute("insert into employees(fullname,job,salary) values(?,?,?)",
                            (fullname, job, salary))
                con.commit()
                return redirect("/demo/employees")
            except Exception as ex:
                print(ex)
                msg = "Sorry! Could not add employee!"

            con.close()
            return render(request, 'add_employee2.html',
                          {'form': f, 'message': msg})
        else:
            return render(request, 'add_employee2.html', {'form': f})


def ajax_demo(request):
    return render(request, 'ajax_demo.html')

def send_datetime(request):
    return HttpResponse(str(datetime.datetime.now()))
