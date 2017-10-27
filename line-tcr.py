# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re

cl = LINETCR.LINE()
cl.login(token='ElZKK6tLDu0eyaUhN6Jd.wGHnUPoZICFQRy+75j/exq.lX/oZl5nPwOCkQguO0mSnAnlRZ5pdORhl+fPRsOmVmk=')
cl.loginResult()

ki = LINETCR.LINE()
ki.login(token='ElVkA38IcorcUxDkDOSe.4MFt5OMs6ONpT0S07BNDVG.OrseUhyFSCqU+98EYSxwTeypy50NpUoSGAeW/7yWSvc=')
ki.loginResult()

ki2 = LINETCR.LINE()
ki2.login(token='EloUQyweq7p5G1ytV5bd.KUj2glYGVicN1FzgZ+WmJq.waMHSa4krpKjACqm1AxeB+48RYWgpTmDBK574SleRsw=')
ki2.loginResult()

ki3 = LINETCR.LINE()
ki3.login(token='EliJsCuFLLDZqUgLK9G4.srjUosW4RgcA0sSjVMH6Ta.1CQEU0SWykooTdXV9Sq4HZUPo18UIq5GC6IqmNj0luU=')
ki3.loginResult()

ki4 = LINETCR.LINE()
ki4.login(token='ElZObuppUAUupq6IO9o6.xkaL7HAdfdzB4bRIIC04jG.o4unKYYxDBO2+7sADrmjKi1IEHYn9OdzA4hmESD1uaA=')
ki4.loginResult()

ki5 = LINETCR.LINE()
ki5.login(token='Elg9TZOLHTOmewAwOkOf.HuRJhr2+tXSO7GIUgJ97dW.QumxN1RtbcOaP0Af2lgR8O0PwrzfBtlZuuVyIEXxPXE=')
ki5.loginResult()

ki6 = LINETCR.LINE()
ki6.login(token='ElWKAohPPALD3uTo4FM8.MQvnSQmxLZyecm+cYLEska.lHV9y7aHHl02XMs8Hg6qCpDFD2TrwblCWFo8mbtGrM8=')
ki6.loginResult()

ki7 = LINETCR.LINE()
ki7.login(token='ElOT4z62cngOMhnaksp0.kyYSuXdNfp5bf4YY/jNWCa.Y8phHSkO2ZZsP2ryIYibtx4AJIqRhcx50MP5tVZSPQo=')
ki7.loginResult()

ki8 = LINETCR.LINE()
ki8.login(token='El8xiaPOcNYjIHXgEzWb.jcL1Oteip7VRVtpL0w/zIW.eWfQqpTa2+5aaAibRvEe3U+oh4/Tm5acylY8aLMmwwc=')
ki8.loginResult()

ki9 = LINETCR.LINE()
ki9.login(token='ElkvLqaL0dFnvxFymaSc.aYbkAqXV5gf9Eu4MbqlVBa.+tCZNKWGK8JKFNw8KDWLtKzFUCtB0YfPWvdD9cqGayA=')
ki9.loginResult()

ki10 = LINETCR.LINE()
ki10.login(token='El3CCDAee6R30lWDs8ua.Ii7xOC92aAdE6psIz8+ZUG.XSYqYpa0megZ5wiz6wqqPfqK7oC8qr23XOgZyy+ueyU=')
ki10.loginResult()

print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage =""" **IP《 U_K 》●Bot○>> Help Menu**
↠Public Command↞
√ [Bot]- -Show Contact All Bot
√ [Group id]- -Show Group ID
√ [Ginfo]- -Show Group Info
√ [Mid all]- -Show all the Bot(s) MID
√ [Respon]- -Check Response Bot
√ [Speed]- -Check Kecepatan Bot
√ [Banlist]- -Check Banned Contact
√ [Gn G.Name]- -Change Group Name
√ [Cancel]- -Cancel Group Invitation
√ [Tag All]- -Tag All Member
√ [View]- -View Setting
√ [Open]- -Open Url
√ [Close]- -Close Url
√ [Stafflist]
√ [Set]

       ∧🎀∧ ∧🎩∧
  =≡( *•ω•) (•ω•* )≡=
     ⊂⊂ニ )( ニ⊃⊃
-=≡ (_(_／   ＼_)_) ≡=-


↠KICKER↞
**Protect / Damage Your Group**
√ [Banned @] Bann Target
√ [Unban @]   Unbann Target
√ [Nk @]    Kick Target User
√ [Kill @]   Kick Target Bann
√ [All]  Invite Semua Bot
√ [Mayhem] Do not use in d'group

》》》○●༄✰•U-K.MORA•✰࿐●○《《《
》》》○●༄✰•U-K.YENA•✰࿐●○《《《

☆        (\__/) ||
☆        (•ㅅ•) ||
☆        / 　 づิ
"""

Setgroup =""" **Bot Protection Key**
√ [AllProtection]~[AllProtection on / off]
√[Protect QR]~[Qr on / off]
√ [Mid Check]~[Contact On / Off]
√ [Reject Invite]~[Guest On / Off]
√ [Protect Cancel]~[Proc on / off]
√ [Member Protect]~[MProtection on /off]
"""
KAC=[cl,ki,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10]

mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = ki2.getProfile().mid
Cmid = ki3.getProfile().mid
Dmid = ki4.getProfile().mid
Emid = ki5.getProfile().mid
Fmid = ki6.getProfile().mid
Gmid = ki7.getProfile().mid
Hmid = ki8.getProfile().mid
Imid = ki9.getProfile().mid
Jmid = ki10.getProfile().mid

