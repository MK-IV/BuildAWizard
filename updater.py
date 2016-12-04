import xbmc, xbmcgui
import shutil
import os
import re
import downloader
import extract



def OPEN_URL(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    return link
    
def UpdateCheck(AddonTitle, addon_id):
    try:
        dp = xbmcgui.DialogProgress()
        dp.create(AddonTitle,'Checking for updates...','', 'Please Wait')
        link = OPEN_URL('https://raw.githubusercontent.com/MK-IV/BuildAWizard/master/addon.xml').replace('\n','').replace('\r','')
        match = re.compile('BAWversion="(.+?)"').findall(link)
        for mk4version in match:
            xbmc.log(Title+' is checking for core updates...')
            xbmc.log(addon_id+' Latest version='+BAWversion+' Installed version='+ADDON.getAddonInfo("version")+'')
            if mk4version > ADDON.getAddonInfo('version'):
                xbmc.log(AddonTitle+' Update files found... Attempting update...')
                #try:
                ADDONS = xbmc.translatePath(os.path.join('special://home','addons',''))
                path = xbmc.translatePath(os.path.join('special://home/addons','packages'))
                dp = xbmcgui.DialogProgress()
                dp.create(AddonTitle,'Downloading '+Title+' update...','', 'Please Wait')
                lib=os.path.join(path, 'BuildAWizard-master.zip')
                try:
                    os.remove(lib)
                except:
                    pass
                downloader.download('https://github.com/MK-IV/BuildAWizard/archive/master.zip', lib, dp)
                dp.update(0,'Downloading '+Title+' update... [COLOR lime]Finished[/COLOR]', 'Installing...')
                extract.all(lib,ADDONS,dp)
                time.sleep(.5)
                try:
                    os.remove(lib)
                except:
                    pass
                addontmp = xbmc.translatePath(os.path.join(Addons+'BuildAWizard-master/','addon.xml'))
                defaulttmp = xbmc.translatePath(os.path.join(Addons+'BuildAWizard-master/','default.py'))
                local = xbmc.translatePath(os.path.join(Addons,addon_id))
                master = xbmc.translatePath(os.path.join(Addons,'BuildAWizard-master'))
                link = open(os.path.join(local, 'default.py')
                match = re.compile('addonname="(.+?)"wizardname="(.+?)"providername="(.+?)"zipurl="(.+?)"').findall(link)
                for addonname,wizardname,providername,zipurl in match:
                    a=open((addontemp).read()
                    b=a.replace('addonname',addonname).replace('wizardname',wizardname).replace('providername',providername)
                    f = open((os.path.join(root, file)), mode='w')
                    f.write(str(b))
                    f.close()
                    time.sleep(2)
                    a=open(defaulttemp).read()
                    b=a.replace('addonname',addon_id).replace('wizardname',name).replace('providername',proname).replace('zipurl',url)
                    f.write(str(b))
                    f.close()
                    pass
                shutil.rmtree(Local)
                os.rename(Master,Local)
                xbmc.executebuiltin("Container.Refresh")
                dp.close
                #except: pass
            else: pass
    except: pass
