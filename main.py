import os
import random
import time
import subprocess

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_terminal()

if os.name == 'nt':
    exe_path = os.path.join("windows", "thegame.exe")
    if os.path.exists(exe_path):
        subprocess.run(exe_path)
else:
    if os.uname().sysname == 'Darwin':
        exe_path = os.path.join("mac", "thegame")
    else:
        exe_path = os.path.join("linux", "thegame")
    if os.path.exists(exe_path):
        subprocess.run(exe_path)


def c():
    x = random.uniform(1, 3)
    y = 0
    while y < x:
        print("Searching..", end="\r")
        time.sleep(0.25)
        clear_terminal()
        time.sleep(0.25)
        print("Searching...", end="\r")
        clear_terminal()
        y += 0.45

c()

clear_terminal()

print("Found: ", "\n\n\n\n\n\n\n")
time.sleep(0.75)

m = [
    ['t', 'y', 'c', 'e', 'z', 't', 'e', 'q', 'z', 'k', 'a', 'i', 'h', 'd', 'b', 'b', 'i'],
    ['y', 'w', 'l', 'd', 'd', 't', 'j', 'q', 'c', 'p', 'h', 'v', 'c', 'g', 'g', 'q', 'h'],
    ['c', 'o', 'm', 'm', 'a', 'n', 'd', 's', 'v', 'o', 'i', 'c', 'e', 'm', 'a', 'i', 'l'],
    ['i', 'z', 'm', 'e', 'c', 'x', 'd', 'e', 't', 'j', 'e', 'c', 'k', 'e', 'w', 't', 'j'],
    ['n', 'b', 'r', 'v', 'b', 'a', 'z', 'a', 'i', 'g', 'c', 'c', 't', 'n', 'n', 'j', 'u'],
    ['t', 'c', 'o', 'v', 'b', 'a', 'l', 'f', 'm', 'w', 'a', 'a', 'h', 'u', 'r', 'b', 'b'],
    ['e', 'm', 'e', 'm', 'o', 'r', 'y', 'l', 'e', 'b', 'w', 'm', 'n', 'g', 'r', 'd', 'k'],
    ['r', 'b', 'v', 'u', 's', 'u', 'o', 'n', 'l', 'i', 'g', 'e', 'e', 'l', 'u', 'e', 'c'],
    ['n', 'b', 'y', 'f', 'w', 'e', 'd', 'a', 'p', 'i', 'p', 'r', 'u', 's', 'l', 'z', 's'],
    ['e', 'z', 's', 'd', 'e', 'd', 't', 'p', 'd', 'v', 's', 'a', 'c', 's', 'z', 'v', 'o'],
    ['t', 'y', 'g', 's', 'a', 'f', 'l', 't', 'd', 'c', 'g', 't', 'v', 'e', 'a', 'u', 'u'],
    ['d', 'd', 'm', 's', 'c', 'a', 'g', 'd', 'i', 'a', 'a', 's', 'a', 'a', 'z', 'p', 'n'],
    ['l', 'e', 'o', 'd', 'h', 'r', 'l', 'm', 'u', 'n', 't', 's', 'y', 'r', 'e', 'l', 'd'],
    ['d', 'r', 'l', 'l', 'n', 's', 'o', 'j', 'b', 'f', 'g', 'e', 't', 'c', 'b', 'h', 's'],
    ['h', 'q', 'q', 'e', 'o', 'l', 'a', 'l', 'a', 'r', 'm', 's', 'm', 'h', 'p', 'v', 'k'],
    ['r', 'i', 'n', 'g', 't', 'o', 'n', 'e', 'l', 'n', 'e', 't', 'w', 'o', 'r', 'k', 'y'],
    ['r', 'x', 'h', 'n', 'h', 'e', 'c', 'a', 'l', 'l', 'w', 'a', 'i', 't', 'i', 'n', 'g']
]

w = ["addnew", "scroll", "memory", "create", "broadcast", "sounds", "pictures", "games", "camera", "alarm", "search",
     "menu", "date", "calllist", "time", "ringtone", "internet", "commands", "back", "settings", "network", "delete",
     "callwaiting", "voicemail"]

def f(m, w):
    r = len(m)
    c = len(m[0])
    p = []
    z = 0

    print("WORDS FOUND:\n")

    for s in w:
        l = len(s)
        found = False

        for i in range(r):
            rs = "".join(m[i])
            if s in rs:
                si = rs.index(s)
                ei = si + l - 1
                for j in range(si, ei + 1):
                    p.append((i, j, '\033[91m'))
                found = True

        for j in range(c):
            cs = "".join(m[i][j] for i in range(r))
            if s in cs:
                si = cs.index(s)
                ei = si + l - 1
                for i in range(si, ei + 1):
                    p.append((i, j, '\033[32m'))
                found = True

        for i in range(r - l + 1):
            for j in range(c - l + 1):
                ds = "".join(m[i + k][j + k] for k in range(l))
                if s in ds:
                    si = ds.index(s)
                    ei = si + l - 1
                    for k in range(si, ei + 1):
                        p.append((i + k, j + k, '\033[94m'))
                    found = True

        for i in range(r - l + 1):
            for j in range(l - 1, c):
                ds = "".join(m[i + k][j - k] for k in range(l))
                if s in ds:
                    si = ds.index(s)
                    ei = si + l - 1
                    for k in range(si, ei + 1):
                        p.append((i + k, j - k, '\033[94m'))  
                    found = True

        for i in range(l - 1, r):
            for j in range(c - l + 1):
                ds = "".join(m[i - k][j + k] for k in range(l))
                if s in ds:
                    si = ds.index(s)
                    ei = si + l - 1
                    for k in range(si, ei + 1):
                        p.append((i - k, j + k, '\033[94m'))  
                    found = True

        if found:
            z += 1
        else:
            print(f"WORD NOT FOUND: {s}")

    for i in range(r):
        for j in range(c):
            f_flag = False
            for pi, pj, cc in p:
                if i == pi and j == pj:
                    print(cc + '\033[1m' + m[i][j] + '\033[0m ', end='')
                    f_flag = True
                    break
            if not f_flag:
                print(m[i][j], end=' ')
        print()

    return z

if executable_path and os.path.exists(executable_path):
    clear_terminal() 
    subprocess.run([executable_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
else:
    print("Executable not found.")

f_count = f(m, w)
print(f"\nNumber of words found: {f_count}")