Bots=[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid,"udee46099e25e71f1fd1817cae9e7c429","u060faad0b4c2f6561f4bbdeef3670312"]
admin=["udee46099e25e71f1fd1817cae9e7c429","u060faad0b4c2f6561f4bbdeef3670312"]
staff=["udee46099e25e71f1fd1817cae9e7c429"]
adminMID=["udee46099e25e71f1fd1817cae9e7c429","u060faad0b4c2f6561f4bbdeef3670312"]
wait = {
    'contact':True,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':True,
    'message':"Thanks for add me",
    "lang":"JP",
    "comment":"Thanks for add me",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":True,
    "cName":"IP ディータ",
    "cName2":"ディータ1つ " ,
    "cName3":"ディータ二人 ",
    "cName4":"ディータ三 ",
    "cName5":"ディータ4人 ",
    "cName6":"ディータ五 ",
    "cName7":"ディータ6 ",
    "cName8":"ディータ7人 ",
    "cName9":"ディータ8人 ",
    "cName10":"ディータ9人 ",
    "cName11":"ディータ10人 ",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "ProtectQR":False,
    "Protectguest":False,
    "Protectcancel":False,
    "protectionOn":True,
    "atjointicket":True,
    "MProtection":False,
    "AllProtection":False
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

setTime = {}
setTime = wait2['setTime']


def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def NOTIFIED_ACCEPT_GROUP_INVITATION(op):
    print op
    try:
        cl.sendText(op.param1, cl.getContact(op.param2).displayName + "Selamat Datang😊\n " + group.name + "Salam Kenal Kak")
        ki.sendText(msg,to,"moga betah ya kaka .yg sopan & jangan nakal ya kakak")
    except Exception as e:
        print e
        print ("\n\nNOTIFIED_ACCEPT_GROUP_INVITATION\n\n")
        return
def NOTIFIED_KICKOUT_FROM_GROUP(op):
    try:
        cl.sendText(op.param1, cl.getContact(op.param3).displayName + " Jangan Main Kick!\n(/*´･ω･*\)")
    except Exception as e:
        print e
        print ("\n\nNOTIFIED_KICKOUT_FROM_GROUP\n\n")
        return
def NOTIFIED_LEAVE_GROUP(op):
    print op
    try:
        cl.sendText(op.param1, cl.getContact(op.param2).displayName + " Papay\n(*´･ω･*)")
        ki.sendText(msg,to,"Semoga Tenang Bagi yang Meninggalkan Grup 🏳️")
    except Exception as e:
        print e
        print ("\n\nNOTIFIED_LEAVE_GROUP\n\n")
        return
def NOTIFIED_READ_MESSAGE(op):
    print op
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
        #-------Protect Qr-------#
        if op.type == 11:
            if wait["ProtectQR"] == True:
                if op.param2 not in Bots or staff:
                    G = cl.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    cl.updateGroup(G)
                if op.param2 in wait["blacklist"]:
                    pass
                #if op.param2 in wait["whitelist"]:
                    #pass
                else:
                    wait["blacklist"][op.param2] = True

        #------Finish------#
        # -INV KICK- #
        if op.type == 13:
            if wait["Protectguest"] == True:
                if op.param2 in Bots or staff:
                	pass
                else:
                    random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                if op.param2 in wait["blacklist"]:
                    pass
                #if op.param2 in wait["whitelist"]:
                    #pass
                else:
                        wait["blacklist"][op.param2] = True

        #------FINISH------#
        #--CANCEL KICK--#
        if op.type == 32:
            if wait["Protectcancel"] == True:
                if op.param2 not in Bots or staff:
                    random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                if op.param2 in wait["blacklist"]:
                    pass
                #if op.param2 in wait["whitelist"]:
                    #pass
                else:
                    wait["blacklist"][op.param2] = True

        if op.type == 17:
                if op.param2 not in Bots:
                    if op.param2 not in admin:
                        random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])

        if op.type == 15:
            random.choice(KAC).sendText(op.param1, "Ada Yang Mati la... :)")
            print op.param3 + "has left the group"


        if op.type == 17:
            group = cl.getGroup(op.param1)
            cb = Message()
            cb.to = op.param1
            cb.text = cl.getContact(op.param2).displayName + " Selamat Datang di " + group.name
            cl.sendMessage(cb)

        if op.type == 19:
                if op.param2 not in Bots:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        wait["blacklist"][op.param2] = True
                        pass

        if op.type == 19:
           if op.param2 not in Bots:
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])

        if op.type == 19:
            if op.param3 not in Bots:
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.inviteIntoGroup(op.param1,op.param3)
                        adm.acceptGroupInvitation(op.param1)
                    except:
                        random.choice(KAC).inviteIntoGroup(op.param1,op.param3)
                        adm.acceptGroupInvitation(op.param1)

