import json
import os
from collections import Counter

def clearScreen():
    input()
    os.system('cls')

class Login:
    def __init__(self,username,password):
        self.__username = username
        self.__password = password

    def getName(self):
        return self.__username
    
    def getLogin(self):
        with open ('data.json') as json_file:
            data=json.load(json_file)
            for i in data['user'] :
                if self.__username in i['username'] and self.__password in i['password']:
                    return True
    
    def getConfirm(self):
        with open ('data.json') as json_file:
            data=json.load(json_file)
            for i in data['user'] :
                if self.__username in i['username'] and self.__password in i['password']:
                    if (i['status'] == False):
                        return False
                    else:
                        return True
    
    def getDebit(self):
        with open ('data.json') as json_file:
            data=json.load(json_file)
            for i in data['user'] :
                if self.__username in i['username'] and self.__password in i['password']:
                    return i['debit']

class Sighup:
    def __init__(self,username,password,email):
        self.__username = username
        self.__password = password
        self.__email = email
        
        if not os.path.isfile('data.json'):
            data={}
            data['user']=[]
            data['user'].append({
                'username' : self.__username,
                'password' : self.__password,
                'email' : self.__email,
                'debit' : 0,
                'status' : False,
            })
            with open ('data.json','w') as json_file :
                json.dump(data,json_file)
        else:
            data={
                'username' : self.__username,
                'password' : self.__password,
                'email' : self.__email,
                'debit' : 0,
                'status' : False,
            }
            with open ('data.json') as json_file :
                jsonData=json.load(json_file)
                temp=jsonData['user']
                temp.append(data)
            with open ('data.json','w') as json_file:
                json.dump(jsonData,json_file)

class admin:
    def __init__(self):
        j=0
        with open ('data.json') as json_file:
            data=json.load(json_file)
            for i in data['user'] :
                if (i['status']==True):
                    j+=1
                    self.__user={
                        i['username']
                    }
                    print(str(j)+'. '+ i['username'])

    def eraserUser(self,nomor):
        a=Counter(self.__user)
        if nomor in a:
            with open ('data.json') as json_file:
                data=json.load(json_file)
                for i in data['user'] :
                    if (i['status']==True):
                        print(i['username'])
        else:
            return "Nasabah tidak ada"

def dashboardUser(user):
    print('Selamat datang ' + user.getName())
    print("---"*8)
    print('1. Lihat saldo\n2. Tambah Saldo\n3. Ganti Password\n4. Keluar')
    print('---'*8)
    pilihan=input('Masukkan pilihan : ')
    if(pilihan == '1'):
        print('Saldo anda : Rp' + str(user.getDebit()))

def dashboardAdmin():
    print('Selamat datang di dashboard admin')
    print('---'*8)
    print('1. Lihat nasabah\n2. Lihat pendaftar\n3. Keluar')
    print('---'*8)
    pilihan1=input('Masukkan pilihan : ')
    if (pilihan1=='1'):
        Admin=admin()
        print('\n1. Hapus nasabah\n2. Kembali')
        pilihan2=input('Masukkan pilihan : ')
        if (pilihan2=='1'):
            pilihan3=int(input('Masukkan nomer nasabah'))
            pilihan3-=1
            Admin.eraserUser(pilihan3)
        elif (pilihan2=='2'):
            clearScreen()
            dashboardAdmin()

def loginDashboard():
    clearScreen()
    print('Tekan 9 untuk batal')
    username = input("Username : ")
    if (username=='9'):
        return True
    password = input("Password : ")
    if (password=='9'):
        return True
    user = Login(username,password)
    if user.getLogin():
        if user.getConfirm():
            clearScreen()
            dashboardUser(user)
        else:
            print('Username belum dikonfirmasi oleh admin')
    elif (username == 'admin' and password == 'admin'):
        clearScreen()
        dashboardAdmin()
    else:
        print('Username atau password salah')

def daftarDashboard():
    clearScreen()
    print('Tekan 9 untuk batal')
    username = input("Username : ")
    if (username=='9'):
        return True
    password = input("Password : ")
    if (password=='9'):
        return True
    email = input("Email : ")
    if (email=='9'):
        return True
    user = Sighup(username,password,email)

while (True):
    print('Selamat datang di applikasi perbankan')
    print("---"*8)
    print("1. Login\n2. Daftar")
    print("---"*8)
    pilihan=input("Masukkan Pilihan : ")
    if (pilihan=='1'):
        loginDashboard()
    elif (pilihan=='2'):
        daftarDashboard()
    else:
        print("Pilihan tidak ada")
    clearScreen()