from LineAPI.linepy import *
from LineAPI.akad.ttypes import *
from multiprocessing import Pool, Process
from LineAPI.akad.ttypes import ContentType as Type
from gtts import gTTS
from time import sleep
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from googletrans import Translator
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, six, ast, pytz, urllib, urllib3, urllib.parse, traceback, atexit, subprocess,html5lib

#ririn = LINE("TOKENMU")
#ririn = LINE("EAIFkaHLR5Z3sDuZITI4.QsIZ0MXwN8b4syWcqqzz5a.lLsfayHD0cIZ5RDUaVxRCHF7ep5882cIo+bwQVNEM2o=")
ririn = LINE("EA2PlRvjcvkUlJETFSpb.NIeRDPE7hLtZYua3WkTrgW./BGNlJDI0enTU4qvIc+gnTaQBkfGjsqgTsNmFD2qsyw=")

ririnMid = ririn.profile.mid
ririnProfile = ririn.getProfile()
ririnSettings = ririn.getSettings()
ririnPoll = OEPoll(ririn)
botStart = time.time()
temp_flood = {}
msg_dict = {}

wait = {
    "autoAdd": True,
    "autoCancel": {"on":True,"members":3},
    "autoJoin": True,
    "autoLeave": False,
    "autoRead": False,
    "autoRespon": True,
    "autoReply": False,
    "autoJoinTicket": True,
    "checkContact": False,
    "checkPost": True,
    "checkSticker": False,
    "changePictureProfile": False,
    "changeCover": False,
    "changeGroupPicture": [],
    "invite": {},
    "keyCommand": "",
    "leaveRoom": True,
    "myProfile": {
        "displayName": "",
        "coverId": "",
        "pictureStatus": "",
        "statusMessage": ""
    },
    "mimic": {
        "copy": False,
        "status": False,
        "target": {}
    },
    "Protectcancel": True,
    "Protectgr": True,
    "Protectinvite": True,
    "Protectjoin": False,
    "setKey": False,
    "sider": False,
    "unsendMessage": True
}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

read = {
    "ROM": {},
    "readPoint": {},
    "readMember": {},
    "readTime": {}
}

list_language = {
    "list_textToSpeech": {
        "id": "Indonesia",
        "af" : "Afrikaans",
        "sq" : "Albanian",
        "ar" : "Arabic",
        "hy" : "Armenian",
        "bn" : "Bengali",
        "ca" : "Catalan",
        "zh" : "Chinese",
        "zh-cn" : "Chinese (Mandarin/China)",
        "zh-tw" : "Chinese (Mandarin/Taiwan)",
        "zh-yue" : "Chinese (Cantonese)",
        "hr" : "Croatian",
        "cs" : "Czech",
        "da" : "Danish",
        "nl" : "Dutch",
        "en" : "English",
        "en-au" : "English (Australia)",
        "en-uk" : "English (United Kingdom)",
        "en-us" : "English (United States)",
        "eo" : "Esperanto",
        "fi" : "Finnish",
        "fr" : "French",
        "de" : "German",
        "el" : "Greek",
        "hi" : "Hindi",
        "hu" : "Hungarian",
        "is" : "Icelandic",
        "id" : "Indonesian",
        "it" : "Italian",
        "ja" : "Japanese",
        "km" : "Khmer (Cambodian)",
        "ko" : "Korean",
        "la" : "Latin",
        "lv" : "Latvian",
        "mk" : "Macedonian",
        "no" : "Norwegian",
        "pl" : "Polish",
        "pt" : "Portuguese",
        "ro" : "Romanian",
        "ru" : "Russian",
        "sr" : "Serbian",
        "si" : "Sinhala",
        "sk" : "Slovak",
        "es" : "Spanish",
        "es-es" : "Spanish (Spain)",
        "es-us" : "Spanish (United States)",
        "sw" : "Swahili",
        "sv" : "Swedish",
        "ta" : "Tamil",
        "th" : "Thai",
        "tr" : "Turkish",
        "uk" : "Ukrainian",
        "vi" : "Vietnamese",
        "cy" : "Welsh"
    },
    "list_translate": {    
        "af": "afrikaans",
        "sq": "albanian",
        "am": "amharic",
        "ar": "arabic",
        "hy": "armenian",
        "az": "azerbaijani",
        "eu": "basque",
        "be": "belarusian",
        "bn": "bengali",
        "bs": "bosnian",
        "bg": "bulgarian",
        "ca": "catalan",
        "ceb": "cebuano",
        "ny": "chichewa",
        "zh-cn": "chinese (simplified)",
        "zh-tw": "chinese (traditional)",
        "co": "corsican",
        "hr": "croatian",
        "cs": "czech",
        "da": "danish",
        "nl": "dutch",
        "en": "english",
        "eo": "esperanto",
        "et": "estonian",
        "tl": "filipino",
        "fi": "finnish",
        "fr": "french",
        "fy": "frisian",
        "gl": "galician",
        "ka": "georgian",
        "de": "german",
        "el": "greek",
        "gu": "gujarati",
        "ht": "haitian creole",
        "ha": "hausa",
        "haw": "hawaiian",
        "iw": "hebrew",
        "hi": "hindi",
        "hmn": "hmong",
        "hu": "hungarian",
        "is": "icelandic",
        "ig": "igbo",
        "id": "indonesian",
        "ga": "irish",
        "it": "italian",
        "ja": "japanese",
        "jw": "javanese",
        "kn": "kannada",
        "kk": "kazakh",
        "km": "khmer",
        "ko": "korean",
        "ku": "kurdish (kurmanji)",
        "ky": "kyrgyz",
        "lo": "lao",
        "la": "latin",
        "lv": "latvian",
        "lt": "lithuanian",
        "lb": "luxembourgish",
        "mk": "macedonian",
        "mg": "malagasy",
        "ms": "malay",
        "ml": "malayalam",
        "mt": "maltese",
        "mi": "maori",
        "mr": "marathi",
        "mn": "mongolian",
        "my": "myanmar (burmese)",
        "ne": "nepali",
        "no": "norwegian",
        "ps": "pashto",
        "fa": "persian",
        "pl": "polish",
        "pt": "portuguese",
        "pa": "punjabi",
        "ro": "romanian",
        "ru": "russian",
        "sm": "samoan",
        "gd": "scots gaelic",
        "sr": "serbian",
        "st": "sesotho",
        "sn": "shona",
        "sd": "sindhi",
        "si": "sinhala",
        "sk": "slovak",
        "sl": "slovenian",
        "so": "somali",
        "es": "spanish",
        "su": "sundanese",
        "sw": "swahili",
        "sv": "swedish",
        "tg": "tajik",
        "ta": "tamil",
        "te": "telugu",
        "th": "thai",
        "tr": "turkish",
        "uk": "ukrainian",
        "ur": "urdu",
        "uz": "uzbek",
        "vi": "vietnamese",
        "cy": "welsh",
        "xh": "xhosa",
        "yi": "yiddish",
        "yo": "yoruba",
        "zu": "zulu",
        "fil": "Filipino",
        "he": "Hebrew"
    }
}

try:
    with open("Log_data.json","r",encoding="utf_8_sig") as f:
        msg_dict = json.loads(f.read())
except:
    print("╔═════════════════════════\n║╔════════════════════════\n║╠❂➣ DNA BERHASIL LOGIN\n║╚════════════════════════\n╚═════════════════════════")
    
wait["myProfile"]["displayName"] = ririnProfile.displayName
wait["myProfile"]["statusMessage"] = ririnProfile.statusMessage
wait["myProfile"]["pictureStatus"] = ririnProfile.pictureStatus
coverId = ririn.getProfileDetail()["result"]["objectId"]
wait["myProfile"]["coverId"] = coverId
apikey_com = "ua928b3d26c569fc078498c02410659e4"
Extr = ririn.getContact(apikey_com).displayName

def restartBot():
    print ("[ INFO ] BOT RESTART")
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
def delExpire():
    if temp_flood != {}:
        for tmp in temp_flood:
            if temp_flood[tmp]["expire"] == True:
                if time.time() - temp_flood[tmp]["time"] >= 3*10:
                    temp_flood[tmp]["expire"] = False
                    temp_flood[tmp]["time"] = time.time()
                    try:
                        ririn.sendMessage(tmp, "Bot kembali aktif")
                    except Exception as error:
                        logError(error)
    
def logError(text):
    ririn.log("[ ERROR ] {}".format(str(text)))
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = "{}, {} - {} - {} | {}".format(str(hasil), str(inihari.strftime('%d')), str(bln), str(inihari.strftime('%Y')), str(inihari.strftime('%H:%M:%S')))
    with open("logError.txt","a") as error:
        error.write("\n[ {} ] {}".format(str(time), text))

def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > timedelta(1):
            if "path" in msg_dict[data]:
                ririn.deleteFile(msg_dict[data]["path"])
            del msg_dict[data]
            
