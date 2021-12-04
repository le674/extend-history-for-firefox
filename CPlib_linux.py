#!/usr/bin/python3
import smtplib, ssl, re, sqlite3, datetime,subprocess,time

def way_of_file(way_to_name_of_file):# the num is made to dict if we search firefox or an other browser, 0 => firefox, 1 => others
    proc = subprocess.Popen(f"find /home -iname {way_to_name_of_file}",stdout = subprocess.PIPE, shell = True)
    test = proc.stdout.read()
    test = test.decode("utf-8")
    list = test.split("\n")
    if(len(test) == 0):
        return 0
    else:
        return list# if it return 0 then the file doesn't exist


def path_firefox_history(embranchement):#if embranchement = 0 then we link the places.sqlite else we link History.db
    if(embranchement == 0):
        list = way_of_file("places.sqlite")
    else:
        list = way_of_file("History.db")
    if(list == 0):
        return 0
    else:
        for path in list:
            pieces = path.split('/')
            try:
                if((".mozilla" in pieces) and ((pieces[len(pieces) - 1] == "places.sqlite") or (pieces[len(pieces) - 1] == "History.db"))):
                    return [path]
            except:
                pass
        return 0# if return 0 then print("firefox not found")

def path_others_history():# on retourn la liste vide si on a pas d'autres chemins
    paths = []
    list = way_of_file("History")
    if(list == 0):
        return 0
    else:
        for path in list:
            pieces = path.split('/')
            try:
                if((pieces[len(pieces) - 2] == "Default") and (pieces[len(pieces) - 1] == "History")):
                    paths.append(path)
            except:
                pass
        return paths

def time_addition(first_time,second_time):
    T0 = first_time.split(':')
    T1 = second_time.split(':')
    seconde = int(T0[2]) + int(T1[2])
    minutes = int(T0[1]) + int(T1[1])
    hours   = int(T0[0]) + int(T1[0])
    wast = seconde/60
    seconde = int(seconde % 60)
    minutes = minutes + wast
    wast = minutes/60
    minutes = int(minutes % 60)
    hours   = int(hours + wast)
    return f"{hours}:{minutes}:{seconde}"

def test_if_ext_exist():
    way = 0
    ext_name = "LightningEyes"#here write the name of our extension
    try:
        path = way_of_file("LightningEyes")
        way = 1
    except Exception as e:
        way = 0
    return way
#print(path_firefox_history(1))
