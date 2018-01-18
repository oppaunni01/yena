# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time, random, sys, ast, re, os, io, json, subprocess, threading, string, codecs, requests, ctypes, urllib, wikipedia, tempfile
from bs4 import BeautifulSoup
from urllib import urlopen
import requests
from io import StringIO
from threading import Thread
from googletrans import Translator

cl = LINETCR.LINE()
cl.login(token='EooEuoL8b5qJYLIN25l9.3UrGMEjECFh9gbFk6EFekq.kvQPsk4Cbf1Oe5a6xVTXG/sqIo8bSW3aDp+1NeL7GwM=')#uk1
cl.loginResult()

ki = LINETCR.LINE()
ki.login(token='EopoZQ49sfSOAX6hBeH7.KN6gqRyZQ0iuRiU5jNIj1W.xbYexNOBmhqAs3waOGtE/MkcIFPa3EKEr3KESNyS6Xk=')#uk2
ki.loginResult()

kk = LINETCR.LINE()
kk.login(token='EorfCRZClyvMN3MB9VOe.F6loN/ws9FaPqFRwqoggJG.FmFHkhig5zIMiHQwdNDd7Mq9K4LeuK8cXTEL4LDo38w=')#uk3
kk.loginResult()

kc = LINETCR.LINE()
kc.login(token='EoXBecqW3ERWe7LBgJg3.9qPM7NC2vWiRtQTZ/x4SyW.jAIYdZ+leAeW1/MLtZcWvqQLNkGkqmGcYnZsZmQ/NDk=')#uk4
kc.loginResult()

kg = LINETCR.LINE()
kg.login(token='EoLs7GzeWQvBTHe8PG6e.9lU+Lm8IEAdBW1wrKZGG7G.6qNWB1Ch2MBwISjX5ZFUvoIDyBGvR9vEI46dtAE2+eQ=')#uk5
kg.loginResult()

kh = LINETCR.LINE()
kh.login(token='Eod7dzA8UvmD1IxCZmPa.4873flXX7QJRw4jo2j7roG.fWe5i9/VBidflBRmvSvAy0XpfRJVwpvWKUOKIxLl+2o=')#uk6
kh.loginResult()

ka = LINETCR.LINE()
ka.login(token='EogbsaEup2vVM5mxtdB8.MQvnSQmxLZyecm+cYLEska.IjlXmLZLDqz59W1LM/TIkILZ+nnGakSVGVCiECXO9Is=')#uk7
ka.loginResult()

kb = LINETCR.LINE()
kb.login(token='EoB6OhiaRd2em6cV5Nu6.xkaL7HAdfdzB4bRIIC04jG.VummEw+rE6v+WwQzUjnfqUCMMMHQ7puipbooYzf/NE8=')#uk8
kb.loginResult()

kd = LINETCR.LINE()
kd.login(token='Eoiau00seLMIDdNJY150.X7ONBO4L4YtA49fO3i6lua.1dmRvQWkoDQ+/zWe1XyF92JaB8spDNF+zi8fLWcuC9k=')#uk9
kd.loginResult()

ke = LINETCR.LINE()
ke.login(token='EottLf29uAXUnlRbVJdb.tyEjT4SUhBFf7gJV34m+gW./n/Z5f1ID/4y/77xJGctC0D/igq8J6tI8kY4rLBz+0s=')#uk10
ke.loginResult()

mr = LINETCR.LINE()
mr.login(token='EojgEBlv4nUUyHe93di4.srjUosW4RgcA0sSjVMH6Ta.dLECyIIo8gVt7ZUViaadrwIcACEWRYSLthu8gBoWl6o=')#mr
mr.loginResult()

print "uk mora-yena login success"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""=࿅ོ࿆༼U.K-mora_yena bot selfbot༽࿅ོ࿆=

️=========================
 =࿅ོ࿆༼menu comand selfbot༽࿅ོ࿆=
=========================
࿅ོ࿆[Id︎]
࿅ོ࿆[Mid]
࿅ོ࿆[Me︎]
࿅ོ࿆[TL︎:「Text」]
࿅ོ࿆[Mc 「mid」]
࿅ོ࿆[K on/off]
࿅ོ࿆[Join︎ on/off]
࿅ོ࿆[Gcancel:︎「Number of people」]
࿅ོ࿆[Group cancelalll︎]
࿅ོ࿆[Leave︎ on/off]
࿅ོ࿆[Add on/off]
࿅ོ࿆[Share on/off]
࿅ོ࿆[Message change:「text」]
࿅ོ࿆[Message check]
࿅ོ࿆[Confirm]
࿅ོ࿆[Jam on/off]
࿅ོ࿆[Change clock:「name」]
࿅ོ࿆[Up]Memperbaharui Jam
࿅ོ࿆[Uk join 「Uk1-9」]
࿅ོ࿆[Uk bye 「Uk1-9」]
࿅ོ࿆[Uk:version]
࿅ོ࿆[Uk:creator]

=========================
 =࿅ོ࿆༼menu comand the group༽࿅ོ࿆=
=========================
࿅ོ࿆[Mybio]
࿅ོ࿆[Myvid]
࿅ོ࿆[Mypict]
࿅ོ࿆[Getpict 「@」] By Tag
࿅ོ࿆[Getvid 「@」] By Tag
࿅ོ࿆[Getgrup image]
࿅ོ࿆[Friendlist]
࿅ོ࿆[Memlist]
࿅ོ࿆[Gruplist]
࿅ོ࿆[Curl]Menutup Url Grup
࿅ོ࿆[Ourl]Membuka Url Grup
࿅ོ࿆[url]Url Grup
࿅ོ࿆[url:「Group ID」]
࿅ོ࿆[Invite：「mid」]
࿅ོ࿆[Kick：「mid」]
࿅ོ࿆[Ginfo]Info Grup
࿅ོ࿆[jointicket]
࿅ོ࿆[Cancel]Membatalkan undangan grup
࿅ོ࿆[Gn 「group name」]
࿅ོ࿆[Nk 「name」]
࿅ོ࿆[Gcreator:inv]
࿅ོ࿆[Tag]
࿅ོ࿆[Setlastpoint]
࿅ོ࿆[Viewlastseen]
࿅ོ࿆[Han:groupcreator]

=========================
 =࿅ོ࿆༼menu comand kicker༽࿅ོ࿆=
=========================
࿅ོ࿆[Copy 「@」] By Tag
࿅ོ࿆[Backup]
࿅ོ࿆[uk cam] Memasukkan Bot Assist Kedalam Group
࿅ོ࿆[uk out:bye] Mengeluarkan Bot Assist Dari Group
࿅ོ࿆[Mid 「@」] By Tag
࿅ོ࿆[Bye 「@」] By Tag
࿅ོ࿆[Bye]
࿅ོ࿆[Kill ban]Kick user yang ada dalam daftar Ban
࿅ོ࿆[Kill 「@」]
࿅ོ࿆[Ban 「@」] By Tag
࿅ོ࿆[Unban 「@」] By Tag
࿅ོ࿆[Ban︎] Share Contact
࿅ོ࿆[Unban︎] Share Contact
࿅ོ࿆[Banlist︎]Cek Daftar Ban
࿅ོ࿆[Contact ban]
࿅ོ࿆[Cleanse]
࿅ོ࿆[Cek ban]
࿅ོ࿆[Uk mid 「Han1-9」]
࿅ོ࿆[Uk ︎invite:「mid」]
࿅ོ࿆[Uk ︎rename:「name」]
࿅ོ࿆[Uk ︎gift 「Han1-9」]
࿅ོ࿆[Hallo Uk]
࿅ོ࿆[Bot cancel]
࿅ོ࿆[Title:]

=========================
 =࿅ོ࿆༼menu comand protect༽࿅ོ࿆=
=========================
࿅ོ࿆[Set:blockinvite:on]
࿅ོ࿆[Set:blockinvite:off]
࿅ོ࿆[Protect qr on]
࿅ོ࿆[Protect qr off]
࿅ོ࿆[Protect cancel on]
࿅ོ࿆[Protect cancel off]

=========================
 =࿅ོ࿆༼menu comand search༽࿅ོ࿆=
=========================
🎶࿅ོ࿆music 「Artis - Judul Lagu」
🎼࿅ོ࿆Lirik 「Artis - Judul Lagu」
🖼࿅ོ࿆Image 「Gambar Yg Dicari」
🔎࿅ོ࿆google 「Yg Ingin Dicari」
🎞࿅ོ࿆Yt 「Video Yg Dicari」
📱࿅ོ࿆instagram 「Username Yg Dicari」
📖࿅ོ࿆Wikipedia 「Yg Ingin Dicari」
💻࿅ོ࿆Fb 「Username Yg Dicari」

 =࿅ོ࿆༼translete༽࿅ོ࿆=

╔═══¤|࿅ོ࿆| List Translate |࿅ོ࿆|¤═══╗
࿅ོ࿆╠tr-in ->Indonesia
࿅ོ࿆╠tr-en ->English
࿅ོ࿆╠tr-de ->Deutsch
࿅ོ࿆╠tr-kr ->Korea
࿅ོ࿆╠tr-ar ->Arab
࿅ོ࿆╠tr-fr ->France
࿅ོ࿆╠tr-cn ->Chinse
࿅ོ࿆╠tr-jp ->Japan
࿅ོ࿆╠tr-th ->Thailand
࿅ོ࿆╠tr-hi ->Hindia
࿅ོ࿆╠tr-jw ->Jawa
╚══════════════════╝️

"""
helpsMessage ="""࿅ོ࿆Menu Command Bot++
࿅ོ࿆[Setlastpoint]
࿅ོ࿆[Viewlastseen]
࿅ོ࿆[Clear]
࿅ོ࿆[Clearall]
࿅ོ࿆[Cancel on/off]
࿅ོ࿆[Kick on/off]
࿅ོ࿆[Cancel]
࿅ོ࿆[Kickall]
࿅ོ࿆[Speed+]
࿅ོ࿆[Buka]
࿅ོ࿆[Tutup]
࿅ོ࿆[Join]
࿅ོ࿆[Ip]


