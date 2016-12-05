import xbmcaddon, xbmcgui, xbmc, os, sys, urllib, urllib2, xbmcplugin, re, extract, downloader, updater 


USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
addon_id="plugin.program.BauildATester"
ADDON=xbmcaddon.Addon(id=addon_id)
AddonTitle="Builda tester wizard"
proname="amc"
pointerurl="https://mk-iv.github.io"
dialog=xbmcgui.Dialog()
HOME=xbmc.translatePath('special://home/')
dp=xbmcgui.DialogProgress()
FANART=xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))
ICON=xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png')) 
Updater=xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'updater.py'))
VERSION="1.0.0"
Addons26=xbmc.translatePath(os.path.join('special://home/userdata/Database/','Addons26.db'))



def Index():
        link = Open_Url(pointerurl).replace('\n','').replace('\r','')
        match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
        for name,url,iconimage,fanart,description in match:
            addDir(name,url,1,iconimage,fanart,description)
            

def addDir(name,url,mode,iconimage,fanart,description):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok


def platform():
    if xbmc.getCondVisibility('system.platform.android'):
        return 'android'
    elif xbmc.getCondVisibility('system.platform.linux'):
        return 'linux'
    elif xbmc.getCondVisibility('system.platform.windows'):
        return 'windows'
    elif xbmc.getCondVisibility('system.platform.osx'):
        return 'osx'
    elif xbmc.getCondVisibility('system.platform.atv2'):
        return 'atv2'
    elif xbmc.getCondVisibility('system.platform.ios'):
        return 'ios'


