import sys
from tabulate import tabulate
import os, subprocess
import time

def runner(arg):
    langs = ["Python", "JavaScript", "C++", "C", "Ruby", "Objective-C", "Go", "Rust"]

    solutions = {
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

    problems = list(solutions.keys())
    data_map = {i: [] for i in langs}
    if arg in ["*", "report"]:
        for lang in langs:
            setup(lang)
        for problem in problems:
            for lang in langs:
                data_map[lang].append(run(lang, problem))
        if arg == "*":
            formatter("table", data_map, solutions)
        else:
            formatter("report", data_map, solutions)
    elif arg in list(problems.keys()):
        for lang in langs:
            setup(lang)
        data_map[lang].append(run(lang, arg))
        #for i in data_map.keys():
        #    print(data_map[i])
        formatter("table", data_map, solutions)

def setup(lang):
    setup_map = {
        "Python": [],
        "JavaScript": [],
        "C++": ["clang++ .\\cpp\\main.cpp -o .\\cpp\\out.exe"],
        "C": ["clang .\\c\\main.c -o .\\c\\out.exe"],
        "Ruby": [],
        "Objective-C": ["clang -x objective-c .\\oc\\main.m -o .\\oc\\out.exe"],
        "Go": ["go build -o .\\go\\out.exe .\\go\\main.go"],
        "Rust": ["cargo build --manifest-path=.\\rust\\Cargo.toml -r", ".\\rust\\target\\release\\rust.exe 1"],
    }
    if setup_map[lang] != []:
        print(f"COMPILING {lang}")
    for command in setup_map[lang]:
        subprocess.run(command, capture_output=True)

def run(lang, prob):
    command_map = {
        "Python": f"python .\\python\\main.py {prob}",
        "JavaScript": f"node .\\javascript\\main {prob}",
        "C++": f".\\cpp\\out.exe {prob}",
        "C": f".\\c\\out.exe {prob}",
        "Ruby": f"ruby .\\ruby\\main.rb {prob}",
        "Objective-C": f".\\oc\\out.exe {prob}",
        "Go": f".\\go\\out.exe {prob}",
        "Rust": f".\\rust\\target\\release\\rust.exe {prob}"
        }
    t_start = time.perf_counter()
    a = os.popen(command_map[lang]).read()
    t_stop = time.perf_counter()
    diff = int((t_stop-t_start)*1000000)
    return [prob, diff, a[:-1]]

def sorter(x):
    l = [i[1] if i[2] != "NA" else 0 for i in x ]
    r = sum(l)/len(l)
    return r

def colorizer(text, answer, solution):
    if answer == solution:
        return f"\33[35m{text} μs\33[0m"
    elif answer == "NA":
        return f"\33[31mNA\33[0m"
    else:
        return f"\33[31mFA\33[0m"

def formatter(form, data, solutions):
    l = []
    for i in list(data.keys()):
        l.append([i, sorter(data[i])])
    l = sorted(l, key = lambda x: x[1])
    sl = {i[0]: data[i[0]] for i in l}
    headers = ["Problem", "Answer"] + [i for i in sl.keys()]
    table_data =  []
    if form == "table":
        for i in range(len(headers)):
            headers[i] = f"\33[1m{headers[i]}\33[0m"
        for i in range(len(solutions.keys())):
            table_data.append([list(solutions.keys())[i], solutions[list(solutions.keys())[i]]] + [colorizer(sl[j][i][1], sl[j][i][2], solutions[str(i+1)]) for j in sl.keys()])
        for row_num in range(len(table_data)):
            r2 = [i[5:-7] for i in table_data[row_num][2:]]
            ind  = min([int(i) for i in r2 if i != ""])
            table_data[row_num][r2.index(str(ind))+2] = "\33[32m" + table_data[row_num][r2.index(str(ind))+2][5:]
        print("\n"*2)
        print(tabulate(table_data, headers=headers, tablefmt="psql", numalign="center", stralign="center"))
        print("\n")
    elif form == "report":
        print(data)


try:
    runner(sys.argv[1])
except IndexError:
    print("No problem number provided!")
    sys.exit(1)
except FileNotFoundError:
    print("Invalid file number provided!")
    sys.exit(1)


    