def sendMention2(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@dee "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    ririn.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

# DEF MENTION FOOTER
# SC Ori SendMentionV2 By Zero

def sendMention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@Meka Finee "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    ririn.sendMessage(to, textx, {'AGENT_NAME':'「 My Creator 」', 'AGENT_LINK': 'http://line.me/ti/p/ppgIZ0JLDW', 'AGENT_ICON': "https://preview.ibb.co/dpBpCd/20180601_164057.png", 'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def command(text):
    pesan = text.lower()
    if wait["setKey"] == True:
        if pesan.startswith(wait["keyCommand"]):
            cmd = pesan.replace(wait["keyCommand"],"")
        else:
            cmd = "Undefined command"
    else:
        cmd = text.lower()
    return cmd
    
def changeVideoAndPictureProfile(pict, vids):
    try:
        files = {'file': open(vids, 'rb')}
        obs_params = ririn.genOBSParams({'oid': ririnMid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4', 'name': 'Hello_World.mp4'})
        data = {'params': obs_params}
        r_vp = ririn.server.postContent('{}/talk/vp/upload.nhn'.format(str(ririn.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return "Failed update profile"
        ririn.updateProfilePicture(pict, 'vp')
        return "Success update profile"
    except Exception as e:
    	raise Exception("Error change video and picture profile %s"%str(e))

def Musik(to):
    contentMetadata={'previewUrl': "http://dl.profile.line-cdn.net/"+ririn.getContact(ririnMid).picturePath, 'i-installUrl': 'http://itunes.apple.com/app/linemusic/id966142320', 'type': 'mt', 'subText': ririn.getContact(ririnMid).statusMessage if ririn.getContact(ririnMid).statusMessage != '' else 'creator By ɪ̶ɴ̶ɪ̶ᴛ̶ɪ̶ᴀ̶ʟ̶ ᴅ |ID LINE|\nririn.90', 'a-installUrl': 'market://details?id=jp.linecorp.linemusic.android', 'a-packageName': 'jp.linecorp.linemusic.android', 'countryCode': 'JP', 'a-linkUri': 'linemusic://open?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1', 'i-linkUri': 'linemusic://open?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1', 'text': ririn.getContact(ririnMid).displayName, 'id': 'mt000000000d69e2db', 'linkUri': 'https://music.me.me/launch?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1','MSG_SENDER_ICON': "https://os.me.naver.jp/os/p/"+ririnMid,'MSG_SENDER_NAME':  ririn.getContact(ririnMid).displayName,}
    return ririn.sendMessage(to, ririn.getContact(ririnMid).displayName, contentMetadata, 19)
    
def RunTheRun(to, mid, firstmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x \n"
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        today = datetime.today()
        future = datetime(2018,7,25)
        hari = (str(future - today))
        comma = hari.find(",")
        hari = hari[:comma]
        teman = ririn.getAllContactIds()
        gid = ririn.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        eltime = time.time() - mulai
        bot = runtime(eltime)
        h = ririn.getContact(ririnMid)
        ririn.reissueUserTicket()
        My_Id = "http://line.me/ti/p/"+ririn.getUserTicket().id
        text += mention+"WAKTU : "+datetime.strftime(timeNow,'%H:%M:%S')+" INDONESIA\n\nMY GROUP : "+str(len(gid))+"\n\nMY FRIEND: "+str(len(teman))+"\n\nTIME VPS : In "+hari+"\n\nᴄʀᴇᴀᴛᴏʀ ʙʏ : ᴘʀᴀɴᴋʙᴏᴛs. ʟɪɴᴇ ᴠᴇʀ.8.14.2\n\nTANGGAL : "+datetime.strftime(timeNow,'%Y-%m-%d')+"\n\nTIME RUN : \n • "+bot+"\n\nMY TOKEN : "+str(ririn.authToken)+"\n\nMY MID : "+h.mid+"\n\nMY ID LINE : "+My_Id
        ririn.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        ririn.sendMessage(to, "Error :\n" + str(error))

def helpmessage():
    if wait['setKey'] == True:
        key = wait['keyCommand']
    else:
        key = ''
    helpMessage =   "╔════════════════════╗" + "\n" + \
                    "                    ✰ ᴅɴᴀ ʙᴏᴛ ✰" + "\n" + \
                    "╚════════════════════╝" + "\n" + \
                    "╔════════════════════╗" + "\n" + \
                    "    ✪ 🅷🅴🅻🅿 🅼🅴🆂🆂🅰🅶🅴 ✪" + "\n" + \
                    "╠════════════════════╝" + "\n" + \
                    "╠❂➣ " + key + "ʜᴇʟᴘ " + "\n" + \
                    "╠❂➣ " + key + "ʜᴇʟᴘ sᴇʟғ " + "\n" + \
                    "╠❂➣ " + key + "ʜᴇʟᴘ sᴘᴇᴄɪᴀʟ " + "\n" + \
                    "╠❂➣ " + key + "ʜᴇʟᴘ sᴇᴛᴛɪɴɢs " + "\n" + \
                    "╠❂➣ " + key + "ʜᴇʟᴘ ɢʀᴏᴜᴘ " + "\n" + \
                    "╠❂➣ " + key + "ʜᴇʟᴘ ᴍᴇᴅɪᴀ " + "\n" + \
                    "╠❂➣ " + key + "ʜᴇʟᴘ sᴛᴀᴛᴜs " + "\n" + \
                    "╠❂➣ " + key + "ʜᴇʟᴘ ᴛᴛs " + "\n" + \
                    "╠❂➣ " + key + "ʜᴇʟᴘ ᴛʀᴀɴsʟᴀᴛᴇ " + "\n" + \
                    "╠════════════════════╗" + "\n" + \
                    "              ᴄʀᴇᴅɪᴛs ʙʏ : ɪ̶ɴ̶ɪ̶ᴛ̶ɪ̶ᴀ̶ʟ̶ ᴅ" + "\n" + \
                    "╚════════════════════╝" + "\n" + \
                    "╔════════════════════╗" + "\n" + \
                    "                   ✰ ᴅɴᴀ ʙᴏᴛ  ✰" + "\n" + \
                    "╚════════════════════╝"
    return helpMessage

def helpself():
    if wait['setKey'] == True:
        key = wait['keyCommand']
    else:
        key = ''
    helpSelf =   "╔════════════════════╗" + "\n" + \
                    "                    ✰ ᴅɴᴀ ʙᴏᴛ ✰" + "\n" + \
                    "╚════════════════════╝" + "\n" + \
                    "╔════════════════════╗" + "\n" + \
                    "                    ✪ 🆂🅴🅻🅵 ✪" + "\n" + \
                    "╠════════════════════╝" + "\n" + \
                    "╠❂➣ " + key + "ᴀʙᴏᴜᴛ" + "\n" + \
                    "╠❂➣ " + key + "ʙᴀᴄᴋᴜᴘ ᴘʀᴏғɪʟᴇ" + "\n" + \
                    "╠❂➣ " + key + "ʀᴇsᴛᴏʀᴇ ᴘʀᴏғɪʟᴇ" + "\n" + \
                    "╠❂➣ " + key + "ᴄʜᴀɴɢᴇʙɪᴏ「ǫᴜᴇʀʏ」" + "\n" + \
                    "╠❂➣ " + key + "ᴄʜᴀɴɢᴇ ᴘɪᴄᴛᴜʀᴇᴘʀᴏғɪʟᴇ" + "\n" + \
                    "╠❂➣ " + key + "ᴄʜᴀɴɢᴇ ᴅᴜᴀʟ「ᴏɴʟʏ ᴄʀᴇᴀᴛᴏʀ」" + "\n" + \
                    "╠❂➣ " + key + "ᴄʜᴀɴɢᴇɴᴀᴍᴇ「ǫᴜᴇʀʏ」" + "\n" + \
                    "╠❂➣ " + key + "ᴄʟᴏɴᴇ ᴘʀᴏғɪʟᴇ「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
                    "╠❂➣ " + key + "ᴍᴇ" + "\n" + \
                    "╠❂➣ " + key + "ᴍʏᴍɪᴅ" + "\n" + \
                    "╠❂➣ " + key + "ᴍʏɴᴀᴍᴇ" + "\n" + \
                    "╠❂➣ " + key + "ᴍʏʙɪᴏ" + "\n" + \
                    "╠❂➣ " + key + "ᴍʏᴘɪᴄᴛᴜʀᴇ" + "\n" + \
                    "╠❂➣ " + key + "ᴍʏᴠɪᴅᴇᴏᴘʀᴏғɪʟᴇ" + "\n" + \
                    "╠❂➣ " + key + "ᴍʏᴄᴏᴠᴇʀ" + "\n" + \
                    "╠❂➣ " + key + "sᴛᴇᴀʟʙɪᴏ「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
                    "╠❂➣ " + key + "sᴛᴇᴀʟᴄᴏɴᴛᴀᴄᴛ「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
                    "╠❂➣ " + key + "sᴛᴇᴀʟᴄᴏᴠᴇʀ「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
                    "╠❂➣ " + key + "sᴛᴇᴀʟᴍɪᴅ「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
                    "╠❂➣ " + key + "sᴛᴇᴀʟɴᴀᴍᴇ「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
                    "╠❂➣ " + key + "sᴛᴇᴀʟᴘɪᴄᴛᴜʀᴇ「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
                    "╠❂➣ " + key + "sᴛᴇᴀʟᴠɪᴅᴇᴏᴘʀᴏғɪʟᴇ「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
                    "╠❂➣ " + key + "sᴛᴇᴀʟᴅᴜᴀʟᴘʀᴏғɪʟᴇ「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
                    "╠════════════════════╗" + "\n" + \
                    "              ᴄʀᴇᴅɪᴛs ʙʏ : ɪ̶ɴ̶ɪ̶ᴛ̶ɪ̶ᴀ̶ʟ̶ ᴅ" + "\n" + \
                    "╚════════════════════╝" + "\n" + \
                    "╔════════════════════╗" + "\n" + \
                    "                   ✰ ᴅɴᴀ ʙᴏᴛ  ✰" + "\n" + \
                    "╚════════════════════╝"
    return helpSelf

def helpspecial():
    if wait['setKey'] == True:
        key = wait['keyCommand']
    else:
        key = ''
    helpSpecial =   "╔════════════════════╗" + "\n" + \
                    "                    ✰ ᴅɴᴀ ʙᴏᴛ ✰" + "\n" + \
                    "╚════════════════════╝" + "\n" + \
                    "╔════════════════════╗" + "\n" + \
                    "             ✪ 🆂🅿🅴🅲🅸🅰🅻 ✪" + "\n" + \
                    "╠════════════════════╝" + "\n" + \
                    "╠❂➣ " + key + "ʙᴄ「ᴛᴇxᴛ」" + "\n" + \
                    "╠❂➣ " + key + "ɢʙᴄ「ᴛᴇxᴛ」" + "\n" + \
                    "╠❂➣ " + key + "ᴄʀᴀsʜ" + "\n" + \
                    "╠❂➣ " + key + "ʟᴜʀᴋɪɴɢ" + "\n" + \
                    "╠❂➣ " + key + "ʟᴜʀᴋɪɴɢ「ᴏɴ/ᴏғғ/ʀᴇsᴇᴛ」" + "\n" + \
                    "╠❂➣ " + key + "ᴍᴇɴᴛɪᴏɴ" + "\n" + \
                    "╠❂➣ " + key + "ᴍɪᴍɪᴄᴀᴅᴅ「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
                    "╠❂➣ " + key + "ᴍɪᴍɪᴄᴅᴇʟ「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
                    "╠❂➣ " + key + "ᴍɪᴍɪᴄʟɪsᴛ" + "\n" + \
                    "╠❂➣ " + key + "ᴍɪᴍɪᴄ「ᴏɴ/ᴏғғ」" + "\n" + \
                    "╠❂➣ " + key + "sɪᴅᴇʀ「ᴏɴ/ᴏғғ」" + "\n" + \
                    "╠════════════════════╗" + "\n" + \
                    "              ᴄʀᴇᴅɪᴛs ʙʏ : ɪ̶ɴ̶ɪ̶ᴛ̶ɪ̶ᴀ̶ʟ̶ ᴅ" + "\n" + \
                    "╚════════════════════╝" + "\n" + \
                    "╔════════════════════╗" + "\n" + \
                    "                   ✰ ᴅɴᴀ ʙᴏᴛ  ✰" + "\n" + \
                    "╚════════════════════╝"
    return helpSpecial

def helpsettings():
    if wait['setKey'] == True:
        key = wait['keyCommand']
    else:
        key = ''
    helpSettings =   "╔════════════════════╗" + "\n" + \
                    "                    ✰ ᴅɴᴀ ʙᴏᴛ ✰" + "\n" + \
                    "╚════════════════════╝" + "\n" + \
                    "╔════════════════════╗" + "\n" + \
                    "           ✪ 🆂🅴🆃🆃🅸🅽🅶🆂 ✪" + "\n" + \
                    "╠════════════════════╝" + "\n" + \
                    "╠❂➣ " + key + "ᴀᴜᴛᴏᴀᴅᴅ「ᴏɴ/ᴏғғ」" + "\n" + \
                    "╠❂➣ " + key + "ᴀᴜᴛᴏᴊᴏɪɴ「ᴏɴ/ᴏғғ」" + "\n" + \
                    "╠❂➣ " + key + "ᴀᴜᴛᴏᴊᴏɪɴᴛɪᴄᴋᴇᴛ「ᴏɴ/ᴏғғ」" + "\n" + \
                    "╠❂➣ " + key + "ᴀᴜᴛᴏʟᴇᴀᴠᴇ「ᴏɴ/ᴏғғ」" + "\n" + \
                    "╠❂➣ " + key + "ᴀᴜᴛᴏʀᴇᴀᴅ「ᴏɴ/ᴏғғ」" + "\n" + \
                    "╠❂➣ " + key + "ᴀᴜᴛᴏʀᴇsᴘᴏɴ「ᴏɴ/ᴏғғ」" + "\n" + \
                    "╠❂➣ " + key + "ᴀᴜᴛᴏʀᴇᴘʟʏ「ᴏɴ/ᴏғғ」" + "\n" + \
                    "╠❂➣ " + key + "ᴄʜᴇᴄᴋᴄᴏɴᴛᴀᴄᴛ「ᴏɴ/ᴏғғ」" + "\n" + \
                    "╠❂➣ " + key + "ᴄʜᴇᴄᴋᴘᴏsᴛ「ᴏɴ/ᴏғғ」" + "\n" + \
                    "╠❂➣ " + key + "ᴄʜᴇᴄᴋsᴛɪᴄᴋᴇʀ「ᴏɴ/ᴏғғ」" + "\n" + \
                    "╠❂➣ " + key + "ᴜɴsᴇɴᴅᴄʜᴀᴛ「ᴏɴ/ᴏғғ」" + "\n" + \
                    "╠════════════════════╗" + "\n" + \
                    "              ᴄʀᴇᴅɪᴛs ʙʏ : ɪ̶ɴ̶ɪ̶ᴛ̶ɪ̶ᴀ̶ʟ̶ ᴅ" + "\n" + \
                    "╚════════════════════╝" + "\n" + \
                    "╔════════════════════╗" + "\n" + \
                    "                   ✰ ᴅɴᴀ ʙᴏᴛ  ✰" + "\n" + \
                    "╚════════════════════╝"
    return helpSettings

def helpgroup():
    if wait['setKey'] == True:
        key = wait['keyCommand']
    else:
        key = ''
    helpGroup =   "╔════════════════════╗" + "\n" + \
                    "                    ✰ ᴅɴᴀ ʙᴏᴛ ✰" + "\n" + \
                    "╚════════════════════╝" + "\n" + \
                    "╔════════════════════╗" + "\n" + \
                    "                 ✪ 🅶🆁🅾🆄🅿 ✪" + "\n" + \
                    "╠════════════════════╝" + "\n" + \
                    "╠❂➣ " + key + "ᴀɴɴᴏᴜɴᴄᴇ" + "\n" + \
                    "╠❂➣ " + key + "ᴄʜᴀɴɢᴇɢʀᴏᴜᴘᴘɪᴄᴛᴜʀᴇ" + "\n" + \
                    "╠❂➣ " + key + "ɢʀᴏᴜᴘᴄʀᴇᴀᴛᴏʀ" + "\n" + \
                    "╠❂➣ " + key + "ɢʀᴏᴜᴘɪᴅ" + "\n" + \
                    "╠❂➣ " + key + "ɢʀᴏᴜᴘɴᴀᴍᴇ" + "\n" + \
                    "╠❂➣ " + key + "ɢʀᴏᴜᴘᴘɪᴄᴛᴜʀᴇ" + "\n" + \
                    "╠❂➣ " + key + "ɢʀᴏᴜᴘᴛɪᴄᴋᴇᴛ" + "\n" + \
                    "╠❂➣ " + key + "ɢʀᴏᴜᴘᴛɪᴄᴋᴇᴛ「ᴏɴ/ᴏғғ」" + "\n" + \
                    "╠❂➣ " + key + "ɢʀᴏᴜᴘᴍᴇᴍʙᴇʀʟɪsᴛ" + "\n" + \
                    "╠❂➣ " + key + "ɢʀᴏᴜᴘɪɴғᴏ" + "\n" + \
                    "╠❂➣ " + key + "ɢʀᴏᴜᴘʟɪsᴛ" + "\n" + \
                    "╠❂➣ " + key + "ɪɴᴠɪᴛᴇ" + "\n" + \
                    "╠❂➣ " + key + "ɪɴᴠɪᴛᴇɢᴄ「ᴀᴍᴏᴜɴᴛ」" + "\n" + \
                    "╠════════════════════╗" + "\n" + \
                    "              ᴄʀᴇᴅɪᴛs ʙʏ : ɪ̶ɴ̶ɪ̶ᴛ̶ɪ̶ᴀ̶ʟ̶ ᴅ" + "\n" + \
                    "╚════════════════════╝" + "\n" + \
                    "╔════════════════════╗" + "\n" + \
                    "                   ✰ ᴅɴᴀ ʙᴏᴛ  ✰" + "\n" + \
                    "╚════════════════════╝"
    return helpGroup

def helpmedia():
    if wait['setKey'] == True:
        key = wait['keyCommand']
    else:
        key = ''
    helpMedia =   "╔════════════════════╗" + "\n" + \
                    "                    ✰ ᴅɴᴀ ʙᴏᴛ ✰" + "\n" + \
                    "╚════════════════════╝" + "\n" + \
                    "╔════════════════════╗" + "\n" + \
                    "                  ✪ 🅼🅴🅳🅸🅰 ✪" + "\n" + \
                    "╠════════════════════╝" + "\n" + \
                    "╠❂➣ " + key + "ᴄʜᴇᴄᴋᴘʀᴀʏᴛɪᴍᴇ「ʟᴏᴄᴀᴛɪᴏɴ」" + "\n" + \
                    "╠❂➣ " + key + "ᴄʜᴇᴄᴋᴡᴇᴀᴛʜᴇʀ「ʟᴏᴄᴀᴛɪᴏɴ」" + "\n" + \
                    "╠❂➣ " + key + "ᴄʜᴇᴄᴋᴡᴇʙsɪᴛᴇ「ᴜʀʟ」" + "\n" + \
                    "╠❂➣ " + key + "ɪɴsᴛᴀɢʀᴀᴍ「ᴜsᴇʀɴᴀᴍᴇ」" + "\n" + \
                    "╠❂➣ " + key + "ᴊᴀᴅᴡᴀʟ ᴛᴠ" + "\n" + \
                    "╠❂➣ " + key + "ʀᴇᴛʀᴏᴡᴀᴠᴇ:「ᴛᴇxᴛ:ᴛᴇxᴛ:ᴛᴇxᴛ」" + "\n" + \
                    "╠❂➣ " + key + "sᴇᴀʀᴄʜɪᴍᴀɢᴇ 「sᴇᴀʀᴄʜ」" + "\n" + \
                    "╠❂➣ " + key + "sᴇᴀʀᴄʜᴍᴜsɪᴄ 「sᴇᴀʀᴄʜ」" + "\n" + \
                    "╠❂➣ " + key + "sᴇᴀʀᴄʜʏᴏᴜᴛᴜʙᴇ「sᴇᴀʀᴄʜ」" + "\n" + \
                    "╠❂➣ " + key + "ᴛɪᴋᴛᴏᴋ" + "\n" + \
                    "╠❂➣ " + key + "ʏᴛᴍᴘ3:「ᴜʀʟ」" + "\n" + \
                    "╠❂➣ " + key + "ʏᴛᴍᴘ4:「ᴜʀʟ」" + "\n" + \
                    "╠❂➣ " + key + "/ᴄᴀʟʟ「ɴᴏ ᴛʟᴘ」" + "\n" + \
                    "╠❂➣ " + key + "/sᴍs:「ɴᴏ ᴛʟᴘ」" + "\n" + \
                    "╠════════════════════╗" + "\n" + \
                    "              ᴄʀᴇᴅɪᴛs ʙʏ : ɪ̶ɴ̶ɪ̶ᴛ̶ɪ̶ᴀ̶ʟ̶ ᴅ" + "\n" + \
                    "╚════════════════════╝" + "\n" + \
                    "╔════════════════════╗" + "\n" + \
                    "                   ✰ ᴅɴᴀ ʙᴏᴛ  ✰" + "\n" + \
                    "╚════════════════════╝"
    return helpMedia

def helpstatus():
    if wait['setKey'] == True:
        key = wait['keyCommand']
    else:
        key = ''
    helpStatus =   "╔════════════════════╗" + "\n" + \
                    "                    ✰ ᴅɴᴀ ʙᴏᴛ ✰" + "\n" + \
                    "╚════════════════════╝" + "\n" + \
                    "╔════════════════════╗" + "\n" + \
                    "               ✪ 🆂🆃🅰🆃🆄🆂 ✪" + "\n" + \
                    "╠════════════════════╝" + "\n" + \
                    "╠❂➣ " + key + "ʀᴇsᴛᴀʀᴛ" + "\n" + \
                    "╠❂➣ " + key + "ʀᴜɴᴛɪᴍᴇ" + "\n" + \
                    "╠❂➣ " + key + "sᴘ" + "\n" + \
                    "╠❂➣ " + key + "sᴘᴇᴇᴅ" + "\n" + \
                    "╠❂➣ " + key + "sᴛᴀᴛᴜs" + "\n" + \
                    "╠❂➣ ᴍʏᴋᴇʏ" + "\n" + \
                    "╠❂➣ sᴇᴛᴋᴇʏ「ᴏɴ/ᴏғғ」" + "\n" + \
                    "╠════════════════════╗" + "\n" + \
                    "              ᴄʀᴇᴅɪᴛs ʙʏ : ɪ̶ɴ̶ɪ̶ᴛ̶ɪ̶ᴀ̶ʟ̶ ᴅ" + "\n" + \
                    "╚════════════════════╝" + "\n" + \
                    "╔════════════════════╗" + "\n" + \
                    "                   ✰ ᴅɴᴀ ʙᴏᴛ  ✰" + "\n" + \
                    "╚════════════════════╝"
    return helpStatus

def helptexttospeech():
    if wait['setKey'] == True:
        key = wait['keyCommand']
    else:
        key = ''
    helpTextToSpeech =  "╔════════════════════╗" + "\n" + \
                        "                    ✰ ᴅɴᴀ ʙᴏᴛ ✰" + "\n" + \
                        "╚════════════════════╝" + "\n" + \
                        "╔════════════════════╗" + "\n" + \
                        "          ◄]·✪·ᴛᴇxᴛᴛᴏsᴘᴇᴇᴄʜ·✪·[►" + "\n" + \
                        "╠════════════════════╝ " + "\n" + \
                        "╠❂➣ " + key + "ᴀғ : ᴀғʀɪᴋᴀᴀɴs" + "\n" + \
                        "╠❂➣ " + key + "sǫ : ᴀʟʙᴀɴɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴀʀ : ᴀʀᴀʙɪᴄ" + "\n" + \
                        "╠❂➣ " + key + "ʜʏ : ᴀʀᴍᴇɴɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ʙɴ : ʙᴇɴɢᴀʟɪ" + "\n" + \
                        "╠❂➣ " + key + "ᴄᴀ : ᴄᴀᴛᴀʟᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴢʜ : ᴄʜɪɴᴇsᴇ" + "\n" + \
                        "╠❂➣ " + key + "ᴢʜʏᴜᴇ : ᴄʜɪɴᴇsᴇ (ᴄᴀɴᴛᴏɴᴇsᴇ)" + "\n" + \
                        "╠❂➣ " + key + "ʜʀ : ᴄʀᴏᴀᴛɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴄs : ᴄᴢᴇᴄʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴅᴀ : ᴅᴀɴɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ɴʟ : ᴅᴜᴛᴄʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴇɴ : ᴇɴɢʟɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴇɴᴀᴜ : ᴇɴɢʟɪsʜ (ᴀᴜsᴛʀᴀʟɪᴀ)" + "\n" + \
                        "╠❂➣ " + key + "ᴇɴᴜᴋ : ᴇɴɢʟɪsʜ (ᴜᴋ)" + "\n" + \
                        "╠❂➣ " + key + "ᴇɴᴜs : ᴇɴɢʟɪsʜ (ᴜs)" + "\n" + \
                        "╠❂➣ " + key + "ᴇᴏ : ᴇsᴘᴇʀᴀɴᴛᴏ" + "\n" + \
                        "╠❂➣ " + key + "ғɪ : ғɪɴɴɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ғʀ : ғʀᴇɴᴄʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴅᴇ : ɢᴇʀᴍᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴇʟ : ɢʀᴇᴇᴋ" + "\n" + \
                        "╠❂➣ " + key + "ʜɪ : ʜɪɴᴅɪ" + "\n" + \
                        "╠❂➣ " + key + "ʜᴜ : ʜᴜɴɢᴀʀɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ɪs : ɪᴄᴇʟᴀɴᴅɪᴄ" + "\n" + \
                        "╠❂➣ " + key + "ɪᴅ : ɪɴᴅᴏɴᴇsɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ɪᴛ : ɪᴛᴀʟɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴊᴀ : ᴊᴀᴘᴀɴᴇsᴇ" + "\n" + \
                        "╠❂➣ " + key + "ᴋᴍ : ᴋʜᴍᴇʀ (ᴄᴀᴍʙᴏᴅɪᴀɴ)" + "\n" + \
                        "╠❂➣ " + key + "ᴋᴏ : ᴋᴏʀᴇᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ʟᴀ : ʟᴀᴛɪɴ" + "\n" + \
                        "╠❂➣ " + key + "ʟᴠ : ʟᴀᴛᴠɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴍᴋ : ᴍᴀᴄᴇᴅᴏɴɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ɴᴏ : ɴᴏʀᴡᴇɢɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴘʟ : ᴘᴏʟɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴘᴛ : ᴘᴏʀᴛᴜɢᴜᴇsᴇ" + "\n" + \
                        "╠❂➣ " + key + "ʀᴏ : ʀᴏᴍᴀɴɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ʀᴜ : ʀᴜssɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "sʀ : sᴇʀʙɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "sɪ : sɪɴʜᴀʟᴀ" + "\n" + \
                        "╠❂➣ " + key + "sᴋ : sʟᴏᴠᴀᴋ" + "\n" + \
                        "╠❂➣ " + key + "ᴇs : sᴘᴀɴɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴇsᴇs : sᴘᴀɴɪsʜ (sᴘᴀɪɴ)" + "\n" + \
                        "╠❂➣ " + key + "ᴇsᴜs : sᴘᴀɴɪsʜ (ᴜs)" + "\n" + \
                        "╠❂➣ " + key + "sᴡ : sᴡᴀʜɪʟɪ" + "\n" + \
                        "╠❂➣ " + key + "sᴠ : sᴡᴇᴅɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴛᴀ : ᴛᴀᴍɪʟ" + "\n" + \
                        "╠❂➣ " + key + "ᴛʜ : ᴛʜᴀɪ" + "\n" + \
                        "╠❂➣ " + key + "ᴛʀ : ᴛᴜʀᴋɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴜᴋ : ᴜᴋʀᴀɪɴɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴠɪ : ᴠɪᴇᴛɴᴀᴍᴇsᴇ" + "\n" + \
                        "╠❂➣ " + key + "ᴄʏ : ᴡᴇʟsʜ" + "\n" + \
                        "╠════════════════════╗" + "\n" + \
                        "              ᴄʀᴇᴅɪᴛs ʙʏ : ɪ̶ɴ̶ɪ̶ᴛ̶ɪ̶ᴀ̶ʟ̶ ᴅ" + "\n" + \
                        "╚════════════════════╝" + "\n" + \
                        "╔════════════════════╗" + "\n" + \
                        "                    ✰ ᴅɴᴀ ʙᴏᴛ ✰" + "\n" + \
                        "╚════════════════════╝" + "\n" + \
                        "ᴄᴏɴᴛᴏʜ : " + key + "sᴀʏ-ɪᴅ ʀɪʀɪɴ"
    return helpTextToSpeech

def helptranslate():
    if wait['setKey'] == True:
        key = wait['keyCommand']
    else:
        key = ''
    helpTranslate = "╔════════════════════╗" + "\n" + \
                        "                     ✰ ᴅɴᴀ ʙᴏᴛ ✰" + "\n" + \
                        "╚════════════════════╝" + "\n" + \
                        "╔════════════════════╗" + "\n" + \
                        "             ◄]·✪·ᴛʀᴀɴsʟᴀᴛᴇ·✪·[►" + "\n" + \
                        "╠════════════════════╝" + "\n" + \
                        "╠❂➣ " + key + "ᴀғ : ᴀғʀɪᴋᴀᴀɴs" + "\n" + \
                        "╠❂➣ " + key + "sǫ : ᴀʟʙᴀɴɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴀᴍ : ᴀᴍʜᴀʀɪᴄ" + "\n" + \
                        "╠❂➣ " + key + "ᴀʀ : ᴀʀᴀʙɪᴄ" + "\n" + \
                        "╠❂➣ " + key + "ʜʏ : ᴀʀᴍᴇɴɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴀᴢ : ᴀᴢᴇʀʙᴀɪᴊᴀɴɪ" + "\n" + \
                        "╠❂➣ " + key + "ᴇᴜ : ʙᴀsǫᴜᴇ" + "\n" + \
                        "╠❂➣ " + key + "ʙᴇ : ʙᴇʟᴀʀᴜsɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ʙɴ : ʙᴇɴɢᴀʟɪ" + "\n" + \
                        "╠❂➣ " + key + "ʙs : ʙᴏsɴɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ʙɢ : ʙᴜʟɢᴀʀɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴄᴀ : ᴄᴀᴛᴀʟᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴄᴇʙ : ᴄᴇʙᴜᴀɴᴏ" + "\n" + \
                        "╠❂➣ " + key + "ɴʏ : ᴄʜɪᴄʜᴇᴡᴀ" + "\n" + \
                        "╠❂➣ " + key + "ᴢʜᴄɴ : ᴄʜɪɴᴇsᴇ (sɪᴍᴘʟɪғɪᴇᴅ)" + "\n" + \
                        "╠❂➣ " + key + "ᴢʜᴛᴡ : ᴄʜɪɴᴇsᴇ (ᴛʀᴀᴅɪᴛɪᴏɴᴀʟ)" + "\n" + \
                        "╠❂➣ " + key + "ᴄᴏ : ᴄᴏʀsɪᴄᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ʜʀ : ᴄʀᴏᴀᴛɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴄs : ᴄᴢᴇᴄʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴅᴀ : ᴅᴀɴɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ɴʟ : ᴅᴜᴛᴄʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴇɴ : ᴇɴɢʟɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴇᴏ : ᴇsᴘᴇʀᴀɴᴛᴏ" + "\n" + \
                        "╠❂➣ " + key + "ᴇᴛ : ᴇsᴛᴏɴɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴛʟ : ғɪʟɪᴘɪɴᴏ" + "\n" + \
                        "╠❂➣ " + key + "ғɪ : ғɪɴɴɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ғʀ : ғʀᴇɴᴄʜ" + "\n" + \
                        "╠❂➣ " + key + "ғʏ : ғʀɪsɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ɢʟ : ɢᴀʟɪᴄɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴋᴀ : ɢᴇᴏʀɢɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴅᴇ : ɢᴇʀᴍᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴇʟ : ɢʀᴇᴇᴋ" + "\n" + \
                        "╠❂➣ " + key + "ɢᴜ : ɢᴜᴊᴀʀᴀᴛɪ" + "\n" + \
                        "╠❂➣ " + key + "ʜᴛ : ʜᴀɪᴛɪᴀɴ ᴄʀᴇᴏʟᴇ" + "\n" + \
                        "╠❂➣ " + key + "ʜᴀ : ʜᴀᴜsᴀ" + "\n" + \
                        "╠❂➣ " + key + "ʜᴀᴡ : ʜᴀᴡᴀɪɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ɪᴡ : ʜᴇʙʀᴇᴡ" + "\n" + \
                        "╠❂➣ " + key + "ʜɪ : ʜɪɴᴅɪ" + "\n" + \
                        "╠❂➣ " + key + "ʜᴍɴ : ʜᴍᴏɴɢ" + "\n" + \
                        "╠❂➣ " + key + "ʜᴜ : ʜᴜɴɢᴀʀɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ɪs : ɪᴄᴇʟᴀɴᴅɪᴄ" + "\n" + \
                        "╠❂➣ " + key + "ɪɢ : ɪɢʙᴏ" + "\n" + \
                        "╠❂➣ " + key + "ɪᴅ : ɪɴᴅᴏɴᴇsɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ɢᴀ : ɪʀɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ɪᴛ : ɪᴛᴀʟɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴊᴀ : ᴊᴀᴘᴀɴᴇsᴇ" + "\n" + \
                        "╠❂➣ " + key + "ᴊᴡ : ᴊᴀᴠᴀɴᴇsᴇ" + "\n" + \
                        "╠❂➣ " + key + "ᴋɴ : ᴋᴀɴɴᴀᴅᴀ" + "\n" + \
                        "╠❂➣ " + key + "ᴋᴋ : ᴋᴀᴢᴀᴋʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴋᴍ : ᴋʜᴍᴇʀ" + "\n" + \
                        "╠❂➣ " + key + "ᴋᴏ : ᴋᴏʀᴇᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴋᴜ : ᴋᴜʀᴅɪsʜ (ᴋᴜʀᴍᴀɴᴊɪ)" + "\n" + \
                        "╠❂➣ " + key + "ᴋʏ : ᴋʏʀɢʏᴢ" + "\n" + \
                        "╠❂➣ " + key + "ʟᴏ : ʟᴀᴏ" + "\n" + \
                        "╠❂➣ " + key + "ʟᴀ : ʟᴀᴛɪɴ" + "\n" + \
                        "╠❂➣ " + key + "ʟᴠ : ʟᴀᴛᴠɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ʟᴛ : ʟɪᴛʜᴜᴀɴɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ʟʙ : ʟᴜxᴇᴍʙᴏᴜʀɢɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴍᴋ : ᴍᴀᴄᴇᴅᴏɴɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴍɢ : ᴍᴀʟᴀɢᴀsʏ" + "\n" + \
                        "╠❂➣ " + key + "ᴍs : ᴍᴀʟᴀʏ" + "\n" + \
                        "╠❂➣ " + key + "ᴍʟ : ᴍᴀʟᴀʏᴀʟᴀᴍ" + "\n" + \
                        "╠❂➣ " + key + "ᴍᴛ : ᴍᴀʟᴛᴇsᴇ" + "\n" + \
                        "╠❂➣ " + key + "ᴍɪ : ᴍᴀᴏʀɪ" + "\n" + \
                        "╠❂➣ " + key + "ᴍʀ : ᴍᴀʀᴀᴛʜɪ" + "\n" + \
                        "╠❂➣ " + key + "ᴍɴ : ᴍᴏɴɢᴏʟɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴍʏ : ᴍʏᴀɴᴍᴀʀ (ʙᴜʀᴍᴇsᴇ)" + "\n" + \
                        "╠❂➣ " + key + "ɴᴇ : ɴᴇᴘᴀʟɪ" + "\n" + \
                        "╠❂➣ " + key + "ɴᴏ : ɴᴏʀᴡᴇɢɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴘs : ᴘᴀsʜᴛᴏ" + "\n" + \
                        "╠❂➣ " + key + "ғᴀ : ᴘᴇʀsɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴘʟ : ᴘᴏʟɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴘᴛ : ᴘᴏʀᴛᴜɢᴜᴇsᴇ" + "\n" + \
                        "╠❂➣ " + key + "ᴘᴀ : ᴘᴜɴᴊᴀʙɪ" + "\n" + \
                        "╠❂➣ " + key + "ʀᴏ : ʀᴏᴍᴀɴɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ʀᴜ : ʀᴜssɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "sᴍ : sᴀᴍᴏᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ɢᴅ : sᴄᴏᴛs ɢᴀᴇʟɪᴄ" + "\n" + \
                        "╠❂➣ " + key + "sʀ : sᴇʀʙɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "sᴛ : sᴇsᴏᴛʜᴏ" + "\n" + \
                        "╠❂➣ " + key + "sɴ : sʜᴏɴᴀ" + "\n" + \
                        "╠❂➣ " + key + "sᴅ : sɪɴᴅʜɪ" + "\n" + \
                        "╠❂➣ " + key + "sɪ : sɪɴʜᴀʟᴀ" + "\n" + \
                        "╠❂➣ " + key + "sᴋ : sʟᴏᴠᴀᴋ" + "\n" + \
                        "╠❂➣ " + key + "sʟ : sʟᴏᴠᴇɴɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "sᴏ : sᴏᴍᴀʟɪ" + "\n" + \
                        "╠❂➣ " + key + "ᴇs : sᴘᴀɴɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "sᴜ : sᴜɴᴅᴀɴᴇsᴇ" + "\n" + \
                        "╠❂➣ " + key + "sᴡ : sᴡᴀʜɪʟɪ" + "\n" + \
                        "╠❂➣ " + key + "sᴠ : sᴡᴇᴅɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴛɢ : ᴛᴀᴊɪᴋ" + "\n" + \
                        "╠❂➣ " + key + "ᴛᴀ : ᴛᴀᴍɪʟ" + "\n" + \
                        "╠❂➣ " + key + "ᴛᴇ : ᴛᴇʟᴜɢᴜ" + "\n" + \
                        "╠❂➣ " + key + "ᴛʜ : ᴛʜᴀɪ" + "\n" + \
                        "╠❂➣ " + key + "ᴛʀ : ᴛᴜʀᴋɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴜᴋ : ᴜᴋʀᴀɪɴɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴜʀ : ᴜʀᴅᴜ" + "\n" + \
                        "╠❂➣ " + key + "ᴜᴢ : ᴜᴢʙᴇᴋ" + "\n" + \
                        "╠❂➣ " + key + "ᴠɪ : ᴠɪᴇᴛɴᴀᴍᴇsᴇ" + "\n" + \
                        "╠❂➣ " + key + "ᴄʏ : ᴡᴇʟsʜ" + "\n" + \
                        "╠❂➣ " + key + "xʜ : xʜᴏsᴀ" + "\n" + \
                        "╠❂➣ " + key + "ʏɪ : ʏɪᴅᴅɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ʏᴏ : ʏᴏʀᴜʙᴀ" + "\n" + \
                        "╠❂➣ " + key + "ᴢᴜ : ᴢᴜʟᴜ" + "\n" + \
                        "╠❂➣ " + key + "ғɪʟ : ғɪʟɪᴘɪɴᴏ" + "\n" + \
                        "╠❂➣ " + key + "ʜᴇ : ʜᴇʙʀᴇᴡ" + "\n" + \
                        "╠════════════════════╗" + "\n" + \
                        "              ᴄʀᴇᴅɪᴛs ʙʏ : ɪ̶ɴ̶ɪ̶ᴛ̶ɪ̶ᴀ̶ʟ̶ ᴅ" + "\n" + \
                        "╚════════════════════╝" + "\n" + \
                        "╔════════════════════╗" + "\n" + \
                        "                    ✰ ᴅɴᴀ ʙᴏᴛ ✰" + "\n" + \
                        "╚════════════════════╝" + "\n" + \
                        "ᴄᴏɴᴛᴏʜ : " + key + "ᴛʀ-ɪᴅ ʀɪʀɪɴ"
    return helpTranslate
    
def ririnBot(op):
    try:
        if op.type == 0:
            print ("[ 0 ] Succes")
            return

        if op.type == 5:
            print ("[ 5 ] Add Contact")
            if wait["autoAdd"] == True:
                ririn.findAndAddContactsByMid(op.param1)
            ririn.sendMessageWithContent(op.param1, "╔════════════════════╗\n                   「ᴀᴜᴛᴏ ʀᴇᴘʟʏ」\n                             ʙʏ:\n                    ✰ ᴅɴᴀ ʙᴏᴛ ✰\n╚════════════════════╝\n       ʜᴀʟʟᴏ, ᴛʜᴀɴᴋs ғᴏʀ ᴀᴅᴅ ᴍᴇ\n\n                    ᴏᴘᴇɴ ᴏʀᴅᴇʀ :\n               ✪ sᴇʟғʙᴏᴛ ᴏɴʟʏ ✪\n            ✪ sᴇʟғʙᴏᴛ + ᴀssɪsᴛ ✪\n                ✪ ʙᴏᴛ ᴘʀᴏᴛᴇᴄᴛ ✪\n              「ᴀʟʟ ʙᴏᴛ ᴘʏᴛʜᴏɴ з」\n             ɪᴛs ᴄᴏᴏʟ ᴡɪᴛʜ ғᴏᴏᴛᴇʀ\n\n         ᴍɪɴᴀᴛ ᴘᴄ ᴀᴋᴜɴ ᴅɪ ғᴏᴏᴛᴇʀ :",'Auto Add.','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')

        if op.type == 13:
            print ("[ 13 ] Invite Into Group")
            if ririnMid in op.param3:
                if wait["autoJoin"] == True:
                    ririn.acceptGroupInvitation(op.param1)
                dan = ririn.getContact(op.param2)
                tgb = ririn.getGroup(op.param1)
                sendMention(op.param1, "ʜᴀʟᴏ @!, ᴛʜx ғᴏʀ ɪɴᴠɪᴛᴇ ᴍᴇ ᴛᴏ {}".format(str(tgb.name)),[op.param2])
                
        if op.type == 15:
        	dan = ririn.getContact(op.param2)
        	tgb = ririn.getGroup(op.param1)
        	sendMention(op.param1, "ɴᴀʜ ᴋᴀɴ ʙᴀᴘᴇʀ @!, ɢᴀᴋ ᴜsᴀʜ ʙᴀʟɪᴋ ᴅɪ {} ʟᴀɢɪ ʏᴀ\nsᴇʟᴀᴍᴀᴛ ᴊᴀʟᴀɴ ᴅᴀɴ sᴇᴍᴏɢᴀʜ ᴛᴇɴᴀɴɢ ᴅɪʟᴜᴀʀ sᴀɴᴀ 😘😘😘".format(str(tgb.name)),[op.param2])
        	
        if op.type == 17:
        	dan = ririn.getContact(op.param2)
        	tgb = ririn.getGroup(op.param1)
        	sendMention(op.param1, "ʜᴏʟᴀ @!,\nᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ɢʀᴏᴜᴘ {} \nᴊᴀɴɢᴀɴ ʟᴜᴘᴀ ᴄʜᴇᴄᴋ ɴᴏᴛᴇ ʏᴀ \nᴀᴡᴀs ᴋᴀʟᴀᴜ ʙᴀᴘᴇʀᴀɴ 😘😘😘".format(str(tgb.name)),[op.param2])

        if op.type == 22:
            if wait["leaveRoom"] == True:
                ririn.leaveRoom(op.param1)

        if op.type == 24:
            if wait["leaveRoom"] == True:
                ririn.leaveRoom(op.param1)

        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
                if wait["invite"] == True:
                    _name = msg.contentMetadata["displayName"]
                    invite = msg.contentMetadata["mid"]
                    groups = ririn.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            ririn.sendMessageWithContent(msg.to, _name +  " sᴜᴅᴀʜ ᴅɪ ᴅᴀʟᴀᴍ ɢʀᴜᴘ",'Invite User.','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                ririn.findAndAddContactsByMid(target)
                                ririn.inviteIntoGroup(msg.to,[target])
                                ririn.sendMessageWithContent(msg.to,"Invite " + _name,'Invite	User.','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                                wait["invite"] = False
                                break                              
                            except:             
                                    ririn.sendMessageWithContent(msg.to,"ᴇʀʀᴏʀ",'Invite	User.','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                                    wait["invite"] = False
                                    break
            else:
                if wait["invite"] == True:
                    _name = msg.contentMetadata["displayName"]
                    invite = msg.contentMetadata["mid"]
                    groups = ririn.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            ririn.sendMessageWithContent(msg.to, _name + " sᴜᴅᴀʜ ᴅɪ ᴅᴀʟᴀᴍ ɢʀᴜᴘ",'Invite Member.','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                ririn.findAndAddContactsByMid(target)
                                ririn.inviteIntoGroup(msg.to,[target])
                                ririn.sendMessageWithContent(msg.to,"Invite " + _name,'Invite Member.','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                                wait["invite"] = False
                                break                              
                            except:             
                                    ririn.sendMessageWithContent(msg.to,"ᴇʀʀᴏʀ",'Invite Member.','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                                    wait["invite"] = False
                                    break

        if op.type == 25:
            try:
                print ("[ 25 ] SEND MESSAGE")
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                setKey = wait["keyCommand"].title()
                if wait["setKey"] == False:
                    setKey = ''
                if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                    if msg.toType == 0:
                        if sender != ririn.profile.mid:
                            to = sender
                        else:
                            to = receiver
                    elif msg.toType == 1:
                        to = receiver
                    elif msg.toType == 2:
                        to = receiver
                    if msg.contentType == 0:
                        if text is None:
                            return
                        else:
                            cmd = command(text)
#------------------------------------============================------------------------------------#
#======================-----------✰ ᴅɴᴀ ʙᴏᴛ ✰-----------======================#
#------------------------------------============================------------------------------------#
                            if cmd == "help":
                                helpMessage = helpmessage()
                                ririn.sendMessageWithContent(to, str(helpMessage),'Help.','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                            elif cmd == "help settings":
                                helpSettings = helpsettings()
                                ririn.sendMessageWithContent(to, str(helpSettings),'Help Settings.','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                            elif cmd == "help status":
                                helpStatus = helpstatus()
                                ririn.sendMessageWithContent(to, str(helpStatus),'Help Status.','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                            elif cmd == "help self":
                                helpSelf = helpself()
                                ririn.sendMessageWithContent(to, str(helpSelf),'Help Self.','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                            elif cmd == "help special":
                                helpSpecial = helpspecial()
                                ririn.sendMessageWithContent(to, str(helpSpecial),'Help Special.','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                            elif cmd == "help group":
                                helpGroup = helpgroup()
                                ririn.sendMessageWithContent(to, str(helpGroup),'Help Group.','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                            elif cmd == "help media":
                                helpMedia = helpmedia()
                                ririn.sendMessageWithContent(to, str(helpMedia),'Help Media.','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                            elif cmd == "help tts":
                                helpTextToSpeech = helptexttospeech()
                                ririn.sendMessageWithContent(to, str(helpTextToSpeech),'Help Text To Speech.','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                            elif cmd.startswith("say-"):
                                sep = text.split("-")
                                sep = sep[1].split(" ")
                                lang = sep[0]
                                say = text.replace("say-" + lang + " ","")
                                if lang not in list_language["list_textToSpeech"]:
                                    return ririn.sendMessage(to, "Language not found")
                                tts = gTTS(text=say, lang=lang)
                                tts.save("hasil.mp3")
                                ririn.sendAudio(to,"hasil.mp3")
                            elif cmd == "help translate":
                                helpTranslate = helptranslate()
                                ririn.sendMessageWithContent(to, str(helpTranslate),'Help Translate.','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                            elif cmd.startswith("tr-"):
                                sep = text.split("-")
                                sep = sep[1].split(" ")
                                lang = sep[0]
                                say = text.replace("tr-" + lang + " ","")
                                if lang not in list_language["list_translate"]:
                                    return ririn.sendMessage(to, "Language not found")
                                translator = Translator()
                                hasil = translator.translate(say, dest=lang)
                                A = hasil.text
                                ririn.sendMessage(to, str(A))
#------------------------------------============================------------------------------------#
#======================-----------✰ ᴅɴᴀ ʙᴏᴛ ✰-----------======================#
#------------------------------------============================------------------------------------#
                            if cmd == "about":
                                try:
                                	arr = []
                                	owner = "ua928b3d26c569fc078498c02410659e4"
                                	creator = ririn.getContact(owner)
                                	contact = ririn.getContact(ririnMid)
                                	grouplist = ririn.getGroupIdsJoined()
                                	contactlist = ririn.getAllContactIds()
                                	blockedlist = ririn.getBlockedContactIds()
                                	mi_d = creator.mid
                                	ret_ = "╔══[ ᴀʙᴏᴜᴛ ʙᴏᴛ ]"
                                	ret_ += "\n╠✪ ʟɪɴᴇ : {}".format(contact.displayName)
                                	ret_ += "\n╠✪ ɢʀᴏᴜᴘ : {}".format(str(len(grouplist)))
                                	ret_ += "\n╠✪ ғʀɪᴇɴᴅ : {}".format(str(len(contactlist)))
                                	ret_ += "\n╠✪ ʙʟᴏᴄᴋᴇᴅ : {}".format(str(len(blockedlist)))
                                	ret_ += "\n╠══[ ᴀʙᴏᴜᴛ ʙᴏᴛ ]"
                                	ret_ += "\n╠✪ ᴠᴇʀsɪᴏɴ : ᴘʀᴇᴍɪᴜᴍ sᴇʟғ ᴘʏз"
                                	ret_ += "\n╠✪ ᴄʀᴇᴀᴛᴏʀ : {}".format(creator.displayName)
                                	ret_ += "\n╚══[ ᴅᴏɴ'ᴛ ʙᴇ ʀᴇᴍᴀᴋᴇ 😝 ]"
                                	ririn.sendMessageWithContent(msg.to, str(ret_),'Creator.','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                                	ririn.sendContact(msg.to, mi_d)
                                except Exception as e:
                                	ririn.sendMessageWithContent(msg.to, str(e),'Creator.','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                            elif cmd == "backup profile":
                                try:
                                    profile = ririn.getProfile()
                                    wait["myProfile"]["displayName"] = str(profile.displayName)
                                    wait["myProfile"]["statusMessage"] = str(profile.statusMessage)
                                    wait["myProfile"]["pictureStatus"] = str(profile.pictureStatus)
                                    coverId = ririn.getProfileDetail()["result"]["objectId"]
                                    wait["myProfile"]["coverId"] = str(coverId)
                                    ririn.sendMessageWithContent(to, "ʙᴀᴄᴋᴜᴘ ᴘʀᴏғɪʟᴇ sᴜᴄᴄᴇs",'Backup Profile.','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                                except Exception as e:
                                    ririn.sendMessageWithContent(to, "ʙᴀᴄᴋᴜᴘ ᴘʀᴏғɪʟᴇ ғᴀɪʟᴇᴅ",'Backup Profile.','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                                    logError(error)
                            elif cmd == "restore profile":
                                try:
                                    ririnProfile = ririn.getProfile()
                                    ririnProfile.displayName = str(wait["myProfile"]["displayName"])
                                    ririnProfile.statusMessage = str(wait["myProfile"]["statusMessage"])
                                    ririnProfile.pictureStatus = str(wait["myProfile"]["pictureStatus"])
                                    ririn.updateProfileAttribute(8, ririnProfile.pictureStatus)
                                    ririn.updateProfile(ririnProfile)
                                    coverId = str(wait["myProfile"]["coverId"])
                                    ririn.updateProfileCoverById(coverId)
                                    ririn.sendMessageWithContent(to, "ʀᴇsᴛᴏʀᴇ ᴘʀᴏғɪʟᴇ sᴜᴄᴄᴇs, ᴡᴀɪᴛ ᴀ ғᴇᴡ ᴍɪɴᴜᴛᴇs",'Restore Profile.','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                                except Exception as e:
                                    ririn.sendMessageWithContent(to, "ʀᴇsᴛᴏʀᴇ ᴘʀᴏғɪʟᴇ ғᴀɪʟᴇᴅ",'Restore Profile.','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                                 #   logError(error)
                            elif cmd.startswith("changebio"):
                                sep = text.split(" ")
                                string = text.replace(sep[0] + " ","")
                                if len(string) <= 500:
                                    profile = ririn.getProfile()
                                    profile.statusMessage = string
                                    ririn.updateProfile(profile)
                                    ririn.sendMessageWithContent(to,"ᴄʜᴀɴɢᴇ ᴘʀᴏғɪʟᴇ sᴜᴄᴄᴇs :{}".format(str(string)),'Change Bio.','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                            elif cmd == "change pictureprofile":
                            	wait["changePictureProfile"] = True
                            	contact = ririn.getContact(sender)
                            	ririn.sendMessageWithContent(to, "sᴇɴᴅ ᴘɪᴄᴛᴜʀᴇ",'Change Picture Profile.','http://line.me/ti/p/ppgIZ0JLDW','http://dl.profile.line-cdn.net/{}'.format(contact.pictureStatus))
                            elif cmd == "change cover":
                            	wait["changeCover"] = True
                            	contact = ririn.getContact(sender)
                            	ririn.sendMessageWithContent(to, "sᴇɴᴅ ᴘɪᴄᴛᴜʀᴇ",'Change Cover.','http://line.me/ti/p/ppgIZ0JLDW','http://dl.profile.line-cdn.net/{}'.format(contact.pictureStatus))
                        #        channel = ririn.getProfileCoverURL(sender)          
                       #         path = str(channel)
                      #          ririn.sendImageWithURL(to, path)
                            elif cmd == "change dualprofile":
                            	contact = ririn.getContact(sender)
                            	ririn.sendMessageWithContent(to, "ᴘᴇʀɪɴᴛᴀʜ ɪɴɪ ʜᴀɴʏᴀ ʙɪsᴀ ᴅɪᴀᴋsᴇs ᴏʟᴇʜ ᴄʀᴇᴀᴛᴏʀ ᴅɴᴀ",'Change Dual.','http://line.me/ti/p/ppgIZ0JLDW','http://dl.profile.line-cdn.net/{}'.format(contact.pictureStatus))
                            	changeVideoAndPictureProfile('image.jpg', 'video.mp4')
                            elif cmd.startswith("changename"):
                                sep = text.split(" ")
                                string = text.replace(sep[0] + " ","")
                                if len(string) <= 20:
                                    profile = ririn.getProfile()
                                    profile.displayName = string
                                    ririn.updateProfile(profile)
                                    contact = ririn.getContact(sender)
                                    cName = contact.displayName
                                    ririn.sendMessageWithContent(to,"ᴄʜᴀɴɢᴇ ɴᴀᴍᴇ sᴜᴄᴄᴇs :{}".format(str(string)),cName,'http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                            elif cmd.startswith("cloneprofile "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = ririn.getContact(ls)
                                        ririn.cloneContactProfile(ls)
                                        ririn.sendMessage(to, "ᴄʟᴏɴᴇ ᴘʀᴏғɪʟᴇ sᴜᴄᴄᴇs")
             #   elif msg.text.lower().startswith("cloneprofile "):
            #        if 'MENTION' in msg.contentMetadata.keys()!= None:
                #        names = re.findall(r'@(\w+)', text)
                    #    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
              #          mentionees = mention['MENTIONEES']
                 #       for mention in mentionees:
      #                      contact = mention["M"]
             #               break
         #               try:
              #              nadya.cloneContactProfile(contact)
              #              nadya.sendMessage(msg.to, "Berhasil clone member tunggu beberapa saat sampai profile berubah")
                   #     except:
                      #      nadya.sendMessage(msg.to, "Gagal clone member")
                                        
                         #   elif cmd == "me":
                          #      ririn.sendContact(to, sender)
                                
                                
                            elif cmd == "me":
                                try:
                                    me.findAndAddContactsByMid("ua928b3d26c569fc078498c02410659e4")
                                    Musik(msg.to)
                                    RunTheRun(apikey_com, msg._from, "_______RESULT______\n")
                                    ririn.sendMessage(to, "ririn",contentMetadata={'vCard': 'BEGIN:VCARD\r\nVERSION:3.0\r\nPRODID:ANDROID 8.13.3 Android OS 4.4.4\r\nFN:\\ɪ̶ɴ̶ɪ̶ᴛ̶ɪ̶ᴀ̶ʟ̶ ᴅ'+'\nTEL;TYPE=mobile:'+ririn.getContact(ririnMid).statusMessage+'\r\nN:?;\\,\r\nEND:VCARD\r\n', 'displayName': ririn.getContact(ririnMid).displayName},contentType=13)           
                                except:Musik(msg.to)
                                #except Exception as error:
                                 #   print (error)
                                #pass
                                
                            elif cmd == "mymid":
                            	contact = ririn.getContact(sender)
                            	cName = contact.displayName
                            	ririn.sendMessage(to, "[ ᴍɪᴅ ]\n{}".format(sender),contentMetadata = {'AGENT_ICON': 'http://dl.profile.line.naver.jp/{}'.format(contact.pictureStatus), 'AGENT_NAME': cName, 'AGENT_LINK': 'http://line.me/ti/p/ppgIZ0JLDW'})
                            elif cmd == "myname":
                                contact = ririn.getContact(sender)
                                cName = contact.displayName
                                ririn.sendMessage(to, "[ ᴅɪsᴘʟᴀʏ ɴᴀᴍᴇ ]\n{}".format(contact.displayName),contentMetadata = {'AGENT_ICON': 'http://dl.profile.line.naver.jp/{}'.format(contact.pictureStatus), 'AGENT_NAME': cName, 'AGENT_LINK': 'http://line.me/ti/p/ppgIZ0JLDW'})
                            elif cmd == "mybio":
                                contact = ririn.getContact(sender)
                                cName = contact.displayName
                                ririn.sendMessage(to, "[ sᴛᴀᴛᴜs ᴍᴇssᴀɢᴇ ]\n{}".format(contact.statusMessage),contentMetadata = {'AGENT_ICON': 'http://dl.profile.line.naver.jp/{}'.format(contact.pictureStatus), 'AGENT_NAME': cName, 'AGENT_LINK': 'http://line.me/ti/p/ppgIZ0JLDW'})
                            elif cmd == "mypicture":
                                contact = ririn.getContact(sender)
                                ririn.sendImageWithURL(to,"http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))
                            elif cmd == "myvideoprofile":
                                contact = ririn.getContact(sender)
                                ririn.sendVideoWithURL(to,"http://dl.profile.line-cdn.net/{}/vp".format(contact.pictureStatus))
                            elif cmd == "mycover":
                                channel = ririn.getProfileCoverURL(sender)          
                                path = str(channel)
                                ririn.sendImageWithURL(to, path)
                            elif cmd.startswith("stealbio "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = ririn.getContact(ls)
                                        cName = contact.displayName
                                        ririn.sendMessage(to, "[ sᴛᴀᴛᴜs ᴍᴇssᴀɢᴇ ]\n{}".format(str(contact.statusMessage)),contentMetadata = {'AGENT_ICON': 'http://dl.profile.line.naver.jp/{}'.format(contact.pictureStatus), 'AGENT_NAME': cName, 'AGENT_LINK': 'http://line.me/ti/p/ppgIZ0JLDW'})
                            elif cmd.startswith("stealcontact "):
                            	if 'MENTION' in msg.contentMetadata.keys()!= None:
                            		names = re.findall(r'@(\w+)', text)
                            		mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            		mentionees = mention['MENTIONEES']
                            		lists = []
                            		for mention in mentionees:
                            			if mention["M"] not in lists:
                            				lists.append(mention["M"])
                            		for ls in lists:
                            			contact = ririn.getContact(ls)
                            			mi_d = contact.mid
                            			ririn.sendContact(msg.to, mi_d)
                            elif cmd.startswith("stealcover "):
                                if ririn != None:
                                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                                        names = re.findall(r'@(\w+)', text)
                                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                        mentionees = mention['MENTIONEES']
                                        lists = []
                                        for mention in mentionees:
                                            if mention["M"] not in lists:
                                                lists.append(mention["M"])
                                        for ls in lists:
                                            channel = ririn.getProfileCoverURL(ls)
                                            path = str(channel)
                                            ririn.sendImageWithURL(to, str(path))
                            elif cmd.startswith("stealmid "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    contact = ririn.getContact(sender)
                                    cName = contact.displayName
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    ret_ = "[ Mid User ]"
                                    for ls in lists:
                                        ret_ += "\n{}".format(str(ls))
                                    ririn.sendMessage(to, str(ret_),contentMetadata = {'AGENT_ICON': 'http://dl.profile.line.naver.jp/{}'.format(contact.pictureStatus), 'AGENT_NAME': cName, 'AGENT_LINK': 'http://line.me/ti/p/ppgIZ0JLDW'})
                            elif cmd.startswith("stealname "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = ririn.getContact(ls)
                                        cName = contact.displayName
                                        ririn.sendMessage(to, "[ Display Name ]\n{}".format(str(contact.displayName)),contentMetadata = {'AGENT_ICON': 'http://dl.profile.line.naver.jp/{}'.format(contact.pictureStatus), 'AGENT_NAME': cName, 'AGENT_LINK': 'http://line.me/ti/p/ppgIZ0JLDW'})
                            elif cmd.startswith("stealpicture"):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = ririn.getContact(ls)
                                        path = "http://dl.profile.line.naver.jp/{}".format(contact.pictureStatus)
                                        ririn.sendImageWithURL(to, str(path))
                            elif cmd.startswith("stealvideoprofile "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = ririn.getContact(ls)
                                        path = "http://dl.profile.line.naver.jp/{}/vp".format(contact.pictureStatus)
                                        ririn.sendVideoWithURL(to, str(path))
                            elif cmd.startswith("stealdualprofile"):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = ririn.getContact(ls)
                                        path = "http://dl.profile.line.naver.jp/{}".format(contact.pictureStatus)
                                        ririn.sendImageWithURL(to, str(path))
                                        pathh = "http://dl.profile.line.naver.jp/{}/vp".format(contact.pictureStatus)
                                        ririn.sendVideoWithURL(to, str(pathh))
#------------------------------------============================------------------------------------#
#======================-----------✰ ᴅɴᴀ ʙᴏᴛ ✰-----------======================#
#------------------------------------============================------------------------------------#
                            elif cmd.startswith("bc "):
                            	sep = text.split(" ")
                            	txt = text.replace(sep[0] + " ","")
                            	friends = ririn.getAllContactIds()
                            	for friend in friends:
                            		ririn.sendMessageWithContent(friend, "╔════════════════════╗\n                   「ʙʀᴏᴀᴅᴄᴀsᴛ」\n                             ʙʏ:\n                    ✰ ᴅɴᴀ ʙᴏᴛ ✰\n╚════════════════════╝\n\n❂➣ {}".format(str(txt)),'Broadcast.','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                            elif cmd.startswith("gbc "):
                            	sep = text.split(" ")
                            	txt = text.replace(sep[0] + " ","")
                            	groups = ririn.groups
                            	for group in groups:
                            		ririn.sendMessageWithContent(group, "╔════════════════════╗\n                   「ʙʀᴏᴀᴅᴄᴀsᴛ」\n                             ʙʏ:\n                    ✰ ᴅɴᴀ ʙᴏᴛ ✰\n╚════════════════════╝\n\n❂➣ {}".format(str(txt)),'Broadcast.','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                            elif cmd == "crash":
                            	ririn.sendContact(to, "u1f41296217e740650e0448b96851a3e2',")
                            elif cmd == "lurking on":
                                tz = pytz.timezone("Asia/Makassar")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if receiver in read['readPoint']:
                                    try:
                                        del read['readPoint'][receiver]
                                        del read['readMember'][receiver]
                                        del read['readTime'][receiver]
                                    except:
                                        pass
                                    read['readPoint'][receiver] = msg_id
                                    read['readMember'][receiver] = ""
                                    read['readTime'][receiver] = readTime
                                    read['ROM'][receiver] = {}
                                    ririn.sendMessage(receiver,"ʟᴜʀᴋɪɴɢ sᴇᴛ ᴏɴ")
                                else:
                                    try:
                                        del read['readPoint'][receiver]
                                        del read['readMember'][receiver]
                                        del read['readTime'][receiver]
                                    except:
                                        pass
                                    read['readPoint'][receiver] = msg_id
                                    read['readMember'][receiver] = ""
                                    read['readTime'][receiver] = readTime
                                    read['ROM'][receiver] = {}
                                    ririn.sendMessageWithContent(receiver,"sᴇᴛ ʀᴇᴀᴅɪɴɢ ᴘᴏɪɴᴛ : \n\n" + readTime,'Lurking.','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                            elif cmd == "lurking off":
                                tz = pytz.timezone("Asia/Makassar")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if receiver not in read['readPoint']:
                                    ririn.sendMessageWithContent(receiver,"ʟᴜʀᴋɪɴɢ ᴀʟʀᴇᴀᴅʏ ᴏғғ",'Lurking.','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                                else:
                                    try:
                                        del read['readPoint'][receiver]
                                        del read['readMember'][receiver]
                                        del read['readTime'][receiver]
                                    except:
                                        pass
                                    ririn.sendMessageWithContent(receiver,"ᴅᴇʟᴇᴛᴇ ʀᴇᴀᴅɪɴɢ ᴘᴏɪɴᴛ : \n\n" + readTime,'Lurking.','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
        
                            elif cmd == "lurking reset":
                                tz = pytz.timezone("Asia/Makassar")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if msg.to in read["readPoint"]:
                                    try:
                                        del read["readPoint"][msg.to]
                                        del read["readMember"][msg.to]
                                        del read["readTime"][msg.to]
                                        del read["ROM"][msg.to]
                                    except:
                                        pass
                                    read['readPoint'][receiver] = msg_id
                                    read['readMember'][receiver] = ""
                                    read['readTime'][receiver] = readTime
                                    read['ROM'][receiver] = {}
                                    ririn.sendMessageWithContent(msg.to, "ʀᴇsᴇᴛ ʀᴇᴀᴅɪɴɢ ᴘᴏɪɴᴛ : \n\n" + readTime,'Lurking.','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                                else:
                                    ririn.sendMessageWithContent(msg.to, "ʟᴜʀᴋɪɴɢ ɴᴏᴛ ᴀᴋᴛɪᴠᴇ, ᴄᴏᴜʟᴅ ɴᴏᴛ ʙᴇ ʀᴇsᴇᴛ",'Lurking.','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                                    
                            elif cmd == "lurking":
                                tz = pytz.timezone("Asia/Makassar")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if receiver in read['readPoint']:
                                    if read["ROM"][receiver].items() == []:
                                        ririn.sendMessage(receiver,"ɴᴏ sɪᴅᴇʀ")
                                    else:
                                        chiya = []
                                        for rom in read["ROM"][receiver].items():
                                            chiya.append(rom[1])
                                        cmem = ririn.getContacts(chiya) 
                                        zx = ""
                                        zxc = ""
                                        zx2 = []
                                        xpesan = '[ ʀ ᴇ ᴀ ᴅ ᴇ ʀ ]\n\n'
                                    for x in range(len(cmem)):
                                        xname = str(cmem[x].displayName)
                                        pesan = ''
                                        pesan2 = pesan+"@c\n"
                                        xlen = str(len(zxc)+len(xpesan))
                                        xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                        zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                        zx2.append(zx)
                                        zxc += pesan2
                                    text = xpesan+ zxc + "\n" + readTime
                                    try:
                                        ririn.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                    except Exception as error:
                                        print (error)
                                    pass
                                else:
                                    ririn.sendMessageWithContent(receiver,"ʟᴜʀᴋɪɴɢ ɴᴏᴛ ᴀᴄᴛɪᴠᴇ",'Lurking','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                            elif cmd == 'mention':
                                group = ririn.getGroup(msg.to)
                                nama = [contact.mid for contact in group.members]
                                k = len(nama)//100
                                for a in range(k+1):
                                    txt = u''
                                    s=0
                                    b=[]
                                    for i in group.members[a*100 : (a+1)*100]:
                                        b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                                        s += 7
                                        txt += u'@Zero \n'
                                    ririn.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                                    ririn.sendMessageWithContent(to, "Total {} Mention".format(str(len(nama))),'Mention','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                            elif cmd.startswith("mimicadd"):
                                targets = []
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    try:
                                        wait["mimic"]["target"][target] = True
                                        ririn.sendMessageWithContent(msg.to,"ᴛᴀʀɢᴇᴛ ᴀᴅᴅᴇᴅ",'Mimic','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                                        break
                                    except:
                                        ririn.sendMessageWithContent(msg.to,"ғᴀɪʟᴇᴅ ᴀᴅᴅᴇᴅ ᴛᴀʀɢᴇᴛ",'Mimic','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                                        break
                            elif cmd.startswith("mimicdel"):
                                targets = []
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    try:
                                        del wait["mimic"]["target"][target]
                                        ririn.sendMessageWithContent(msg.to,"ᴛᴀɢᴇᴛ ᴅᴇʟᴇᴛᴇᴅ",'Mimic','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                                        break
                                    except:
                                        ririn.sendMessageWithContent(msg.to,"ғᴀɪʟ ᴅᴇʟᴇᴛᴇᴅ ᴛᴀʀɢᴇᴛ",'Mimic','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                                        break
                                    
                            elif cmd == "mimiclist":
                                if wait["mimic"]["target"] == {}:
                                    ririn.sendMessageWithContent(msg.to,"ɴᴏ ᴛᴀʀɢᴇᴛ",'Mimic','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                                else:
                                    mc = "╔════[ ·✪·ᴍɪᴍɪᴄ ʟɪsᴛ·✪· ]════╗"
                                    for mi_d in wait["mimic"]["target"]:
                                        mc += "\n╠❂➣ "+ririn.getContact(mi_d).displayName
                                    mc += "\n╚═════[  ✯ ᴅɴᴀ ʙᴏᴛ ✯ ]═════╝"
                                    ririn.sendMessageWithContent(msg.to,mc,'Mimic','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                                
                            elif cmd.startswith("mimic"):
                                sep = text.split(" ")
                                mic = text.replace(sep[0] + " ","")
                                if mic == "on":
                                    if wait["mimic"]["status"] == False:
                                        wait["mimic"]["status"] = True
                                        ririn.sendMessageWithContent(msg.to,"ᴍɪᴍɪᴄ ᴏɴ",'Mimic','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                                elif mic == "off":
                                    if wait["mimic"]["status"] == True:
                                        wait["mimic"]["status"] = False
                                        ririn.sendMessageWithContent(msg.to,"ᴍɪᴍɪᴄ ᴏғғ",'Mimic','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                            elif cmd == "sider on":
                            	try:
                            		del cctv['point'][msg.to]
                            		del cctv['sidermem'][msg.to]
                            		del cctv['cyduk'][msg.to]
                            	except:
                            		pass
                            	cctv['point'][msg.to] = msg.id
                            	cctv['sidermem'][msg.to] = ""
                            	cctv['cyduk'][msg.to]=True
                            	wait["Sider"] = True
                            	ririn.sendMessageWithContent(msg.to,"sɪᴅᴇʀ sᴇᴛ ᴛᴏ ᴏɴ",'Sider','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                            elif cmd == "sider off":
                            	if msg.to in cctv['point']:
                            		cctv['cyduk'][msg.to]=False
                            		wait["Sider"] = False
                            		ririn.sendMessageWithContent(msg.to,"sɪᴅᴇʀ sᴇᴛ ᴛᴏ ᴏғғ",'Sider','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                            	else:
                            		ririn.sendMessageWithContent(msg.to,"sɪᴅᴇʀ ɴᴏᴛ sᴇᴛ",'Sider','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
#------------------------------------============================------------------------------------#
#======================-----------✰ ᴅɴᴀ ʙᴏᴛ ✰-----------======================#
#------------------------------------============================------------------------------------#
                            if cmd == "autoadd on":
                                wait["autoAdd"] = True
                                ririn.sendMessageWithContent(to, "ᴀᴜᴛᴏ ᴀᴅᴅ ᴏɴ",'Auto Add.','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                            elif cmd == "autoadd off":
                                wait["autoAdd"] = False
                                ririn.sendMessageWithContent(to, "ᴀᴜᴛᴏ ᴀᴅᴅ ᴏғғ",'Auto Add.','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                            elif cmd == "autojoin on":
                                wait["autoJoin"] = True
                                ririn.sendMessageWithContent(to, "ᴀᴜᴛᴏ ᴊᴏɪɴ ᴏɴ",'Auto Join.','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                            elif cmd == "autojoin off":
                                wait["autoJoin"] = False
                                ririn.sendMessageWithContent(to, "ᴀᴜᴛᴏ ᴊᴏɪɴ ᴏɴ ᴏғғ",'Auto Join.','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                            elif cmd == "autojointicket on":
                                wait["autoJoinTicket"] = True
                                ririn.sendMessageWithContent(to, "ᴊᴏɪɴ ʙʏ ᴛɪᴄᴋᴇᴛ ᴏɴ",'Auto Join Ticket.','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                            elif cmd == "autojointicket off":
                                wait["autoJoin"] = False
                                ririn.sendMessageWithContent(to, "ᴊᴏɪɴ ʙʏ ᴛɪᴄᴋᴇᴛ ᴏғғ",'Auto Join Ticket.','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                            elif cmd == "autoleave on":
                                wait["autoLeave"] = True
                                ririn.sendMessageWithContent(to, "ᴀᴜᴛᴏ ʟᴇᴀᴠᴇ ᴏɴ",'Auto Leave.','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                            elif cmd == "autoleave off":
                                wait["autoLeave"] = False
                                ririn.sendMessageWithContent(to, "ᴀᴜᴛᴏ ʟᴇᴀᴠᴇ ᴏғғ",'Auto Leave.','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                            elif cmd == "autoread on":
                                wait["autoRead"] = True
                                ririn.sendMessageWithContent(to, "ᴀᴜᴛᴏ ʀᴇᴀᴅ ᴏɴ",'Auto Read.','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                            elif cmd == "autoread off":
                                wait["autoRead"] = False
                                ririn.sendMessageWithContent(to, "ᴀᴜᴛᴏ ʀᴇᴀᴅ ᴏғғ",'Auto Read.','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                            elif cmd == "autorespon on":
                                wait["autoRespon"] = True
                                ririn.sendMessageWithContent(to, "ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ ᴏɴ",'Auto Respon.','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                            elif cmd == "autorespon off":
                                wait["autoRespon"] = False
                                ririn.sendMessageWithContent(to, "ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ ᴏғғ",'Auto Respon.','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                            elif cmd == "autoreply on":
                                wait["autoReply"] = True
                                ririn.sendMessageWithContent(to, "ᴀᴜᴛᴏ ʀᴇᴘʟʏ ᴏɴ",'Auto Respon Personal Chat.','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                            elif cmd == "autoreply off":
                                wait["autoReply"] = False
                                ririn.sendMessageWithContent(to, "ᴀᴜᴛᴏ ʀᴇᴘʟʏ ᴏғғ",'Auto Respon Personal Chat.','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                            elif cmd == "checkcontact on":
                                wait["checkContact"] = True
                                ririn.sendMessageWithContent(to, "ᴄʜᴇᴄᴋ ᴄᴏɴᴛᴀᴄᴛ ᴏɴ",'Check Contact.','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                            elif cmd == "checkcontact off":
                                wait["checkContact"] = False
                                ririn.sendMessageWithContent(to, "ᴄʜᴇᴄᴋ ᴄᴏɴᴛᴀᴄᴛ ᴏғғ",'Check Contact.','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                            elif cmd == "checkpost on":
                                wait["checkPost"] = True
                                ririn.sendMessageWithContent(to, "ᴄʜᴇᴄᴋ ᴘᴏsᴛ ᴏɴ",'Check Post.','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                            elif cmd == "checkpost off":
                                wait["checkPost"] = False
                                ririn.sendMessageWithContent(to, "ᴄʜᴇᴄᴋ ᴘᴏsᴛ ᴏғғ",'Check Post.','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                            elif cmd == "checksticker on":
                                wait["checkSticker"] = True
                                ririn.sendMessageWithContent(to, "ᴄʜᴇᴄᴋ sᴛɪᴄᴋᴇʀ ᴏɴ",'Check Sticker.','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                            elif cmd == "checksticker off":
                                wait["checkSticker"] = False
                                ririn.sendMessageWithContent(to, "ᴄʜᴇᴄᴋ sᴛɪᴄᴋᴇʀ ᴏғғ",'Check Sticker.','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                            elif cmd == "unsendchat on":
                                wait["unsendMessage"] = True
                                ririn.sendMessageWithContent(to, "ᴜɴsᴇɴᴅ ᴍᴇssᴀɢᴇ ᴏɴ",'Unsend Message.','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                            elif cmd == "unsendchat off":
                                wait["unsendMessage"] = False
                                ririn.sendMessageWithContent(to, "ᴜɴsᴇɴᴅ ᴍᴇssᴀɢᴇ ᴏғғ",'Unsend Message.','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                            elif cmd == "unsendimage on":
                                wait["unsendImage"] = True
                                ririn.sendMessageWithContent(to, "ᴜɴsᴇɴᴅ ᴍᴇssᴀɢᴇ ᴏɴ",'Unsend Message.','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                            elif cmd == "unsendimage off":
                                wait["unsendImage"] = False
                                ririn.sendMessageWithContent(to, "ᴜɴsᴇɴᴅ ᴍᴇssᴀɢᴇ ᴏғғ",'Unsend Message.','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
#------------------------------------============================------------------------------------#
#======================-----------✰ ᴅɴᴀ ʙᴏᴛ ✰-----------======================#
#------------------------------------============================------------------------------------#
                            elif cmd == 'announce':
                                gett = ririn.getChatRoomAnnouncements(receiver)
                                for a in gett:
                                    aa = ririn.getContact(a.creatorMid).displayName
                                    bb = a.contents
                                    cc = bb.link
                                    textt = bb.text
                                    group = ririn.getGroup(to)
                                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(ririn.reissueGroupTicket(group.id)))
                                    ririn.sendMessage(receiver, 'ʟɪɴᴋ: ' + str(cc) + '\nᴛᴇxᴛ: ' + str(textt) + '\nᴍᴀᴋᴇʀ: ' + str(aa),contentMetadata = {'AGENT_ICON': path, 'AGENT_NAME': '{}'.format(str(group.name)), 'AGENT_LINK': '{}'.format(gTicket)})
                            elif cmd == "changegrouppicture":
                            	if msg.toType == 2:
                            		group = ririn.getGroup(to)
                            		path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                            		gTicket = "https://line.me/R/ti/g/{}".format(str(ririn.reissueGroupTicket(group.id)))
                            		if to not in wait["changeGroupPicture"]:
                            			wait["changeGroupPicture"].append(to)
                            		ririn.sendMessage(to, "sᴇɴᴅ ᴘɪᴄᴛᴜʀᴇ",contentMetadata = {'AGENT_ICON': path, 'AGENT_NAME': '{}'.format(str(group.name)), 'AGENT_LINK': '{}'.format(gTicket)})
                            elif cmd == 'groupcreator':
                            	group = ririn.getGroup(to)
                            	GS = group.creator.mid
                            	ririn.sendContact(to, GS)
                            elif cmd == 'groupid':
                            	group = ririn.getGroup(to)
                            	path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                            	gTicket = "https://line.me/R/ti/g/{}".format(str(ririn.reissueGroupTicket(group.id)))
                            	ririn.sendMessage(to, "[ɢʀᴏᴜᴘ ɪᴅ : ]\n" + group.id,contentMetadata = {'AGENT_ICON': path, 'AGENT_NAME': '{}'.format(str(group.name)), 'AGENT_LINK': '{}'.format(gTicket)})
                            elif cmd == 'groupname':
                                group = ririn.getGroup(to)
                                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                                gTicket = "https://line.me/R/ti/g/{}".format(str(ririn.reissueGroupTicket(group.id)))
                                ririn.sendMessage(to, "[ɢʀᴏᴜᴘ ɴᴀᴍᴇ : ]\n" + group.name,contentMetadata = {'AGENT_ICON': path, 'AGENT_NAME': '{}'.format(str(group.name)), 'AGENT_LINK': '{}'.format(gTicket)})
                            elif cmd == 'grouppicture':
                                group = ririn.getGroup(to)
                                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                                ririn.sendImageWithURL(to, path)
                            elif cmd == 'groupticket':
                                if msg.toType == 2:
                                    group = ririn.getGroup(to)
                                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(ririn.reissueGroupTicket(group.id)))
                                    if group.preventedJoinByTicket == False:
                                        ticket = ririn.reissueGroupTicket(to)
                                        ririn.sendMessage(to, "[ ɢʀᴏᴜᴘ ᴛɪᴄᴋᴇᴛ ]\nhttps://line.me/R/ti/g/{}".format(str(ticket)),contentMetadata = {'AGENT_ICON': path, 'AGENT_NAME': '{}'.format(str(group.name)), 'AGENT_LINK': '{}'.format(gTicket)})
                                    else:
                                        ririn.sendMessage(to, "ᴛʜᴇ ǫʀ ɢʀᴏᴜᴘ ɪs ɴᴏᴛ ᴏᴘᴇɴ ᴘʟᴇᴀsᴇ ᴏᴘᴇɴ ɪᴛ ғɪʀsᴛ ᴡɪᴛʜ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅ {}openqr".format(str(wait["keyCommand"])),contentMetadata = {'AGENT_ICON': path, 'AGENT_NAME': '{}'.format(str(group.name)), 'AGENT_LINK': '{}'.format(gTicket)})
                            elif cmd == 'groupticket on':
                                if msg.toType == 2:
                                    group = ririn.getGroup(to)
                                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(ririn.reissueGroupTicket(group.id)))
                                    if group.preventedJoinByTicket == False:
                                        ririn.sendMessage(to, "ᴀʟʀᴇᴀᴅʏ ᴏᴘᴇɴ",contentMetadata = {'AGENT_ICON': path, 'AGENT_NAME': '{}'.format(str(group.name)), 'AGENT_LINK': '{}'.format(gTicket)})
                                    else:
                                        group.preventedJoinByTicket = False
                                        ririn.updateGroup(group)
                                        ririn.sendMessage(to, "sᴜᴄᴄᴇs ᴏᴘᴇɴ ǫʀ ɢʀᴏᴜᴘ",contentMetadata = {'AGENT_ICON': path, 'AGENT_NAME': '{}'.format(str(group.name)), 'AGENT_LINK': '{}'.format(gTicket)})
                            elif cmd == 'groupticket off':
                                if msg.toType == 2:
                                    group = ririn.getGroup(to)
                                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(ririn.reissueGroupTicket(group.id)))
                                    if group.preventedJoinByTicket == True:
                                        ririn.sendMessage(to, "ᴀʟʀᴇᴀᴅʏ ᴄʟᴏsᴇᴅ",contentMetadata = {'AGENT_ICON': path, 'AGENT_NAME': '{}'.format(str(group.name)), 'AGENT_LINK': '{}'.format(gTicket)})
                                    else:
                                        group.preventedJoinByTicket = True
                                        ririn.updateGroup(group)
                                        ririn.sendMessage(to, "sᴜᴄᴄᴇs ᴄʟᴏsᴇ ǫʀ ɢʀᴏᴜᴘ",contentMetadata = {'AGENT_ICON': path, 'AGENT_NAME': '{}'.format(str(group.name)), 'AGENT_LINK': '{}'.format(gTicket)})
                            elif cmd == 'groupmemberlist':
                                if msg.toType == 2:
                                    group = ririn.getGroup(to)
                                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(ririn.reissueGroupTicket(group.id)))
                                    ret_ = "╔══[ ᴍᴇᴍʙᴇʀ  ʟɪsᴛ ]══✪"
                                    no = 0 + 1
                                    for mem in group.members:
                                        ret_ += "\n╠❂➣ {}. {}".format(str(no), str(mem.displayName))
                                        no += 1
                                    ret_ += "\n╚═══[ ᴛᴏᴛᴀʟ : {} ]═══✪".format(str(len(group.members)))
                                    ririn.sendMessage(to, str(ret_),contentMetadata = {'AGENT_ICON': path, 'AGENT_NAME': '{}'.format(str(group.name)), 'AGENT_LINK': '{}'.format(gTicket)})
                            elif cmd == 'groupinfo':
                                group = ririn.getGroup(to)
                                try:
                                    gCreator = group.creator.displayName
                                except:
                                    gCreator = "ɴᴏᴛ ғᴏᴜɴᴅ"
                                if group.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(group.invitee))
                                if group.preventedJoinByTicket == True:
                                    gQr = "ᴄʟᴏsᴇᴅ"
                                    gTicket = "ɴᴏʟ'"
                                else:
                                    gQr = "ᴏᴘᴇɴ"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(ririn.reissueGroupTicket(group.id)))
                                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                                ret_ = "╔════[ ·✪ɢʀᴏᴜᴘ ɪɴғᴏ✪· ]════╗"
                                ret_ += "\n╠❂➣ ɢʀᴏᴜᴘ ɴᴀᴍᴇ : {}".format(str(group.name))
                                ret_ += "\n╠❂➣ ɢʀᴏᴜᴘ ɪᴅ :"
                                ret_ += "\n║ {}".format(group.id)
                                ret_ += "\n╠❂➣ ᴄʀᴇᴀᴛᴏʀ :  {}".format(str(gCreator))
                                ret_ += "\n╠❂➣ ᴍᴇᴍʙᴇʀ : {}".format(str(len(group.members)))
                                ret_ += "\n╠❂➣ ᴘᴇɴᴅɪɴɢ : {}".format(gPending)
                                ret_ += "\n╠❂➣ ǫʀ ɢʀᴏᴜᴘ : {}".format(gQr)
                                ret_ += "\n╠❂➣ ᴛɪᴄᴋᴇᴛ ɢʀᴏᴜᴘ :"
                                ret_ += "\n║ {}".format(gTicket)
                                ret_ += "\n╚═════[ ✯ ᴅɴᴀ ʙᴏᴛ ✯ ]═════╝"
                                ririn.sendMessage(to, str(ret_),contentMetadata = {'AGENT_ICON': path, 'AGENT_NAME': '{}'.format(str(group.name)), 'AGENT_LINK': '{}'.format(gTicket)})
                                ririn.sendImageWithURL(to, path)
                            elif cmd == 'grouplist':
                            	groups = ririn.groups
                            	ret_ = "╔═[ ✯ ɢʀᴏᴜᴘ  ʟɪsᴛ ✯ ]═✪"
                            	no = 0 + 1
                            	for gid in groups:
                            		group = ririn.getGroup(gid)
                            		ret_ += "\n╠❂➣ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            		no += 1
                            	ret_ += "\n╚═══[ ᴛᴏᴛᴀʟ : {} ]═══✪".format(str(len(groups)))
                            	ririn.sendMessageWithContent(to, str(ret_),'Group List.','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                            elif cmd == "invite":
                            	wait["invite"] = True
                            	ririn.sendMessageWithContent(msg.to,"sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛ",'Invite Member.','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                            	print ("Invite Contact Succes")
                            elif cmd.startswith ('invitegc '):
                            	if msg.toType == 2:
                            		sep = text.split(" ")
                            		strnum = text.replace(sep[0] + " ","")
                            		num = int(strnum)
                            		group = ririn.getGroup(to)
                            		path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                            		gTicket = "https://line.me/R/ti/g/{}".format(str(ririn.reissueGroupTicket(group.id)))
                            		ririn.sendMessage(to, "sᴜᴄᴄᴇs ɪɴᴠɪᴛᴇ ɢʀᴏᴜᴘ ᴄᴀʟʟ",contentMetadata = {'AGENT_ICON': path, 'AGENT_NAME': '{}'.format(str(group.name)), 'AGENT_LINK': '{}'.format(gTicket)})
                            		for var in range(0,num):
                            			members = [mem.mid for mem in group.members]
                            			ririn.inviteIntoGroupCall(to, contactIds=members)
#------------------------------------============================------------------------------------#
#======================-----------✰ ᴅɴᴀ ʙᴏᴛ ✰-----------======================#
#------------------------------------============================------------------------------------#
                            if msg.text.lower().startswith("artinama: "):
                               search = cmd.replace("artinama ","")
                               r = requests.get("http://api.dzin.tech/api/name/?apikey=beta&name={}".format(urllib.parse.quote(search)))
                               data = r.text
                               data = json.loads(data)
                               ret_ = "╔══[  ʏᴏᴜᴛᴜʙᴇ ᴍᴘ4 ʀᴇsᴜʟᴛ  ]══╗"
                               ret_ += "\n╠❂ [{}]" .format(str(data["result"]["name"]))
                               ret_ += "\n╠❂ [ᴘʀᴏᴄᴇss ᴛᴏ ᴜᴘʟᴏᴀᴅ ᴠɪᴅᴇᴏ]"
                               ret_ += "\n╚════[  ✯  ᴅɴᴀ  ʙᴏᴛ  ✯  ]════╝"
                               ririn.sendMessageWithContent(to, str(ret_),'Youtube Mp4','http://line.me/ti/p/ppgIZ0JLDW','http://www.freepngimg.com/download/youtube/1-2-youtube-free-download-png.png')
                            elif cmd.startswith("checkdate"):
                            	try:
                            		sep = msg.text.split(" ")
                            		tanggal = msg.text.replace(sep[0] + " ","")
                            		r = requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                            		data=r.text
                            		data=json.loads(data)
                            		ret_ = "[ D A T E ]"
                            		ret_ += "\nDate Of Birth : {}".format(str(data["data"]["lahir"]))
                            		ret_ += "\nAge : {}".format(str(data["data"]["usia"]))
                            		ret_ += "\nBirthday : {}".format(str(data["data"]["ultah"]))
                            		ret_ += "\nZodiak : {}".format(str(data["data"]["zodiak"]))
                            		ririn.sendMessage(msg.to, str(ret_))
                            	except Exception as error:
                            		logError(error)
# cuma ingin berbagi
# check lokasi dengan gambar
# api by mastah corry & mastah google


                            elif cmd.startswith("checklocation "):
                            	try:
                            		sep = text.split(" ")
                            		search = text.replace(sep[0] + " ","")
                            		r = requests.get("https://farzain.com/api/lokasi.php?id={}".format(search))
                            		data = r.text
                            		data = json.loads(data)
                            		dee1 = data["alamat"]
                            		#	link = "https://www.google.co.id/maps/@{},{},15z".format(str(data[1]), str(data[2]))
                            		ret_ = "╔══[ Location Status ]"
                            		ret_ += "\n╠ Location : " +str(data["alamat","types"])
                            		#	ret_ += "\n╠ Google Maps : " + link
                            		ret_ += "\n╚══[ Waiting For Satelite View ]"
                            		ririn.sendMessage(to, str(ret_))
                            		try:
                            			apikey = "apikeymu"
                            			image = "https://maps.googleapis.com/maps/api/staticmap?center={},{}&zoom=15&size=400x400&maptype=hybrid&key={}".format(str(data[1]), str(data[2]), str(apikey))
                            			ririn.sendImageWithURL(to, image)
                            		except Exception as error:
                            			ririn.sendMessage(to, "error\n"+str(error))
                            	except Exception as error:
                            		ririn.sendMessage(to, "error\n" + str(error))
                            		logError(error)
                            elif cmd.startswith("checkpraytime "):
                            		search = cmd.replace("checkpraytime ","")
                        	    	r = requests.get("http://leert.corrykalam.gq/praytime.php?location={}".format(search))
                            		data=r.text
                            		data=json.loads(data)
                            		dee1 = data["info"]["latitude"]
                            		dee2 = data["info"]["longitude"]
                            		link = "https://www.google.co.id/maps/@{},{},15z".format(str(dee1), str(dee2))
                            		ss = requests.get("http://rahandiapi.herokuapp.com/sswebAPI?key=betakey&link={}".format(urllib.parse.quote(link)))
                            		ret_ = "╔═══[ ᴊᴀᴅᴡᴀʟ sʜᴏʟᴀᴛ ]═══❂"
                            		ret_ += "\n╠═════[ {} ]════❂".format(search)
                            		ret_ += "\n╠❂➣ sʜᴜʙᴜʜ   = " +str(data["pray_time"]["subuh"])
                            		ret_ += "\n╠❂➣ ᴅᴢᴜʜᴜʀ   = " +str(data["pray_time"]["dzuhur"])
                            		ret_ += "\n╠❂➣ ᴀsʜʀ        = " +str(data["pray_time"]["ashar"])
                            		ret_ += "\n╠❂➣ ᴍᴀɢʜʀɪʙ = " +str(data["pray_time"]["maghrib"])
                            		ret_ += "\n╠❂➣ ɪsʜᴀ         = " +str(data["pray_time"]["isha"])
                            		ret_ += "\n╠❂➣ ɪᴍsʏᴀᴋ    = " +str(data["pray_time"]["imsak"])
                            		ret_ += "\n╠════[ " +str(data["info"]["date"])
                            		ret_ += " ]═══❂\n╚════[ ✯ ᴅɴᴀ ʙᴏᴛ ✯ ]═══❂"
                            		ririn.sendMessage(to, str(ret_),contentMetadata = {'AGENT_ICON': 'https://img00.deviantart.net/5562/i/2014/095/4/5/muhammad__pbuhahp__and_allah_calligraphy_gold_by_sheikh1-d7d8fjd.png', 'AGENT_NAME': 'Pray Time.', 'AGENT_LINK': 'http://line.me/ti/p/ppgIZ0JLDW'})
          #                  		ririn.sendImageWithURL(to, str(ss))
                            elif cmd.startswith("checkweather "):
                                try:
                                    sep = text.split(" ")
                                    location = text.replace(sep[0] + " ","")
                                    r = requests.get("https://farzain.com/api/cuaca.php?id={}".format(location))
                                    data = r.text
                                    data = json.loads(data)
                                    tz = pytz.timezone("Asia/Jakarta")
                                    timeNow = datetime.now(tz=tz)
                                    if "result" not in data:
                                        ret_ = "╔═══[ ᴡᴇᴀᴛʜᴇʀ sᴛᴀᴛᴜs ]"
                                        ret_ += "\n╠❂➣ ʟᴏᴄᴀᴛɪᴏɴ : " +str(data["respon"]["tempat"])
                                        ret_ += "\n╠❂➣ cuaca : " +str(data["respon"]["cuaca"])
                                        ret_ += "\n╠❂➣ sᴜʜᴜ : " +str(data["respon"]["suhu"])
                                        ret_ += "\n╠❂➣ ᴋᴇʟᴇᴍʙᴀʙᴀɴ : " +str(data["respon"]["kelembapan"])
                                        ret_ += "\n╠❂➣ ᴛᴇᴋᴀɴᴀɴ ᴜᴅᴀʀᴀ : " +str(data["respon"]["udara"])
                                        ret_ += "\n╠❂➣ ᴋᴇᴄᴇᴘᴀᴛᴀɴ ᴀɴɢɪɴ : " +str(data["respon"]["angin"])
                                        ret_ += "\n╠════[ ᴛɪᴍᴇ sᴛᴀᴛᴜs ]"
                                        ret_ += "\n╠❂➣ ᴛᴀɴɢɢᴀʟ : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                        ret_ += "\n╠❂➣ ᴊᴀᴍ : " + datetime.strftime(timeNow,'%H:%M:%S') + " ᴡɪʙ"
                                        ret_ += "\n╚════[ ✯ ᴅɴᴀ ʙᴏᴛ ✯ ]"
                                        ririn.sendMessage(msg.to, str(ret_),contentMetadata = {'AGENT_ICON': 'http://www.transparentpng.com/download/temperature/hot-sunny-weather-cloud-sea-temperature-png-34.png', 'AGENT_NAME': 'Weather.', 'AGENT_LINK': 'http://line.me/ti/p/ppgIZ0JLDW'})
                                except Exception as error:
                                    logError(error)
                            elif cmd.startswith("checkwebsite"):
                                try:
                                    sep = text.split(" ")
                                    query = text.replace(sep[0] + " ","")
                                    r = requests.get("http://rahandiapi.herokuapp.com/sswebAPI?key=betakey&link={}".format(urllib.parse.quote(query)))
                                    data = r.text
                                    data = json.loads(data)
                                    ririn.sendImageWithURL(to, data["result"])
                                except Exception as error:
                                    logError(error)
                            elif cmd.startswith("instagram "):
                            	try:
                            		search = cmd.replace("instagram ","")
                        	    	r=requests.get("https://api.dzin.tech/api/instaprofile/?apikey=beta&username={}".format(urllib.parse.quote(search)))
                            		data=r.text
                            		data=json.loads(data)
                            		ret_ = "「 Instagram 」\n"
                            		ret_ += "\nUsername : " +str(data["result"]["username"])
                            		ret_ += "\nName : " +str(data["result"]["name"])
                            		ret_ += "\nBio : " +str(data["result"]["bio"])
                            		ret_ += "\nFollowers : " +str(data["result"]["followers"])
                            		ret_ += "\nFollowing : " +str(data["result"]["following"])
                            		ret_ += "\nPost Count : " +str(data["result"]["mediacount"])
                            		ret_ += "\nPrivate : " +str(data["result"]["private"])
                            		url = data["result"]["url"]
                            		path = data["result"]["photo"]
                            		ririn.sendImageWithURL(to, str(path))
                            		ririn.sendMessage(to, str(ret_),contentMetadata = {'AGENT_ICON': 'http://api.ntcorp.us/storage/get/52cAE97', 'AGENT_NAME': 'Instagram.', 'AGENT_LINK': str(url)})
                            	except:
                            		ririn.sendMessage(to, "Username not found.",contentMetadata = {'AGENT_ICON': 'http://api.ntcorp.us/storage/get/52cAE97', 'AGENT_NAME': 'Instagram.', 'AGENT_LINK': str(url)})
                            elif text.lower() == "tiktok":
                            	result = "https://farzain.com/api/tiktok.php"
                            	ririn.sendVideoWithURL(to, str(result))
                            elif text.lower() == "jadwal tv":
                            	result = requests.get("http://ari-api.herokuapp.com/jadwaltv").json()["result"];no=1;tv="╔══════[ ᴊᴀᴅᴡᴀʟ ᴛᴠ ]══════╗\n║\n"
                            	for wildan in result:
                            		tv+="╠❂➣ {}. {} \n╠[ {} ({}) ]\n".format(str(no), str(wildan["channelName"]), str(wildan["acara"]), str(wildan["jam"]))
                            		no+=1
                            	tv+="║\n╚═══════[  ғɪɴɪsʜ  ]═══════╝";ririn.sendMessageWithContent(to, str(tv),'Jadwal Tv.','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                            elif cmd.startswith("retrowave: "):
                            	try:
                            		separate = msg.text.split(" ")
                            		teks = msg.text.replace(separate[0] + " ","")
                            		pemisah = teks.split(":")
                            		nad1 = pemisah[0]
                            		nad2 = pemisah[1]
                            		nad3 = pemisah[2] 
                            		nmor = ["1","2","3","4","5"]
                            		bg = random.choice(nmor)
                            		nmor2 = ["1","2","3","4"]
                            		tt = random.choice(nmor2)
                            		url = requests.get("http://leert.corrykalam.gq/retrowave.php?text1="+nad1+"&text2="+nad2+"&text3="+nad3+"&btype="+bg+"&ttype="+tt)
                            		data = url.json()
                            		ririn.sendImageWithURL(msg.to, str(data["image"]))
                            	except Exception as error:
                            		pass
                            elif cmd.startswith("searchimage"):
                                try:
                                    separate = msg.text.split(" ")
                                    search = msg.text.replace(separate[0] + " ","")
                                    r = requests.get("http://rahandiapi.herokuapp.com/imageapi?key=betakey&q={}".format(search))
                                    data = r.text
                                    data = json.loads(data)
                                    if data["result"] != []:
                                        items = data["result"]
                                        path = random.choice(items)
                                        a = items.index(path)
                                        b = len(items)
                                        ririn.sendImageWithURL(to, str(path))
                                except Exception as error:
                                    logError(error)
                            elif cmd.startswith("searchlyric"):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split("|")
                                search = cond[0]
                                api = requests.get("Sttp://api.secold.com/joox/cari/{}".format(str(search)))
                                data = api.text
                                data = json.loads(data)
                                if len(cond) == 1:
                                    num = 0
                                    ret_ = "╔══[ ʀᴇsᴜʟᴛ ʟʏʀɪᴄ ]"
                                    for lyric in data["results"]:
                                        num += 1
                                        ret_ += "\n╠❂➣ {}. {}".format(str(num), str(lyric["single"]))
                                        ret_ += "\n╚══[ ᴛᴏᴛᴀʟ {} ᴍᴜsɪᴄ ]".format(str(len(data["results"])))
                                        ret_ += "\n\nᴜɴᴛᴜᴋ ᴍᴇʟɪʜᴀᴛ ᴅᴇᴛᴀɪʟs ʟʏʀɪᴄ, sɪʟᴀʜᴋᴀɴ ɢᴜɴᴀᴋᴀɴ ᴄᴏᴍᴍᴀɴᴅ {}sᴇᴀʀᴄʜʟʏʀɪᴄ {}|「ɴᴜᴍʙᴇʀ」".format(str(setKey), str(search))
                                        ririn.sendMessage(msg.to, str(ret_))
                                elif len(cond) == 2:
                                    num = int(cond[1])
                                    if num <= len(data["results"]):
                                        lyric = data["results"][num - 1]
                                        api = requests.get("http://api.secold.com/joox/sid/{}".format(str(lyric["songid"])))
                                        data = api.text
                                        data = json.loads(data)
                                        lyrics = data["results"]["lyric"]
                                        lyric = lyrics.replace('ti:','Title - ')
                                        lyric = lyric.replace('ar:','Artist - ')
                                        lyric = lyric.replace('al:','Album - ')
                                        removeString = "[1234567890.:]"
                                        for char in removeString:
                                            lyric = lyric.replace(char,'')
                                            ririn.sendMessage(msg.to, str(lyric))
                            elif cmd.startswith("searchmusic "):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split("|")
                                search = str(cond[0])
                                result = requests.get("http://api.ntcorp.us/joox/search?q={}".format(str(search)))
                                data = result.text
                                data = json.loads(data)
                                if len(cond) == 1:
                                    num = 0
                                    ret_ = "╔══[ ʀᴇsᴜʟᴛ ᴍᴜsɪᴄ ]"
                                    for music in data["result"]:
                                        num += 1
                                        ret_ += "\n╠ {}. {}".format(str(num), str(music["single"]))
                                    ret_ += "\n╚══[ ᴛᴏᴛᴀʟ {} ᴍᴜsɪᴄ ] ".format(str(len(data["result"])))
                                    ret_ += "\n\nᴜɴᴛᴜᴋ ᴍᴇʟɪʜᴀᴛ ᴅᴇᴛᴀɪʟs ᴍᴜsɪᴄ, sɪʟᴀʜᴋᴀɴ ɢᴜɴᴀᴋᴀɴ ᴄᴏᴍᴍᴀɴᴅ {}sᴇᴀʀᴄʜᴍᴜsɪᴄ {}|「ɴᴜᴍʙᴇʀ」".format(str(setKey), str(search))
                                    ririn.sendMessageWithContent(msg.to, str(ret_),'JOOX MUSIC.','http://joox.com','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                                elif len(cond) == 2:
                                    num = int(cond[1])
                                    if num <= len(data["result"]):
                                        music = data["result"][num - 1]
                                        result = requests.get("http://api.ntcorp.us/joox/song_info?sid={}".format(str(music["sid"])))
                                        data = result.text
                                        data = json.loads(data)
                                        if data["result"] != []:
                                            ret_ = "╔══════[ ᴍᴜsɪᴄ ]"
                                            ret_ += "\n╠❂➣ ᴛɪᴛʟᴇ : {}".format(str(data["result"]["song"]))
                                            ret_ += "\n╠❂➣ ᴀʟʙᴜᴍ : {}".format(str(data["result"]["album"]))
                                            ret_ += "\n╠❂➣ sɪᴢᴇ : {}".format(str(data["result"]["size"]))
                                            ret_ += "\n╠❂➣ ʟɪɴᴋ :  {}".format(str(data["result"]["mp3"][0]))
                                            ret_ += "\n╚════[ ✯ ᴅɴᴀ ʙᴏᴛ ✯ ]"
                                            ririn.sendImageWithURL(to, str(data["result"]["img"]))
                                            ririn.sendMessageWithContent(msg.to, str(ret_),'{}'.format(str(data["result"]["song"])),'{}'.format(str(data["result"]["mp3"][0])),'{}'.format(str(data["result"]["img"])))
                                            ririn.sendAudioWithURL(to, str(data["result"]["mp3"][0]))
                            elif cmd.startswith("searchyoutube"):
                                sep = text.split(" ")
                                search = text.replace(sep[0] + " ","")
                                params = {"search_query": search}
                                r = requests.get("https://www.youtube.com/results", params = params)
                                soup = BeautifulSoup(r.content, "html5lib")
                                ret_ = "╔═══[  ʏᴏᴜᴛᴜʙᴇ ʀᴇsᴜʟᴛ  ]═══╗"
                                datas = []
                                for data in soup.select(".yt-lockup-title > a[title]"):
                                    if "&lists" not in data["href"]:
                                        datas.append(data)
                                for data in datas:
                                    ret_ += "\n╠❂➣ {}".format(str(data["title"]))
                                    ret_ += "\n╠[ https://www.youtube.com{} ]".format(str(data["href"]))
                                ret_ += "\n╚══════[ ᴛᴏᴛᴀʟ {} ]══════╝".format(len(datas))
                                ririn.sendMessageWithContent(to, str(ret_),'Youtube','http://line.me/ti/p/ppgIZ0JLDW','http://www.freepngimg.com/download/youtube/1-2-youtube-free-download-png.png')
                            elif msg.text.lower().startswith("ytmp3: "):
                               sep = msg.text.split(" ")
                               query = text.replace(sep[0] + " ","")
                               r = requests.get("http://leert.corrykalam.gq/yt.php?url={}".format(urllib.parse.quote(query)))
                               data = r.text
                               data = json.loads(data)
                               video = data["mp4"]["360"]
                               ret_ = "╔══[  ʏᴏᴜᴛᴜʙᴇ ᴍᴘ3 ʀᴇsᴜʟᴛ  ]══╗"
                               ret_ += "\n╠❂ [{}]" .format(str(data["tittle"]))
                               ret_ += "\n╠❂ [ᴘʀᴏᴄᴇss ᴛᴏ ᴜᴘʟᴏᴀᴅ ᴀᴜᴅɪᴏ]"
                               ret_ += "\n╚════[  ✯  ᴅɴᴀ  ʙᴏᴛ  ✯  ]════╝"
                               ririn.sendMessageWithContent(to, str(ret_),'Youtube Mp3','http://line.me/ti/p/ppgIZ0JLDW','http://www.freepngimg.com/download/youtube/1-2-youtube-free-download-png.png')
                               ririn.sendAudioWithURL(to, video)
                            elif msg.text.lower().startswith("ytmp4: "):
                               sep = msg.text.split(" ")
                               query = text.replace(sep[0] + " ","")
                               r = requests.get("http://leert.corrykalam.gq/yt.php?url={}".format(urllib.parse.quote(query)))
                               data = r.text
                               data = json.loads(data)
                               video = data["mp4"]["360"]
                               ret_ = "╔══[  ʏᴏᴜᴛᴜʙᴇ ᴍᴘ4 ʀᴇsᴜʟᴛ  ]══╗"
                               ret_ += "\n╠❂ [{}]" .format(str(data["tittle"]))
                               ret_ += "\n╠❂ [ᴘʀᴏᴄᴇss ᴛᴏ ᴜᴘʟᴏᴀᴅ ᴠɪᴅᴇᴏ]"
                               ret_ += "\n╚════[  ✯  ᴅɴᴀ  ʙᴏᴛ  ✯  ]════╝"
                               ririn.sendMessageWithContent(to, str(ret_),'Youtube Mp4','http://line.me/ti/p/ppgIZ0JLDW','http://www.freepngimg.com/download/youtube/1-2-youtube-free-download-png.png')
                               ririn.sendVideoWithURL(to, video)
                            elif cmd.startswith('/call '):
                                try:
                                    call = text.replace('/call ','')
                                    r = requests.get('https://farzain.com/api/prank.php?id='+call+'&type=2')
                                    sendMention(receiver, "@!       sᴜᴋsᴇs ᴍᴇʟᴀᴋᴜᴋᴀɴ ᴘᴀɴɢɢɪʟᴀɴ ᴋᴇ ɴᴏᴍᴏʀ "+call,[sender])
                                except Exception as e:
                                    ririn.sendMessage(receiver, str(e))
                                    logError(e)
                            elif cmd.startswith('/sms '):
                                try:
                                    sms = text.replace('/sms ','')
                                    r = requests.get('https://farzain.com/api/prank.php?id='+sms+'&type=1')
                                    sendMention(receiver, "@!       sᴜᴋsᴇs ᴍᴇɴɢɪʀɪᴍ ᴘᴇsᴀɴ ᴋᴇ ɴᴏᴍᴏʀ "+sms,[sender])
                                except Exception as e:
                                    ririn.sendMessage(receiver, str(e))
                                    logError(e)
#------------------------------------============================------------------------------------#
#======================-----------✰ ᴅɴᴀ ʙᴏᴛ ✰-----------======================#
#------------------------------------============================------------------------------------#
                            if cmd == "restart":
                                ririn.sendMessageWithContent(to, "ʙᴏᴛ ʜᴀᴠᴇ ʙᴇᴇɴ ʀᴇsᴛᴀʀᴛ",'Restart.','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                                restartBot()
                            elif cmd == "runtime":
                                timeNow = time.time()
                                runtime = timeNow - botStart
                                runtime = format_timespan(runtime)
                                ririn.sendMessageWithContent(to, "ʀᴜɴɴɪɴɢ ɪɴ.. {}".format(str(runtime)),'Run Time','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                            elif cmd == "sp":
                            	ririn.sendMessageWithContent(to, "❂➣ ʟᴏᴀᴅɪɴɢ...",'Process.','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                            	sp = int(round(time.time() *1000))
                            	ririn.sendMessageWithContent(to,"ᴍʏ sᴘᴇᴇᴅ : %sms" % (sp - op.createdTime),'Speed.','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                            elif cmd == "speed":
                            	start = time.time()
                            	ririn.sendMessageWithContent(to, "❂➣ ʟᴏᴀᴅɪɴɢ...",'Process.','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                            	elapsed_time = time.time() - start
                            	ririn.sendMessageWithContent(to, "ᴍʏ sᴘᴇᴇᴅ : %sms" % (elapsed_time),'Speed.','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                            elif cmd == "status":
                                try:
                                    ret_ = "╔═════[ ·✪·sᴛᴀᴛᴜs·✪· ]═════╗"
                                    if wait["autoAdd"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴀᴜᴛᴏ ᴀᴅᴅ 「⚪」"
                                    else: ret_ += "\n╠❂➣ [ ᴏғғ ] ᴀᴜᴛᴏ ᴀᴅᴅ 「⚫」"
                                    if wait["autoJoin"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴀᴜᴛᴏ ᴊᴏɪɴ 「⚪」"
                                    else: ret_ += "\n╠❂➣ [ ᴏғғ ] ᴀᴜᴛᴏ ᴊᴏɪɴ 「⚫」"
                                    if wait["autoLeave"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴀᴜᴛᴏ ʟᴇᴀᴠᴇ 「⚪」"
                                    else: ret_ += "\n╠❂➣ [ ᴏғғ ] ᴀᴜᴛᴏ ʟᴇᴀᴠᴇ 「⚫」"
                                    if wait["autoJoinTicket"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴊᴏɪɴ ᴛɪᴄᴋᴇᴛ 「⚪」"
                                    else: ret_ += "\n╠❂➣ [ ᴏғғ ] ᴊᴏɪɴ ᴛɪᴄᴋᴇᴛ 「⚫」"
                                    if wait["autoRead"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴀᴜᴛᴏ ʀᴇᴀᴅ 「⚪」"
                                    else: ret_ += "\n╠❂➣ [ ᴏғғ ] ᴀᴜᴛᴏ ʀᴇᴀᴅ 「⚫」"
                                    if wait["autoRespon"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ 「⚪」"
                                    else: ret_ += "\n╠❂➣ [ ᴏғғ ] ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ 「⚫」"
                                    if wait["autoReply"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴀᴜᴛᴏ ʀᴇᴘʟʏ 「⚪」"
                                    else: ret_ += "\n╠❂➣ [ ᴏғғ ] ᴀᴜᴛᴏ ʀᴇᴘʟʏ 「⚫」"
                                    if wait["checkContact"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴄʜᴇᴄᴋ ᴄᴏɴᴛᴀᴄᴛ 「⚪」"
                                    else: ret_ += "\n╠❂➣ [ ᴏғғ ] ᴄʜᴇᴄᴋ ᴄᴏɴᴛᴀᴄᴛ 「⚫」"
                                    if wait["checkPost"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴄʜᴇᴄᴋ ᴘᴏsᴛ 「⚪」"
                                    else: ret_ += "\n╠❂➣ [ ᴏғғ ] ᴄʜᴇᴄᴋ ᴘᴏsᴛ 「⚫」"
                                    if wait["checkSticker"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴄʜᴇᴄᴋ sᴛɪᴄᴋᴇʀ 「⚪」"
                                    else: ret_ += "\n╠❂➣ [ ᴏғғ ] ᴄʜᴇᴄᴋ sᴛɪᴄᴋᴇʀ 「⚫」"
                                    if wait["setKey"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] sᴇᴛ ᴋᴇʏ 「⚪」"
                                    else: ret_ += "\n╠❂➣ [ ᴏғғ ] sᴇᴛ ᴋᴇʏ 「⚫」"
                                    if wait["unsendMessage"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴜɴsᴇɴᴅ ᴍsɢ 「⚪」"
                                    else: ret_ += "\n╠❂➣ [ ᴏғғ ] ᴜɴsᴇɴᴅ ᴍsɢ 「⚫」"
                                    ret_ += "\n╚═════[ ✯ ᴅɴᴀ ʙᴏᴛ ✯ ]═════╝"
                                    ririn.sendMessageWithContent(to, str(ret_),'Status.','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                                except Exception as e:
                                    ririn.sendMessageWithContent(msg.to, str(e),'Status.','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                        if cmd == "mykey":
                            ririn.sendMessage(to, "KeyCommand Saat ini adalah [ {} ]".format(str(wait["keyCommand"])))
                        elif cmd == "setkey on":
                            wait["setKey"] = True
                            ririn.sendMessage(to, "Berhasil mengaktifkan setkey")
                        elif text.lower() == "setkey off":
                            wait["setKey"] = False
                            ririn.sendMessage(to, "Berhasil menonaktifkan setkey")
#------------------------------------============================------------------------------------#
#======================-----------✰ ᴅɴᴀ ʙᴏᴛ ✰-----------======================#
#------------------------------------============================------------------------------------#
                    elif msg.contentType == 1:
                    	if wait["changePictureProfile"] == True:
                    		path = ririn.downloadObjectMsg(msg_id)
                    		wait["changePictureProfile"] = False
                    		ririn.updateProfilePicture(path)
                    		contact = ririn.getContact(sender)
                    		ririn.sendMessageWithContent(to, "sᴜᴄᴄᴇs ᴄʜᴀɴɢᴇ ᴘʜᴏᴛᴏ ᴘʀᴏғɪʟᴇ",'Succes Change Picture.','http://line.me/ti/p/ppgIZ0JLDW','http://dl.profile.line-cdn.net/{}'.format(contact.pictureStatus))
                    	if msg.contentType == 1:
                        	if wait["changeCover"] == True:
                        		path = ririn.downloadObjectMsg(msg_id)
                        		wait["changeCover"] = False
                        		ririn.updateProfileCover(path)
                        		contact = ririn.getContact(sender)
                        		ririn.sendMessageWithContent(to, "sᴜᴄᴄᴇs ᴄʜᴀɴɢᴇ ᴘʜᴏᴛᴏ ᴘʀᴏғɪʟᴇ",'Succes Change Picture.','http://line.me/ti/p/ppgIZ0JLDW','http://dl.profile.line-cdn.net/{}'.format(contact.pictureStatus))
                    	if msg.toType == 2:
                            if to in wait["changeGroupPicture"]:
                                path = ririn.downloadObjectMsg(msg_id)
                                wait["changeGroupPicture"].remove(to)
                                ririn.updateGroupPicture(to, path)
                                group = ririn.getGroup(to)
                                pathh = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                                gTicket = "https://line.me/R/ti/g/{}".format(str(ririn.reissueGroupTicket(group.id)))
                                ririn.sendMessage(to, "sᴜᴄᴄᴇs ᴄʜᴀɴɢᴇ ᴘʜᴏᴛᴏ ɢʀᴏᴜᴘ",contentMetadata = {'AGENT_ICON': pathh, 'AGENT_NAME': '{}'.format(str(group.name)), 'AGENT_LINK': '{}'.format(gTicket)})
                    elif msg.contentType == 7:
                        if wait["checkSticker"] == True:
                            stk_id = msg.contentMetadata['STKID']
                            stk_ver = msg.contentMetadata['STKVER']
                            pkg_id = msg.contentMetadata['STKPKGID']
                            ret_ = "╔════[ sᴛɪᴄᴋᴇʀ ɪɴғᴏ ] "
                            ret_ += "\n╠❂➣ sᴛɪᴄᴋᴇʀ ɪᴅ : {}".format(stk_id)
                            ret_ += "\n╠❂➣ sᴛɪᴄᴋᴇʀ ᴘᴀᴄᴋᴀɢᴇs ɪᴅ : {}".format(pkg_id)
                            ret_ += "\n╠❂➣ sᴛɪᴄᴋᴇʀ ᴠᴇʀsɪᴏɴ : {}".format(stk_ver)
                            ret_ += "\n╠❂➣ sᴛɪᴄᴋᴇʀ ᴜʀʟ : line://shop/detail/{}".format(pkg_id)
                            ret_ += "\n╚════[ ✯ ᴅɴᴀ ʙᴏᴛ ✯ ]"
                            ririn.sendMessageWithContent(to, str(ret_),'Check Sticker.','line://shop/detail/{}'.format(pkg_id),'https://preview.ibb.co/dpBpCd/20180601_164057.png')
                    elif msg.contentType == 13:
                        if wait["checkContact"] == True:
                            try:
                                contact = ririn.getContact(msg.contentMetadata["mid"])
                                if ririn != None:
                                    cover = ririn.getProfileCoverURL(msg.contentMetadata["mid"])
                                else:
                                    cover = "Tidak dapat masuk di line channel"
                                path = "http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                                try:
                                    ririn.sendImageWithURL(to, str(path))
                                except:
                                    pass
                                ret_ = "╔═══[ ᴅᴇᴛᴀɪʟs ᴄᴏɴᴛᴀᴄᴛ ]"
                                ret_ += "\n╠❂➣ ɴᴀᴍᴀ : {}".format(str(contact.displayName))
                                ret_ += "\n╠❂➣ ᴍɪᴅ : {}".format(str(msg.contentMetadata["mid"]))
                                ret_ += "\n╠❂➣ ʙɪᴏ : {}".format(str(contact.statusMessage))
                                ret_ += "\n╠❂➣ ɢᴀᴍʙᴀʀ ᴘʀᴏғɪʟᴇ : http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                                ret_ += "\n╠❂➣ ɢᴀᴍʙᴀʀ ᴄᴏᴠᴇʀ : {}".format(str(cover))
                                ret_ += "\n╚════[ ✯ ᴅɴᴀ ʙᴏᴛ ✯ ]"
                                ririn.sendMessageWithContent(to, str(ret_),'{}'.format(str(contact.displayName)),'http://line.me/ti/p/ppgIZ0JLDW','http://dl.profile.line-cdn.net/{}'.format(str(contact.pictureStatus)))
                            except:
                                ririn.sendMessageWithContent(to, "ᴋᴏɴᴛᴀᴋ ᴛɪᴅᴀᴋ ᴠᴀʟɪᴅ",'Check Contact.','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                    elif msg.contentType == 16:
                        if wait["checkPost"] == True:
                            try:
                                ret_ = "╔════[ ᴅᴇᴛᴀɪʟs ᴘᴏsᴛ ]"
                                if msg.contentMetadata["serviceType"] == "GB":
                                    contact = ririn.getContact(sender)
                                    auth = "\n╠❂➣ ᴀᴜᴛʜᴏʀ : {}".format(str(contact.displayName))
                                else:
                                    auth = "\n╠❂➣ ᴀᴜᴛʜᴏʀ : {}".format(str(msg.contentMetadata["serviceName"]))
                                purl = "\n╠❂➣ ᴜʀʟ : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                                ret_ += auth
                                ret_ += purl
                                if "mediaOid" in msg.contentMetadata:
                                    object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                                    if msg.contentMetadata["mediaType"] == "V":
                                        if msg.contentMetadata["serviceType"] == "GB":
                                            ourl = "\n╠❂➣ ᴏʙᴊᴇᴄᴛ ᴜʀʟ : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                            murl = "\n╠❂➣ ᴍᴇᴅɪᴀ ᴜʀʟ : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                        else:
                                            ourl = "\n╠❂➣ ᴏʙᴊᴇᴄᴛ ᴜʀʟ : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                            murl = "\n╠❂➣ ᴍᴇᴅɪᴀ ᴜʀʟ : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                        ret_ += murl
                                    else:
                                        if msg.contentMetadata["serviceType"] == "GB":
                                            ourl = "\n╠❂➣ ᴏʙᴊᴇᴄᴛ ᴜʀʟ : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                        else:
                                            ourl = "\n╠❂➣ ᴏʙᴊᴇᴄᴛ ᴜʀʟ : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                    ret_ += ourl
                                if "stickerId" in msg.contentMetadata:
                                    stck = "\n╠❂➣ sᴛɪᴄᴋᴇʀ : https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                                    ret_ += stck
                                if "text" in msg.contentMetadata:
                                    text = "\n╠❂➣ ɴᴏᴛᴇ : {}".format(str(msg.contentMetadata["text"]))
                                    ret_ += text
                                ret_ += "\n╚════[ ✯ ᴅɴᴀ ʙᴏᴛ ✯ ]"
                                ririn.sendMessageWithContent(to, str(ret_),'{}'.format(str(contact.displayName)),'http://line.me/ti/p/ppgIZ0JLDW','http://dl.profile.line-cdn.net/{}'.format(str(contact.pictureStatus)))
                            except:
                                ririn.sendMessageWithContent(to, "ɪɴᴠᴀʟɪᴅ ᴘᴏsᴛ",'Check Post.','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
            except Exception as error:
                logError(error)
                traceback.print_tb(error.__traceback__)
                
        if op.type in [25, 26]:
            if op.type == 25: print ("[ 25 ] SEND MESSAGE")
            else: print ("[ 26 ] RECEIVE MESSAGE")
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            cmd = command(text)
            isValid = True
            setKey = wait["keyCommand"].title()
            if wait["setKey"] == False: setKey = ''
            if isValid != False:
                if msg.toType == 0 and sender != ririnMid: to = sender
                else: to = receiver
                if receiver in temp_flood:
                    if temp_flood[receiver]["expire"] == True:
                        if cmd == "open" and sender == ririnMid:
                            temp_flood[receiver]["expire"] = False
                            temp_flood[receiver]["time"] = time.time()
                            ririn.sendMessage(to, "Bot kembali aktif")
                        return
                    elif time.time() - temp_flood[receiver]["time"] <= 5:
                        temp_flood[receiver]["flood"] += 1
                        if temp_flood[receiver]["flood"] >= 20:
                            temp_flood[receiver]["flood"] = 0
                            temp_flood[receiver]["expire"] = True
                            ret_ = "Spam terdeteksi, Bot akan silent selama 30 detik pada ruangan ini atau ketik {}Open untuk mengaktifkan kembali.".format(setKey)
                            ririn.sendMessage(to, str(ret_))
                    else:
                         temp_flood[receiver]["flood"] = 0
                         temp_flood[receiver]["time"] = time.time()
                else:
                    temp_flood[receiver] = {
    	                "time": time.time(),
    	                "flood": 0,
    	                "expire": False
                    }
                
        if op.type == 26:
            msg = op.message
            if wait["autoReply"] == True:
                if msg.toType == 0:                	
                    ririn.sendChatChecked(msg._from,msg.id)
                    contact = ririn.getContact(msg._from)
                    cName = contact.displayName
                    balas = ["╔════════════════════╗\n                   「ᴀᴜᴛᴏ ʀᴇᴘʟʏ」\n                             ʙʏ:\n                    ✰ ᴅɴᴀ ʙᴏᴛ ✰\n╚════════════════════╝\n\nʜᴀʟʟᴏ 「  @! 」\nᴍᴏʜᴏɴ ᴍᴀᴀғ sᴀʏᴀ sᴇᴅᴀɴɢ sɪʙᴜᴋ, ɪɴɪ ᴀᴅᴀʟᴀʜ ᴘᴇsᴀɴ ᴏᴛᴏᴍᴀᴛɪs, ᴊɪᴋᴀ ᴀᴅᴀ ʏᴀɴɢ ᴘᴇɴᴛɪɴɢ ᴍᴏʜᴏɴ ʜᴜʙᴜɴɢɪ sᴀʏᴀ ɴᴀɴᴛɪ, ᴛᴇʀɪᴍᴀᴋᴀsɪʜ...","╔════════════════════╗\n                   「ᴀᴜᴛᴏ ʀᴇᴘʟʏ」\n                             ʙʏ:\n                    ✰ ᴅɴᴀ ʙᴏᴛ ✰\n╚════════════════════╝\n\nʜᴀʟʟᴏ 「 @! 」\nsᴀʏᴀ ʟᴀɢɪ sɪʙᴜᴋ ʏᴀ ᴋᴀᴋ ᴊᴀɴɢᴀɴ ᴅɪɢᴀɴɢɢᴜ","╔════════════════════╗\n                   「ᴀᴜᴛᴏ ʀᴇᴘʟʏ」\n                             ʙʏ:\n                    ✰ ᴅɴᴀ ʙᴏᴛ ✰\n╚════════════════════╝\n\nʜᴀʟʟᴏ 「 @! 」\nsᴀʏᴀ sᴇᴅᴀɴɢ ᴛɪᴅᴜʀ ᴋᴀᴋ"]
                    dee = "" + random.choice(balas)
                    ririn.sendImageWithURL(msg._from, "http://dl.profile.line-cdn.net{}".format(contact.picturePath))
                    sendMention(msg._from,dee)
                
        if op.type == 26:
            try:
                print ("[ 26 ] RECIEVE MESSAGE")
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                    if msg.toType == 0:
                        if sender != ririn.profile.mid:
                            to = sender
                        else:
                            to = receiver
                    elif msg.toType == 1:
                        to = receiver
                    elif msg.toType == 2:
                        to = receiver
                    if wait["autoRead"] == True:
                        ririn.sendChatChecked(to, msg_id)
                    if to in read["readPoint"]:
                        if sender not in read["ROM"][to]:
                            read["ROM"][to][sender] = True
                    if sender in wait["mimic"]["target"] and wait["mimic"]["status"] == True and wait["mimic"]["target"][sender] == True:
                        text = msg.text
                        if text is not None:
                            ririn.sendMessage(msg.to,text,'My Creator.','http://line.me/ti/p/ppgIZ0JLDW','https://preview.ibb.co/dpBpCd/20180601_164057.png')
                    if wait["unsendMessage"] == True:
                        try:
                            msg = op.message
                            if msg.toType == 0:
                                ririn.log("[{} : {}]".format(str(msg._from), str(msg.text)))
                            else:
                                ririn.log("[{} : {}]".format(str(msg.to), str(msg.text)))
                                msg_dict[msg.id] = {"text": msg.text, "from": msg._from, "createdTime": msg.createdTime, "contentType": msg.contentType, "contentMetadata": msg.contentMetadata}
                        except Exception as error:
                            logError(error)
                    if msg.contentType == 0:
                        if text is None:
                            return
                        if "/ti/g/" in msg.text.lower():
                            if wait["autoJoinTicket"] == True:
                                link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                links = link_re.findall(text)
                                n_links = []
                                for l in links:
                                    if l not in n_links:
                                        n_links.append(l)
                                for ticket_id in n_links:
                                    group = ririn.findGroupByTicket(ticket_id)
                                    ririn.acceptGroupInvitationByTicket(group.id,ticket_id)
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(ririn.reissueGroupTicket(group.id)))
                                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                                    ririn.sendMessage(to, "sᴜᴄᴄᴇssғᴜʟʟʏ ᴇɴᴛᴇʀᴇᴅ ᴛʜᴇ ɢʀᴏᴜᴘ %s" % str(group.name),contentMetadata = {'AGENT_ICON': path, 'AGENT_NAME': '{}'.format(str(group.name)), 'AGENT_LINK': '{}'.format(gTicket)})
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if ririnMid in mention["M"]:
                                    if wait["autoRespon"] == True:
                                    	ririn.sendChatChecked(sender,msg_id)
                                    	contact = ririn.getContact(sender)
                                    	cName = contact.displayName
                                    	balas = ["ᴏɪ「" + cName+ "」ᴊᴏᴍʙʟᴏ ʏᴇᴇ \nɴɢᴀᴘᴀɪɴ ᴛᴀɢ ᴛᴀɢ ɢᴡ","awas「" + cName + "」ᴊᴀɴɢᴀɴ ᴋᴇsᴇʀɪɴɢᴀɴ ᴛᴀɢ\nɴᴛᴀʀ ᴋᴇᴛᴀɢɪʜᴀɴ ʟᴏʜ","ᴄɪʏᴇᴇ「" + cName + "」ʏᴀɴɢ ᴅᴇᴍᴇɴ ʙᴀɴɢᴇᴛ ᴛᴀɢ ᴀǫ\nᴋᴀɴɢᴇɴ ʏᴇᴇᴇ..."]
                                    	dee = "" + random.choice(balas)
                                    	ririn.sendImageWithURL(sender, "http://dl.profile.line-cdn.net{}".format(contact.picturePath))
                                    	ririn.sendMessage(sender,dee,contentMetadata = {'AGENT_ICON': 'https://preview.ibb.co/dpBpCd/20180601_164057.png', 'AGENT_NAME': 'Auto Respon.', 'AGENT_LINK': 'http://line.me/ti/p/ppgIZ0JLDW'})
            except Exception as error:
                logError(error)
                traceback.print_tb(error.__traceback__)
                
        if op.type == 65:
            print ("[ 65 ] NOTIFIED DESTROY MESSAGE")
            if wait["unsendMessage"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                            contact = ririn.getContact(msg_dict[msg_id]["from"])
                            if contact.displayNameOverridden != None:
                                name_ = contact.displayNameOverridden
                                contact = ririn.getContact(sender)
                                cName = contact.displayName
                                gTicket = "https://line.me/R/ti/g/{}".format(str(ririn.reissueGroupTicket(group.id)))
                            else:
                                name_ = contact.displayName
                                ret_ = "sᴇɴᴅ ᴍᴇssᴀɢᴇ ᴄᴀɴᴄᴇʟʟᴇᴅ."
                                ret_ += "\nsᴇɴᴅᴇʀ : @!      "
                                ret_ += "\nsᴇɴᴅ ᴀᴛ : {}".format(str(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"]))))
                                ret_ += "\nᴛʏᴘᴇ : {}".format(str(Type._VALUES_TO_NAMES[msg_dict[msg_id]["contentType"]]))
                                ret_ += "\nᴛᴇxᴛ : {}".format(str(msg_dict[msg_id]["text"]))
                                sendMention(at, str(ret_), [contact.mid])
                            del msg_dict[msg_id]
                        else:
                            ririn.sendMessage(at,"sᴇɴᴛᴍᴇssᴀɢᴇ ᴄᴀɴᴄᴇʟʟᴇᴅ,ʙᴜᴛ ɪ ᴅɪᴅɴ'ᴛ ʜᴀᴠᴇ ʟᴏɢ ᴅᴀᴛᴀ.\nsᴏʀʀʏ > <",contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/{}'.format(contact.pictureStatus), 'AGENT_NAME': '{}'.format(str(contact.displayName)), 'AGENT_LINK': gTicket})
                except Exception as error:
                    logError(error)
                    traceback.print_tb(error.__traceback__)
                    
        if op.type == 55:
        	try:
        		group_id = op.param1
        		user_id=op.param2
        		subprocess.Popen('echo "'+ user_id+'|'+str(op.createdTime)+'" >> dataSeen/%s.txt' % group_id, shell=True, stdout=subprocess.PIPE, )
        	except Exception as e:
        		print(e)
	      
        if op.type == 55:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = ririn.getContact(op.param2).displayName
                            dan = ririn.getContact(op.param2)
                            tgb = ririn.getGroup(op.param1)
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n• " + Name
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        sendMention(op.param1, "ᴡᴏʏ ☞ @! ☜\nᴅɪ {} ᴋᴏᴋ ᴅɪᴇᴍ ᴅɪᴇᴍ ʙᴀᴇ...\nsɪɴɪ ɪᴋᴜᴛ ɴɢᴏᴘɪ".format(str(tgb.name)),[op.param2])
                                        ririn.sendContact(op.param1, op.param2)
                                        ririn.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan.picturePath))
                                    else:
                                        sendMention(op.param1, "ᴍʙʟᴏ ☞ @! ☜\nɴɢɪɴᴛɪᴘ ᴅᴏᴀɴɢ ʟᴜ ᴅɪ {} \nsɪɴɪ ɢᴀʙᴜɴɢ ᴍᴀ ᴋɪᴛᴀ".format(str(tgb.name)),[op.param2])
                                        ririn.sendContact(op.param1, op.param2)
                                        ririn.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan.picturePath))
                                else:
                                    sendMention(op.param1, "ʜɪʟɪʜ ☞ @! ☜\nɴɢᴀᴘᴀɪɴ ʟᴜ...\nɢᴀʙᴜɴɢ ᴄʜᴀᴛ sɪɴɪ ᴅɪ {} ".format(str(tgb.name)),[op.param2])
                                    ririn.sendContact(op.param1, op.param2)
                                    ririn.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan.picturePath))
                        else:
                            pass
                    else:
                        pass
                except:
                    pass

        else:
            pass
                
        if op.type == 55:
            print ("[ 55 ] NOTIFIED READ MESSAGE")
            try:
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                else:
                   pass
            except Exception as error:
                logError(error)
                traceback.print_tb(error.__traceback__)
    except Exception as error:
        logError(error)
        traceback.print_tb(error.__traceback__)

while True:
    try:
        delete_log()
        ops = ririnPoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                ririnBot(op)
                ririnPoll.setRevision(op.revision)
    except Exception as error:
        logError(error)
        
def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")
atexit.register(atend)