#        if op.type == 15:
 #           random.choice(KAC).sendText(op.param1, cl.getContact(op.param2).displayName + " Good Bye\n(*´･ω･*)")
  #        print op.param3 + "has left the group"

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
                        X = ki2.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki2.updateGroup(X)
                        Ti = ki2.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        ki.updateGroup(X)
                        Ti = ki.reissueGroupTicket(op.param1)


                if op.param3 in Bmid:
                    if op.param2 in Cmid:
                        X = ki3.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki3.updateGroup(X)
                        Ti = ki3.reissueGroupTicket(op.param1)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        ki2.updateGroup(X)
                        Ti = ki2.reissueGroupTicket(op.param1)

                if op.param3 in Cmid:
                    if op.param2 in Dmid:
                        X = ki4.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki4.updateGroup(X)
                        Ti = ki4.reissueGroupTicket(op.param1)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        ki3.updateGroup(X)
                        Ti = ki3.reissueGroupTicket(op.param1)

                if op.param3 in Dmid:
                    if op.param2 in Emid:
                        X = ki5.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki5.updateGroup(X)
                        Ti = ki5.reissueGroupTicket(op.param1)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        ki4.updateGroup(X)
                        Ti = ki4.reissueGroupTicket(op.param1)


                if op.param3 in Emid:
                    if op.param2 in Fmid:
                        X = ki6.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki6.updateGroup(X)
                        Ti = ki6.reissueGroupTicket(op.param1)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        ki5.updateGroup(X)
                        Ti = ki5.reissueGroupTicket(op.param1)


                if op.param3 in Fmid:
                    if op.param2 in Gmid:
                        X = ki7.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki7.updateGroup(X)
                        Ti = ki7.reissueGroupTicket(op.param1)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        ki6.updateGroup(X)
                        Ti = ki6.reissueGroupTicket(op.param1)


                if op.param3 in Gmid:
                    if op.param2 in Hmid:
                        X = ki8.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki8.updateGroup(X)
                        Ti = ki8.reissueGroupTicket(op.param1)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        ki7.updateGroup(X)
                        Ti = ki7.reissueGroupTicket(op.param1)


                if op.param3 in Hmid:
                    if op.param2 in Imid:
                        X = ki9.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki9.updateGroup(X)
                        Ti = ki9.reissueGroupTicket(op.param1)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        ki8.updateGroup(X)
                        Ti = k8.reissueGroupTicket(op.param1)


                if op.param3 in Imid:
                    if op.param2 in Jmid:
                        X = ki10.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki10.updateGroup(X)
                        Ti = ki10.reissueGroupTicket(op.param1)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        ki9.updateGroup(X)
                        Ti = ki9.reissueGroupTicket(op.param1)

                if op.param3 in Jmid:
                    if op.param2 in mid:
                        X = cl.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        ki10.updateGroup(X)
                        Ti = ki10.reissueGroupTicket(op.param1)

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
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
#---------------------------------------------
        if op.type == 19:
                if mid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        ki.knviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        #if op.param2 in wait["whitelist"]:
                            #pass
                        else:
                            wait["blacklist"][op.param2] = True

                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ti = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ti)
                        ki.acceptGroupInvitationByTicket(op.param1,Ti)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ti)
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        X = cl.getGroup(op.param1)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                        if op.param2 in wait["blacklist"]:
                            pass
                        #if op.param2 in wait["whitelist"]:
                            #pass
                        else:
                            wait["blacklist"][op.param2] = True


                if Amid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        #if op.param2 in wait["whitelist"]:
                            #pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki.updateGroup(G)
                    Ticket = ki.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    #if op.param2 in wait["whitelist"]:
                        #pass
                    else:
                        wait["blacklist"][op.param2] = True


                if Bmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        #if op.param2 in wait["whitelist"]:
                            #pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki3.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki3.updateGroup(G)
                    Ticket = ki3.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    #if op.param2 in wait["whitelist"]:
                        #pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Cmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        #if op.param2 in wait["whitelist"]:
                            #pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki3.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki3.updateGroup(G)
                    Ticket = ki3.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    #if op.param2 in wait["whitelist"]:
                        #pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Dmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        #if op.param2 in wait["whitelist"]:
                            #pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki4.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki4.updateGroup(G)
                    Ticket = ki4.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    #if op.param2 in wait["whitelist"]:
                        #pass
                    else:
                        wait["blacklist"][op.param2] = True


                if Emid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki5.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki5.updateGroup(G)
                    Ticket = ki5.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    #if op.param2 in wait["whitelist"]:
                        #pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Fmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        #if op.param2 in wait["whitelist"]:
                            #pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki6.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki6.updateGroup(G)
                    Ticket = ki6.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    #if op.param2 in wait["whitelist"]:
                        #pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Gmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        #if op.param2 in wait["whitelist"]:
                            #pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki6.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki6.updateGroup(G)
                    Ticket = ki6.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    #if op.param2 in wait["whitelist"]:
                        #pass
                    else:
                        wait["blacklist"][op.param2] = True


                if Hmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        #if op.param2 in wait["whitelist"]:
                            #pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki8.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki8.updateGroup(G)
                    Ticket = ki8.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    #if op.param2 in wait["whitelist"]:
                        #pass
                    else:
                        wait["blacklist"][op.param2] = True


                if Imid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        #if op.param2 in wait["whitelist"]:
                            #pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki9.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki9.updateGroup(G)
                    Ticket = ki9.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    #if op.param2 in wait["whitelist"]:
                        #pass
                    else:
                        wait["blacklist"][op.param2] = True


                if Jmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        #if op.param2 in wait["whitelist"]:
                            #pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki10.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki10.updateGroup(G)
                    Ticket = ki10.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    #if op.param2 in wait["whitelist"]:
                        #pass
                    else:
                        wait["blacklist"][op.param2] = True

        if op.type == 19:
                if op.param3 in Bots:
                    wait["blacklist"][op.param2] = True

        if op.type == 19:
            if wait["MProtection"] == True:
                if op.param2 not in Bots and staff:
                    random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                if op.param2 in wait["blacklist"]:
                    pass
                #if op.param2 in wait["whitelist"]:
                    #pass
                else:
                    wait["blacklist"][op.param2] = True
        if op.type == 19:
		    if op.param3 in admin:
		        cl.kickoutFromGroup(op.param1,[op.param2])
		        cl.inviteIntoGroup(op.param1,[op.param3])
		    else:
		        pass
        if op.type == 19:
                    if op.param3 in admin:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])
                    else:
                        pass
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
                for tag in wait["blacklist"]:
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
                if msg.from_ == profile.mid:
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            X = cl.getGroup(list_[1])
                            X.preventJoinByTicket = True
                            cl.updateGroup(X)
                        except:
                            cl.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"already")
                        wait["wblack"] = False

                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"decided not to comment")

               elif wait["dblack"] == True:
                 if msg.from_ in admin:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        #ki.sendText(msg.to,"deleted")
                        #kk.sendText(msg.to,"deleted")
                        #kc.sendText(msg.to,"deleted")
                        wait["dblack"] = False
                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        #ki.sendText(msg.to,"It is not in the black list")
                        #kk.sendText(msg.to,"It is not in the black list")
                        #kc.sendText(msg.to,"It is not in the black list")
               elif wait["wblacklist"] == True:
                 if msg.from_ in admin:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"already")
                        #ki.sendText(msg.to,"already")
                        #kk.sendText(msg.to,"already")
                        #kc.sendText(msg.to,"already")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"aded")
                        #ki.sendText(msg.to,"aded")
                        #kk.sendText(msg.to,"aded")
                        #kc.sendText(msg.to,"aded")

               elif wait["dblacklist"] == True:
                 if msg.from_ in admin:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        #ki.sendText(msg.to,"deleted")
                        #kk.sendText(msg.to,"deleted")
                        #kc.sendText(msg.to,"deleted")
                        wait["dblacklist"] = False
                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        #ki.sendText(msg.to,"It is not in the black list")
                        #kk.sendText(msg.to,"It is not in the black list")
                        #kc.sendText(msg.to,"It is not in the black list")
               elif wait["contact"] == True:
                 if msg.from_ in admin:
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
            elif msg.contentType == 16:
              if msg.from_ in admin:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["Key","help","Help"]:
              if msg.from_ in admin:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpt)
            elif msg.text in ["Setgroup"]:
              if msg.from_ in admin:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,Setgroup)
                    else:
                        cl.sendText(msg.to,Sett)
            elif ("Gn " in msg.text):
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn ","")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")
            elif ("Cv1 gn " in msg.text):
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Cv1 gn ","")
                    ki.updateGroup(X)
                else:
                    ki.sendText(msg.to,"It can't be used besides the group.")
            elif ("Cv2 gn " in msg.text):
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Cv2 gn ","")
                    kk.updateGroup(X)
                else:
                    kk.sendText(msg.to,"It can't be used besides the group.")
            elif ("Cv3 gn " in msg.text):
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Cv3 gn ","")
                    kc.updateGroup(X)
                else:
                    kc.sendText(msg.to,"It can't be used besides the group.")
            elif "Kick " in msg.text:
              if msg.from_ in admin:
                    midd = msg.text.replace("Kick ","")
                    ki.kickoutFromGroup(msg.to,[midd])
            elif "1 kick " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("1 kick ","")
                ki.kickoutFromGroup(msg.to,[midd])
            elif "2 kick " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("2 kick ","")
                ki2.kickoutFromGroup(msg.to,[midd])
            elif "3 kick " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("3 kick ","")
                ki3.kickoutFromGroup(msg.to,[midd])
            elif "Invite " in msg.text:
              if msg.from_ in admin:
                    midd = msg.text.replace("Invite ","")
                    ki.findAndAddContactsByMid(midd)
                    ki.inviteIntoGroup(msg.to,[midd])
            elif "1 invite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Cv1 invite ","")
                ki.findAndAddContactsByMid(midd)
                ki.inviteIntoGroup(msg.to,[midd])
            elif "2 invite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Cv2 invite ","")
                ki2.findAndAddContactsByMid(midd)
                ki2.inviteIntoGroup(msg.to,[midd])
            elif "3 invite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Cv3 invite ","")
                ki3.findAndAddContactsByMid(midd)
                ki3.inviteIntoGroup(msg.to,[midd])
            elif "Me @" in msg.text:
                msg.contentType = 13
                _name = msg.text.replace("Me @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        msg.contentMetadata = {'mid': g.mid}
                        cl.sendMessage(msg)
                    else:
                        pass
            elif msg.text in ["Me"]:
              if msg.from_ in admin:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
            elif msg.text in ["1"]:
              if msg.from_ in admin:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid}
                ki.sendMessage(msg)
            elif msg.text in ["2"]:
              if msg.from_ in admin:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Bmid}
                ki2.sendMessage(msg)
            elif msg.text in ["3"]:
              if msg.from_ in admin:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Cmid}
                ki3.sendMessage(msg)
            elif msg.text in ["4"]:
              if msg.from_ in admin:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Dmid}
                ki4.sendMessage(msg)
            elif msg.text in ["5"]:
              if msg.from_ in admin or staff:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Emid}
                ki5.sendMessage(msg)
            elif msg.text in ["6"]:
              if msg.from_ in admin:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Fmid}
                ki6.sendMessage(msg)
            elif msg.text in ["7"]:
              if msg.from_ in admin:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Gmid}
                ki7.sendMessage(msg)
            elif msg.text in ["8"]:
              if msg.from_ in admin:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Hmid}
                ki8.sendMessage(msg)
            elif msg.text in ["9"]:
              if msg.from_ in admin:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Imid}
                ki9.sendMessage(msg)
            elif msg.text in ["10"]:
              if msg.from_ in admin:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Jmid}
                ki10.sendMessage(msg)

            elif msg.text in ["Bot"]:
              if msg.from_ in admin:
            	msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid}
                ki.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': Bmid}
                ki2.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': Cmid}
                ki3.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': Dmid}
                ki4.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': Emid}
                ki5.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': Fmid}
                ki6.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': Gmid}
                ki7.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': Hmid}
                ki8.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': Imid}
                ki9.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': Jmid}
                ki10.sendMessage(msg)

            elif msg.text in ["æ„›ã®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text in ["æ„›ã®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Cv1 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '6'}
                msg.text = None
                ki.sendMessage(msg)
            elif msg.text in ["æ„›ã®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Cv2 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '8'}
                msg.text = None
                kk.sendMessage(msg)
            elif msg.text in ["æ„›ã®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Cv3 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '10'}
                msg.text = None
                kc.sendMessage(msg)
            elif msg.text in ["æ„›ã®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","All gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '12'}
                msg.text = None
                ki.sendMessage(msg)
                kk.sendMessage(msg)
                kc.sendMessage(msg)
         #-----Fungsi List Group------#
            elif msg.text in ["List group"]:
                if msg.from_ in admin:
                    gid = cl.getGroupIdsJoined()
                    h = ""
                    for i in gid:
                        h += "[~]%s\n" % (cl.getGroup(i).name +str (len (cl.getGroup(i).members)))
                    cl.sendText(msg.to,"========[List Group]========\n"+ h +"Total Group :" +str(len(gid)))

         #-----Finish--------#
         #-------------Fungsi Creator Start-----------------#
            elif msg.text in ["Creator"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    msg.contentType = 13
                    Creatorbot = "udee46099e25e71f1fd1817cae9e7c429"
                    try:
                        msg.contentMetadata = {'mid': Creatorbot}

                    except:
                        Creatorbot = "Error"
                    cl.sendText(msg.to, "My Creator : IP/nhttp://line.me/ti/p/Tq1A2KSg0K")
                    cl.sendMessage(msg)

          #-------------Fungsi Creator Finish-----------------#
          #-------------Fungsi Kick By Tag---------------------#
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
                            random.choice(KAC).sendText(op.param1, cl.getContact(op.param3).displayName + " ~Sorry (*´･ω･*)")
                        except:
                            pass
           #-------------Fungsi Kick By Tag---------------------#
           #-------------Fungsi Ban By Tag---------------------#
            elif ("BL " in msg.text):
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      wait["blacklist"][target] = True
                      f=codecs.open('st2__b.json','w','utf-8')
                      json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                      cl.sendText(msg.to,"Succes Blacklist")
                   except:
                      pass
          #-------------Fungsi Ban By Tag Finish---------------------#
            elif msg.text in ["cancel","Cancel"]:
              if msg.from_ in admin:
                if msg.toType == 2:
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
            elif msg.text in ["Cv cancel","Bot cancel"]:
              if msg.from_ in admin:
                if msg.toType == 2:
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
            elif msg.text in ["Open","Link on"]:
              if msg.from_ in admin:
                    if msg.toType == 2:
                        X = ki.getGroup(msg.to)
                        X.preventJoinByTicket = False
                        ki.updateGroup(X)
                        if wait["lang"] == "JP":
                            ki.sendText(msg.to,"Done")
                        else:
                            ki.sendText(msg.to,"already open")
                    else:
                        if wait["lang"] == "JP":
                            ki.sendText(msg.to,"Can not be used outside the group")
                        else:
                            ki.sendText(msg.to,"Not for use less than group")

            elif msg.text in ["1 open","Cv1 link on"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = ki.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    ki.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done ")
                    else:
                        cl.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")

            elif msg.text in ["Close","Link off"]:
              if msg.from_ in admin:
                    if msg.toType == 2:
                        X = cl.getGroup(msg.to)
                        X.preventJoinByTicket = True
                        ki.updateGroup(X)
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Done")
                        else:
                            cl.sendText(msg.to,"already close")
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Can not be used outside the group")
                        else:
                            cl.sendText(msg.to,"Not for use less than group")

            elif msg.text in ["1 close","Cv1 link off"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = ki.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    ki.updateGroup(X)
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Done ")
                    else:
                        ki.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ki.sendText(msg.to,"Not for use less than group")

            elif "jointicket " in msg.text.lower():
              if msg.from_ in admin:
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
				cl.acceptGroupInvitationByTicket(group.id,ticket_id)
				cl.sendText(msg.to,"Sukses join ke grup %s" % str(group.name))
            elif msg.text == "Ginfo":
              if msg.from_ in admin:
                if msg.toType == 2:
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


            elif "Mid all" == msg.text:
              if msg.from_ in admin:
                cl.sendText(msg.to,mid)
                ki.sendText(msg.to,Amid)
                ki2.sendText(msg.to,Bmid)
                ki3.sendText(msg.to,Cmid)
                ki4.sendText(msg.to,Dmid)
                ki5.sendText(msg.to,Emid)
                ki6.sendText(msg.to,Fmid)
                ki7.sendText(msg.to,Gmid)
                ki8.sendText(msg.to,Hmid)
                ki9.sendText(msg.to,Imid)
                ki10.sendText(msg.to,Jmid)
            elif "Mid" == msg.text:
              if msg.from_ in admin:
                cl.sendText(msg.to,mid)
            elif msg.text in ["Wkwk"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "100",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Hehehe"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "10",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Galon"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "9",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["You"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "7",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Hadeuh"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "6",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Please"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "4",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Haaa"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "3",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Lol"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "110",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Hmmm"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "101",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif msg.text in ["Welcome"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "247",
                                     "STKPKGID": "3",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["TL:"]:
              if msg.from_ in admin or staff:
                tl_text = msg.text.replace("TL:","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])

            elif "MeUp n " in msg.text:
            	if msg.from_ in Bots:
                    string = msg.text.replace("MeUp n ","")
                    if len(string.decode('utf-8')) <= 20:
                        profile = cl.getProfile()
                        profile.displayName = string
                        cl.updateProfile(profile)
                        cl.sendText(msg.to,"name " + string + "Done")

            elif "1Up" in msg.text:
              if msg.from_ in admin:
                    string = msg.text.replace("1Up n ","")
                    if len(string.decode('utf-8')) <= 20:
                        profile = cl.getProfile()
                        profile.displayName = string
                        ki.updateProfile(profile)
                        ki.sendText(msg.to,"name " + string + "Done")
            elif "2Up" in msg.text:
              if msg.from_ in admin:
                    string = msg.text.replace("2Up n ","")
                    if len(string.decode('utf-8')) <= 20:
                        profile = cl.getProfile()
                        profile.displayName = string
                        ki2.updateProfile(profile)
                        ki2.sendText(msg.to,"name" + string + "Done")

            elif "3Up" in msg.text:
              if msg.from_ in admin:
                    string = msg.text.replace("3Up n ","")
                    if len(string.decode('utf-8')) <= 20:
                        profile = cl.getProfile()
                        profile.displayName = string
                        ki3.updateProfile(profile)
                        ki3.sendText(msg.to,"name" + string + "Done")
            elif "4Up" in msg.text:
              if msg.from_ in admin:
                    string = msg.text.replace("4Up n ","")
                    if len(string.decode('utf-8')) <= 20:
                        profile = cl.getProfile()
                        profile.displayName = string
                        ki4.updateProfile(profile)
                        ki4.sendText(msg.to,"name" + string + "Done")
            elif "5Up" in msg.text:
              if msg.from_ in admin:
                    string = msg.text.replace("5Up n ","")
                    if len(string.decode('utf-8')) <= 20:
                        profile = cl.getProfile()
                        profile.displayName = string
                        ki5.updateProfile(profile)
                        ki5.sendText(msg.to,"name" + string + "Done")

            elif "6Up" in msg.text:
              if msg.from_ in admin:
                    string = msg.text.replace("6Up n ","")
                    if len(string.decode('utf-8')) <= 20:
                        profile = cl.getProfile()
                        profile.displayName = string
                        ki6.updateProfile(profile)
                        ki6.sendText(msg.to,"name" + string + "Done")
            elif "7Up" in msg.text:
              if msg.from_ in admin:
                    string = msg.text.replace("7Up n ","")
                    if len(string.decode('utf-8')) <= 20:
                        profile = cl.getProfile()
                        profile.displayName = string
                        ki7.updateProfile(profile)
                        ki7.sendText(msg.to,"name" + string + "Done")
            elif "8Up" in msg.text:
              if msg.from_ in admin:
                    string = msg.text.replace("8Up n ","")
                    if len(string.decode('utf-8')) <= 20:
                        profile = cl.getProfile()
                        profile.displayName = string
                        ki8.updateProfile(profile)
                        ki8.sendText(msg.to,"name" + string + "Done")
            elif "9Up" in msg.text:
              if msg.from_ in admin:
                    string = msg.text.replace("9Up n ","")
                    if len(string.decode('utf-8')) <= 20:
                        profile = cl.getProfile()
                        profile.displayName = string
                        ki9updateProfile(profile)
                        ki9.sendText(msg.to,"name " + string + "Done")
            elif "10Up" in msg.text:
              if msg.from_ in admin:
                    string = msg.text.replace("10Up n ","")
                    if len(string.decode('utf-8')) <= 20:
                        profile = cl.getProfile()
                        profile.displayName = string
                        ki10.updateProfile(profile)
                        ki10.sendText(msg.to,"name " + string + "Done")

            elif "AllUp" in msg.text:
              if msg.from_ in admin:
                string = msg.text.replace("AllUp n ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                    ki2.updateProfile(profile)
                    ki3.updateProfile(profile)
                    ki4.updateProfile(profile)
                    ki5.updateProfile(profile)
                    ki6.updateProfile(profile)
                    ki7.updateProfile(profile)
                    ki8.updateProfile(profile)
                    ki9.updateProfile(profile)
                    ki10.updateProfile(profile)
                    ki.sendText(msg.to,"name" + string + "Done")
                    ki2.sendText(msg.to,"name" + string + "Done")
                    ki3.sendText(msg.to,"name" + string + "Done")
                    ki4.sendText(msg.to,"name" + string + "Done")
                    ki5.sendText(msg.to,"name" + string + "Done")
                    ki6.sendText(msg.to,"name" + string + "Done")
                    ki7.sendText(msg.to,"name" + string + "Done")
                    ki8.sendText(msg.to,"name" + string + "Done")
                    ki9.sendText(msg.to,"name" + string + "Done")
                    ki10.sendText(msg.to,"name" + string + "Done")
            elif msg.text in ["Mc "]:
              if msg.from_ in admin:
                mmid = msg.text.replace("Mc ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
#-----------protection start-----------------#
            elif msg.text in ["AllProt on"]:
              if msg.from_ in admin:
            	    if wait["AllProtection"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"All Protection On")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["MProtection"] = True
                        wait["Protectguest"] = True
                        wait["ProtectQR"] = True
                        wait["Protectcancel"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"All Protection On")
                        else:
                            cl.sendText(msg.to,"done")
            elif msg.text in ["AllProt off"]:
            	if msg.from_ in Bots or staff:
            	    if wait["AllProtection"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"All Protection Off")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["MProtection"] = False
                        wait["Protectguest"] = False
                        wait["ProtectQR"] = False
                        wait["Protectcancel"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"All Protection Off")
                        else:
                            cl.sendText(msg.to,"done")
            elif msg.text in ["MProtection on","MProt on"]:
              if msg.from_ in admin:
                    if wait["MProtection"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Member Protection On")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["MProtection"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Member Protection On")
                        else:
                            cl.sendText(msg.to,"done")
            elif msg.text in ["MProtection off","MProt off"]:
              if msg.from_ in admin:
                    if wait["MProtection"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Member Protection Off")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["MProtection"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Member Protection Off")
                        else:
                            cl.sendText(msg.to,"done")
            elif msg.text in ["Blockinvite on","guest on"]:
              if msg.from_ in admin:
                    if wait["Protectguest"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Block Invitation On")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["Protectguest"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Block Invitation On")
                        else:
                            cl.sendText(msg.to,"done")
            elif msg.text in ["Blockinvite off","guest off"]:
              if msg.from_ in admin:
                    if wait["Protectguest"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Blockinvitation Off")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["Protectguest"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Blockinvitation Off")
                        else:
                            cl.sendText(msg.to,"done")
            elif msg.text in ["Qrp on","qr on"]:
              if msg.from_ in admin:
                    if wait["ProtectQR"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"QR Protection On")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["ProtectQR"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"QR Protection On")
                        else:
                            cl.sendText(msg.to,"done")
            elif msg.text in ["Qrp off","qr off"]:
              if msg.from_ in admin:
                    if wait["ProtectQR"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"QR Protection Off")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["ProtectQR"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"QR Protection Off")
                        else:
                            cl.sendText(msg.to,"done")
            elif msg.text in ["Proc on","proc on"]:
              if msg.from_ in admin:
                    if wait["Protectcancel"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Protect cancel on")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["Protectcancel"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Protect cancel on")
                        else:
                            cl.sendText(msg.to,"done")
            elif msg.text in ["Proc off","proc off"]:
              if msg.from_ in admin:
                    if wait["Protectcancel"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Protect cancel off")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["Protectcancel"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Protect cancel off")
                        else:
                            cl.sendText(msg.to,"done")
#-------------protection finish-----------------------
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
            elif msg.text in ["Set"]:
              if msg.from_ in admin:
                md = ""
                if wait["MProtection"] == True: md+=" MProtection : on\n"
                else: md+=" MProtection : off\n"
                if wait["Protectcancel"] == True: md+=" Protect Cancel : on\n"
                else: md+=" Protect Cancel : off\n"
                if wait["ProtectQR"] == True: md+=" Protect Qr : on\n"
                else: md+=" Protect Qr : off\n"
                if wait["Protectguest"] == True: md+=" Block Invite : on\n"
                else: md+=" Block Invite : off\n"
                if wait["contact"] == True: md+=" Contact : on\n"
                else: md+=" Contact : off\n"
                if wait["autoJoin"] == True: md+=" Auto join : on\n"
                else: md +=" Auto join : off\n"
                if wait["autoCancel"]["on"] == True:md+=" Group cancel :" + str(wait["autoCancel"]["members"]) + "\n"
                else: md+= " Group cancel : off\n"
                if wait["leaveRoom"] == True: md+=" Auto leave : on\n"
                else: md+=" Auto leave : off\n"
                if wait["timeline"] == True: md+=" Share : on\n"
                else:md+=" Share : off\n"
                if wait["autoAdd"] == True: md+=" Auto add : on\n"
                else:md+=" Auto add : off\n"
                if wait["commentOn"] == True: md+=" Comment : on\n"
                else:md+=" Comment : off\n"
                if wait["atjointicket"] == True: md+=" Auto Join Group by Ticket : on\n"
                else:md+=" Auto Join Group by Ticket : off\n"
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
                if msg.toType == 2:
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
            elif msg.text in ["1 gurl"]:
              if msg.from_ in admin:
                if msg.toType == 2:
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
            elif msg.text in ["Cv2 gurl"]:
              if msg.from_ in admin:
                if msg.toType == 2:
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
            elif msg.text in ["JUp"]:
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
#-----------------------------------------------
            elif msg.text in ["Moracam","Oppakam"]:
                if msg.from_ in admin or Bots:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        G = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        cl.updateGroup(G)

            elif msg.text in ["Yenacam","Yenakam"]:
                if msg.from_ in admin:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.0)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.0)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.0)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.0)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.0)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.0)
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.0)
                        ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.0)
                        ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.0)
                        ki10.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.0)
                        G = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        cl.updateGroup(G)
#-----------------------------------------------
            elif msg.text in ["Byemora","Byeoppa"]:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        ginfo = cl.getGroup(msg.to)
                        try:
                            ki.leaveGroup(msg.to)
                            ki2.leaveGroup(msg.to)
                            ki3.leaveGroup(msg.to)
			    ki4.leaveGroup(msg.to)
			    ki5.leaveGroup(msg.to)
                            ki6.leaveGroup(msg.to)
                            ki7.leaveGroup(msg.to)
			    ki8.leaveGroup(msg.to)
			    ki9.leaveGroup(msg.to)
			    ki10.leaveGroup(msg.to)
			    cl.leaveGroup(msg.to)
                        except:
                            pass

            elif msg.text in ["Byeyena","Byeunni"]:
                if msg.from_ in Bots:
                    if msg.toType == 2:
                        ginfo = cl.getGroup(msg.to)
                        try:
                            ki.leaveGroup(msg.to)
                            ki2.leaveGroup(msg.to)
                            ki3.leaveGroup(msg.to)
			    ki4.leaveGroup(msg.to)
			    ki5.leaveGroup(msg.to)
                            ki6.leaveGroup(msg.to)
                            ki7.leaveGroup(msg.to)
			    ki8.leaveGroup(msg.to)
			    ki9.leaveGroup(msg.to)
			    ki10.leaveGroup(msg.to)
                        except:
                            pass
#----------------------------------------------
            elif msg.text in ["tagall","Tag all"]:
                group = cl.getGroup(msg.to)
                jw = [contact.mid for contact in group.members]
                cb = ""
	        cb2 = ""
                strt = int(0)
                akh = int(0)
                for rs in jw:
                    xname = cl.getContact(rs).displayName
                    xlen = int(len('x')+1)
                    akh = akh + xlen
                    cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(rs)+"},"""
                    strt = strt + int(len('x')+3)
		    akh = akh + 2
		    cb2 += "@x \n"
                cb = (cb[:int(len(cb)-1)])
                msg.contentType = 0
                msg.text = cb2
                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                try:
                    cl.sendMessage(msg)
                except Exception as error:
                    print error

            elif msg.text in ["Kill"]:
            	if msg.from_ in Bots or staff:
                    if msg.toType == 2:
                        group = ki.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in wait["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            ki.sendText(msg.to,"Sorry!!")
                            ki2.sendText(msg.to,"（´・ω・｀)")
                            return
                        for jj in matched_list:
                            try:
                                klist=[ki,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[jj])
                                print (msg.to,[jj])
                            except:
                                pass

#--------------kick all------------------

            elif "Mayhem" in msg.text:
              if msg.from_ in Bots:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("Mayhem","")
                    gs = ki.getGroup(msg.to)
                    gs = ki2.getGroup(msg.to)
                    gs = ki3.getGroup(msg.to)
                    #gs = ki4.getGroup(msg.to)
                    #gs = ki5.getGroup(msg.to)
                    ki.sendText(msg.to,"「 Mayhem 」\nMayhem is STARTING♪\n abort to abort♪")
                    ki2.sendText(msg.to,"「 Mayhem 」\n46 victims shall yell hul·la·ba·loo♪\nhələbəˈlo͞o hələbəˌlo͞o")
                    ki3.sendText(msg.to,"Good Bye (*´･ω･*)")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki2.sendText(msg.to,"Not Found")
                    else:
                        for target in targets:
                            if target not in Bots and staff:
                                try:
                                   klist=[ki,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10]
                                   kicker=random.choice(klist)
                                   kicker.kickoutFromGroup(msg.to,[target])
                                   print (msg.to,[g.mid])
                                except:
                                   ki3.sendText(msg.to,"Mayhem done")

            elif "Kickuk" in msg.text:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        print "ok"
                        _name = msg.text.replace("Kickuk","")
                        gs = ki.getGroup(msg.to)
                        gs = ki2.getGroup(msg.to)
                        gs = ki3.getGroup(msg.to)
                        #ki.sendText(msg.to,"Just some casual cleansing ô")
                        #ki2.sendText(msg.to,"Group cleansed.")
                        #ki3.sendText(msg.to,"Fuck You All")
                        targets = []
                        for g in gs.members:
                            if _name in g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            ki.sendText(msg.to,"Not found.")
                            ki2.sendText(msg.to,"Not found.")
                            ki3.sendText(msg.to,"Not found.")
                        else:
                            for target in targets:
                            	if target not in Bots and admin:
                                    try:
                                        klist=[ki,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10]
                                        kicker=random.choice(klist)
                                        kicker.kickoutFromGroup(msg.to,[target])
                                        print (msg.to,[g.mid])
                                    except:
                                        ki.sendText(msg.to,"Group cleanse")
                                        ki2.sendText(msg.to,"Group cleanse")
                                        ki3.sendText(msg.to,"Group cleanse")
#---------kick all finish------------

            elif "Nk " in msg.text:
                  if msg.from_ in Bots:
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
                               if target not in Bots and admin:
                                try:
                                    klist=[cl,ki,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10]
                                    kicker=random.choice(klist)
                                    kicker.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ki.sendText(msg.to,"Sorry...")
                                    ki3.sendText(msg.to,"（´・ω・｀)")


            elif "Blacklist @ " in msg.text:
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
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    k3.sendText(msg.to,"Succes ")
                                except:
                                    ki.sendText(msg.to,"error")


            elif "Banned @" in msg.text:
                if msg.from_ in Bots or staff:
                    if msg.toType == 2:
                        print "[Banned] Sukses"
                        _name = msg.text.replace("Banned @","")
                        _nametarget = _name.rstrip(' ')
                        gs = cl.getGroup(msg.to)
                        gs = ki.getGroup(msg.to)
                        gs = ki2.getGroup(msg.to)
                        gs = ki3.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to,"Dilarang Banned Bot")
                            #ki.sendText(msg.to,"Dilarang Banned Bot")
                            #ki2.sendText(msg.to,"Dilarang Banned Bot")
                            #ki3.sendText(msg.to,"Dilarang Banned Bot")
                        else:
                            for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,"Akun telah sukses di banned")
                                except:
                                    ki.sendText(msg.to,"Error")


            elif "Unbanned @" in msg.text:
                if msg.from_ in Bots or staff:
                    if msg.toType == 2:
                        print "[Unban] Sukses"
                        _name = msg.text.replace("Unban @","")
                        _nametarget = _name.rstrip(' ')
                        gs = cl.getGroup(msg.to)
                        gs = ki.getGroup(msg.to)
                        gs = ki2.getGroup(msg.to)
                        gs = ki3.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to,"Tidak Ditemukan.....")
                            #ki.sendText(msg.to,"Tidak Ditemukan.....")
                            #ki2sendText(msg.to,"Tidak Ditemukan.....")
                            #ki3.sendText(msg.to,"Tidak Ditemukan.....")
                        else:
                            for target in targets:
                                try:
                                    del wait["blacklist"][target]
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,"Akun Bersih Kembali")
                                except:
                                    ki.sendText(msg.to,"Error")