"""
stickerMessage =""" ╔═══¤|࿅ོ࿆| List Sticker|࿅ོ࿆|¤═══╗
࿅ོ࿆╠Omg
࿅ོ࿆╠Hmmmm
࿅ོ࿆╠Hahaha
࿅ོ࿆╠Numpang Lewat
࿅ོ࿆╠Enek
࿅ོ࿆╠Wkwkwk
࿅ོ࿆╠Sip
࿅ོ࿆╠???
࿅ོ࿆╠Hmmm
࿅ོ࿆╠Wkwk
࿅ོ࿆╠Welcome
࿅ོ࿆╠Hehehe
╚══════════════════╝️
"""
KAC=[cl,ki,kk,kc,kg,kh,ka,kb,kd,ke]
DEF=[ki,kk,kc,kg,kh,ka,kb,kd,ke]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
Dmid = kh.getProfile().mid
Emid = kg.getProfile().mid
Fmid = ka.getProfile().mid
Gmid = kb.getProfile().mid
Hmid = kd.getProfile().mid
Imid = ke.getProfile().mid

Bots=[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid]
admin=["udee46099e25e71f1fd1817cae9e7c429"]

with open('bl.json') as fp:
    wait3 = json.load(fp)

wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':False,
    'autoAdd':True,
    'message':"Nah Lho Ketauan Ngeadd :p",
    "lang":"JP",
    "comment":"Thanks for add me",
    "clock":False,
    "cName":"!💋🕉unni͡° ͜ʖ ͡°oppa",
    "sticker":False,
    "ProtectKick":False,
    "ProtectQR":False,
    "alwayRead":False,
    "WC":True,
    "Gbye":True,
    "QrMessage":True,
    "Protectguest":False,
    "Protectcancel":False,
    "protectionOn":False,
    "atjointicket":False,
    "kickMention":False,
    "detectMention":False
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }
    
wait3 = {
    "copy":False,
    "copy2":"target",
    "target":{}
    }

settings = {
    "simiSimi":{}
    }

res = {
    'num':{},
    'us':{},
    'au':{},
    }

setTime = {}
setTime = wait2['setTime']

contact = cl.getProfile()
backup = cl.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

mulai = time.time()

agent = {'User-Agent' : "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)"}

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     #If the Current Version of Python is 3.0 or above
        import urllib,request    #urllib library for Extracting web pages
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        #If the Current Version of Python is 2.x
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"

#Finding 'Next Image' from the given raw page


def yt(query):
    with requests.session() as s:
         isi = []
         if query == "":
             query = "S1B tanysyz" 
         s.headers['user-agent'] = 'Mozilla/5.0'
         url = 'http://www.youtube.com/results'
         params = {'search_query': query}
         r = s.get(url, params=params)
         soup = BeautifulSoup(r.content, 'html5lib')
         for a in soup.select('.yt-lockup-title > a[title]'):
            if '&list=' not in a['href']:
                if 'watch?v' in a['href']:
                    b = a['href'].replace('watch?v=', '')
                    isi += ['youtu.be' + b]
         return isi

def post_content(self, urls, data=None, files=None):
        return self._session.post(urls, headers=self._headers, data=data, files=files)

def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    #If no links are found then give an error!
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+90)
        end_content = s.find(',"ow"',start_content-90)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content
        
def sendAudio(self, to, path):
        objectId = self.sendMessage(to=to, text=None, contentType = 3).id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'media',
            'oid': objectId,
            'size': len(open(path, 'rb').read()),
            'type': 'audio',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }
        r = self.server.postContent(self.server.LINE_OBS_DOMAIN + '/talk/m/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Upload audio failure.')
        return True
        
def sendAudio(self, to_, path):
        M = Message(to=to_,contentType = 3)
        M.contentMetadata = None
        M.contentPreview = None
        M_id = self.Talk.client.sendMessage(0,M).id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'media',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'audio',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }
        r = self.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Upload image failure.')
        return True
        
def sendAudioWithURL(self, to_, url):
        path = 'pythonLiness.data'
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open(path, 'w') as f:
                shutil.copyfileobj(r.raw, f)
        else:
            raise Exception('Download Audio failure.')
        try:
            self.sendAudio(to_, path)
        except Exception as e:
            raise e
            
#Getting all links with the help of '_images_get_next_image'
def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      #Append all the links in the list named 'Links'
            time.sleep(0.1)        #Timer could be used to slow down the request for image downloads
            page = page[end_content:]
    return items
    
def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     #If the Current Version of Python is 3.0 or above
        import urllib,request    #urllib library for Extracting web pages
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        #If the Current Version of Python is 2.x
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"
            
def upload_tempimage(client):
    '''
        Upload a picture of a kitten. We don't ship one, so get creative!
    '''
    config = {
        'album': album,
        'name':  'bot auto upload',
        'title': 'bot auto upload',
        'description': 'bot auto upload'
    }

    print("Uploading image... ")
    image = client.upload_from_path(image_path, config=config, anon=False)
    print("Done")
    print()
    
def summon(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print "[Command] Tag All"
    try:
       cl.sendMessage(msg)
    except Exception as error:
       print error
       
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs)

def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False

def CloneContactProfile(self, mid):
  contact = self.getContact(mid)
  profile = self.getProfile()
  profile.displayName = contact.displayName
  profile.statusMessage = contact.pictureStatus
  self.updateProfilePicture(profile.pictureStatus)
  return self.updateProfile(profile)

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name
                wait2['ROM'][op.param1][op.param2] = "・" + Name
        else:
            pass
    except:
        pass

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))

        if op.type == 11:
           if wait["QrMessage"] == True:
               if op.param2 in Bots:
                   return
               ki.sendText(op.param1,cl.getContact(op.param2).displayName + "Please don't open qr")
               print "Update group"

        #------Open QR Kick start------#
        if op.type == 11:
           if wait["ProtectQR"] == True:
               if op.param2 not in Bots:
                   if op.param2 in Bots:
                       pass
                       G = ka.getGroup(op.param1)
                       G.preventJoinByTicket = True
                       random.choice(DEF).kickoutFromGroup(op.param1,[op.param2])
                       random.choice(DEF).updateGroup(G)
        #------Open QR Kick finish-----#

        #------Invite User Kick start------#
        if op.type == 13:
           if wait["Protectguest"] == True:
               if op.param2 not in Bots:
                  random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
        #------Invite User Kick Finish------#

        if op.type == 13:
                if op.param3 in mid:
                    if op.param2 in Amid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)

                if op.param3 in Amid:
                    if op.param2 in Bmid:
                        X = kk.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)

                if op.param3 in Bmid:
                    if op.param2 in Cmid:
                        X = kc.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)
                        kk.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)

                if op.param3 in Cmid:
                    if op.param2 in Dmid:
                        X = kh.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kh.updateGroup(X)
                        Ti = kh.reissueGroupTicket(op.param1)
                        kc.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kh.updateGroup(X)
                        Ti = kh.reissueGroupTicket(op.param1)

                if op.param3 in Dmid:
                    if op.param2 in Emid:
                        X = kg.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kg.updateGroup(X)
                        Ti = kg.reissueGroupTicket(op.param1)
                        kh.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kg.updateGroup(X)
                        Ti = kg.reissueGroupTicket(op.param1)

                if op.param3 in Emid:
                    if op.param2 in Fmid:
                        X = ka.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ka.updateGroup(X)
                        Ti = ka.reissueGroupTicket(op.param1)
                        kg.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        ka.updateGroup(X)
                        Ti = ka.reissueGroupTicket(op.param1)

                if op.param3 in Fmid:
                    if op.param2 in Gmid:
                        X = kb.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kb.updateGroup(X)
                        Ti = kb.reissueGroupTicket(op.param1)
                        ka.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kb.updateGroup(X)
                        Ti = kb.reissueGroupTicket(op.param1)

                if op.param3 in Gmid:
                    if op.param2 in Hmid:
                        X = kd.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kd.updateGroup(X)
                        Ti = kd.reissueGroupTicket(op.param1)
                        kb.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kd.updateGroup(X)
                        Ti = kd.reissueGroupTicket(op.param1)

                if op.param3 in Hmid:
                    if op.param2 in Imid:
                        X = ke.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ke.updateGroup(X)
                        Ti = ke.reissueGroupTicket(op.param1)
                        kd.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        ke.updateGroup(X)
                        Ti = ke.reissueGroupTicket(op.param1)

                if op.param3 in Imid:
                    if op.param2 in mid:
                        X = cl.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                        ke.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)

        if op.type == 13:
            print op.param1
            print op.param2
            print op.param3
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait3["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)

        if op.type == 15:
            if wait["Gbye"] == True:
                if op.param2 in Bots:
                    return
                ki.sendText(op.param1,cl.getContact(op.param2).displayName + " Good Bye\n(´･ω･`)")
                print "MEMBER OUT GROUP"

        if op.type == 17:
            if wait["WC"] == True:
                if op.param2 in Bots:
                    return
                ginfo = cl.getGroup(op.param1)
                ki.sendText(op.param1,cl.getContact(op.param2).displayName + " Welcome\n(´･ω･`)")
                ki.sendText(op.param1, "Owner Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName)
                print "MEMBER HAS JOIN THE GROUP"

        if op.type == 17:
            if op.param2 not in Bots:
                joinblacklist = op.param2.replace("·",',')
                joinblacklistX = joinblacklist.split(",")
                matched_list = []
                for tag in wait3["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, joinblacklistX)
                if matched_list == []:
                    pass
                else:
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])

        if op.type == 19:
           if op.param2 not in Bots:
               if op.param2 in Bots:
                   pass
                   random.choice(DEF).kickoutFromGroup(op.param1,[op.param2])
                   random.choice(DEF).inviteIntoGroup(op.param1,[op.param3])

        if op.type == 19:
                if not op.param2 in Bots:
                    try:
                        gs = cl.getGroup(op.param1)
                        gs = ki.getGroup(op.param1)
                        gs = kk.getGroup(op.param1)
                        gs = kc.getGroup(op.param1)
                        gs = kh.getGroup(op.param1)
                        gs = kg.getGroup(op.param1)
                        gs = ka.getGroup(op.param1)
                        gs = kb.getGroup(op.param1)
                        gs = kd.getGroup(op.param1)
                        gs = ke.getGroup(op.param1)
                        targets = [op.param2]
                        for target in targets:
                           try:
                               wait3["blacklist"][target] = True
                               with open('bl.json', 'w') as fp:
                                   json.dump(wait3, fp, sort_keys=True, indent=4)
                           except:
                            return
                    except Exception, e:
                        print e

        if op.type == 19:
                if op.param3 in admin:
                    random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])

                if mid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kc.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait3["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait3["blacklist"][op.param2] = True
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ki.updateGroup(G)
                    Ti = ki.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    if op.param2 in wait3["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait3["blacklist"][op.param2] = True

                if Amid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        kh.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait3["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait3["blacklist"][op.param2] = True

                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki.updateGroup(G)
                    Ticket = ki.reissueGroupTicket(op.param1)
                    if op.param2 in wait3["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait3["blacklist"][op.param2] = True
                if Bmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        kh.kickoutFromGroup(op.param1,[op.param2])
                        kg.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait3["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait3["blacklist"][op.param2] = True

                    X = kc.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kk.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kk.updateGroup(G)
                    Ticket = kk.reissueGroupTicket(op.param1)
                    if op.param2 in wait3["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait3["blacklist"][op.param2] = True

                if Cmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kh.kickoutFromGroup(op.param1,[op.param2])
                        kg.kickoutFromGroup(op.param1,[op.param2])
                        ka.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait3["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait3["blacklist"][op.param2] = True

                    X = kh.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kh.updateGroup(X)
                    Ti = kh.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kc.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kc.updateGroup(G)
                    Ticket = kc.reissueGroupTicket(op.param1)
                    if op.param2 in wait3["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait3["blacklist"][op.param2] = True

                if Dmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kg.kickoutFromGroup(op.param1,[op.param2])
                        ka.kickoutFromGroup(op.param1,[op.param2])
                        kb.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait3["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait3["blacklist"][op.param2] = True

                    X = kg.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kg.updateGroup(X)
                    Ti = kg.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kh.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kh.updateGroup(G)
                    Ticket = kh.reissueGroupTicket(op.param1)
                    if op.param2 in wait3["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait3["blacklist"][op.param2] = True

                if Emid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ka.kickoutFromGroup(op.param1,[op.param2])
                        kb.kickoutFromGroup(op.param1,[op.param2])
                        kd.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wai3["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait3["blacklist"][op.param2] = True

                    X = ka.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ka.updateGroup(X)
                    Ti = ka.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kg.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kg.updateGroup(G)
                    Ticket = kg.reissueGroupTicket(op.param1)
                    if op.param2 in wait3["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait3["blacklist"][op.param2] = True

                if Fmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kb.kickoutFromGroup(op.param1,[op.param2])
                        kd.kickoutFromGroup(op.param1,[op.param2])
                        ke.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait3["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait3["blacklist"][op.param2] = True

                    X = kb.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kb.updateGroup(X)
                    Ti = kb.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ka.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ka.updateGroup(G)
                    Ticket = ka.reissueGroupTicket(op.param1)
                    if op.param2 in wait3["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait3["blacklist"][op.param2] = True

                if Gmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kd.kickoutFromGroup(op.param1,[op.param2])
                        ke.kickoutFromGroup(op.param1,[op.param2])
                        cl.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait3["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait3["blacklist"][op.param2] = True

                    X = kd.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kd.updateGroup(X)
                    Ti = kd.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kb.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kb.updateGroup(G)
                    Ticket = kb.reissueGroupTicket(op.param1)
                    if op.param2 in wait3["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait4["blacklist"][op.param2] = True

                if Hmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ke.kickoutFromGroup(op.param1,[op.param2])
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait3["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait3["blacklist"][op.param2] = True

                    X = ke.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ke.updateGroup(X)
                    Ti = ke.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kd.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kd.updateGroup(G)
                    Ticket = kd.reissueGroupTicket(op.param1)
                    if op.param2 in wait3["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait3["blacklist"][op.param2] = True

                if Imid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait3["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait3["blacklist"][op.param2] = True

                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ke.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ke.updateGroup(G)
                    Ticket = ke.reissueGroupTicket(op.param1)
                    if op.param2 in wait3["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait3["blacklist"][op.param2] = True
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait3["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == "udee46099e25e71f1fd1817cae9e7c429":
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            X = cl.getGroup(list_[1])
                            X.preventJoinByTicket = True
                            cl.updateGroup(X)
                        except:
                            cl.sendText(msg.to,"error")

        #------Cancel User Kick start------#
        if op.type == 32:
            if wait["Protectcancel"] == True:
              if op.param2 not in admin:
                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
        #-----Cancel User Kick Finish------#

            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
            if msg.contentType == 16:
                url = msg.contentMetadata["postEndUrl"]
                ki.like(url8[25:58], url[66:], likeType=1001)
                ki.comment(url[25:58], url[66:], "Auto Like by Rayhan\n\nhttp://line.me/ti/p/~mhmmdraaaayhan")
        if op.type == 26:
            msg = op.message
            if msg.to in settings["simiSimi"]:
                if settings["simiSimi"][msg.to] == True:
                    if msg.text is not None:
                        text = msg.text
                        r = requests.get("http://api.ntcorp.us/chatbot/1/?text=" + text.replace(" ","+") + "&key=beta1.nt")
                        data = r.text
                        data = json.loads(data)
                        if data['status'] == 200:
                            if data['result']['result'] == 100:
                                cl.sendText(msg.to, "[From Simi]\n" + data['result']['response'].encode('utf-8'))

            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                     contact = cl.getContact(msg.from_)
                     cName = contact.displayName
                     balas = [cName + " Ngapain Ngetag?, ", cName + "Gw masih tidur,kalo ada perlu pc aja " + cName + "?", "Ada Perlu apa, " + cName + "?", "Apaan?", "Dont Tag Me!", cName + "Gak Usah Tag,Kalo Penting Pc aja!"]
                     ret_ = "[Auto Respond]\n" + random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in admin:
                                  cl.sendText(msg.to,ret_)

            elif 'MENTION' in msg.contentMetadata.keys() != None:
                if wait["detectMention"] == True:
                    msg.contentType = 7
                    msg.text = None
                    msg.contentMetadata = {
                                         "STKID": "16846765",
                                         "STKPKGID": "8543",
                                         "STKVER": "7" }
                    for mention in mentionees:
                           if mention['M'] in admin:
                                  cl.sendMessage(msg)

            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["kickMention"] == True:
                     contact = cl.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["",cName + " Ngapain Ngetag?, ", cName + "Gw masih tidur,kalo ada perlu pc aja " + cName + "?", "Ada Perlu apa, " + cName + "?","Apaan?. ", "Dont Tag Me!"]
                     ret_ = "[Auto Respond]\n" + random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_)
                                  cl.kickoutFromGroup(msg.to,[msg.from_])
                                  break
                              
            if wait["alwayRead"] == True:
                if msg.toType == 0:
                    cl.sendChatChecked(msg.from_,msg.id)
                else:
                    cl.sendChatChecked(msg.to,msg.id)
        if op.type == 25 or op.type == 26:
            msg = op.message
            if msg.contentType == 13:
                if wait3["wblack"] == True:
                   with open('bl.json', 'w') as fp:
                       json.dump(wait3, fp, sort_keys=True, indent=4)
                   if msg.contentMetadata["mid"] in wait3["commentBlack"]:
                        cl.sendText(msg.to,"already")
                        wait3["wblack"] = False
                        with open('bl.json', 'w') as fp:
                            json.dump(wait3, fp, sort_keys=True, indent=4)
                   else:
                        wait3["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait3["wblack"] = False
                        with open('bl.json', 'w') as fp:
                            json.dump(wait3, fp, sort_keys=True, indent=4)
                        cl.sendText(msg.to,"decided not to comment")
                elif wait3["dblack"] == True:
                     with open('bl.json', 'w') as fp:
                         json.dump(wait3, fp, sort_keys=4, indent=4)
                     if msg.contentMetadata["mid"] in wait3["commentBlack"]:
                         del wait3["commentBlack"][msg.contentMetadata["mid"]]
                         with open('bl.json', 'w') as fp:
                             json.dump(wait3, fp, sort_keys=True, indent=4)
                         cl.sendText(msg.to,"deleted")
                         wait3["dblack"] = False
                         with open('bl.json', 'w') as fp:
                             json.dump(wait3, fp, sort_keys=True, indent=4)
                     else:
                         wait3["dblack"] = False
                         with open('bl.json', 'w') as fp:
                             json.dump(wait3, fp, sort_keys=True, indent=4)
                         cl.sendText(msg.to,"It is not in the black list")
                elif wait3["wblacklist"] == True:
                     with open('bl.json', 'w') as fp:
                         json.dump(wait3, fp, sort_keys=True, indent=4)
                     if msg.contentMetadata["mid"] in wait3["blacklist"]:
                         cl.sendText(msg.to,"already")
                         wait3["wblacklist"] = False
                         with open('bl.json', 'w') as fp:
                             json.dump(wait3, fp, sort_keys=True, indent=4)
                     else:
                         wait3["blacklist"][msg.contentMetadata["mid"]] = True
                         with open('bl.json', 'w') as fp:
                             json.dump(wait3, fp, sort_keys=True, indent=4)
                         wait3["wblacklist"] = False
                         with open('bl.json', 'w') as fp:
                             json.dump(wait3, fp, sort_keys=True, indent=4)
                         cl.sendText(msg.to,"aded")

                elif wait3["dblacklist"] == True:
                     with open('bl.json', 'w') as fp:
                         json.dump(wait3, fp, sort_keys=True, indent=4)
                     if msg.contentMetadata["mid"] in wait3["blacklist"]:
                         del wait3["blacklist"][msg.contentMetadata["mid"]]
                         with open('bl.json', 'w') as fp:
                             json.dump(wait3, fp, sort_keys=True, indent=4)
                         cl.sendText(msg.to,"deleted")
                         wait3["dblacklist"] = False
                         with open('bl.json', 'w') as fp:
                             json.dump(wait3, fp, sort_keys=True, indent=4)

                     else:
                         wait3["dblacklist"] = False
                         with open('bl.json', 'w') as fp:
                            json.dump(wait3, fp, sort_keys=True, indent=4)
                         cl.sendText(msg.to,"It is not in the black list")
                elif wait["contact"] == True:
                     msg.contentType = 0
                     cl.sendText(msg.to,msg.contentMetadata["mid"])
                     if 'displayName' in msg.contentMetadata:
                         contact = cl.getContact(msg.contentMetadata["mid"])
                         try:
                             cu = cl.channel.getCover(msg.contentMetadata["mid"])
                         except:
                             cu = ""
                         cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                     else:
                         contact = cl.getContact(msg.contentMetadata["mid"])
                         try:
                             cu = cl.channel.getCover(msg.contentMetadata["mid"])
                         except:
                             cu = ""
                         cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif 'MENTION' in msg.contentMetadata.keys() != None:
                if wait["detectMention"] == True:
                    msg.contentType = 7
                    msg.text = None
                    msg.contentMetadata = {
                                         "STKID": "16846765",
                                         "STKPKGID": "8543",
                                         "STKVER": "7" }
                    for mention in mentionees:
                           if mention['M'] in admin:
                                  cl.sendMessage(msg)
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.contentType == 7:
                if wait['sticker'] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    filler = "══════════\n『 Sticker Info 』\n══════════\nSTKID : %s\nSTKPKGID : %s\nSTKVER : %s\n══════════\n『 Link 』\n══════════\nline://shop/detail/%s" % (stk_id,pkg_id,stk_ver,pkg_id)
                    cl.sendText(msg.to, filler) 
                else: 
                    pass
            elif msg.text is None:
                return
            elif msg.text in ["Key","command","Command","cmd"]:
                if msg.from_ in admin:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,helpMessage)
                        cl.sendText(msg.to,helpsMessage)
                    else:
                        cl.sendText(msg.to,helpt)
                        cl.sendText(msg.to,helpst)
            elif msg.text in ["Sticker List","sticker list"]:
                if msg.from_ in admin:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,stickerMessage)
                    else:
                        cl.sendText(msg.to,stickert)
            elif ("Gn " in msg.text):
                if msg.from_ in admin:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn ","")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")
            elif ("Uk1 gn " in msg.text):
                if msg.from_ in admin:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Uk1 gn ","")
                    ki.updateGroup(X)
                else:
                    ki.sendText(msg.to,"It can't be used besides the group.")
            elif ("Uk2 gn " in msg.text):
                if msg.from_ in admin:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Uk2 gn ","")
                    kk.updateGroup(X)
                else:
                    kk.sendText(msg.to,"It can't be used besides the group.")
            elif ("Uk3 gn " in msg.text):
                if msg.from_ in admin:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Uk3 gn ","")
                    kc.updateGroup(X)
                else:
                    kc.sendText(msg.to,"It can't be used besides the group.")
            elif "Kick " in msg.text:
                if msg.from_ in admin:
                    midd = msg.text.replace("Kick ","")
                    cl.kickoutFromGroup(msg.to,[midd])
            elif "Uk1 kick " in msg.text:
                if msg.from_ in admin:
                    midd = msg.text.replace("Uk1 kick ","")
                    ki.kickoutFromGroup(msg.to,[midd])
            elif "Uk2 kick " in msg.text:
                if msg.from_ in admin:
                    midd = msg.text.replace("Uk2 kick ","")
                    kk.kickoutFromGroup(msg.to,[midd])
            elif "Uk3 kick " in msg.text:
                if msg.from_ in admin:
                    midd = msg.text.replace("Uk3 kick ","")
                    kc.kickoutFromGroup(msg.to,[midd])
            elif "Uk4 kick " in msg.text:
                if msg.from_ in admin:
                    midd = msg.text.replace("Uk4 kick ","")
                    kh.kickoutFromGroup(msg.to,[midd])
            elif "Uk5 kick " in msg.text:
                if msg.from_ in admin:
                    midd = msg.text.replace("Uk5 kick ","")
                    kg.kickoutFromGroup(msg.to,[midd])
            elif "Uk6 kick " in msg.text:
                if msg.from_ in admin:
                    midd = msg.text.replace("Uk6 kick ","")
                    ka.kickoutFromGroup(msg.to,[midd])
            elif "Uk7 kick " in msg.text:
                if msg.from_ in admin:
                    midd = msg.text.replace("Uk7 kick ","")
                    kb.kickoutFromGroup(msg.to,[midd])
            elif "Uk8 kick " in msg.text:
                if msg.from_ in admin:
                    midd = msg.text.replace("Uk8 kick ","")
                    kd.kickoutFromGroup(msg.to,[midd])
            elif "Uk9 kick " in msg.text:
                if msg.from_ in admin:
                    midd = msg.text.replace("Uk9 kick ","")
                    ke.kickoutFromGroup(msg.to,[midd])
            elif "Invite " in msg.text:
                if msg.from_ in admin:
                    midd = msg.text.replace("Invite ","")
                    cl.findAndAddContactsByMid(midd)
                    cl.inviteIntoGroup(msg.to,[midd])
            elif "Uk1 invite " in msg.text:
                if msg.from_ in admin:
                    midd = msg.text.replace("Uk1 invite ","")
                    ki.findAndAddContactsByMid(midd)
                    ki.inviteIntoGroup(msg.to,[midd])
            elif "Uk2 invite " in msg.text:
                if msg.from_ in admin:
                    midd = msg.text.replace("Uk2 invite ","")
                    kk.findAndAddContactsByMid(midd)
                    kk.inviteIntoGroup(msg.to,[midd])
            elif "Uk3 invite " in msg.text:
                if msg.from_ in admin:
                    midd = msg.text.replace("Uk3 invite ","")
                    kc.findAndAddContactsByMid(midd)
                    kc.inviteIntoGroup(msg.to,[midd])
            elif "Uk4 invite " in msg.text:
                if msg.from_ in admin:
                    midd = msg.text.replace("Uk4 invite ","")
                    kh.findAndAddContactsByMid(midd)
                    kh.inviteIntoGroup(msg.to,[midd])
            elif "Uk5 invite " in msg.text:
                if msg.from_ in admin:
                    midd = msg.text.replace("Uk5 invite ","")
                    kg.findAndAddContactsByMid(midd)
                    kg.inviteIntoGroup(msg.to,[midd])
            elif "Uk6 invite " in msg.text:
                if msg.from_ in admin:
                    midd = msg.text.replace("Uk6 invite ","")
                    ka.findAndAddContactsByMid(midd)
                    ka.inviteIntoGroup(msg.to,[midd])
            elif "Uk7 invite " in msg.text:
                if msg.from_ in admin:
                    midd = msg.text.replace("Uk7 invite ","")
                    kb.findAndAddContactsByMid(midd)
                    kb.inviteIntoGroup(msg.to,[midd])
            elif "Uk8 invite " in msg.text:
                if msg.from_ in admin:
                    midd = msg.text.replace("Uk8 invite ","")
                    kd.findAndAddContactsByMid(midd)
                    kd.inviteIntoGroup(msg.to,[midd])
            elif "Uk9 invite " in msg.text:
                if msg.from_ in admin:
                    midd = msg.text.replace("Uk9 invite ","")
                    ke.findAndAddContactsByMid(midd)
                    ke.inviteIntoGroup(msg.to,[midd])
            elif msg.text in ["My Uk"]:
                if msg.from_ in admin:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': Amid}
                    cl.sendMessage(msg)

                    msg.contentType = 13
                    msg.contentMetadata = {'mid': Bmid}
                    cl.sendMessage(msg)

                    msg.contentType = 13
                    msg.contentMetadata = {'mid': Cmid}
                    cl.sendMessage(msg)

                    msg.contentType = 13
                    msg.contentMetadata = {'mid': Dmid}
                    cl.sendMessage(msg)

                    msg.contentType = 13
                    msg.contentMetadata = {'mid': Emid}
                    cl.sendMessage(msg)

                    msg.contentType = 13
                    msg.contentMetadata = {'mid': Fmid}
                    cl.sendMessage(msg)

                    msg.contentType = 13
                    msg.contentMetadata = {'mid': Gmid}
                    cl.sendMessage(msg)

                    msg.contentType = 13
                    msg.contentMetadata = {'mid': Hmid}
                    cl.sendMessage(msg)

                    msg.contentType = 13
                    msg.contentMetadata = {'mid': Imid}
                    cl.sendMessage(msg)
            elif msg.text in ["Me"]:
                if msg.from_ in admin:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': mid}
                    cl.sendMessage(msg)
            elif msg.text in ["Uk1"]:
                if msg.from_ in admin:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': Amid}
                    ki.sendMessage(msg)
            elif msg.text in ["Uk2"]:
                if msg.from_ in admin:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': Bmid}
                    kk.sendMessage(msg)
            elif msg.text in ["Uk3"]:
                if msg.from_ in admin:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': Cmid}
                    kc.sendMessage(msg)
            elif msg.text in ["Uk4"]:
                if msg.from_ in admin:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': Dmid}
                    kh.sendMessage(msg)
            elif msg.text in ["Uk5"]:
                if msg.from_ in admin:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': Emid}
                    kg.sendMessage(msg)
            elif msg.text in ["Uk6"]:
                if msg.from_ in admin:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': Fmid}
                    ka.sendMessage(msg)
            elif msg.text in ["Uk7"]:
                if msg.from_ in admin:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': Gmid}
                    kb.sendMessage(msg)
            elif msg.text in ["Uk8"]:
                if msg.from_ in admin:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': Hmid}
                    kd.sendMessage(msg)
            elif msg.text in ["Uk9"]:
                if msg.from_ in admin:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': Imid}
                    ke.sendMessage(msg)
            elif msg.text in ["æ„›ã®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Gift","Nih"]:
                if msg.from_ in admin:
                    msg.contentType = 9
                    msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                        'PRDTYPE': 'THEME',
                                        'MSGTPL': '5'}
                    msg.text = None
                    cl.sendMessage(msg)
            elif msg.text in ["æ„›ã®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Han1 gift"]:
                if msg.from_ in admin:
                    msg.contentType = 9
                    msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                        'PRDTYPE': 'THEME',
                                        'MSGTPL': '6'}
                    msg.text = None
                    ki.sendMessage(msg)
            elif msg.text in ["æ„›ã®ãƒ—ãƒ¬ã‚¼ãƒ��ãƒˆ","Han2 gift"]:
                if msg.from_ in admin:
                    msg.contentType = 9
                    msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                        'PRDTYPE': 'THEME',
                                        'MSGTPL': '8'}
                    msg.text = None
                    kk.sendMessage(msg)
            elif msg.text in ["æ„›ã®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Han3 gift"]:
                if msg.from_ in admin:
                    msg.contentType = 9
                    msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                        'PRDTYPE': 'THEME',
                                        'MSGTPL': '10'}
                    msg.text = None
                    kc.sendMessage(msg)
            elif msg.text in ["æ„›ã^a®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Han4 gift"]:
                if msg.from_ in admin:
                    msg.contentType = 9
                    msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                        'PRDTYPE': 'THEME',
                                        'MSGTPL': '5'}
                    msg.text = None
                    kh.sendMessage(msg)
            elif msg.text in ["��„›ã^a®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Han5 gift"]:
                if msg.from_ in admin:
                    msg.contentType = 9
                    msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                        'PRDTYPE': 'THEME',
                                        'MSGTPL': '6'}
                    msg.text = None
                    kg.sendMessage(msg)
            elif msg.text in ["æ„›ã^a®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Han6 gift"]:
                if msg.from_ in admin:
                    msg.contentType = 9
                    msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                        'PRDTYPE': 'THEME',
                                        'MSGTPL': '8'}
                    msg.text = None
                    ka.sendMessage(msg)
            elif msg.text in ["æ„›ã^a®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Han7 gift"]:
                if msg.from_ in admin:
                    msg.contentType = 9
                    msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                        'PRDTYPE': 'THEME',
                                        'MSGTPL': '10'}
                    msg.text = None
                    kb.sendMessage(msg)
            elif msg.text in ["æ„›ã^a®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Han8 gift"]:
                if msg.from_ in admin:
                    msg.contentType = 9
                    msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                        'PRDTYPE': 'THEME',
                                        'MSGTPL': '5'}
                    msg.text = None
                    kd.sendMessage(msg)
            elif msg.text in ["æ„›ã^a®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Han9 gift"]:
                if msg.from_ in admin:
                    msg.contentType = 9
                    msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                        'PRDTYPE': 'THEME',
                                        'MSGTPL': '6'}
                    msg.text = None
                    ke.sendMessage(msg)
            elif msg.text in ["æ„›ã®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","All gift"]:
                if msg.from_ in admin:
                    msg.contentType = 9
                    msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                        'PRDTYPE': 'THEME',
                                        'MSGTPL': '12'}
                    msg.text = None
                    ki.sendMessage(msg)
                    kk.sendMessage(msg)
                    kc.sendMessage(msg)
                    kh.sendMessage(msg)
                    kg.sendMessage(msg)
                    ka.sendMessage(msg)
                    kb.sendMessage(msg)
                    kd.sendMessage(msg)
                    ke.sendMessage(msg)
            elif msg.text in ["cancel","Cancel"]:
                if msg.from_ in admin:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No one is inviting")
                        else:
                            cl.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Han cancel","Bot cancel"]:
                if msg.from_ in admin:
                    G = k3.getGroup(msg.to)
                    if G.invitee is not None:
                        gInviMids = [contact.mid for contact in G.invitee]
                        k3.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            k3.sendText(msg.to,"No one is inviting")
                        else:
                            k3.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        k3.sendText(msg.to,"Can not be used outside the group")
                    else:
                        k3.sendText(msg.to,"Not for use less than group")
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
            elif msg.text in ["Ourl","Link on"]:
                if msg.from_ in admin:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Uk1 ourl","Uk1 link on"]:
                if msg.from_ in admin:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    ki.updateGroup(X)
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Done Han")
                    else:
                        ki.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Uk2 ourl","Uk2 link on"]:
                if msg.from_ in admin:
                    X = kk.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    kk.updateGroup(X)
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Done Han")
                    else:
                        kk.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kk.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Uk3 ourl","Uk3 link on"]:
                if msg.from_ in admin:
                    X = kc.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Done Han")
                    else:
                        kc.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kc.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Curl","Link off"]:
                if msg.from_ in admin:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Uk1 curl","Uk1 link off"]:
                if msg.from_ in admin:
                    X = ki.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    ki.updateGroup(X)
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Done Han")
                    else:
                        ki.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ki.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Uk2 curl","Uk2 link off"]:
                if msg.from_ in admin:
                    X = kk.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    kk.updateGroup(X)
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Done Han")
                    else:
                        kk.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kk.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Uk3 curl","Uk3 link off"]:
                if msg.from_ in admin:
                    X = kc.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    kc.updateGroup(X)
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Done Han")
                    else:
                        kc.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kc.sendText(msg.to,"Not for use less than group")
            elif "jointicket " in msg.text.lower():
		rplace=msg.text.lower().replace("jointicket ")
		if rplace == "on":
			wait["atjointicket"]=True
		elif rplace == "off":
			wait["atjointicket"]=False
		cl.sendText(msg.to,"Auto Join Group by Ticket is %s" % str(wait["atjointicket"]))
            elif '/ti/g/' in msg.text.lower():
		link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
		links = link_re.findall(msg.text)
		n_links=[]
		for l in links:
			if l not in n_links:
				n_links.append(l)
		for ticket_id in n_links:
			if wait["atjointicket"] == True:
				group=cl.findGroupByTicket(ticket_id)
				cl.acceptGroupInvitationByTicket(group.mid,ticket_id)
				cl.sendText(msg.to,"Sukses join ke grup %s" % str(group.name))
            elif msg.text == "Ginfo":
                if msg.from_ in admin:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\nmembers:" + str(len(ginfo.members)) + "members\npending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif "Id" == msg.text:
                if msg.from_ in admin:
                    cl.sendText(msg.to,msg.to)
            elif "All mid" == msg.text:
                if msg.from_ in admin:
                    cl.sendText(msg.to,mid)
                    ki.sendText(msg.to,Amid)
                    kk.sendText(msg.to,Bmid)
                    kc.sendText(msg.to,Cmid)
                    kh.sendText(msg.to,Dmid)
                    kg.sendText(msg.to,Emid)
                    ka.sendText(msg.to,Fmid)
                    kb.sendText(msg.to,Gmid)
                    kd.sendText(msg.to,Hmid)
                    ke.sendText(msg.to,Imid)
            elif "Mid" == msg.text:
                if msg.from_ in admin:
                    cl.sendText(msg.to,mid)
            elif "Uk1 mid" == msg.text:
                if msg.from_ in admin:
                    ki.sendText(msg.to,Amid)
            elif "Uk2 mid" == msg.text:
                if msg.from_ in admin:
                    kk.sendText(msg.to,Bmid)
            elif "Uk3 mid" == msg.text:
                if msg.from_ in admin:
                    kc.sendText(msg.to,Cmid)
            elif "Uk4 mid" == msg.text:
                if msg.from_ in admin:
                    kh.sendText(msg.to,Dmid)
            elif "Uk5 mid" == msg.text:
                if msg.from_ in admin:
                    kg.sendText(msg.to,Emid)
            elif "Uk6 mid" == msg.text:
                if msg.from_ in admin:
                    ka.sendText(msg.to,Fmid)
            elif "Uk7 mid" == msg.text:
                if msg.from_ in admin:
                    kb.sendText(msg.to,Gmid)
            elif "Uk8 mid" == msg.text:
                if msg.from_ in admin:
                    kd.sendText(msg.to,Hmid)
            elif "Uk9 mid" == msg.text:
                if msg.from_ in admin:
                    ke.sendText(msg.to,Imid)
            elif msg.text in ["Numpang Lewat"]:
                if msg.from_ in admin:
                    msg.contentType = 7
                    msg.text = None
                    msg.contentMetadata = {
                                         "STKID": "12842260",
                                         "STKPKGID": "1318245",
                                         "STKVER": "1" }
                    cl.sendMessage(msg)
            elif msg.text in ["Sip"]:
                if msg.from_ in admin:
                    msg.contentType = 7
                    msg.text = None
                    msg.contentMetadata = {
                                         "STKID": "12344",
                                         "STKPKGID": "853",
                                         "STKVER": "1" }
                    cl.sendMessage(msg)
            elif msg.text in ["Enek"]:
                if msg.from_ in admin:
                    msg.contentType = 7
                    msg.text = None
                    msg.contentMetadata = {
                                         "STKID": "18687389",
                                         "STKPKGID": "1520987",
                                         "STKVER": "1" }
                    cl.sendMessage(msg)
            elif msg.text in ["Wkwkwk"]:
                if msg.from_ in admin:
                    msg.contentType = 7
                    msg.text = None
                    msg.contentMetadata = {
                                         "STKID": "16846776",
                                         "STKPKGID": "8543",
                                         "STKVER": "7" }
                    cl.sendMessage(msg)
            elif msg.text in ["Hmmmm"]:
                if msg.from_ in admin:
                    msg.contentType = 7
                    msg.text = None
                    msg.contentMetadata = {
                                         "STKID": "2754665",
                                         "STKPKGID": "1066653",
                                         "STKVER": "1" }
                    cl.sendMessage(msg)
            elif msg.text in ["Hahaha"]:
                if msg.from_ in admin:
                    msg.contentType = 7
                    msg.text = None
                    msg.contentMetadata = {
                                         "STKID": "18687390",
                                         "STKPKGID": "1520987",
                                         "STKVER": "1" }
                    cl.sendMessage(msg)
            elif msg.text in ["???"]:
                if msg.from_ in admin:
                    msg.contentType = 7
                    msg.text = None
                    msg.contentMetadata = {
                                         "STKID": "16846765",
                                         "STKPKGID": "8543",
                                         "STKVER": "7" }
                    cl.sendMessage(msg)
            elif msg.text in ["Omg"]:
                if msg.from_ in admin:
                    msg.contentType = 7
                    msg.text = None
                    msg.contentMetadata = {
                                         "STKID": "18687401",
                                         "STKPKGID": "1520987",
                                         "STKVER": "1" }
                    cl.sendMessage(msg)
            elif msg.text in ["Wkwk"]:
                if msg.from_ in admin:
                    msg.contentType = 7
                    msg.text = None
                    msg.contentMetadata = {
                                         "STKID": "100",
                                         "STKPKGID": "1",
                                         "STKVER": "100" }
                    ki.sendMessage(msg)
                    kk.sendMessage(msg)
            elif msg.text in ["Hehehe"]:
                if msg.from_ in admin:
                    msg.contentType = 7
                    msg.text = None
                    msg.contentMetadata = {
                                         "STKID": "14689881",
                                         "STKPKGID": "1374347",
                                         "STKVER": "1" }
                    cl.sendMessage(msg)
            elif msg.text in ["Galon"]:
                if msg.from_ in admin:
                    msg.contentType = 7
                    msg.text = None
                    msg.contentMetadata = {
                                         "STKID": "9",
                                         "STKPKGID": "1",
                                         "STKVER": "100" }
                    ki.sendMessage(msg)
                    kk.sendMessage(msg)
            elif msg.text in ["You"]:
                if msg.from_ in admin:
                    msg.contentType = 7
                    msg.text = None
                    msg.contentMetadata = {
                                         "STKID": "7",
                                         "STKPKGID": "1",
                                         "STKVER": "100" }
                    ki.sendMessage(msg)
                    kk.sendMessage(msg)
            elif msg.text in ["Hadeuh"]:
                if msg.from_ in admin:
                    msg.contentType = 7
                    msg.text = None
                    msg.contentMetadata = {
                                         "STKID": "6",
                                         "STKPKGID": "1",
                                         "STKVER": "100" }
                    ki.sendMessage(msg)
                    kk.sendMessage(msg)
            elif msg.text in ["Please"]:
                if msg.from_ in admin:
                    msg.contentType = 7
                    msg.text = None
                    msg.contentMetadata = {
                                         "STKID": "4",
                                         "STKPKGID": "1",
                                         "STKVER": "100" }
                    ki.sendMessage(msg)
                    kk.sendMessage(msg)
            elif msg.text in ["Haaa"]:
                if msg.from_ in admin:
                    msg.contentType = 7
                    msg.text = None
                    msg.contentMetadata = {
                                         "STKID": "3",
                                         "STKPKGID": "1",
                                         "STKVER": "100" }
                    ki.sendMessage(msg)
                    kk.sendMessage(msg)
            elif msg.text in ["Lol"]:
                if msg.from_ in admin:
                    msg.contentType = 7
                    msg.text = None
                    msg.contentMetadata = {
                                         "STKID": "110",
                                         "STKPKGID": "1",
                                         "STKVER": "100" }
                    ki.sendMessage(msg)
                    kk.sendMessage(msg)
            elif msg.text in ["Hmmm"]:
                if msg.from_ in admin:
                    msg.contentType = 7
                    msg.text = None
                    msg.contentMetadata = {
                                         "STKID": "101",
                                         "STKPKGID": "1",
                                         "STKVER": "100" }
                    ki.sendMessage(msg)
            elif msg.text in ["Welcome"]:
                if msg.from_ in admin:
                    msg.contentType = 7
                    msg.text = None
                    msg.contentMetadata = {
                                         "STKID": "14689862",
                                         "STKPKGID": "1374347",
                                         "STKVER": "1" }
                    cl.sendMessage(msg)
            elif msg.text in ["TL:"]:
                if msg.from_ in admin:
                    tl_text = msg.text.replace("TL:","")
                    cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif msg.text in ["Cn "]:
                if msg.from_ in admin:
                    string = msg.text.replace("Cn ","")
                    if len(string.decode('utf-8')) <= 20:
                        profile = cl.getProfile()
                        profile.displayName = string
                        cl.updateProfile(profile)
                        cl.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Uk1 rename "]:
                if msg.from_ in admin:
                    string = msg.text.replace("Han1 rename ","")
                    if len(string.decode('utf-8')) <= 20:
                        profile_B = ki.getProfile()
                        profile_B.displayName = string
                        ki.updateProfile(profile_B)
                        ki.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Uk2 rename "]:
                if msg.from_ in admin:
                    string = msg.text.replace("Han2 rename ","")
                    if len(string.decode('utf-8')) <= 20:
                        profile_B = kk.getProfile()
                        profile_B.displayName = string
                        kk.updateProfile(profile_B)
                        kk.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Mc "]:
                if msg.from_ in admin:
                    mmid = msg.text.replace("Mc ","")
                    msg.contentType = 13
                    msg.contentMetadata = {"mid":mmid}
                    cl.sendMessage(msg)
            elif msg.text in ["Sticker on","Sticker:on"]:
                if msg.from_ in admin:
                    wait['sticker'] = True
                    cl.sendText(msg.to,"Sticker Info On")
            elif msg.text in ["Sticker off","Sticker:off"]:
                if msg.from_ in admin:
                    wait['sticker'] = False
                    cl.sendText(msg.to,"Sticker Info Off")
            elif msg.text in ["Simisimi on","Simisimi:on"]:
                if msg.from_ in admin:
                    settings["simiSimi"][msg.to] = True
                    cl.sendText(msg.to,"Simi mode On")
            elif msg.text in ["Simisimi off","Simisimi:off"]:
                if msg.from_ in admin:
                    settings["simiSimi"][msg.to] = False
                    cl.sendText(msg.to,"Simi mode Off")
            elif msg.text in ["Autoread on","Read on"]:
                if msg.from_ in admin:
                    wait['alwayRead'] = True
                    cl.sendText(msg.to,"Auto read On")
            elif msg.text in ["Autoread off","Read off"]:
                if msg.from_ in admin:
                    wait['alwayRead'] = False
                    cl.sendText(msg.to,"Auto read Off")
            elif msg.text in ["Kicktag on","Autokick:on"]:
                if msg.from_ in admin:
                    wait["kickMention"] = True
                    cl.sendText(msg.to,"Auto Kick tag ON")
            elif msg.text in ["Kicktag off","Autokick:off"]:
                if msg.from_ in admin:
                    wait["kickMention"] = False
                    cl.sendText(msg.to,"Auto Kick tag OFF")
            elif msg.text in ["Welcome on","WC:on"]:
                if msg.from_ in admin:
                    wait["WC"] = True
                    cl.sendText(msg.to,"Welcome On")
            elif msg.text in ["Welcome off","WC:off"]:
                if msg.from_ in admin:
                    wait["WC"] = False
                    cl.sendText(msg.to,"Welcome Off")
            elif msg.text in ["Good Bye On","Gbye:on"]:
                if msg.from_ in admin:
                    wait["Gbye"] = True
                    cl.sendText(msg.to,"Good Bye On")
            elif msg.text in ["Good Bye Off","Gbye:off"]:
                if msg.from_ in admin:
                    wait["Gbye"] = False
                    cl.sendText(msg.to,"Good Bye On")
            elif msg.text in ["QM:on"]:
                if msg.from_ in admin:
                    wait["QrMessage"] = True
                    cl.sendText(msg.to,"Qr Message On")
            elif msg.text in ["QM:off"]:
                if msg.from_ in admin:
                    wait["QM"] = False
                    cl.sendText(msg.to,"Qr Message Off")
            elif msg.text in ["Respon Tag On","RTag:on"]:
              if msg.from_ in admin:
                if wait["detectMention"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Respon Tag On")
                    else:
                        cl.sendText(msg.to,"Sudah On")
                else:
                    wait["detectMention"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Respon Tag On")
                    else:
                        cl.sendText(msg.to,"Sudah On")
            elif msg.text in ["Respon Tag Off","RTag:off"]:
              if msg.from_ in admin:
                if wait["detectMention"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Respon Tag Off")
                    else:
                        cl.sendText(msg.to,"Sudah Off")
              else:
                  wait["detectMention"] = False
                  if wait["lang"] == "JP":
                      cl.sendText(msg.to,"Auto Respon Tag Off")
                  else:
                      cl.sendText(msg.to,"Sudah Off")
            elif msg.text in ["Set:blockinvite:on","set:blockinvite:on"]:
              if msg.from_ in admin:
                if wait["Protectguest"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Block Invite On")
                    else:
                        cl.sendText(msg.to,"Kelar")
                else:
                    wait["Protectguest"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Block Invite On")
                    else:
                        cl.sendText(msg.to,"Kelar")
            elif msg.text in ["Set:blockinvite:off","set:blockinvite:off"]:
              if msg.from_ in admin:
                if wait["Protectguest"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Block Invite Off")
                    else:
                        cl.sendText(msg.to,"Kelar")
                else:
                    wait["Protectguest"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Block Invite Off")
                    else:
                        cl.sendText(msg.to,"Kelar")
            elif msg.text in ["Protect qr on","protect qr on"]:
              if msg.from_ in admin:
                if wait["ProtectQR"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR On")
                    else:
                        cl.sendText(msg.to,"Kelar")
                else:
                    wait["ProtectQR"] == True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR On")
                    else:
                        cl.sendText(msg.to,"Kelar")
            elif msg.text in ["Protect qr off","protect  qr off"]:
              if msg.from_ in admin:
                if wait["ProtectQR"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Off")
                    else:
                        cl.sendText(msg.to,"Kelar")
                else:
                    wait["ProtectQR"] == False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Off")
                    else:
                        cl.sendText(msg.to,"Kelar")
            elif msg.text in ["Protect cancel on","protect cancel on"]:
              if msg.from_ in admin:
                if wait["Protectcancel"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Cancel On")
                    else:
                        cl.sendText(msg.to,"Sudah On")
                else:
                    wait["Protectcancel"] == True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Cancel On")
                    else:
                        cl.sendText(msg.to,"Sudah On")
            elif msg.text in ["Protect cancel off","protect cancel off"]:
              if msg.from_ in admin:
                if wait["Protectcancel"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Cancel Off")
                    else:
                        cl.sendText(msg.to,"Sudah Off")
                else:
                    wait["Protectcancel"] == False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Cancel Off")
                    else:
                        cl.sendText(msg.to,"Sudah Off")
            elif msg.text in ["Backup","backup"]:
                if msg.from_ in admin:
                    try:
                        cl.updateDisplayPicture(backup.pictureStatus)
                        cl.updateProfile(backup)
                        cl.sendText(msg.to, "Backup Succes")
                    except Exception as e:
                        cl.sendText(msg.to, str(e))
            elif msg.text in ["é€£çµ¡å…ˆ:ã‚ªãƒ³","K on","Contact on","é¡¯ç¤ºï¼šé–‹"]:
                if msg.from_ in admin:
                  if wait["contact"] == True:
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"already on")
                      else:
                          cl.sendText(msg.to,"done")
                  else:
                      wait["contact"] = True
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"already on")
                      else:
                          cl.sendText(msg.to,"done")
            elif msg.text in ["é€£çµ¡å…ˆ:ã‚ªãƒ•","K off","Contact off","é¡¯ç¤ºï¼šé—œ"]:
                if msg.from_ in admin:
                  if wait["contact"] == False:
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"already off")
                      else:
                          cl.sendText(msg.to,"done ")
                  else:
                      wait["contact"] = False
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"already off")
                      else:
                          cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å‚åŠ :ã‚ªãƒ³","Join on","Auto join:on","è‡ªå‹•åƒåŠ ï¼šé–‹"]:
                if msg.from_ in admin:
                    if wait["autoJoin"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already on")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["autoJoin"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already on")
                        else:
                            cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å‚åŠ :ã‚ªãƒ•","Join off","Auto join:off","è‡ªå‹•åƒåŠ ï¼šé—œ"]:
                if msg.from_ in admin:
                    if wait["autoJoin"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already off")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["autoJoin"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already off")
                        else:
                            cl.sendText(msg.to,"done")
            elif msg.text in ["Gcancel:"]:
                if msg.from_ in admin:
                    try:
                        strnum = msg.text.replace("Gcancel:","")
                        if strnum == "off":
                            wait["autoCancel"]["on"] = False
                            if wait["lang"] == "JP":
                                cl.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                            else:
                                cl.sendText(msg.to,"å…³äº†é‚€è¯·æ‹’ç»ã€‚è¦æ—¶å¼€è¯·æŒ‡å®šäººæ•°å‘é€")
                        else:
                            num =  int(strnum)
                            wait["autoCancel"]["on"] = True
                            if wait["lang"] == "JP":
                                cl.sendText(msg.to,strnum + "The group of people and below decided to automatically refuse invitation")
                            else:
                                cl.sendText(msg.to,strnum + "ä½¿äººä»¥ä¸‹çš„å°ç»„ç”¨è‡ªåŠ¨é‚€è¯·æ‹’ç»")
                    except:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Value is wrong")
                        else:
                            cl.sendText(msg.to,"Bizarre ratings")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ³","Leave on","Auto leave:on","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé–‹"]:
                if msg.from_ in admin:
                    if wait["leaveRoom"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already on")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["leaveRoom"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"done")
                        else:
                            cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ•","Leave off","Auto leave:off","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé—œ"]:
                if msg.from_ in admin:
                    if wait["leaveRoom"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already off")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["leaveRoom"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"done")
                        else:
                            cl.sendText(msg.to,"already")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ³","Share on","Share on"]:
                if msg.from_ in admin:
                    if wait["timeline"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already on")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["timeline"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"done")
                        else:
                            cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ•","Share off","Share off"]:
                if msg.from_ in admin:
                    if wait["timeline"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already off")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["timeline"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"done")
                        else:
                            cl.sendText(msg.to,"è¦äº†å…³æ–­ã€‚")
            elif msg.text in ["Settings"]:
                if msg.from_ in admin:
                    md = ""
                    if wait["sticker"] == True: md+="🛡 Sticker Info : ✔\n"
                    else: md+="🛡 Sticker Info : ❌\n"
                    if wait["alwayRead"] == True: md+="🛡 Auto Read : ✔\n"
                    else: md+="🛡 Auto Read : ❌\n"
                    if wait["WC"] == True: md+="🛡 Welcome : ✔\n"
                    else: md+="🛡 Welcome : ❌\n"
                    if wait["Gbye"] == True: md+="🛡 Good Bye : ✔\n"
                    else: md+="🛡 Good Bye : ❌\n"
                    if wait["QrMessage"] == True: md+="🛡 Qr Message : ✔\n"
                    else: md+="🛡 Qr Message : ❌\n"
                    if wait["kickMention"] == True: md+="🛡 Kick Mention : ✔\n"
                    else: md+="🛡 Kick Mention : ❌\n"
                    if wait["detectMention"] == True: md+="🛡 Auto Respon Tag : ✔\n"
                    else: md+="🛡 Auto Respon Tag : ❌\n"
                    if wait["Protectcancel"] == True: md+="🛡 Protect Cancel : ✔\n"
                    else: md+="🛡 Protect Cancel : ❌\n"
                    if wait["ProtectQR"] == True: md+="🛡 Protect Qr : ✔\n"
                    else: md+="🛡 Protect Qr : ❌\n"
                    if wait["Protectguest"] == True: md+="🛡 Block Invite : ✔\n"
                    else: md+="🛡 Block Invite : ❌\n"
                    if wait["contact"] == True: md+="🛡 Contact : ✔\n"
                    else: md+="🛡 Contact : ❌\n"
                    if wait["autoJoin"] == True: md+="🛡 Auto join : ✔\n"
                    else: md+="🛡 Auto join : ❌\n"
                    if wait["autoCancel"]["on"] == True:md+="🛡 Group cancel :" + str(wait["autoCancel"]["members"]) + "\n"
                    else: md+="🛡 Group cancel : ❌\n"
                    if wait["leaveRoom"] == True: md+="🛡 Auto leave : ✔\n"
                    else: md+="🛡 Auto leave : ❌\n"
                    if wait["timeline"] == True: md+="🛡 Share : ✔\n"
                    else: md+="🛡 Share : ❌\n"
                    if wait["autoAdd"] == True: md+="🛡 Auto add : ✔\n"
                    else: md+="🛡 Auto add : ❌\n"
                    if wait3["commentOn"] == True: md+="🛡 Comment : ✔\n"
                    else: md+="🛡 Comment : ❌\n"
                    cl.sendText(msg.to,md)
            elif "album merit " in msg.text:
                gid = msg.text.replace("album merit ","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"There is no album")
                    else:
                        cl.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç›¸å†Œ"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
                    cl.sendText(msg.to,mg)
            elif "album " in msg.text:
                if msg.from_ in admin:
                    gid = msg.text.replace("album ","")
                    album = cl.getAlbum(gid)
                    if album["result"]["items"] == []:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"There is no album")
                        else:
                            cl.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
                    else:
                        if wait["lang"] == "JP":
                            mg = "The following is the target album"
                        else:
                            mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç›¸å†Œ"
                        for y in album["result"]["items"]:
                            if "photoCount" in y:
                                mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                            else:
                                mg += str(y["title"]) + ":0sheet\n"
            elif "album remove " in msg.text:
                if msg.from_ in admin:
                    gid = msg.text.replace("album remove ","")
                    albums = cl.getAlbum(gid)["result"]["items"]
                    i = 0
                    if albums != []:
                        for album in albums:
                            cl.deleteAlbum(gid,album["id"])
                            i += 1
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,str(i) + "Deleted albums")
                    else:
                        cl.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
            elif msg.text in ["Group id","ç¾¤çµ„å…¨id"]:
                if msg.from_ in admin:
                    gid = cl.getGroupIdsJoined()
                    h = ""
                    for i in gid:
                        h += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                    cl.sendText(msg.to,h)
            elif msg.text in ["Cancelall"]:
                if msg.from_ in admin:
                    gid = cl.getGroupIdsInvited()
                    for i in gid:
                        cl.rejectGroupInvitation(i)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"All invitations have been refused")
                    else:
                        cl.sendText(msg.to,"æ‹’ç»äº†å…¨éƒ¨çš„é‚€è¯·ã€‚")
            elif "album removeâ†’" in msg.text:
                if msg.from_ in admin:
                    gid = msg.text.replace("album removeâ†’","")
                    albums = cl.getAlbum(gid)["result"]["items"]
                    i = 0
                    if albums != []:
                        for album in albums:
                            cl.deleteAlbum(gid,album["id"])
                            i += 1
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,str(i) + "Albums deleted")
                    else:
                        cl.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ³","Add on","Auto add:on","è‡ªå‹•è¿½åŠ ï¼šé–‹"]:
                if msg.from_ in admin:
                    if wait["autoAdd"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already on")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["autoAdd"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"done")
                        else:
                            cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ•","Add off","Auto add:off","è‡ªå‹•è¿½åŠ ï¼šé—œ"]:
                if msg.from_ in admin:
                    if wait["autoAdd"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already off")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["autoAdd"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"done")
                        else:
                            cl.sendText(msg.to,"è¦äº†å…³æ–­ã€‚")
            elif "Message change: " in msg.text:
                if msg.from_ in admin:
                    wait["message"] = msg.text.replace("Message change: ","")
                    cl.sendText(msg.to,"message changed")
            elif "Message add: " in msg.text:
                if msg.from_ in admin:
                    wait["message"] = msg.text.replace("Message add: ","")
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"message changed")
                    else:
                        cl.sendText(msg.to,"doneã€‚")
            elif msg.text in ["Message","è‡ªå‹•è¿½åŠ å•å€™èªžç¢ºèª"]:
                if msg.from_ in admin:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"message change to\n\n" + wait["message"])
                    else:
                        cl.sendText(msg.to,"The automatic appending information is set as followsã€‚\n\n" + wait["message"])
            elif "Comment:" in msg.text:
                if msg.from_ in admin:
                    c = msg.text.replace("Comment:","")
                    if c in [""," ","\n",None]:
                        cl.sendText(msg.to,"message changed")
                    else:
                        wait["comment"] = c
                        cl.sendText(msg.to,"changed\n\n" + c)
            elif "Add comment:" in msg.text:
                if msg.from_ in admin:
                    c = msg.text.replace("Add comment:","")
                    if c in [""," ","\n",None]:
                        cl.sendText(msg.to,"String that can not be changed")
                    else:
                        wait["comment"] = c
                        cl.sendText(msg.to,"changed\n\n" + c)
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ³","Comment on","Comment:on","è‡ªå‹•é¦–é ç•™è¨€ï¼šé–‹"]:
                if msg.from_ in admin:
                    if wait["commentOn"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"done")
                        else:
                            cl.sendText(msg.to,"already on")
                    else:
                        wait["commentOn"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"done")
                        else:
                            cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ•","Comment on","Comment off","è‡ªå‹•é¦–é ç•™è¨€ï¼šé—œ"]:
                if msg.from_ in admin:
                    if wait["commentOn"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"done")
                        else:
                            cl.sendText(msg.to,"already off")
                    else:
                        wait["commentOn"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"done")
                        else:
                            cl.sendText(msg.to,"è¦äº†å…³æ–­ã€‚")
            elif msg.text in ["Comment","ç•™è¨€ç¢ºèª"]:
                if msg.from_ in admin:
                    cl.sendText(msg.to,"message changed to\n\n" + str(wait["comment"]))
            elif msg.text in ["Gurl"]:
                if msg.from_ in admin:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Uk1 gurl"]:
                if msg.from_ in admin:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        ki.updateGroup(x)
                    gurl = ki.reissueGroupTicket(msg.to)
                    ki.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Uk2 gurl"]:
                if msg.from_ in admin:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        kk.updateGroup(x)
                    gurl = kk.reissueGroupTicket(msg.to)
                    kk.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Uk3 gurl"]:
                if msg.from_ in admin:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        kc.updateGroup(x)
                    gurl = kc.reissueGroupTicket(msg.to)
                    kc.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Comment bl "]:
                if msg.from_ in admin:
                    wait["wblack"] = True
                    cl.sendText(msg.to,"add to comment bl")
            elif msg.text in ["Comment wl "]:
                if msg.from_ in admin:
                    wait["dblack"] = True
                    cl.sendText(msg.to,"wl to comment bl")
            elif msg.text in ["Comment bl confirm"]:
                if msg.from_ in admin:
                    if wait["commentBlack"] == {}:
                        cl.sendText(msg.to,"confirmed")
                    else:
                        cl.sendText(msg.to,"Blacklist")
                        mc = ""
                        for mi_d in wait["commentBlack"]:
                            mc += "" +cl.getContact(mi_d).displayName + "\n"
                        cl.sendText(msg.to,mc)
            elif msg.text in ["Jam on"]:
                if msg.from_ in admin:
                    if wait["clock"] == True:
                        cl.sendText(msg.to,"already on")
                    else:
                        wait["clock"] = True
                        now2 = datetime.now()
                        nowT = datetime.strftime(now2,"(%H:%M)")
                        profile = cl.getProfile()
                        profile.displayName = wait["cName"] + nowT
                        cl.updateProfile(profile)
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Jam off"]:
                if msg.from_ in admin:
                    if wait["clock"] == False:
                        cl.sendText(msg.to,"already off")
                    else:
                        wait["clock"] = False
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Change clock "]:
                if msg.from_ in admin:
                    n = msg.text.replace("Change clock ","")
                    if len(n.decode("utf-8")) > 13:
                        cl.sendText(msg.to,"changed")
                    else:
                        wait["cName"] = n
                        cl.sendText(msg.to,"changed to\n\n" + n)
            elif msg.text in ["Up"]:
                if msg.from_ in admin:
                    if wait["clock"] == True:
                        now2 = datetime.now()
                        nowT = datetime.strftime(now2,"(%H:%M)")
                        profile = cl.getProfile()
                        profile.displayName = wait["cName"] + nowT
                        cl.updateProfile(profile)
                        cl.sendText(msg.to,"Jam Update")
                    else:
                        cl.sendText(msg.to,"Please turn on the name clock")

            elif msg.text == "Setlastpoint":
                if msg.from_ in admin:
                    cl.sendText(msg.to, "Set the lastseens' point(｀・ω・´)")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    now2 = datetime.now()
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                    wait2['ROM'][msg.to] = {}
                    print wait2
            elif msg.text == "Viewlastseen":
                if msg.from_ in admin:
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"

                        cl.sendText(msg.to, "People who readed %s\nthat's it\n\nPeople who have ignored reads\n%sIt is abnormal ♪\n\nReading point creation date n time:\n[%s]"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendText(msg.to, "An already read point has not been set.\n「set」you can send ♪ read point will be created ♪")


#-----------------------------------------------

#-----------------------------------------------

            elif msg.text in ["Uk cam"]:
                if msg.from_ in admin:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        kh.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        kg.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        ka.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        kd.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        G = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        cl.sendText(msg.to,"Hallo %s" % str(group.name))
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        cl.updateGroup(G)
                        cl.sendText(msg.to,"Hallo %s" % str(group.name))

            elif msg.text in ["Uk1 join"]:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  ki.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = kk.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ki.updateGroup(G)
                  Ticket = kk.reissueGroupTicket(msg.to)

            elif msg.text in ["Uk2 join"]:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  kk.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = ki.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  kk.updateGroup(G)
                  Ticket = kk.reissueGroupTicket(msg.to)

#-----------------------------------------------
#.acceptGroupInvitationByTicket(msg.to,Ticket)
            elif msg.text in ["Uk3 join"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                        print "kicker ok"
                        G.preventJoinByTicket = True
                        kc.updateGroup(G)

            elif msg.text in ["Uk4 join"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        kh.acceptGroupInvitationByTicket(msg.to,Ticket)
                        print "kicker ok"
                        G.preventJoinByTicket = True
                        kh.updateGroup(G)

            elif msg.text in ["Uk5 join"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        kg.acceptGroupInvitationByTicket(msg.to,Ticket)
                        print "kicker ok"
                        G.preventJoinByTicket = True
                        kg.updateGroup(G)

            elif msg.text in ["Uk6 join"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ka.acceptGroupInvitationByTicket(msg.to,Ticket)
                        print "kicker ok"
                        G.preventJoinByTicket = True
                        ka.updateGroup(G)

            elif msg.text in ["Uk7 join"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                        print "kicker ok"
                        G.preventJoinByTicket = True
                        kb.updateGroup(G)

            elif msg.text in ["Uk8 join"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        kd.acceptGroupInvitationByTicket(msg.to,Ticket)
                        print "kicker ok"
                        G.preventJoinByTicket = True
                        kd.updateGroup(G)

            elif msg.text in ["Uk9 join"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                        print "kicker ok"
                        G.preventJoinByTicket = True
                        ke.updateGroup(G)
#-----------------------------------------------
            elif msg.text in ["Uk out"]:
                if msg.from_ in admin:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                        kk.leaveGroup(msg.to)
                        kc.leaveGroup(msg.to)
                        kh.leaveGroup(msg.to)
                        kg.leaveGroup(msg.to)
                        ka.leaveGroup(msg.to)
                        kb.leaveGroup(msg.to)
                        kd.leaveGroup(msg.to)
                        ke.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Jinlip"]:
                if msg.from_ in admin:
                    ginfo = cl.getGroup(msg.to)
                    msg.contentType = 7
                    msg.text = None
                    msg.contentMetadata = {
                                         "STKID": "18687405",
                                         "STKPKGID": "1520987",
                                         "STKVER": "1" }
                    cl.sendMessage(msg)
                    try:
                        cl.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Uk1 bye"]:
                if msg.from_ in admin:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Uk2 bye"]:
                if msg.from_ in admin:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kk.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Uk3 bye"]:
                if msg.from_ in admin:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kc.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Uk4 bye"]:
                if msg.from_ in admin:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kh.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Uk5 bye"]:
                if msg.from_ in admin:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kg.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Uk6 bye"]:
                if msg.from_ in admin:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ka.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Han7 bye"]:
                if msg.from_ in admin:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kb.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Uk8 bye"]:
                if msg.from_ in admin:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kd.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Uk9 bye"]:
                if msg.from_ in admin:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ke.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Bye 2"]:
                if msg.from_ in admin:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                        kk.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Cv1 @bye"]:
                if msg.from_ in admin:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Cv2 @bye"]:
                if msg.from_ in admin:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kk.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Cv3 @bye"]:
                if msg.from_ in admin:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kc.leaveGroup(msg.to)
                    except:
                        pass
#----------------------------------------
            elif "Copy " in msg.text:
              if msg.from_ in admin:
                  if msg.toType == 2:
                   targets = []
                  key = eval(msg.contentMetadata["MENTION"])
                  key["MENTIONEES"][0]["M"]
                  for x in key["MENTIONEES"]:
                      targets.append(x["M"])
                  for target in targets:
                      try:
                          contact = cl.getContact(target)
                          X = contact.displayName
                          profile = cl.getProfile()
                          profile.displayName = X
                          cl.updateProfile(profile)
                          cl.sendText(msg.to, "Success")
                          #------------------------------------------------
                          Y = contact.statusMessage
                          lol = cl.getProfile()
                          lol.statusMessage = Y
                          cl.updateProfile(lol)
                          #------------------------------------------------
                          P = contact.pictureStatus
                          cl.updateProfilePicture(P)
                      except Exception as e:
                          cl.sendText(msg.to, "failed")
                          print e


            elif "Mycopy @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace("Mycopy @","")
                        _nametarget = _name.rstrip(' ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "Tidak Ada Target Copy")
                        else:
                            for target in targets:
                                try:
                                    cl.cloneContactProfile(target)
                                    cl.sendText(msg.to, "Sukses Copy Profile")
                                except Exception as e:
                                    print e



            elif msg.text in ["Mybackup"]:
                try:
                    cl.updateDisplayPicture(mybackup.pictureStatus)
                    cl.updateProfile(mybackup)
                    cl.sendText(msg.to, "Backup Sukses Bosqu")
                except Exception as e:
                    cl.sendText(msg.to, str (e))

#================================================

            elif "Copy @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace("Copy @","")
                        _nametarget = _name.rstrip(' ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "Tidak Ada Target Copy")
                        else:
                            for target in targets:
                                try:
                                    ki.cloneContactProfile(target)
                                    kk.cloneContactProfile(target)
                                    kc.cloneContactProfile(target)
                                    kh.cloneContactProfile(target)
                                    kg.cloneContactProfile(target)
                                    ka.cloneContactProfile(target)
                                    kb.cloneContactProfile(target)
                                    kd.cloneContactProfile(target)
                                    ke.cloneContactProfile(target)
                                    cl.sendText(msg.to, "Sukses Copy Profile")
                                except Exception as e:
                                    print e




            elif msg.text in ["Kembali"]:
                try:
                    ki.updateDisplayPicture(backup.pictureStatus)
                    ki.updateProfile(backup)
                    kk.updateDisplayPicture(backup.pictureStatus)
                    kk.updateProfile(backup)
                    kc.updateDisplayPicture(backup.pictureStatus)
                    kc.updateProfile(backup)
                    kh.updateDisplayPicture(backup.pictureStatus)
                    kh.updateProfile(backup)
                    kg.updateDisplayPicture(backup.pictureStatus)
                    kg.updateProfile(backup)
                    ka.updateDisplayPicture(backup.pictureStatus)
                    ka.updateProfile(backup)
                    kb.updateDisplayPicture(backup.pictureStatus)
                    kb.updateProfile(backup)
                    kd.updateDisplayPicture(backup.pictureStatus)
                    kd.updateProfile(backup)
                    ke.updateDisplayPicture(backup.pictureStatus)
                    ke.updateProfile(backup)
                    cl.sendText(msg.to, "Backup Sukses Bosqu")
                except Exception as e:
                    cl.sendText(msg.to, str (e))

#----------------------------------------
            elif ("Ban " in msg.text):
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      wait3["blacklist"][target] = True
                      with open('bl.json', 'w') as fp:
                           json.dump(wait3, fp, sort_keys=True, indent=4)
                      cl.sendText(msg.to,"Succes Banned")
                   except:
                      pass
#----------------------------------------
            elif ("Unban " in msg.text):
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      del wait3["blacklist"][target]
                      with open('bl.json', 'w') as fp:
                           json.dump(wait3, fp, sort_keys=True, indent=4)
                      cl.sendText(msg.to,"Succes UnBanned")
                   except:
                      pass
#----------------------------------------
            elif ("Bye " in msg.text):
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      cl.kickoutFromGroup(msg.to,[target])
                   except:
                      pass
#----------------------------------------
            elif msg.text in ["Kick on","kick on","Kickall","kickall","Kick all","kick all","Cleanse","cleanse","Nuke","nuke",".Kick on"]:
                    try:
                        cl.sendText(msg.to,"Mau ngapain?")
                        cl.kickoutFromGroup(msg.to,[msg.from_])
                    except:
                        pass

#----------------------------------------
            elif "Gift @" in msg.text:
                if msg.from_ in admin:
                    _name = msg.text.replace("Gift @","")
                    _nametarget = _name.rstrip(' ')
                    gs = cl.getGroup(msg.to)
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            msg.contentType = 9
                            msg.contentMetadata={'PRDID':'89131c1a-e549-4bd5-9e60-e24de0d2e252',
                                                 'PRDTYPE': 'THEME',
                                                 'MSGTPL': '10'}
                            msg.text = None
                            cl.sendMessage(msg,g)
#----------------------------------------
            elif "Mid @" in msg.text:
                if msg.from_ in admin:
                    _name = msg.text.replace("Mid @","")
                    _nametarget = _name.rstrip(' ')
                    gs = cl.getGroup(msg.to)
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            cl.sendText(msg.to, g.mid)
                        else:
                            pass
#----------------------------------------
            elif "Spam " in msg.text:
               if msg.from_ in admin:
                txt = msg.text.split(" ")
                jmlh = int(txt[2])
                teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+" ","")
                tulisan = jmlh * (teks+"\n")
                 #@rid1bdbx
                if txt[1] == "on":
                    if jmlh <= 1000:
                        for x in range(jmlh):
                            cl.sendText(msg.to, teks)
                    else:
                       cl.sendText(msg.to, "Kelebihan batas:v")
                elif txt[1] == "off":
                    if jmlh <= 1000:
                        cl.sendText(msg.to, tulisan)
                    else:
                        cl.sendText(msg.to, "Kelebihan batas :v")
#----------------------------------------
            if "Gbc: " in msg.text:
              if msg.from_ in admin:
                print "Berhasil BC ke Semua Grup"
                bctxt = msg.text.replace("Gbc : ","")
                n = cl.getGroupIdsJoined()
                for people in n:
                    cl.sendText(people, (bctxt))
                    
            if "Fbc: " in msg.text:
              if msg.from_ in admin:
                print "BroadCast Ke Semua Teman Berhasil"
                bctxt = msg.text.replace("Fbc: ","")
                n = ki.getAllContactIds()
                for people in n:
                    ki.sendText(people, (bctxt))
#----------------------------------------
            elif msg.text in ["Gcreator:inv"]:
              if msg.from_ in admin:    
                if msg.toType == 2:
                   ginfo = cl.getGroup(msg.to)
                   gCreator = ginfo.creator.mid
                   try:
                      cl.findAndAddContactsByMid(gCreator)
                      cl.inviteIntoGroup(msg.to,[gCreator])
                      print "Berhasil Invite Pembuat Grup"
                   except:
                      pass                        
#----------------------------------------
            elif "Uk:groupcreator" == msg.text:
                if msg.from_ in admin:
                            try:
                                group = cl.getGroup(msg.to)
                                GS = group.creator.mid
                                M = Message()
                                M.to = msg.to
                                M.contentType = 13
                                M.contentMetadata = {'mid': GS}
                                cl.sendMessage(M)
                            except:
                                W = group.members[0].mid
                                M = Message()
                                M.to = msg.to
                                M.contentType = 13
                                M.contentMetadata = {'mid': W}
                                cl.sendMessage(M)
                                cl.sendText(msg.to,"old user")

#----------------------------------------
            elif msg.text in ["Backup","backup"]:
                if msg.from_ in admin:
                    try:
                       cl.updateDisplayPicture(backup.pictureStatus)
                       cl.updateProfile(backup)
                    except Exception as e:
                       cl.sendText(msg.to, str(e))
#----------------------------------------
            elif msg.text in ["Uk:creator"]:
                if msg.toType == 2:
                      msg.contentType = 13
                      Creatorbot = "udee46099e25e71f1fd1817cae9e7c429"
                      try:
                          msg.contentMetadata = {'mid': Creatorbot}
                      except:
                        Creatorbot = "Error"
                      ki.sendText(msg.to, "My Creator : Uk_morayena")
                      ki.sendMessage(msg)
#----------------------------------------
            elif msg.text in ["Tag"]:
              if msg.from_ in admin:
                group = cl.getGroup(msg.to)
                nama = [contact.mid for contact in group.members]
                cb = ""
                cb2 = ""
                strt = int(0)
                akh = int(0)
                for md in nama:
                    akh = akh + int(5)
                    cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                    strt = strt + int(6)
                    akh = akh + 1
                    cb2 += "@nrik\n"
                cb = (cb[:int(len(cb)-1)])
                msg.contentType = 0
                msg.text = cb2
                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                try:
                    cl.sendMessage(msg)
                except Exception as error:
                    print error

    
            elif msg.text in ["Friendlist"]:
                if msg.from_ in admin:
                    contactlist = cl.getAllContactIds()
                    kontak = cl.getContacts(contactlist)
                    num=1
                    msgs="═════════List Friend═════════"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.displayName)
                        num=(num+1)
                    msgs+="\n═════════List Friend═════════\n\nTotal Friend : %i" % len(kontak)
                    cl.sendText(msg.to, msgs)
                    
            elif msg.text.lower() == '.....':
                if msg.from_ in admin:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "udee46099e25e71f1fd1817cae9e7c429',"}
                    cl.sendMessage(msg)        
                    
            elif msg.text in ["Memlist"]:
                if msg.from_ in admin:
                    kontak = cl.getGroup(msg.to)
                    group = kontak.members
                    num=1
                    msgs="═════════List Member═════════-"
                    for ids in group:
                        msgs+="\n[%i] %s" % (num, ids.displayName)
                        num=(num+1)
                    msgs+="\n═════════List Member═════════\n\nTotal Members : %i" % len(group)
                    cl.sendText(msg.to, msgs)
                
            elif msg.text in ["Gruplist"]:
                if msg.from_ in admin:
                    gruplist = cl.getGroupIdsJoined()
                    kontak = cl.getGroups(gruplist)
                    num=1
                    msgs="═════════List Grup═════════"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.name)
                        num=(num+1)
                    msgs+="\n═════════List Grup═════════\n\nTotal Grup : %i" % len(kontak)
                    cl.sendText(msg.to, msgs)    
#-----------------------------------------------
            elif msg.text in ["Kill"]:
                if msg.from_ in admin:
                    group = ki.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait3["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        kk.sendText(msg.to,"Fuck You")
                        kc.sendText(msg.to,"Fuck You")
                        return
                    for jj in matched_list:
                        try:
                            klist=[ki,kk,kc,kh,kg,ka]
                            kicker=random.choice(klist)
                            kicker.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
            elif "Attack" in msg.text:
                if msg.from_ in admin:
                    print "ok"
                    _name = msg.text.replace("Attack","")
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = kh.getGroup(msg.to)
                    gs = kg.getGroup(msg.to)
                    gs = ka.getGroup(msg.to)
                    gs = kb.getGroup(msg.to)
                    gs = kd.getGroup(msg.to)
                    gs = ke.getGroup(msg.to)
                    ki.sendText(msg.to,"ASSASSIN PLAYER WAS HARE")
                    kk.sendText(msg.to,"JANGAN DI LIATIN DOANG")
                    kc.sendText(msg.to,"YAH RATA NIH KAYA TETE LU RATA")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found.")
                    else:
                        for target in targets:
                            if not target in admin and Bots:
                                try:
                                    klist=[ki,kk,kc,kh,kg,ka,kb,kd,ke]
                                    kicker=random.choice(klist)
                                    kicker.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    cl.sendText(msg.to,"Group Bersih")
            elif "Nk " in msg.text:
                  if msg.from_ in admin:
                       nk0 = msg.text.replace("Nk ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    klist=[cl,ki,kk,kc,kh,kg]
                                    kicker=random.choice(klist)
                                    kicker.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ki.sendText(msg.to,"Succes Han")
                                    kk.sendText(msg.to,"Fuck You")
#-----------------------------------------------           
            elif "Fb " in msg.text:
                if msg.from_ in admin:
                    a = msg.text.replace("Fb ","")
                    b = urllib.quote(a)
                    cl.sendText(msg.to,"「 Mencari 」\n" "Type:Mencari Info\nStatus: Proses")
                    cl.sendText(msg.to, "https://www.facebook.com" + b)
                    cl.sendText(msg.to,"「 Mencari 」\n" "Type:Mencari Info\nStatus: Sukses")

            elif "Image " in msg.text:
                if msg.from_ in admin:
                    search = msg.text.replace("Image ","")
                    url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                    raw_html = (download_page(url))
                    items = []
                    items = items + (_images_get_all_items(raw_html))
                    path = random.choice(items)
                    print path
                    try:
                        cl.sendImageWithURL(msg.to,path)
                    except:
                        pass
                    
            elif 'Youtubemp4 ' in msg.text:
                if msg.from_ in admin:
                    try:
                        textToSearch = (msg.text).replace('Youtubemp4 ', "").strip()
                        query = urllib.quote(textToSearch)
                        url = "https://www.youtube.com/results?search_query=" + query
                        response = urllib2.urlopen(url)
                        html = response.read()
                        soup = BeautifulSoup(html, "html.parser")
                        results = soup.find(attrs={'class': 'yt-uix-tile-link'})
                        ght = ('https://www.youtube.com' + results['href'])
                        cl.sendVideoWithURL(msg.to, ght)
                    except:
                        cl.sendText(msg.to, "Could not find it")

            elif "Yt " in msg.text:
                if msg.from_ in admin:
                    query = msg.text.replace("Yt ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'http://www.youtube.com/results'
                        params = {'search_query': query}
                        r = s.get(url, params=params)
                        soup = BeautifulSoup(r.content, 'html5lib')
                        hasil = ""
                        for a in soup.select('.yt-lockup-title > a[title]'):
                            if '&list=' not in a['href']:
                                hasil += ''.join((a['title'],'\nUrl : http://www.youtube.com' + a['href'],'\n\n'))
                        cl.sendText(msg.to,hasil)
                        print '[Command] Youtube Search'


            elif "youtube:" in msg.text.lower():
                if msg.from_ in admin:
                   query = msg.text.split(":")
                   try:
                       if len(query) == 3:
                           isi = yt(query[2])
                           hasil = isi[int(query[1])-1]
                           cl.sendText(msg.to, hasil)
                       else:
                           isi = yt(query[1])
                           cl.sendText(msg.to, isi[0])
                   except Exception as e:
                       cl.sendText(msg.to, str(e))

            elif "Lirik " in msg.text:
                if msg.from_ in admin:
                    try:
                        songname = msg.text.lower().replace("Lirik ","")
                        params = {'songname': songname}
                        r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                        data = r.text
                        data = json.loads(data)
                        for song in data:
                            hasil = 'Lyric Lagu ('
                            hasil += song[0]
                            hasil += ')\n\n'
                            hasil += song[5]
                            cl.sendText(msg.to, hasil)
                    except Exception as wak:
                            cl.sendText(msg.to, str(wak))
                        
            elif "Wikipedia " in msg.text:
                if msg.from_ in admin:
                  try:
                      wiki = msg.text.lower().replace("Wikipedia ","")
                      wikipedia.set_lang("id")
                      pesan="Title ("
                      pesan+=wikipedia.page(wiki).title
                      pesan+=")\n\n"
                      pesan+=wikipedia.summary(wiki, sentences=1)
                      pesan+="\n"
                      pesan+=wikipedia.page(wiki).url
                      cl.sendText(msg.to, pesan)
                  except:
                          try:
                              pesan="Over Text Limit! Please Click link\n"
                              pesan+=wikipedia.page(wiki).url
                              cl.sendText(msg.to, pesan)
                          except Exception as e:
                              cl.sendText(msg.to, str(e))
                              

            elif 'instagram ' in msg.text.lower():
              if msg.from_ in admin:
                try:
                    instagram = msg.text.lower().replace("instagram ","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/?')
                    soup = BeautifulSoup(html.text, 'html5lib')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    user = "Name: " + text[-2] + "\n"
                    user1 = "Username: " + text[-1] + "\n"
                    followers = "Followers: " + text[0] + "\n"
                    following = "Following: " + text[2] + "\n"
                    post = "Post: " + text[4] + "\n"
                    link = "Link: " + "https://www.instagram.com/" + instagram
                    detail = "====INSTAGRAM INFO USER====\n"
                    details = "\n====INSTAGRAM INFO USER===="
                    cl.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                    cl.sendImageWithURL(msg.to, text1[0])
                except Exception as njer:
                        cl.sendText(msg.to, str(njer))
                
            elif "google " in msg.text:
                if msg.from_ in admin:
                    a = msg.text.replace("google ","")
                    b = urllib.quote(a)
                    cl.sendText(msg.to,"Serching..")
                    cl.sendText(msg.to, "https://www.google.com/" + b)
                    cl.sendText(msg.to,"Done")
#-------------------------------------------------------------------------------
            elif msg.text in ["Mybio"]:
                if msg.from_ in admin:
                    h = cl.getContact(mid)
                    cl.sendText(msg.to,"===[StatusMessage]===\n" + h.statusMessage)
            elif msg.text in ["Mypict"]:
                if msg.from_ in admin:
                    h = cl.getContact(mid)
                    cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in ["Myvid"]:
                if msg.from_ in admin:
                    h = cl.getContact(mid)
                    cl.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in ["Urlpict"]:
                if msg.from_ in admin:
                    h = cl.getContact(mid)
                    cl.sendText(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in ["Mycover"]:
                if msg.from_ in admin:
                    h = cl.getContact(mid)
                    cu = cl.channel.getCover(mid)
                    path = str(cu)
                    cl.sendImageWithURL(msg.to, path)
            elif msg.text in ["Urlcover"]:
                if msg.from_ in admin:
                    h = cl.getContact(mid)
                    cu = cl.channel.getCover(mid)
                    path = str(cu)
                    cl.sendText(msg.to, path)
            elif "Getprofile" in msg.text:
                if msg.from_ in admin:
                    key = eval(msg.contentMetadata["MENTION"])
                    key1 = key["MENTIONEES"][0]["M"]
                    contact = cl.getContact(key1)
                    cu = cl.channel.getCover(key1)
                    path = str(cu)
                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                    try:
                        cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                        cl.sendText(msg.to,"Profile Picture " + contact.displayName)
                        cl.sendImageWithURL(msg.to,image)
                        cl.sendText(msg.to,"Cover " + contact.displayName)
                        cl.sendImageWithURL(msg.to,path)
                    except:
                        pass
            elif "Getcontact" in msg.text:
                if msg.from_ in admin:
                    key = eval(msg.contentMetadata["MENTION"])
                    key1 = key["MENTIONEES"][0]["M"]
                    mmid = cl.getContact(key1)
                    msg.contentType = 13
                    msg.contentMetadata = {"mid": key1}
                    cl.sendMessage(msg)
            elif "Getpict @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]dp executing"
                    _name = msg.text.replace("Getpict @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                contact = cl.getContact(target)
                                path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                cl.sendImageWithURL(msg.to, path)
                            except Exception as e:
                                raise e
                    print "[Command]dp executed"
            elif "Getvid @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]dp executing"
                    _name = msg.text.replace("Getvid @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                contact = cl.getContact(target)
                                path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                cl.sendVideoWithURL(msg.to, path)
                            except Exception as e:
                                raise e
                    print "[Command]dp executed"
            elif "Picturl @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]dp executing"
                    _name = msg.text.replace("Picturl @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                contact = cl.getContact(target)
                                path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                cl.sendText(msg.to, path)
                            except Exception as e:
                                raise e
                    print "[Command]dp executed"
            elif "Getcover @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]cover executing"
                    _name = msg.text.replace("Getcover @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                contact = cl.getContact(target)
                                cu = cl.channel.getCover(target)
                                path = str(cu)
                                cl.sendImageWithURL(msg.to, path)
                            except Exception as e:
                                raise e
                    print "[Command]cover executed"
            elif "Getgrup image" in msg.text:
                if msg.from_ in admin:
                    group = cl.getGroup(msg.to)
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    cl.sendImageWithURL(msg.to,path)
            elif "Urlgrup image" in msg.text:
                if msg.from_ in admin:
                    group = cl.getGroup(msg.to)
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    cl.sendText(msg.to,path)
#-------------------------------------------------------------------------------
            elif "Blacklist @ " in msg.text:
                 if msg.from_ in admin:
                     _name = msg.text.replace("Blacklist @ ","")
                     _kicktarget = _name.rstrip(' ')
                     gs = ki2.getGroup(msg.to)
                     targets = []
                     for g in gs.members:
                         if _kicktarget == g.displayName:
                            targets.append(g.mid)
                            if targets == []:
                                cl.sendText(msg.to,"Not found")
                            else:
                                for target in targets:
                                    try:
                                        wait3["blacklist"][target] = True
                                        f=codecs.open('bl.json','w','utf-8')
                                        json.dump(wait3["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                        k3.sendText(msg.to,"Succes Han")
                                    except:
                                        ki.sendText(msg.to,"error")
            elif "Ban @" in msg.text:
                if msg.from_ in admin:
                    print "[Ban]ok"
                    _name = msg.text.replace("Ban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = kh.getGroup(msg.to)
                    gs = kg.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found Han")
                    else:
                        for target in targets:
                            try:
                                wait3["wblacklist"] = True
                                with open('bl.json', 'w') as fp:
                                     json.load(wait3, fp, sort_keys= True, indent=4)
                                cl.sendText(msg.to,"Succes Han")
                            except:
                                cl.sendText(msg.to,"Error")
            elif "Unban @" in msg.text:
                if msg.from_ in admin:
                    print "[Unban]ok"
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = kh.getGroup(msg.to)
                    gs = kg.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found Han")
                    else:
                        for target in targets:
                            try:
                                wait3["dblacklist"] = True
                                with open('bl.json', 'w') as fp:
                                     json.load(wait3, fp, sort_keys= True, indent=4)
                                cl.sendText(msg.to,"Succes Han")
                            except:
                                ki.sendText(msg.to,"Succes Han")
#-----------------------------------------------
            elif msg.text in ["Han:version"]:
                ki.sendText(msg.to,"═══════Han Version═══════\nVersi saat ini 7.9.8 (Beta Version)\nlast updated 7 Januari 2018 1:35\n-----------------------------\nAuto Like:Error\n-----------------------------\nIP Admin:10.23.34.69\nAdmin Location:Jakarta Barat\n-----------------------------\nServer:Unknown")
                
            elif msg.text in ["Bug List"]:
                ki.sendText(msg.to,"═══════Bug List═══════\n1.Protect QR\n2.Ban By Tag\n3.Unban By Tag\n4.Auto Like\n5.Steal Video\n6.Steal Cover")
#-----------------------------------------------
            elif msg.text in ["Hallo Han"]:
                if msg.from_ in admin:
                    ki.sendText(msg.to,"Hallo Bos Rayhan")
                    kk.sendText(msg.to,"Hallo Bos Rayhan")
                    kc.sendText(msg.to,"Hallo Bos Rayhan")
                    kh.sendText(msg.to,"Hallo Bos Rayhan")
                    kg.sendText(msg.to,"Hallo Bos Rayhan")
                    ka.sendText(msg.to,"Hallo Bos Rayhan")
                    kb.sendText(msg.to,"Hallo Bos Rayhan")
                    kd.sendText(msg.to,"Hallo Bos Rayhan")
                    ke.sendText(msg.to,"Hallo Bos Rayhan")
#-----------------------------------------------
            elif "Bc " in msg.text:
                if msg.from_ in admin:
				bctxt = msg.text.replace("Bc ","")
				ki.sendText(msg.to,(bctxt))
				kk.sendText(msg.to,(bctxt))
				kc.sendText(msg.to,(bctxt))
                                kh.sendText(msg.to,(bctxt))
                                kg.sendText(msg.to,(bctxt))
                                ka.sendText(msg.to,(bctxt))
                                kb.sendText(msg.to,(bctxt))
                                kd.sendText(msg.to,(bctxt))
                                ke.sendText(msg.to,(bctxt))
#-----------------------------------------------
            elif 'music ' in msg.text.lower():
              if msg.from_ in admin:
                try:
                    songname = msg.text.lower().replace('music ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'This is Your Music\n'
                        hasil += 'Judul : ' + song[0]
                        hasil += '\nDurasi : ' + song[1]
                        hasil += '\nLink Download : ' + song[4]
                        cl.sendText(msg.to, hasil)
                        cl.sendText(msg.to, "Please Wait for audio...")
                        cl.sendAudioWithURL(msg.to, song[4])
                except Exception as njer:
                        cl.sendText(msg.to, str(njer))
                        
            elif "Say " in msg.text:
              if msg.from_ in admin:
                 psn = msg.text.replace("Say ","")
                 tts = gTTS(psn, lang='id', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')            

#===============================

            elif msg.text.lower() == 'cpu':
                if msg.from_ in admin:
                    botKernel = subprocess.Popen(["cat","/proc/cpuinfo"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO CPU===")
            elif msg.text.lower() == 'kernel':
                if msg.from_ in admin:
                    botKernel = subprocess.Popen(["uname","-srvmpio"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO KERNEL===")
            elif msg.text.lower() == 'system':
                if msg.from_ in admin:
                    botKernel = subprocess.Popen(["df","-h"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO SYSTEM===")
            elif msg.text.lower() == 'ifconfig':
                if msg.from_ in admin:
                    botKernel = subprocess.Popen(["ifconfig"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO NetStat===")
            elif msg.text.lower() == 'runtime':
                if msg.from_ in admin:
                    botKernel = subprocess.Popen(["runtime"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO IP===")
            elif msg.text.lower() == 'runtime':
                if msg.from_ in admin:
                    eltime = time.time() - mulai
                    van = "Bot sudah berjalan selama "+waktu(eltime)
                    cl.sendText(msg.to,van)
            elif msg.text.lower() == '.reboot':
                    print "[Command]Like executed"
                    try:
                        cl.sendText(msg.to,"Restarting...")
                        restart_program()
                    except:
                        cl.sendText(msg.to,"Please wait")
                        restart_program()
                        pass
#-----------------------------------------------
            elif "Apakah " in msg.text:
                tanya = msg.text.replace("Apakah ","")
                jawab = ("Ya","Tidak")
                jawaban = random.choice(jawab)
                ki.sendText(msg.to,jawaban)
#-----------------------------------------------
            elif ".Sp" in msg.text:
                if msg.from_ in admin:
                    jawab = ("0.0632400894165seconds","0.066333856583seconds","0.0774140357971seconds","0.0825560283661seconds","0.087260103226seconds","0.081302976608seconds","0.08514796257seconds","0.073701000214seconds","0.073701000214seconds","0.070698108673seconds","0.066083993912seconds","0.068862037659seconds","0.088862032959seconds","0.065990972519seconds","0.076188144684seconds","0.084258165359seconds","0.064408836365seconds")
                    jawaban = random.choice(jawab)
                    cl.sendText(msg.to, "Progress...")
                    cl.sendText(msg.to,jawaban)
#-----------------------------------------------

            elif msg.text in ["Cv say hi"]:
                if msg.from_ in admin:
                    ki.sendText(msg.to,"Hi buddy 􀜁􀅔Har Har􏿿")
                    kk.sendText(msg.to,"Hi buddy 􀜁􀅔Har Har􏿿")
                    kc.sendText(msg.to,"Hi buddy 􀜁􀅔Har Har􏿿")

#-----------------------------------------------

            elif msg.text in ["Cv say hinata pekok"]:
                if msg.from_ in admin:
                    ki.sendText(msg.to,"Hinata pekok 􀜁􀅔Har Har􏿿")
                    kk.sendText(msg.to,"Hinata pekok 􀜁􀅔Har Har􏿿")
                    kc.sendText(msg.to,"Hinata pekok 􀜁􀅔Har Har􏿿")
            elif msg.text in ["Cv say didik pekok"]:
                if msg.from_ in admin:
                    ki.sendText(msg.to,"Didik pekok 􀜁􀅔Har Har􏿿")
                    kk.sendText(msg.to,"Didik pekok 􀜁􀅔Har Har􏿿")
                    kc.sendText(msg.to,"Didik pekok 􀜁􀅔Har Har􏿿")
            elif msg.text in ["Han say bobo ah","Bobo dulu ah"]:
                if msg.from_ in admin:
                    ki.sendText(msg.to,"Have a nice dream Han 􀜁􀅔Har Har􏿿")
                    kk.sendText(msg.to,"Have a nice dream Han 􀜁􀅔Har Har􏿿")
                    kc.sendText(msg.to,"Have a nice dream Han 􀜁􀅔Har Har􏿿")
            elif msg.text in ["Cv say chomel pekok"]:
                if msg.from_ in admin:
                    ki.sendText(msg.to,"Chomel pekok 􀜁􀅔Har Har􏿿")
                    kk.sendText(msg.to,"Chomel pekok 􀜁􀅔Har Har􏿿")
                    kc.sendText(msg.to,"Chomel pekok 􀜁􀅔Har Har􏿿")
            elif msg.text in ["#welcome"]:
                if msg.from_ in admin:
                    ki.sendText(msg.to,"Selamat datang di Rayhan Family Room")
                    kk.sendText(msg.to,"Jangan nakal ya!")
#-----------------------------------------------
            elif msg.text in ["PING","Ping","ping"]:
                if msg.from_ in admin:
                    ki.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                    kk.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                    kc.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
#-----------------------------------------------
            elif msg.text in ["Protect On","protect on"]:
                if msg.from_ in admin:
                    cl.sendText(msg.to,"Loading...")
                    ki.sendText(msg.to,"20%")
                    kk.sendText(msg.to,"40%")
                    kc.sendText(msg.to,"60%")
                    kh.sendText(msg.to,"80%")
                    kg.sendText(msg.to,"100%")
                    ka.sendText(msg.to,"Waiting...")
                    cl.sendText(msg.to,"protection is on")
#-----------------------------------------------
            elif "tr-en " in msg.text.lower():
                if msg.from_ in admin:
                    isi = msg.text.replace("tr-en ", "")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='en')
                    F = hasil.text
                    F = F.encode('utf-8')
                    cl.sendText(msg.to, F)
            elif "tr-de " in msg.text.lower():
                if msg.from_ in admin:
                    isi = msg.text.replace("tr-de ", "")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='de')
                    F = hasil.text
                    F = F.encode('utf-8')
                    cl.sendText(msg.to, F)
            elif "tr-kr " in msg.text.lower():
                if msg.from_ in admin:
                    isi = msg.text.replace("tr-kr ", "")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='kr')
                    F = hasil.text
                    F = F.encode('utf-8')
                    cl.sendText(msg.to, F)
            elif "tr-in " in msg.text.lower():
                if msg.from_ in admin:
                    isi = msg.text.replace("tr-in ", "")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='in')
                    F = hasil.text
                    F = F.encode('utf-8')
                    cl.sendText(msg.to, F)
            elif "tr-ar " in msg.text.lower():
                if msg.from_ in admin:
                    isi = msg.text.replace("tr-ar ", "")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ar')
                    F = hasil.text
                    F = F.encode('utf-8')
                    cl.sendText(msg.to, F)
            elif "tr-fr " in msg.text.lower():
                if msg.from_ in admin:
                    isi = msg.text.replace("tr-fr ", "")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='fr')
                    F = hasil.text
                    F = F.encode('utf-8')
                    cl.sendText(msg.to, F)
#-----------------------------------------------

            elif msg.text in ["Sp","Speed","speed"]:
                if msg.from_ in admin:
                    start = time.time()
                    cl.sendText(msg.to, "Progress...")
                    elapsed_time = time.time() - start
                    cl.sendText(msg.to, "%sseconds" % (elapsed_time))

#------------------------------------------------------------------
            elif msg.text in ["Ban"]:
                if msg.from_ in admin:
                    wait3["wblacklist"] = True
                    with open('bl.json', 'w') as fp:
                        json.dump(wait3, fp, sort_keys=True, indent=4)
                    cl.sendText(msg.to,"Kirim Kontak Nya Han")
            elif msg.text in ["Unban"]:
                if msg.from_ in admin:
                    wait3["dblacklist"] = True
                    with open('bl.json', 'w') as fp:
                        json.dump(wait3, fp, sort_keys=True, indent=4)
                    cl.sendText(msg.to,"Kirim Kontak Nya Han")
            elif msg.text in ["Mcheck"]:
              if msg.from_ in admin:
                if wait3["blacklist"] == {}:
                    cl.sendText(msg.to,"Gak Ada")
                else:
                    cl.sendText(msg.to,"Blacklist user")
                    mc = ""
                    for mi_d in wait3["blacklist"]:
                        mc += "�" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text in ["Banlist"]:
              if msg.from_ in admin:
                if wait3["blacklist"] == {}:
                    cl.sendText(msg.to,"Gak Ada")
                else:
                    cl.sendText(msg.to,"Blacklist user")
                    mc = ""
                    for mi_d in wait3["blacklist"]:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text in ["Conban","Contactban","Contact ban"]:
              if msg.from_ in admin:
                if wait3["blacklist"] == {}:
                    cl.sendText(msg.to,"Tidak Ada Blacklist")
                else:
                    cl.sendText(msg.to,"Daftar Blacklist")
                    h = ""
                    for i in wait3["blacklist"]:
                        h = cl.getContact(i)
                        M = Message()
                        M.to = msg.to
                        M.contentType = 13
                        M.contentMetadata = {'mid': i}
                        cl.sendMessage(M)
            elif msg.text in ["Cek ban"]:
                if msg.from_ in admin:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait3["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += mm + "\n"
                    cl.sendText(msg.to,cocoa + "")
            elif msg.text in ["Kill ban"]:
                if msg.from_ in admin:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait3["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"Gak Ada blacklist user")
                        return
                    for jj in matched_list:
                        cl.kickoutFromGroup(msg.to,[jj])
                        ki.kickoutFromGroup(msg.to,[jj])
                        kk.kickoutFromGroup(msg.to,[jj])
                        kc.kickoutFromGroup(msg.to,[jj])
                        kh.kickoutFromGroup(msg.to,[jj])
                        kg.kickoutFromGroup(msg.to,[jj])
                        ka.kickoutFromGroup(msg.to,[jj])
                    cl.sendText(msg.to,"Good Bye")
            elif msg.text in ["Clear"]:
                if msg.from_ in admin:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"I pretended to cancel and canceled.")
            elif "albumâ†’" in msg.text:
                try:
                    albumtags = msg.text.replace("albumâ†’","")
                    gid = albumtags[:6]
                    name = albumtags.replace(albumtags[:34],"")
                    cl.createAlbum(gid,name)
                    cl.sendText(msg.to,name + "created an album")
                except:
                    cl.sendText(msg.to,"Error")
            elif "fakecâ†’" in msg.text:
                try:
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    name = "".join([random.choice(source_str) for x in xrange(10)])
                    anu = msg.text.replace("fakecâ†’","")
                    cl.sendText(msg.to,str(cl.channel.createAlbum(msg.to,name,anu)))
                except Exception as e:
                    try:
                        cl.sendText(msg.to,str(e))
                    except:
                        pass
        if op.type == 55:
            if op.param1 in wait2['readPoint']:
                Name = cl.getContact(op.param2).displayName
                if Name in wait2['readMember'][op.param1]:
                    pass
                else:
                    wait2['readMember'][op.param1] += "\n・" + Name
                    wait2['ROM'][op.param1][op.param2] = "・" + Name
            else:
                cl.sendText
        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True


def autolike():
     for zx in range(0,20):
        hasil = cl.activity(limit=20)
        if hasil['result']['post'][zx]['postInfo']['liked'] == False:
          try:
            ki.like(hasil['result']['post'][zx]['userInfo']['mid'],hasil['result']['post'][zx]['postInfo']['postId'],likeType=1002)
            ki.comment(hasil['result']['post'][zx]['userInfo']['mid'],hasil['result']['post'][zx]['postInfo']['postId'],"Auto Like by Rayhan\n\nhttp://line.me/ti/p/~mhmmdraaaayhan")
            kk.like(hasil['result']['post'][zx]['userInfo']['mid'],hasil['result']['post'][zx]['postInfo']['postId'],likeType=1002)
            kk.comment(hasil['result']['post'][zx]['userInfo']['mid'],hasil['result']['post'][zx]['postInfo']['postId'],"Auto Like by Rayhan\n\nhttp://line.me/ti/p/~mhmmdraaaayhan")
            kc.like(hasil['result']['post'][zx]['userInfo']['mid'],hasil['result']['post'][zx]['postInfo']['postId'],likeType=1002)
            kc.comment(hasil['result']['post'][zx]['userInfo']['mid'],hasil['result']['post'][zx]['postInfo']['postId'],"Auto Like by Rayhan\n\nhttp://line.me/ti/p/~mhmmdraaaayhan")
            kh.like(hasil['result']['post'][zx]['userInfo']['mid'],hasil['result']['post'][zx]['postInfo']['postId'],likeType=1002)
            kh.comment(hasil['result']['post'][zx]['userInfo']['mid'],hasil['result']['post'][zx]['postInfo']['postId'],"Auto Like by Rayhan\n\nhttp://line.me/ti/p/~mhmmdraaaayhan")
            kg.like(hasil['result']['post'][zx]['userInfo']['mid'],hasil['result']['post'][zx]['postInfo']['postId'],likeType=1002)
            kg.comment(hasil['result']['post'][zx]['userInfo']['mid'],hasil['result']['post'][zx]['postInfo']['postId'],"Auto Like by Rayhan\n\nhttp://line.me/ti/p/~mhmmdraaaayhan")
            ka.like(hasil['result']['post'][zx]['userInfo']['mid'],hasil['result']['post'][zx]['postInfo']['postId'],likeType=1002)
            ka.comment(hasil['result']['post'][zx]['userInfo']['mid'],hasil['result']['post'][zx]['postInfo']['postId'],"Auto Like by Rayhan\n\nhttp://line.me/ti/p/~mhmmdraaaayhan")
            kb.like(hasil['result']['post'][zx]['userInfo']['mid'],hasil['result']['post'][zx]['postInfo']['postId'],likeType=1002)
            kb.comment(hasil['result']['post'][zx]['userInfo']['mid'],hasil['result']['post'][zx]['postInfo']['postId'],"Auto Like by Rayhan\n\nhttp://line.me/ti/p/~mhmmdraaaayhan")
            kd.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['post'][zx]['postInfo']['postId'],likeType=1002)
            kd.comment(hasil['result']['post'][zx]['userInfo']['mid'],hasil['result']['post'][zx]['postInfo']['postId'],"Auto Like by Rayhan\n\nhttp://line.me/ti/p/~mhmmdraaaayhan")
            ke.like(hasil['result']['post'][zx]['userInfo']['mid'],hasil['result']['post'][zx]['postInfo']['postId'],likeType=1002)
            ke.comment(hasil['result']['post'][zx]['userInfo']['mid'],hasil['result']['post'][zx]['postInfo']['postId'],"Auto Like by Rayhan\n\nhttp://line.me/ti/p/~mhmmdraaaayhan")
            print "Like"
          except:
            pass
        else:
            print "Already Liked"
     time.sleep(500)
thread2 = threading.Thread(target=autolike)
thread2.daemon = True
thread2.start()

def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)


