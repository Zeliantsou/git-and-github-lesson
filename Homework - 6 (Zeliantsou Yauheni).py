import os
import time
import datetime

zapolnenie_1 = "X" * 6   #"\u2B1B" * 6 🟥
zapolnenie_2 = " " * 4 + "X" * 2   #"\u2B1C" * 4 + "\u2B1B" * 2 ⬜
zapolnenie_3 = "X" * 2 + " " * 2 + "X" * 2   #"\u2B1B" * 2 + "\u2B1C" * 2 + "\u2B1B" * 2
zapolnenie_4 = "X" * 2 + " " * 4   #"\u2B1B" * 2 + "\u2B1C" * 4
empty = " "   #"\u2B1C"
full = "X"   #"\u2B1B"
tochka = empty + full * 2 + empty

def stroki_1_2 (n1, s_t, z1, z2, z3, z4):
    global str_1_2
    if s_t[n1] == "0" or s_t[n1] == "2" or s_t[n1] == "3" or s_t[n1] == "5"\
    or s_t[n1] == "6" or s_t[n1] == "7" or s_t[n1] == "8" or s_t[n1] == "9":
        str_1_2 = str_1_2 + z1
    if s_t[n1] == "1":
        str_1_2 = str_1_2 + z2
    if s_t[n1] == "4":
        str_1_2 = str_1_2 + z3        
def stroki_3_6 (n1, s_t, z1, z2, z3, z4):
    global str_3_6
    if s_t[n1] == "1" or s_t[n1] == "2" or s_t[n1] == "3" or s_t[n1] == "7":
        str_3_6 = str_3_6 + z2
    if s_t[n1] == "0" or s_t[n1] == "4" or s_t[n1] == "8" or s_t[n1] == "9":
        str_3_6 = str_3_6 + z3    
    if s_t[n1] == "5" or s_t[n1] == "6":
        str_3_6 = str_3_6 + z4 
def stroki_7_8 (n1, s_t, z1, z2, z3, z4):
    global str_7_8
    if s_t[n1] == "2" or s_t[n1] == "3" or s_t[n1] == "4" or s_t[n1] == "5"\
    or s_t[n1] == "6" or s_t[n1] == "8" or s_t[n1] == "9":
        str_7_8 = str_7_8 + z1
    if s_t[n1] == "1" or s_t[n1] == "7":
        str_7_8 = str_7_8 + z2
    if s_t[n1] == "0":
        str_7_8 = str_7_8 + z3
def stroki_9_12 (n1, s_t, z1, z2, z3, z4):
    global str_9_12
    if s_t[n1] == "1" or s_t[n1] == "3" or s_t[n1] == "4" or s_t[n1] == "5"\
    or s_t[n1] == "7" or s_t[n1] == "9":
        str_9_12 = str_9_12 + z2
    if s_t[n1] == "0" or s_t[n1] == "6" or s_t[n1] == "8":
        str_9_12 = str_9_12 + z3
    if s_t[n1] == "2":
        str_9_12 = str_9_12 + z4
def stroki_13_14 (n1, s_t, z1, z2, z3, z4):
    global str_13_14
    if s_t[n1] == "0" or s_t[n1] == "2" or s_t[n1] == "3" or s_t[n1] == "5"\
    or s_t[n1] == "6" or s_t[n1] == "8" or s_t[n1] == "9":
        str_13_14 = str_13_14 + z1
    if s_t[n1] == "1" or s_t[n1] == "4" or s_t[n1] == "7":
        str_13_14 = str_13_14 + z2
        
while True:
    time_now = datetime.datetime.now().time()
    str_time = time_now.strftime("%H%M%S")
    str_1_2 = ""
    str_3_6 = ""
    str_7_8 = ""
    str_9_12 = ""
    str_13_14 = ""
    for n in range(6):
        stroki_1_2 (n, str_time, zapolnenie_1, zapolnenie_2, zapolnenie_3, zapolnenie_4)
        stroki_3_6 (n, str_time, zapolnenie_1, zapolnenie_2, zapolnenie_3, zapolnenie_4)
        stroki_7_8 (n, str_time, zapolnenie_1, zapolnenie_2, zapolnenie_3, zapolnenie_4)
        stroki_9_12 (n, str_time, zapolnenie_1, zapolnenie_2, zapolnenie_3, zapolnenie_4)
        stroki_13_14 (n, str_time, zapolnenie_1, zapolnenie_2, zapolnenie_3, zapolnenie_4)
    for n in range(7):
        row_1 = str_1_2[:6] + empty * 2 + str_1_2[6:12] + (tochka if n==3 else empty * 4) + str_1_2[12:18]\
              + empty * 2 + str_1_2[18:24] + (tochka if n==3 else empty * 4) + str_1_2[24:30] + empty * 2\
              + str_1_2[30:36] + "\n"
        row_2 = "\r" + str_3_6[:6] + empty * 2 + str_3_6[6:12] + (tochka if n==2 or n==4 else empty * 4) + str_3_6[12:18]\
              + empty * 2 + str_3_6[18:24] + (tochka if n==2 or n== 4 else empty * 4) + str_3_6[24:30] + empty * 2\
              + str_3_6[30:36] + "\n"
        row_3 = "\r" + str_3_6[:6] + empty * 2 + str_3_6[6:12] + (tochka if n==1 or n==5 else empty * 4) + str_3_6[12:18]\
              + empty * 2 + str_3_6[18:24] + (tochka if n==1 or n==5 else empty * 4) + str_3_6[24:30] + empty * 2\
              + str_3_6[30:36] + "\n"
        row_4 =  "\r" + str_7_8[:6] + empty * 2 + str_7_8[6:12] + (tochka if n==0 or n==6 else empty * 4) + str_7_8[12:18]\
              + empty * 2 + str_7_8[18:24] + (tochka if n==0 else empty * 4) + str_7_8[24:30] + empty * 2 + str_7_8[30:36]\
              + "\n"
        row_5 = "\r" + str_9_12[:6] + empty * 2 + str_9_12[6:12] + (tochka if n==1 or n==5 else empty * 4) + str_9_12[12:18]\
              + empty * 2 + str_9_12[18:24] + (tochka if n==1 or n==5 else empty * 4) + str_9_12[24:30] + empty * 2\
              + str_9_12[30:36] + "\n"
        row_6 = "\r" + str_9_12[:6] + empty * 2 + str_9_12[6:12] + (tochka if n==2 or n== 4 else empty * 4) + str_9_12[12:18]\
              + empty * 2 + str_9_12[18:24] + (tochka if n==2 or n== 4 else empty * 4) + str_9_12[24:30] + empty * 2\
              + str_9_12[30:36] + "\n"    
        row_7 = "\r" + str_13_14[:6] + empty * 2 + str_13_14[6:12] + (tochka if n==3 else empty * 4) + str_13_14[12:18]\
              + empty * 2 + str_13_14[18:24] + (tochka if n==3 else empty * 4) + str_13_14[24:30] + empty * 2\
              + str_13_14[30:36] + "\n"
        os.system("cls")
        print(row_1 * 2, row_2 * 2, row_3 * 2, row_4 * 2, row_5 * 2, row_6 * 2, row_7 * 2)
        time.sleep(-time.time()%1/7)
    time.sleep(-time.time()%1)
input("")