#-----------------------------------------------
            elif msg.text in ["Test"]:
                ki.sendText(msg.to,"Ok Cv 􀨁􀄻double thumbs up􏿿")
                kk.sendText(msg.to,"Ok Cv 􀨁􀄻double thumbs up􏿿")
                kc.sendText(msg.to,"Ok Cv 􀨁􀄻double thumbs up􏿿")
#-----------------------------------------------
            elif "Bc " in msg.text:
				bctxt = msg.text.replace("Bc ","")
				ki.sendText(msg.to,(bctxt))
				kk.sendText(msg.to,(bctxt))
				kc.sendText(msg.to,(bctxt))
#-----------------------------------------------


            elif msg.text in ["Cv say hi"]:
                ki.sendText(msg.to,"Hi buddy 􀜁􀅔Har Har􏿿")
                kk.sendText(msg.to,"Hi buddy 􀜁􀅔Har Har􏿿")
                kc.sendText(msg.to,"Hi buddy 􀜁􀅔Har Har􏿿")

#-----------------------------------------------

            elif msg.text in ["Cv say hinata pekok"]:
                ki.sendText(msg.to,"Hinata pekok 􀜁􀅔Har Har􏿿")
                kk.sendText(msg.to,"Hinata pekok 􀜁􀅔Har Har􏿿")
                kc.sendText(msg.to,"Hinata pekok 􀜁􀅔Har Har􏿿")
            elif msg.text in ["Cv say didik pekok"]:
                ki.sendText(msg.to,"Didik pekok 􀜁􀅔Har Har􏿿")
                kk.sendText(msg.to,"Didik pekok 􀜁􀅔Har Har􏿿")
                kc.sendText(msg.to,"Didik pekok 􀜁􀅔Har Har􏿿")
            elif msg.text in ["Cv say bobo ah","Bobo dulu ah"]:
                ki.sendText(msg.to,"Have a nice dream Cv 􀜁􀅔Har Har􏿿")
                kk.sendText(msg.to,"Have a nice dream Cv 􀜁􀅔Har Har􏿿")
                kc.sendText(msg.to,"Have a nice dream Cv 􀜁􀅔Har Har􏿿")
            elif msg.text in ["Cv say chomel pekok"]:
                ki.sendText(msg.to,"Chomel pekok 􀜁􀅔Har Har􏿿")
                kk.sendText(msg.to,"Chomel pekok 􀜁􀅔Har Har􏿿")
                kc.sendText(msg.to,"Chomel pekok 􀜁􀅔Har Har􏿿")
            elif msg.text in ["#welcome"]:
                ki.sendText(msg.to,"Selamat datang di Chivas Family Room")
                kk.sendText(msg.to,"Jangan nakal ok!")
