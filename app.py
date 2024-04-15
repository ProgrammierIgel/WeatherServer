from flask import Flask, request, render_template, make_response
from Wetter import getweather1
import asyncio

app = Flask(__name__)

# CONFIG
DEBUG = False

@app.route("/wetter/", methods=['POST', 'GET'])
def view():
    if request.method == 'POST':
        data = request.form['data']
        arguments = request.form['arguments']
        if arguments == "add":
            add(data)
        elif arguments == 'delete':
            delete(data)
        print_debug("{} {}".format(data, arguments))

    weathers = []
    for weather in read_f():
        weathers.append([weather, asyncio.run(getweather1(weather))])
    return render_template("weather.html", weathers=weathers)


@app.route("/")
def root():
    return "<html><script>window.location.href='/wetter/'</script><html>"


def add(data):
    file = open("location.txt", 'a')
    file.write("{}\n".format(data))
    return


def read_f():
    file = open('location.txt', "r")
    lines = []
    for line in file.readlines():
        lines.append(line.replace("\n", ""))
    return lines


def delete(entry):
    lines = read_f()
    file = open("location.txt", "r+")
    if entry in lines:
        lines.remove(entry)
    else:
        print_debug("entry to delete not in database")
        return
    file.truncate()
    for line in lines:
        file.write("{}\n".format(line))
    return


@app.route("/login/", methods=['POST', 'GET'])
def admin():
    if request.method == 'POST':
        pw = request.form['password']
        print_debug(pw)
        res = make_response(render_template("to_root.html"))
        res.set_cookie("password", pw)
        return res
    else:
        return render_template("login.html")


@app.route("/root/", methods=['GET'])
def logged_in():
    if request.cookies.get("password") == open("password.txt").read():
        # start_timer(request.remote_addr())
        print_debug(request.cookies.get("password"))
    else:
        return render_template("to_login.html")

def print_debug(s):
    if DEBUG:
        print(f'*** {s} ***')

if __name__ == "__main__":
    app.run(port=3000, debug=DEBUG, host="0.0.0.0")