def Open_Url(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    return link
        
def Wizard(name,url,description):
    path = xbmc.translatePath(os.path.join('special://home/addons','packages'))
    dp = xbmcgui.DialogProgress()        
    dp.create("Builda tester wizard","Downloading required files... ",'', 'Please Wait')
    lib=os.path.join(path, name+'.zip')
    try:
       os.remove(lib)
    except:
       pass
    downloader.download(url, lib, dp)
    addonfolder = xbmc.translatePath(os.path.join('special://','home'))
    dp.update(0,"Downloading required files...[COLOR lime]DONE[/COLOR]", "Extracting")
    if os.path.exists(Addons26):
        TriggerMigration()
        pass
    else:
        pass   
    try: 
        extract.all(lib,addonfolder,dp)
    except IOError as e:
        xbmc.log(''+e+'') 
    dialog.ok("Your Setup Is Almost Finished...", 'The application will now close.', '', 'On your next start please leave it sit for a minute to allow add-ons to update.')
    KillKodi()
 
 
def Crash():  #Exhaust resources to crash the interpreter *** Creates a crash log but good for a last resort.
        sys.setrecursionlimit(1<<30)
        f = lambda f:f(f)
        f(f)
 
def KillKodi():
    myplatform = platform()
    xbmc.log("Platform: " + str(myplatform))
    if myplatform == 'osx': # OSX
        xbmc.log('############   try osx force close  #################')
        try: os.system('killall -9 XBMC')
        except: pass
        try: os.system('killall -9 Kodi')
        except: pass
        try: os._exit(0)
        except: pass	
        try: sys.exit(2)
        except: pass
        Crash()
        dialog.ok("[COLOR=red][B]WARNING  !!![/COLOR][/B]", "If you\'re seeing this message it means the force close", "was unsuccessful. Please force close the MC [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu.",'')
    elif myplatform == 'linux': #Linux
        xbmc.log('############   try linux force close  #################')
        try: os.system('killall XBMC')
        except: pass
        try: os.system('killall Kodi')
        except: pass
        try: os.system('killall -9 xbmc.bin')
        except: pass
        try: os.system('killall -9 kodi.bin')
        except: pass
        try: os._exit(0)
        except: pass	
        try: sys.exit(2)
        except: pass
        Crash()
        dialog.ok("[COLOR=red][B]WARNING  !!![/COLOR][/B]", "If you\'re seeing this message it means the force close", "was unsuccessful. Please force close the MC [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu.",'')
    elif myplatform == 'android': # Android  
        xbmc.log('############   try android force close  #################')
        try: os.system('kill $(ps com.semperpax.spmc16)')
        except: pass
        try: os.system('kill $(ps org.xbmc.kodi)')
        except: pass
        try : os.system('Process.killProcess(android.os.Process.org.fire.guru());')
        except: pass
        try : os.system('Process.killProcess(android.os.Process.org.fire.guruv());')
        except : pass
        try : os.system('Process.killProcess(android.os.Process.com.semperpax.spmc16());')
        except: pass
        try : os.system('Process.killProcess(android.os.Process.org.fire());')
        except: pass
        try : os.system('Process.killProcess(android.os.Process.org.fire,guru());')
        except: pass
        try: os._exit(0)
        except: pass	
        try: sys.exit(2)
        except: pass
        Crash()
        dialog.ok("[COLOR=red][B]PLEASE READ BELOW !!!![/COLOR][/B]", "Your system has been detected as Android, you ", "[COLOR=yellow][B]MUST[/COLOR][/B] force close the MC. [COLOR=red][B]DO NOT PRESS OK[/COLOR][/B]","Pull the power plug on your AndroidTV box now for changes to take effect.")
    elif myplatform == 'windows': # Windows
        xbmc.log('############   try windows force close  #################')
        try:
            os.system('@ECHO off')
            os.system('tskill XBMC.exe')
        except: pass
        try:
            os.system('@ECHO off')
            os.system('tskill Kodi.exe')
        except: pass
        try:
            os.system('@ECHO off')
            os.system('TASKKILL /im Kodi.exe /f')
        except: pass
        try:
            os.system('@ECHO off')
            os.system('TASKKILL /im XBMC.exe /f')
        except: pass
        try: os._exit(0)
        except: pass	
        try: sys.exit(2)
        except: pass
        Crash()
        dialog.ok("[COLOR=red][B]WARNING  !!![/COLOR][/B]", "If you\'re seeing this message it means the force close", "was unsuccessful. Please force close the MC [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu.","Use task manager and NOT ALT F4")
    else: #ATV
        xbmc.log('############   try atv force close  #################')
        try: os.system('killall AppleTV')
        except: pass
        xbmc.log('############   try raspbmc force close  #################') #OSMC / Raspbmc
        try: os.system('sudo initctl stop kodi')
        except: pass
        try: os.system('sudo initctl stop xbmc')
        except: pass
        try: os._exit(0)
        except: pass	
        try: sys.exit(2)
        except: pass
        Crash()
        dialog.ok("[COLOR=red][B]WARNING  !!![/COLOR][/B]", "If you\'re seeing this message it means the force close", "was unsuccessful. Please force close the MC [COLOR=lime]DO NOT[/COLOR] exit via the menu.","Your platform could not be detected so just pull the power cable.")    

def TriggerMigration():
    f = open(Addons26, mode='w')
    f.write('Wiped')
    f.close()
    os.remove(Addons26)

def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param
        
                      
params=get_params()
url=None
name=None
mode=None
iconimage=None
fanart=None
description=None


try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        iconimage=urllib.unquote_plus(params["iconimage"])
except:
        pass
try:        
        mode=int(params["mode"])
except:
        pass
try:        
        fanart=urllib.unquote_plus(params["fanart"])
except:
        pass
try:        
        description=urllib.unquote_plus(params["description"])
except:
        pass
        
        
print str(AddonTitle)+': '+str(VERSION)
print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "IconImage: "+str(iconimage)


if mode==None or url==None or len(url)<1:
        xbmc.log('===========================================================================================')
        xbmc.log('-------------------------------'+AddonTitle+' Started-------------------------------------')
        xbmc.log('===========================================================================================')
        xbmc.log('-------Create your own Wizard with MK-IV\'s Build-A-Wizard Tool in the MK-IV Wizard--------')
        xbmc.log('                                    ===---------===')
        xbmc.log('     ----------------------   Get it at http://get.mkiv.ca   ---------------------')
        xbmc.log('===========================================================================================')
        Index()
        
elif mode==1:
    if os.path.exists(Updater):
        updater.UpdateCheck(AddonTitle, addon_id)
        pass
    else: pass
    Wizard(name,url,description)
        
xbmcplugin.endOfDirectory(int(sys.argv[1]))
