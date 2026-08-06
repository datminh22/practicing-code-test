"""
cac buoc:
0. cho 1 con so random
1.nhan input tu ng choi
2. xu li input so sanh
3. xu ly win game
thêm khả năng ghi nhớ tên người chơi và điểm cao nhất của họ 
xài json để làm bộ nhớ cho game
"""
import random
import time
import json
import os
def read_file():
    if not os.path.exists("trochoi.json"):
        return {}
    with open("trochoi.json", "r", encoding="utf-8") as f:
        return json.load(f)
def write_file(x):
    with open("trochoi.json", "w", encoding="utf-8") as f:
        json.dump(x, f, indent=4, ensure_ascii=False)

def ngaunhien():
    return random.randint(1, 100)
def nhap():
    while True:
        try:

            temp=int(input("NHẬP SỐ BẤT KÌ: "))
            if temp<1 or temp>100:
                print("LỖI SỐ ÂM VÀ SỐ LỚN HƠN 100")
                continue
            return temp
        except Exception as e:
            print("LỖI KHÔNG PHẢI INTEGER:", e)
        


def sosanh(x, a):
    last=time.time()
    flag=True
    for i in range(6):
        if x==a:
            print("WINNER")
            flag=False
            break
        elif x<a:
            print("NHỎ HƠN RỒI!")
            x=nhap()
        else:
            print("LỚN HƠN RỒI!")
            x=nhap()
    cur=time.time()
    print("THỜI GIAN CHƠI GAME:", cur-last)
    if flag:
        print("FAILURE")
    if flag:
        print("0 ĐIỂM BUỒN THÍ!")
        return 0
    else:
            if cur-last<10:
                print("10 ĐIỂM GIỎI THẾ!")
                return 10
            elif cur-last<20:
                print("9 ĐIỂM HAY THẾ!")
                return 9
            elif cur-last<30:
                print("8 ĐIỂM VUI THẾ!")
                return 8
            else:
                print("5 ĐIỂM HƠI NON!")
                return 5
def Champion(luu):
    temp=-99
    for ten in luu:
        if luu[ten]['diem']>temp:
            temp=luu[ten]['diem']
    champion={}
    for ten in luu:
        if luu[ten]['diem']==temp:
            champion[ten]=temp
    print("Danh sách người vô địch:")
    print(champion)
def main():
    print("TRÒ CHƠI ĐOÁN SỐ:")
    luu={}
    luu=read_file()
    while True:
        name=input("Nhập tên người chơi:")
        if name not in luu:
                luu[name]={
                    "diem": 0,
                    "so_lan": 0
                    }
                
        a=ngaunhien()
        x=nhap()
        res=sosanh(x, a)
        if res>luu[name]["diem"]:
            luu[name]["diem"]=res
        luu[name]["so_lan"]+=1

        write_file(luu)
        check=input("Bạn muốn chơi tiếp không? (YES / NO):")
        if check=='YES':
            continue
        else:
            break
    print(luu)
    Champion(luu)
main()