#-----------------------------------------------
            elif msg.text in ["PING","Ping","ping"]:
                ki.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                kk.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                kc.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
#-----------------------------------------------

            elif msg.text in ["Respon","respon"]:
              if msg.from_ in admin:
                ki.sendText(msg.to,"（`・ω・`）")
                ki2.sendText(msg.to,"（`・ω・｀）")
                ki3.sendText(msg.to,"（`・ω・｀）")
                ki4.sendText(msg.to,"（`・ω・｀）")
                ki5.sendText(msg.to,"（`・ω・｀）")
                ki6.sendText(msg.to,"（`・ω・｀）")
                ki7.sendText(msg.to,"（`・ω・｀）")
                ki8.sendText(msg.to,"（`・ω・｀）")
                ki9.sendText(msg.to,"（`・ω・｀）")
                ki10.sendText(msg.to,"（`・ω・｀）")

#-----------------------------------------------

            elif "Spam " in msg.text:
              if msg.from_ in Bots:
                txt = msg.text.split(" ")
                jmlh = int(txt[2])
                teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+ " ","")
                tulisan = jmlh * (teks+"\n")
                 #Keke cantik <3
                if txt[1] == "on":
                    if jmlh <= 500:
                       for x in range(jmlh):
                           cl.sendText(msg.to, teks)
                    else:
                       cl.sendText(msg.to, "Kelebihan batas:v")
                elif txt[1] == "off":
                    if jmlh <= 9999:
                        cl.sendText(msg.to, tulisan)
                    else:
                        cl.sendText(msg.to, "Kelebihan batas :v")

            elif msg.text in ["Speed","Speedbot","speedbot"]:
                if msg.from_ in Bots:
                    start = time.time()
                    cl.sendText(msg.to, "Waiting...")
                    elapsed_time = time.time() - start
                    cl.sendText(msg.to, "%sseconds" % (elapsed_time))

            elif "Add staff @" in msg.text:
                if msg.from_ in Bots:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Add staff @","")
                    _nametarget = _name.rstrip(' ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    #gs = kk.getGroup(msg.to) gs =
                    #kc.getGroup(msg.to)
                    #gs = kg.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.append(target)
                                cl.sendText(msg.to,"Added to the staff list")
                            except:
                                pass
                    print "[Command]Staff add executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")

            elif "Remove staff @" in msg.text:
                if msg.from_ in Bots:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("Remove staff @","")
                    _nametarget = _name.rstrip(' ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    #gs = kk.getGroup(msg.to) gs =
                    #kc.getGroup(msg.to)
                    #gs = kg.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.remove(target)
                                cl.sendText(msg.to,"Removed to the staff list")
                            except:
                                pass
                    print "[Command]Staff remove executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")


            elif "Add admin @" in msg.text:
                if msg.from_ in Bots:
                    print "[Command]admin add executing"
                    _name = msg.text.replace("Add admin @","")
                    _nametarget = _name.rstrip(' ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    #gs = kk.getGroup(msg.to)
                    #gs = kc.getGroup(msg.to)
                    #gs = kg.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.append(target)
                                cl.sendText(msg.to,"Added to the admin list")
                            except:
                                pass
                    print "[Command]admin add executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")


            elif "Remove admin @" in msg.text:
                if msg.from_ in Bots:
                    print "[Command]admin remove executing"
                    _name = msg.text.replace("Remove admin @","")
                    _nametarget = _name.rstrip(' ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    #gs = kk.getGroup(msg.to)
                    #gs = kc.getGroup(msg.to) gs =
                    #kg.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.remove(target)
                                cl.sendText(msg.to,"Removed to the admin list")
                            except:
                                pass
                    print "[Command]admin remove executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")

            elif msg.text in ["Stafflist","stafflist"]:
                if staff == []:
                    ki.sendText(msg.to,"The stafflist is empty")
                else:
                    ki.sendText(msg.to,"Staff list:")
                    mc = ""
                    for mi_d in staff:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    ki.sendText(msg.to,mc)
                    print "[Command]Stafflist executed"

            elif msg.text in ["Admin list","admin list"]:
                if admin == []:
                    ki.sendText(msg.to,"The stafflist is empty")
                else:
                    ki.sendText(msg.to,"Admin list:")
                    mc = ""
                    for mi_d in staff:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    ki.sendText(msg.to,mc)
                    print "[Command]Adminlist executed"

            elif msg.text in ["Ip Like", "Ar like"]:
                if msg.from_ in staff:
                    print "[Command]Like executed"
                    cl.sendText(msg.to,"Trying to Like post(s) from staff")
                    try:
                        likePost()
                    except:
                        pass
