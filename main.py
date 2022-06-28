import sys
from tabulate import tabulate
import os, subprocess
import time

def colorize(text, color):
    if color == "red":
        return f"\33[31mNA μs\33[0m"
    else:
        return f"\33[32m{text} μs\33[0m"

def generate_report(headers, data):

    with open("report.md", "wb") as f:
        report = generate_markdown_report(headers, data)
        f.write(report.encode("utf8"))
    
def generate_markdown_report(headers, data):
    report1 = "<h1 align=\"center\">Implementation Table</h1>\n\n|"


    for head in [headers[0]] + headers[2:]:
        report1 += f"{head}|"
    report1 += "\n|"
    for _ in [headers[0]] + headers[2:]:
        report1 += f":-:|"
    report1 += "\n|"
    for row in data:
        for elmt in [f"-{row[0]}"] + row[2:]:
            if elmt == "NO ANSWER":
                report1 += " :x: |"
            elif elmt[0] == "-":
                report1 += f"{elmt[1:]}|"
            else:
                report1 += f" :heavy_check_mark: |"
        report1 += "\n|"
    report1 = report1[:-2]


    report = "<h1 align=\"center\">Time Table</h1>\n\n|"
    for head in headers:
        report += f"{head}|"
    report += "\n|"
    for _ in headers:
        report += ":-:|"
    report += "\n|"
    for row in data:
        for elmt in row:
            if elmt != "NO ANSWER":
                report += f"{elmt}|"
            else:
                report  += "NO IMP|"
        report += "\n|"
    report = report[:-2]


    r = report1 + "\n\n" + report
    return r


def time_lang(setup, command):
    if setup != "":
        subprocess.run(setup, capture_output=True)
    t_start = time.perf_counter()
    a = os.popen(command).read()
    t_stop = time.perf_counter()
    diff = int((t_stop-t_start)*1000000)
    return (a[:-1], diff)


def measure(problem):
    s_map = {
        "Python": "",
        "JavaScript": "",
        "C++": "clang++ .\\cpp\\main.cpp -o .\\cpp\\out.exe",
        "C": "clang .\\c\\main.c -o .\\c\\out.exe",
        "Ruby": "",
        "Objective-C": "clang -x objective-c .\\oc\\main.m -o .\\oc\\out.exe",
        "Go": "go build -o .\\go\\out.exe .\\go\\main.go",
        }
    c_map = {
        "Python": f"python .\\python\\main.py {sys.argv[1]}",
        "JavaScript": f"node .\\javascript\\main {sys.argv[1]}",
        "C++": f".\\cpp\\out.exe {sys.argv[1]}",
        "C": f".\\c\\out.exe {sys.argv[1]}",
        "Ruby": f"ruby .\\ruby\\main.rb {sys.argv[1]}",
        "Objective-C": f".\\oc\\out.exe {sys.argv[1]}",
        "Go": f".\\go\\out.exe {sys.argv[1]}",
        }
    a = {
        "1": "233168",
        "2": "4613732",
        "3": "6857",
        "4": "906609",
        "5": "232792560",
        "6": "25164150",
        "7": "104743",
        "8": "23514624000",
        #"13": "5537376230",
        #"16": "1366",
        }
    headers = ["Problem", "Answer"] + list(c_map.keys())
    data = []
    if problem in a.keys():
        data.append(clc(s_map, a, problem))
    elif problem == "*" or problem.lower() == "all":
        for i in a.keys():
            data.append(clc(s_map, a, i))
    elif problem.lower() == "r" or problem.lower() == "report":
        for i in a.keys():
            data.append(clc(s_map, a, i, False))
    generate_report(headers, data)
    print("\n"*1)
    print(tabulate(data, headers, tablefmt="psql"))
    print("\n"*1)

def clc(s_map, b, prob, cl:bool = True):
    print(f"COMPILING & CALCULATING PROBLEM: {prob}")
    c_map = {
        "Python": f"python .\\python\\main.py {prob}",
        "JavaScript": f"node .\\javascript\\main {prob}",
        "C++": f".\\cpp\\out.exe {prob}",
        "C": f".\\c\\out.exe {prob}",
        "Ruby": f"ruby .\\ruby\\main.rb {prob}",
        "Objective-C": f".\\oc\\out.exe {prob}",
        "Go": f".\\go\\out.exe {prob}",
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
    for i in range(len(times)):
        if answers[i] == b[prob]:
            if float(times[i]) < m:
                si = i
                m = float(times[i])
            if cl:
                times[i] = colorize(times[i], "green")
            else:
                times[i] = f"{times[i]}  μs"
        else:
            if cl:
                times[i] = colorize(times[i], "red")
            else:
                times[i] = "NO ANSWER"
    if cl:
        times[si] = "\33[1m"+times[si]
    return [prob, b[prob]] + times

try:
    measure(sys.argv[1])
except IndexError:
    print("No problem number provided!")
    sys.exit(1)
except FileNotFoundError:
    print("Invalid file number provided!")
    sys.exit(1)


    
