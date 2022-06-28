import sys
from tabulate import tabulate
import os
import time

def colorize(text, color):
    if color == "red":
        return f"\33[31m{text} μs\33[0m"
    else:
        return f"\33[32m{text} μs\33[0m"

def time_lang(setup, command):
    s = os.system(setup)
    t_start = time.perf_counter()
    a = os.popen(command).read()
    t_stop = time.perf_counter()
    diff = int((t_stop-t_start)*1000000)
    return (a[:-1], diff)


def measure(problem):
    headers = ["Problem"]
    s_map = {
        "Python": "",
        "JavaScript": "",
        "C++": "clang++ .\\cpp\\main.cpp -o .\\cpp\\out.exe",
        "C": "clang .\\c\\main.c -o .\\c\\out.exe",
        "Ruby": "",
        "Objective-C": "clang -x objective-c .\\oc\\main.m -o .\\oc\\out.exe",
    }
    c_map = {
        "Python": f"python .\\python\\main.py {sys.argv[1]}",
        "JavaScript": f"node .\\javascript\\main {sys.argv[1]}",
        "C++": f".\\cpp\\out.exe {sys.argv[1]}",
        "C": f".\\c\\out.exe {sys.argv[1]}",
        "Ruby": f"ruby .\\ruby\\main.rb {sys.argv[1]}",
        "Objective-C": f".\\oc\\out.exe {sys.argv[1]}",
        }
    times = []
    langs = []
    answers = []
    for lang in c_map.keys():
        a = time_lang(s_map[lang], c_map[lang])
        times.append(str(a[1]))
        langs.append(lang)
        answers.append(a[0])
    m = 2**1000
    si = 0
    a = {
        "1": "233168",
        "2": "4613732",
        "3": "6857",
        "5": "232792560",
        "6": "25164150",
        "16": "1366"
    }
    for i in range(len(times)):
        if answers[i] == a[str(problem)]:
            if float(times[i]) < m:
                si = i
                m = float(times[i])
            times[i] = colorize(times[i], "green")
        else:
            times[i] = colorize(times[i], "red")
    times[si] = "\33[1m"+times[si]
    print("\n"*1)
    print(tabulate([[problem]+times], headers+langs, tablefmt="psql"))
    print("\n"*1)

try:
    measure(sys.argv[1])
except IndexError:
    print("No problem number provided!")
    sys.exit(1)
except FileNotFoundError:
    print("Invalid file number provided!")
    sys.exit(1)


    