#--------------------------------------------------------------
            elif msg.text in ["Banned"]:
                if msg.from_ in admin:
                    wait["wblacklist"] = True
                    cl.sendText(msg.to,"send contact")
            elif msg.text in ["Unbanned"]:
                if msg.from_ in admin:
                    wait["dblacklist"] = True
                    cl.sendText(msg.to,"send contact")
   #---------Fungsi Banlist With Tag--------#
            elif msg.text in ["Banlist","ip banlist"]:
              if msg.from_ in admin:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"No user is Blacklisted")
                else:
                    cl.sendText(msg.to,"Blacklisted user")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +ki.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    print "[Command]Banlist executed"
   #---------Fungsi Banlist With Tag Finish--------#


#--------------------------------------------------------------
            elif msg.text in ["Kill"]:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        group = cl.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in wait["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            ki.sendText(msg.to,"There was no blacklist user")
                        #ki2.sendText(msg.to,"There was no blacklist user")
                        #ki3.sendText(msg.to,"There was no blacklist user")
                            return
                        for jj in matched_list:
                            random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                        ki.sendText(msg.to,"Blacklist emang pantas tuk di usir")
#-------------------------------------------------------------------------------
            elif msg.text in ["Gcreator:inv"]:
              if msg.toType == 2:
                ginfo = cl.getGroup(msg.to)
                gCreator = ginfo.creator.mid
                try:
                    cl.findAndAddContactsByMid(gCreator)
                    cl.inviteIntoGroup(msg.to,[gCreator])
                    print "SUKSES INVITE GCREATOR"
                except:
                    pass
            elif msg.text in ["Clear"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        ki.cancelGroupInvitation(msg.to,[_mid])
                    ki.sendText(msg.to,"I pretended to cancel and canceled.")

            elif "midb:" in msg.text:
                midd = msg.text.replace("midb:","")
                wait["blacklist"][midd] = True

            elif "#終了" in msg.text:
                try:
                    import sys
                    sys.exit()
                except:
                    pass
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

def autolike():
    for zx in range(0,20):
        hasil = cl.activity(limit=20)
    if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
        try:
            cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like By : IP\n\nhttp://line.me/ti/p/Tq1A2KSg0K")
            print "Like"
        except:
            pass
    else:
        print "Already Liked"
        time.sleep(500)
while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
