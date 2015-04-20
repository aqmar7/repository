import xbmc, xbmcgui, xbmcplugin
import urllib2,urllib,cgi, re, urlresolver
import urlparse
import HTMLParser
import xbmcaddon
from operator import itemgetter
import traceback,cookielib
import base64,os
try:
    import json
except:
    import simplejson as json
    
__addon__       = xbmcaddon.Addon()
__addonname__   = __addon__.getAddonInfo('name')
__icon__        = __addon__.getAddonInfo('icon')
addon_id = 'plugin.video.ZemTV-shani'
selfAddon = xbmcaddon.Addon(id=addon_id)
profile_path =  xbmc.translatePath(selfAddon.getAddonInfo('profile'))
  
willowCommonUrl=''# this is where the common url will stay
#willowCommonUrl=''

WTVCOOKIEFILE='WTVCookieFile.lwp'
WTVCOOKIEFILE=os.path.join(profile_path, WTVCOOKIEFILE)

 
mainurl='http://www.zemtv.com/'
liveURL='http://www.zemtv.com/live-pakistani-news-channels/'

tabURL ='http://www.eboundservices.com:8888/users/rex/m_live.php?app=%s&stream=%s'

def ShowSettings(Fromurl):
	selfAddon.openSettings()
	
def addLink(name,url,iconimage):
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
	liz.setInfo( type="Video", infoLabels={ "Title": name } )
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
	return ok


def addDir(name,url,mode,iconimage,showContext=False,showLiveContext=False,isItFolder=True, linkType=None):
#	print name
	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
	liz.setInfo( type="Video", infoLabels={ "Title": name } )

	if showContext==True:
		cmd1 = "XBMC.RunPlugin(%s&linkType=%s)" % (u, "DM")
		cmd2 = "XBMC.RunPlugin(%s&linkType=%s)" % (u, "LINK")
		cmd3 = "XBMC.RunPlugin(%s&linkType=%s)" % (u, "Youtube")
		cmd4 = "XBMC.RunPlugin(%s&linkType=%s)" % (u, "PLAYWIRE")
		cmd5 = "XBMC.RunPlugin(%s&linkType=%s)" % (u, "EBOUND")
		cmd6 = "XBMC.RunPlugin(%s&linkType=%s)" % (u, "PLAYWIRE")
		
		liz.addContextMenuItems([('Show All Sources',cmd6),('Play Ebound video',cmd5),('Play Playwire video',cmd4),('Play Youtube video',cmd3),('Play DailyMotion video',cmd1),('Play Tune.pk video',cmd2)])
	if linkType:
		u="XBMC.RunPlugin(%s&linkType=%s)" % (u, linkType)
		
#	if showLiself.wfileveContext==True:
#		cmd1 = "XBMC.RunPlugin(%s&linkType=%s)" % (u, "RTMP")
#		cmd2 = "XBMC.RunPlugin(%s&linkType=%s)" % (u, "HTTP")
#		liz.addContextMenuItems([('Play RTMP Steam (flash)',cmd1),('Play Http Stream (ios)',cmd2)])
	
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=isItFolder)
	return ok
	
def PlayChannel ( channelName ): 
#	print linkType
	url = tabURL.replace('%s',channelName);
	req = urllib2.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
	response = urllib2.urlopen(req)
	link=response.read()
	response.close()
#	print link
	
	match=re.compile('\"(http.*?playlist.m3u.*?)\"').findall(link)
#	print match

	strval = match[0]
#	print strval
	req = urllib2.Request(strval)
	req.add_header('User-Agent', 'Mozilla/5.0(iPad; U; CPU iPhone OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B314 Safari/531.21.10')
	req.add_header('Referer', 'http://www.eboundservices.com:8888/users/rex/m_live.php')
	response = urllib2.urlopen(req)
	link=response.read()
	response.close()
#	print link
	match=re.compile('\"(http.*?hashAESkey=.*?)\"').findall(link)
#	print match
	strval = match[0]

	listitem = xbmcgui.ListItem(channelName)
	listitem.setInfo('video', {'Title': channelName, 'Genre': 'Live TV'})
	playlist = xbmc.PlayList( xbmc.PLAYLIST_VIDEO )
	playlist.clear()
	playlist.add (strval)

	xbmc.Player().play(playlist)
	return

def getUrl(url, cookieJar=None,post=None, timeout=20, headers=None):

    cookie_handler = urllib2.HTTPCookieProcessor(cookieJar)
    opener = urllib2.build_opener(cookie_handler, urllib2.HTTPBasicAuthHandler(), urllib2.HTTPHandler())
    #opener = urllib2.install_opener(opener)
    req = urllib2.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.154 Safari/537.36')
    if headers:
        for h,hv in headers:
            req.add_header(h,hv)

    response = opener.open(req,post,timeout=timeout)
    link=response.read()
    response.close()
    return link;

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


def DisplayChannelNames(url):
	req = urllib2.Request(mainurl)
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
	response = urllib2.urlopen(req)
	link=response.read()
	response.close()
#	print link
#	 match=re.compile('<param name="URL" value="(.+?)">').findall(link)
#	match=re.compile('<a href="(.+?)"').findall(link)
#	match=re.compile('onclick="playChannel\(\'(.*?)\'\);">(.*?)</a>').findall(link)
#	match =re.findall('onclick="playChannel\(\'(.*?)\'\);">(.*?)</a>', link, re.DOTALL|re.IGNORECASE)


	match =re.findall('onclick="playChannel\(\'(.*?)\'\);".?>(.*?)</a>', link, re.DOTALL|re.IGNORECASE)
#	print match
#	print 'val is'
	match=sorted(match,key=itemgetter(1)   )
	for cname in match:
		if cname[0]<>'':
			addDir(cname[1] ,cname[0] ,1,'',isItFolder=False)
	return


def Addtypes():
	addDir('Shows' ,'Shows' ,2,'')
	addDir('Pakistani Live Channels' ,'PakLive' ,2,'')
	addDir('Indian Live Channels' ,'IndianLive' ,2,'')
	addDir('Sports' ,'Live' ,13,'')
	addDir('Settings' ,'Live' ,6,'',isItFolder=False)
	return

def PlayFlashTv(url):
#    patt='(.*?)'
#    print link
#    match_url =re.findall(patt,link)[0]
    referer=[('Referer','http://sports4u.tv/embed/Sky-sports-1.php')]
    res=getUrl(url,headers=referer)
    stream_pat='streamer\',[\'"](.*?)[\'"]'
    playpath_pat='\'file\',\'(.*?)\''
    
    swf_url="http://flashtv.co/ePlayerr.swf"
    pageUrl="http://flashtv.co/embedo.php?live=skky1&vw=650&vh=480" 
    rtmp_url=re.findall(stream_pat,res)[0]
    play_path=re.findall(playpath_pat,res)[0]

    
    video_url= '%s playpath=%s pageUrl=%s swfUrl=%s token=%s timeout=20'%(rtmp_url,play_path,pageUrl,swf_url,'%ZZri(nKa@#Z')
    
    playlist = xbmc.PlayList(1)
    playlist.clear()
    listitem = xbmcgui.ListItem( label = str(name), iconImage = "DefaultVideo.png", thumbnailImage = xbmc.getInfoImage( "ListItem.Thumb" ) )
    playlist.add(video_url,listitem)
    xbmcPlayer = xbmc.Player(xbmc.PLAYER_CORE_AUTO)
    xbmcPlayer.play(playlist) 
    
    
def AddP3gSports(url):

    addDir('Ptv Sports P3G.Tv (requires new rtmp)' ,'http://www.p3g.tv/embedplayer/ptvsports/2/600/400/' ,17,'', False, True,isItFolder=False)
    addDir('Star Sports P3G.Tv (requires new rtmp)' ,'http://www.p3g.tv/embedplayer/starsportse/2/600/400' ,17,'', False, True,isItFolder=False)
    addDir('GeoSuper P3G.Tv (requires new rtmp)' ,'http://www.p3g.tv/embedplayer/geosuper121/2/640/440' ,17,'', False, True,isItFolder=False)
    addDir('Ten Cricket P3G.Tv (requires new rtmp)' ,'http://www.p3g.tv/embedplayer/tencricketzh/2/640/440' ,17,'', False, True,isItFolder=False)
    addDir('Ten sports P3G.Tv (requires new rtmp)' ,'http://www.p3g.tv/embedplayer/tenpkya/2/640/440' ,17,'', False, True,isItFolder=False)
    addDir('Ten action P3G.Tv (requires new rtmp)' ,'http://www.p3g.tv/embedplayer/tenactionse/2/640/440' ,17,'', False, True,isItFolder=False)
    
def AddFlashtv(url):
    addDir('Sky Sports 1' ,'http://flashtv.co/embedo.php?live=skky1&vw=650&vh=480' ,32,'', False, True,isItFolder=False)
    addDir('Sky Sports 2' ,'http://flashtv.co/embedo.php?live=skky2&vw=650&vh=480' ,32,'', False, True,isItFolder=False)
    addDir('Sky Sports 3' ,'http://flashtv.co/embedo.php?live=skky3&vw=650&vh=480' ,32,'', False, True,isItFolder=False)
    addDir('Sky Sports 4' ,'http://flashtv.co/embedo.php?live=skky4&vw=650&vh=480' ,32,'', False, True,isItFolder=False)
    addDir('Sky Sports 5' ,'http://flashtv.co/embedo.php?live=skky5&vw=650&vh=480' ,32,'', False, True,isItFolder=False)
#    addDir('Sky Sports 1' ,'http://www.p3g.tv/embedplayer/tenactionse/2/640/440' ,32,'', False, True,isItFolder=False)
    
    
def AddSports(url):
    match=[]
    match.append((base64.b64decode('U2t5IFNwb3J0IDE='),'manual',base64.b64decode('aHR0cDovL2pweG1sLmphZG9vdHYuY29tL3Z1eG1sLnBocC9qYWRvb3htbC9wbGF5LzMxNg=='),''))
    match.append((base64.b64decode('U2t5IFNwb3J0IDI='),'manual',base64.b64decode('aHR0cDovL2pweG1sLmphZG9vdHYuY29tL3Z1eG1sLnBocC9qYWRvb3htbC9wbGF5LzMyNg=='),''))
    match.append((base64.b64decode('U2t5IFNwb3J0IDQ='),'manual',base64.b64decode('aHR0cDovL2pweG1sLmphZG9vdHYuY29tL3Z1eG1sLnBocC9qYWRvb3htbC9wbGF5LzMxNQ=='),''))
    for m in match:
        cname=m[0]
        curl=m[2]
        imgurl=''
        addDir(Colored(cname.capitalize(),'ZM') ,base64.b64encode(curl) ,11,imgurl, False, True,isItFolder=False)		#name,url,mode,icon
    
    addDir('SmartCric.com (Live matches only)' ,'Live' ,14,'')
    addDir('CricHD.tv (Live Channels)' ,'pope' ,26,'')
#    addDir('Flashtv.co (Live Channels)' ,'flashtv' ,31,'')
    addDir('WatchCric.com (requires new rtmp)-Live matches only' ,'http://www.watchcric.net/' ,16,'') #blocking as the rtmp requires to be updated to send gaolVanusPobeleVoKosat
    addDir('P3G.Tv (requires new rtmp)' ,'P3G'  ,30,'')
    addDir('Willow.Tv (login required)' ,'http://www.willow.tv/' ,19,'')


def PlayPopeLive(url):
    playlist = xbmc.PlayList(1)
    url='rtmp://rtmp.popeoftheplayers.pw:1935/redirect playpath='+url+' swfVfy=true swfUrl=http://popeoftheplayers.pw/atdedead.swf flashVer=WIN\2016,0,0,235 pageUrl=http://popeoftheplayers.pw/atdedead.swf live=true timeout=20 token=#atd%#$ZH'

    playlist.clear()
    listitem = xbmcgui.ListItem( label = str(name), iconImage = "DefaultVideo.png", thumbnailImage = xbmc.getInfoImage( "ListItem.Thumb" ) )
    playlist.add(url,listitem)
    xbmcPlayer = xbmc.Player(xbmc.PLAYER_CORE_AUTO)
    xbmcPlayer.play(playlist) 

def AddPopeLive(url):
    try:
#        req = urllib2.Request(url)
#        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36')
#        response = urllib2.urlopen(req)
#        videoPage =  response.read()
#        response.close()
#        pat='<a href="http://.*?/.*?/(.*?)-Live.*?/(.+?)" '
#        channels=re.findall(pat,videoPage)
#        print channels
        channels=[('Sky Sports 1','47'),('Sky Sports 2','19'),('Sky Sports 3','10'),('Sky Sports 4','16'),('Sky Sports 5','23'),('Sky Sports F1','22') ,('BT Sport 1','13'),('BT Sports 2','15') ,('Willow Cricket','38') ,('Ptv Sports','33')   ]
        for channel in channels:
            print channel
            cname=channel[0]
            cid=channel[1]

#            addDir(cname ,'a',27,'', False, True,isItFolder=False)
            print 'adding'
            addDir(cname ,cid,27,'', False, True,isItFolder=False)
    except: traceback.print_exc(file=sys.stdout)
    
def AddWillSportsOldSeries(url):
    try:
        url_host='http://willowfeeds.willow.tv/willowMatchArchive.json'
        req = urllib2.Request(url_host)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36')
        response = urllib2.urlopen(req)
        if response.info().get('Content-Encoding') == 'gzip':
            from StringIO import StringIO
            import gzip
            buf = StringIO( response.read())
            f = gzip.GzipFile(fileobj=buf)
            res = f.read()
        else:
            res=response.read()

        print repr(res[:100])
        res=res.split('Handle_WLSeriesDetailsObj(')[1][:-2]
        serieses = json.loads(res)
  
        response.close()

        
        for series in serieses:
            sname=series["Name"]
            sid=series["Id"]
            addDir(sname ,sid,24,'')		#name,url,mode,icon
    except: traceback.print_exc(file=sys.stdout)


def AddWillSportsOldSeriesMatches(url):
    addDir(Colored(name,'EB',True) ,'' ,-1,'', False, True,isItFolder=False)		#name,url,mode,icon
    try:
        url_host='http://willowfeeds.willow.tv/willowMatchArchive.json'
        req = urllib2.Request(url_host)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36')
        response = urllib2.urlopen(req)
        if response.info().get('Content-Encoding') == 'gzip':
            from StringIO import StringIO
            import gzip
            buf = StringIO( response.read())
            f = gzip.GzipFile(fileobj=buf)
            res = f.read()
        else:
            res=response.read()

        print repr(res[:100])
        res=res.split('Handle_WLSeriesDetailsObj(')[1][:-2]
        serieses = json.loads(res)
  
        response.close()

        
        for series in serieses:
            sname=series["Name"]
            sid=series["Id"]
            if url==sid:
                for match in series["MatchDetails"]:
                    mname=match["Name"]
                    matchid=match["Id"]
                    sdate=match["StartDate"]
                    addDir(sdate+' - '+mname ,matchid,23,'')		#name,url,mode,icon
    except: traceback.print_exc(file=sys.stdout)

def useMyOwnUserNamePwd():
    willow_username=selfAddon.getSetting( "WillowUserName" ) 
    return not willow_username==""
    
def getWTVCookieJar(updatedUName=False):
    cookieJar=None
    try:
        cookieJar = cookielib.LWPCookieJar()
        if not updatedUName:
            cookieJar.load(WTVCOOKIEFILE,ignore_discard=True)
    except: 
        cookieJar=None

    if not cookieJar:
        cookieJar = cookielib.LWPCookieJar()
    return cookieJar

def performWillowLogin():
    try:

        url='http://www.willow.tv/EventMgmt/Default.asp'
        willow_username=selfAddon.getSetting( "WillowUserName" ) 
        willow_pwd=selfAddon.getSetting( "WillowPassword" ) 
        willow_lasstusername=selfAddon.getSetting( "lastSuccessLogin" ) 
        cookieJar=getWTVCookieJar(willow_username!=willow_lasstusername)
        mainpage = getUrl(url,cookieJar=cookieJar)


        if 'Login/Register' in mainpage:
            url='https://www.willow.tv/EventMgmt/UserMgmt/Login.asp'
            post = {'Email':willow_username,'Password':willow_pwd,'LoginFormSubmit':'true'}
            post = urllib.urlencode(post)
            mainpage = getUrl(url,cookieJar=cookieJar,post=post)
            cookieJar.save (WTVCOOKIEFILE,ignore_discard=True)
            selfAddon.setSetting( id="lastSuccessLogin" ,value=willow_username)
        
        return not 'Login/Register' in mainpage,cookieJar
    except: 
            traceback.print_exc(file=sys.stdout)
    return False,None
    
def getMatchUrl(matchid):
    if not useMyOwnUserNamePwd():
        url_host=willowCommonUrl
        if len(url_host)>0:
            if mode==21:#live
                if ':' in matchid:
                    matchid,partNumber=matchid.split(':')
                    post = {'matchNumber':matchid,'type':'live','partNumber':partNumber,'debug':'1'}
                else:
                    post = {'matchNumber':matchid,'type':'live','debug':'1'}
            else:
                if ':' in matchid:
                    matchid,partNumber=matchid.split(':')
                    post = {'matchNumber':matchid,'type':'replay','partNumber':partNumber,'debug':'1'}
                else:
                    post = {'matchNumber':matchid,'type':'replay','debug':'1'}
            post = urllib.urlencode(post)
            req = urllib2.Request(url_host)
            req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36')
            response = urllib2.urlopen(req,post)
            link=response.read()
            response.close()
            final_url= urllib2.unquote(link)  
            final_url=final_url.split('debug')[0]
            return final_url
        else:
            Msg="Common server is not available, Please enter your own login details."
            dialog = xbmcgui.Dialog()
            ok = dialog.ok('Login Failed', Msg)
            return ''

    else:
        loginworked,cookieJar= performWillowLogin();
        if loginworked:
            WLlive=False
            source_sectionid=''
            returnParts=False
            userid=''
            for i in cookieJar:

                s=repr(i)
                if 'CXMUserId' in s:
                    #print 'ssssssssssssss',s
                    userid=s.split('value=\'')[1].split('%')[0]
            print 'userid',userid
            calltype='Live'
            if mode==21:
                WLlive=True
                matchid,source_sectionid=matchid.split(':')
                st='LiveMatch'
                url='http://www.willow.tv/EventMgmt/%sURL.asp?mid=%s'%(st,matchid)
                pat='secureurl":"(.*?)".*?priority":%s,'%source_sectionid    
                calltype='Live'                
            else:
                if ':' in matchid:
                    matchid,source_sectionid=matchid.split(':')
                    st='Replay'
                    url='https://www.willow.tv/EventMgmt/ReplayURL.asp?mid=%s&userId=%s'%(matchid,userid)
                    pat='secureurl":"(.*?)".*?priority":%s,'%source_sectionid
                    calltype='RecordOne'     
                else:
                    returnParts=True
                    st='Replay'
                    url='https://www.willow.tv/EventMgmt/ReplayURL.asp?mid=%s&userId=%s'%(matchid,userid)
                    pat='"priority":(.+?),'
                    calltype='RecordAll' 
            
            videoPage = getUrl(url,cookieJar=cookieJar)    

            final_url=''
        
            if calltype=='Live' or calltype=='RecordOne':
                videoPage='},\n{'.join(videoPage.split("},{"))
                final_url=re.findall(pat,videoPage)[0]
            else:
                final_url=re.findall(pat,videoPage)
                final_url2=''
                for u in final_url:
                    final_url2+='Part Number:'+u+'='+u+','
                final_url=final_url2[:-1]
            final_url= urllib2.unquote(final_url)  
            final_url=final_url.split('debug')[0]
            return final_url
            

        else:
            Msg="Login failed, please make sure the login details are correct."
            dialog = xbmcgui.Dialog()
            ok = dialog.ok('Login Failed', Msg)
        
    
    
    
def PlayWillowMatch(url):
#    patt='(.*?)'
#    print link
#    match_url =re.findall(patt,link)[0]
    match_url=getMatchUrl(url)
    match_url=match_url+'|User-Agent=Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36'
    playlist = xbmc.PlayList(1)
    playlist.clear()
    listitem = xbmcgui.ListItem( label = str(name), iconImage = "DefaultVideo.png", thumbnailImage = xbmc.getInfoImage( "ListItem.Thumb" ) )
    playlist.add(match_url,listitem)
    xbmcPlayer = xbmc.Player(xbmc.PLAYER_CORE_AUTO)
    xbmcPlayer.play(playlist) 

def AddWillowReplayParts(url):
    try:
        link=getMatchUrl(url)
        sections=link.split(',')
        addDir(Colored(name,'EB',True) ,'' ,-1,'', False, True,isItFolder=False)		#name,url,mode,icon
        for section in sections:
            sname,section_number=section.split('=')
            addDir(sname ,url+':'+section_number,22,'', False, True,isItFolder=False)		#name,url,mode,icon
    except: traceback.print_exc(file=sys.stdout)

def AddWillowCric(url):
    try:
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        patt='json_matchbox = (.*?);'
        match_url =re.findall(patt,link)[0]
        print match_url
        matches=json.loads(match_url)
        print matches
        matchid=matches["result"]["past"][0]["MatchId"]
        addDir(Colored('Live Channel (Experimental)','EB',True) ,'' ,-1,'', False, True,isItFolder=False)		#name,url,mode,icon

        addDir('  Source 1' ,'%s:1'%str(matchid),21,'', False, True,isItFolder=False)		#name,url,mode,icon
        addDir('  Source 2' ,'%s:2'%str(matchid),21,'', False, True,isItFolder=False)		#name,url,mode,icon
        addDir('  Source 3' ,'%s:3'%str(matchid),21,'', False, True,isItFolder=False)		#name,url,mode,icon
        addDir('  Source 4' ,'%s:4'%str(matchid),21,'', False, True,isItFolder=False)		#name,url,mode,icon

        addDir(Colored('Live Games','EB',True) ,'' ,-1,'', False, True,isItFolder=False)		#name,url,mode,icon
        if matches["result"]["live"]:
            live_games=matches["result"]["live"]
            for game in live_games:
                match_name=game["MatchName"]
                match_id=game["MatchId"]
                MatchStartDate=game["MatchStartDate"]
                entry_name=MatchStartDate+' - '+match_name
                #if useMyOwnUserNamePwd():
                #    addDir(entry_name ,match_id,-1,'', False, True,isItFolder=False)		#name,url,mode,icon
                #else:
                for i in range(4):
                    addDir(entry_name+(' source %s'%str(i)) ,match_id+':'+str(i),21,'', False, True,isItFolder=False)		#name,url,mode,icon
#                else:
#                    addDir(entry_name ,match_id,21,'', False, True,isItFolder=False)		#name,url,mode,icon           
        else:
            addDir('  No Games at the moment' ,'' ,-1,'', False, True,isItFolder=False)		#name,url,mode,icon

            
            
        addDir(Colored('Recent Games','EB',True) ,'' ,-1,'', False, True,isItFolder=False)		#name,url,mode,icon
        past_games=matches["result"]["past"]
        for game in past_games:
            match_name=game["MatchName"]
            match_id=game["MatchId"]
            print 'match_id',match_id
            MatchStartDate=game["MatchStartDate"]
            entry_name=MatchStartDate+' - '+match_name
#            addDir(entry_name ,match_id,23,'', False, True,isItFolder=True)		#name,url,mode,icon
            addDir(entry_name ,match_id,23,'')            
    except: traceback.print_exc(file=sys.stdout)
         
    addDir(Colored('All Recorded Series','ZM',True) ,'http://www.willow.tv/EventMgmt/results.asp' ,20,'') #blocking as the rtmp requires to be updated to send gaolVanusPobeleVoKosat
    

    
def AddWatchCric(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    patt='<h1>(.*?)\s*</h1>(.*?)</div>'
    match_url =re.findall(patt,link,re.DOTALL)
    
    patt_sn='sn = "(.*?)"'
    for nm,div in match_url:
            curl=''
            cname=nm.split('<')[0]
            pat_options='<li><a href="(.*?)">(.*?)<'
            match_options =re.findall(pat_options,div)
            addDir(cname ,curl ,-1,'', False, True,isItFolder=False)		#name,url,mode,icon
            if match_options and len(match_options)>0:
                for u,n in match_options:
                    if not u.startswith('htt'):u=url+u
                    curl=u                
                    addDir('    -'+n ,curl ,17,'', False, True,isItFolder=False)		#name,url,mode,icon
            else:
                cname='No streams available'
                curl=''
                addDir('    -'+cname ,curl ,-1,'', False, True,isItFolder=False)		#name,url,mode,icon
                



def AddSmartCric(url):
    req = urllib2.Request('http://www.smartcric.com/')
    req.add_header('User-Agent', 'Mozilla/5.0(iPad; U; CPU iPhone OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B314 Safari/531.21.10')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    patt='performGet\(\'(.+)\''
    match_url =re.findall(patt,link)[0]
    channeladded=False
    patt_sn='sn = "(.*?)"'
    try:
        match_sn =re.findall(patt_sn,link)[0]
        final_url=  match_url+   match_sn
        req = urllib2.Request(final_url)
        req.add_header('User-Agent', 'Mozilla/5.0(iPad; U; CPU iPhone OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B314 Safari/531.21.10')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        sources = json.loads(link)



        addDir('Refresh' ,'Live' ,144,'')
        
        for source in sources["channelsList"]:
            if 1==1:#ctype=='liveWMV' or ctype=='manual':
                print source
                curl=''
                cname=source["caption"]
                fms=source["fmsUrl"]
                print curl
                #if ctype<>'': cname+= '[' + ctype+']'
                addDir(cname ,curl ,-1,'', False, True,isItFolder=False)		#name,url,mode,icon
                if 'streamsList' in source and source["streamsList"] and len(source["streamsList"])>0:
                    for s in source["streamsList"]:
                        cname=s["caption"]
                        curl=s["streamName"]
                        curl="http://"+fms+":1935/mobile/"+curl+"/playlist.m3u8?"+match_sn+"";
                        addDir('    -'+cname ,curl ,15,'', False, True,isItFolder=False)		#name,url,mode,icon
                        channeladded=True
                else:
                    cname='No streams available'
                    curl=''
                    addDir('    -'+cname ,curl ,-1,'', False, True,isItFolder=False)		#name,url,mode,icon
    except: traceback.print_exc(file=sys.stdout)
    if not channeladded:
        cname='No streams available'
        curl=''
        addDir('    -'+cname ,curl ,-1,'', False, True,isItFolder=False)		#name,url,mode,icon 
    addDir('Refresh' ,'Live' ,144,'')
            

    return

def PlayWatchCric(url):
    pat_ifram='<iframe.*?src=(.*?).?"?>'    
    if 'p3g.tv' not in url:
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0(iPad; U; CPU iPhone OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B314 Safari/531.21.10')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match_url =re.findall(pat_ifram,link)[0]
    else:
        match_url=url
        url='http://embed247.com/live.php?ch=Ptv_Sports1&vw=600&vh=400&domain=www.samistream.com'
    req = urllib2.Request(match_url)
    req.add_header('User-Agent', 'Mozilla/5.0(iPad; U; CPU iPhone OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B314 Safari/531.21.10')
    req.add_header('Referer', url)
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    print 'match_url',match_url
        

    ccommand='%s;TRUE;TRUE;'
    swfUrl='http://www.mipsplayer.com/content/scripts/fplayer.swf'
    sitename='www.mipsplayer.com'
    pat_e=' e=\'(.*?)\';'
    app='live'
    
    if 'liveflashplayer.net/resources' in link:
        c='kaskatijaEkonomista'
        swfUrl='http://www.liveflashplayer.net/resources/scripts/fplayer.swf'
        sitename='www.liveflashplayer.net'
        pat_e=' g=\'(.*?)\';'
        app='stream'
        pat_js='channel=\'(.*?)\''

    elif 'www.mipsplayer.com' in link:
        c='gaolVanusPobeleVoKosata'
        ccommand='%s;TRUE;TRUE;'
        swfUrl='http://www.mipsplayer.com/content/scripts/fplayer.swf'
        sitename='www.mipsplayer.com'
        pat_e=' e=\'(.*?)\';'
        app='live'
        pat_js='channel=\'(.*?)\''

    elif 'p3g.tv' in link:
        c='zenataStoGoPuknalaGavolot'
        ccommand='%s;TRUE;TRUE;'
        swfUrl='http://www.p3g.tv/resources/scripts/eplayer.swf'
        sitename='www.p3g.tv'
        pat_e='&g=\'?(.*?)\'?&;?'
        app='stream'
        pat_js='&s=(.*?)&'
        
        
    match_urljs =re.findall(pat_js,link)[0]
    width='480'
    height='380'

    print link
    match_e =re.findall(pat_e,link)[0]
    
    match_urljs=('http://%s/embedplayer/'%sitename)+match_urljs+'/'+match_e+'/'+width+'/'+height
    
    req = urllib2.Request(match_urljs)
    req.add_header('User-Agent', 'Mozilla/5.0(iPad; U; CPU iPhone OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B314 Safari/531.21.10')
    req.add_header('Referer', match_url)
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    
    pat_flash='FlashVars\',.?\'(.*?)\''
    match_flash =re.findall(pat_flash,link)[0]
    matchid=match_flash.split('id=')[1].split('&')[0]
    
    lb_url='http://%s:1935/loadbalancer?%s'%(sitename,matchid)
        
    req = urllib2.Request(lb_url)
    req.add_header('User-Agent', 'Mozilla/5.0(iPad; U; CPU iPhone OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B314 Safari/531.21.10')
    req.add_header('Referer', match_urljs)
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    ip=link.split('=')[1]
    

    sid=match_flash.split('s=')[1].split('&')[0]

    ccommand=ccommand%c
    url='rtmp://%s/%s playpath=%s?id=%s pageUrl=%s swfUrl=%s Conn=S:OK ccommand=%s timeout=20'%(ip,app,sid,matchid,match_urljs,swfUrl,ccommand)
    print url
    playlist = xbmc.PlayList(1)
    playlist.clear()
    listitem = xbmcgui.ListItem( label = str(name), iconImage = "DefaultVideo.png", thumbnailImage = xbmc.getInfoImage( "ListItem.Thumb" ) )
    playlist.add(url,listitem)
    xbmcPlayer = xbmc.Player(xbmc.PLAYER_CORE_AUTO)
    xbmcPlayer.play(playlist) 
    
def PlaySmartCric(url):
    playlist = xbmc.PlayList(1)
    playlist.clear()
    listitem = xbmcgui.ListItem( label = str(name), iconImage = "DefaultVideo.png", thumbnailImage = xbmc.getInfoImage( "ListItem.Thumb" ) )
    playlist.add(url,listitem)
    xbmcPlayer = xbmc.Player(xbmc.PLAYER_CORE_AUTO)
    xbmcPlayer.play(playlist) 
        
def AddEnteries(type):
#	print "addenT"
    if type=='Shows':
        AddShows(mainurl)
    elif type=='Next Page':
        AddShows(url)
    else:
        #addDir(Colored('ZemTv Channels','ZM',True) ,'ZEMTV' ,10,'', False, True,isItFolder=False)		#name,url,mode,icon
        #AddChannels();#AddChannels()
        isPakistani=(type=='Pakistani Live Channels')
        print 'isPakistani',isPakistani
        if isPakistani:        
            addDir(Colored('EboundServices Channels','EB',True) ,'ZEMTV' ,10,'', False, True,isItFolder=False)		#name,url,mode,icon
            try:
                AddChannelsFromEbound();#AddChannels()
            except: pass
        addDir(Colored('Other sources','ZM',True) ,'ZEMTV' ,10,'', False, True,isItFolder=False)
        try:
            AddChannelsFromOthers(isPakistani)
        except:
            print 'somethingwrong'
            traceback.print_exc(file=sys.stdout)
    return

def AddChannelsFromOthers(isPakistani):
    main_ch='(<section_name>Pakistani<\/section_name>.*?<\/section>)'

    if not isPakistani:
        main_ch='(<section_name>Hindi<\/section_name>.*?<\/section>)'

    patt='<item><name>(.*?)<.*?<link>(.*?)<.*?albumart>(.*?)<'
    match=[]    
    if 1==2:#stop this as its not working
        url=base64.b64decode("aHR0cDovL2pweG1sLmphZG9vdHYuY29tL3Z1eG1sLnBocC9qYWRvb3htbC9pdGVtcy8xMzE0LyVkLw==")

        pageIndex=0
        try:
            while True:
                newUrl=url%pageIndex
                pageIndex+=24
                req = urllib2.Request(newUrl)
                req.add_header('User-Agent', 'Mozilla/5.0(iPad; U; CPU iPhone OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B314 Safari/531.21.10')
                response = urllib2.urlopen(req)
                link=response.read()
                response.close()
                totalcountPattern='<totalitems>(.*?)<'
                totalcount =int(re.findall(totalcountPattern,link)[0])
                
                #match =re.findall(main_ch,link)[0]
                matchtemp =re.findall(patt,link)
                for cname,curl,imgurl in matchtemp:
                    match.append((cname,'plus',curl,imgurl))
                #match+=matchtemp
                if pageIndex>totalcount:
                    break
        except: pass
    try:
        patt='<channel><channel_number>.*?<channel_name>(.+?[^<])</channel_name><channel_type>(.+?)</channel_type>.*?[^<"]<channel_url>(.+?[^<])</channel_url>.*?</channel>'
        url=base64.b64decode("aHR0cDovL2ZlcnJhcmlsYi5qZW10di5jb20vaW5kZXgucGhwLzJfNC9neG1sL2NoYW5uZWxfbGlzdA==")
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0(iPad; U; CPU iPhone OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B314 Safari/531.21.10')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        
        match_temp =re.findall(main_ch,link)[0]
        match_temp=re.findall(patt,match_temp)
        for cname,ctype,curl in match_temp:
            match.append((cname,ctype,curl,''))

        match +=re.findall(patt,match_temp)
    except: pass
        
    if isPakistani:
        match.append(('Ary digital','manual','cid:475',''))
        match.append(('Ary digital','manual','cid:981',''))
        match.append(('Ary digital Europe','manual','cid:587',''))
        match.append(('Ary digital World','manual','cid:589',''))
        match.append(('Ary News','manual','cid:474',''))
        match.append(('Ary News World','manual','cid:591',''))
        match.append(('Express News','manual','cid:275',''))
        match.append(('Express News','manual','cid:788',''))
        match.append(('Express Entertainment','manual','cid:260',''))
        match.append(('Express Entertainment','manual','cid:793',''))

        match.append(('ETV Urdu','manual','etv',''))
        match.append(('Ary Zindagi','manual','http://live.aryzindagi.tv/','http://www.aryzindagi.tv/wp-content/uploads/2014/10/Final-logo-2.gif'))


        
        match.append((base64.b64decode('U2t5IFNwb3J0IDE='),'manual',base64.b64decode('aHR0cDovL2pweG1sLmphZG9vdHYuY29tL3Z1eG1sLnBocC9qYWRvb3htbC9wbGF5LzMxNg=='),''))
        match.append((base64.b64decode('U2t5IFNwb3J0IDI='),'manual',base64.b64decode('aHR0cDovL2pweG1sLmphZG9vdHYuY29tL3Z1eG1sLnBocC9qYWRvb3htbC9wbGF5LzMyNg=='),''))
        match.append((base64.b64decode('U2t5IFNwb3J0IDQ='),'manual',base64.b64decode('aHR0cDovL2pweG1sLmphZG9vdHYuY29tL3Z1eG1sLnBocC9qYWRvb3htbC9wbGF5LzMxNQ=='),''))

        ##other v2
    if 1==2:    
        match.append((base64.b64decode('U2tpIFNwb3J0IDEgVjI='),'manual',base64.b64decode('cnRtcGU6Ly80Ni4yNDYuMjkuMTYyOjE5MzUvbGl2ZS8gcGxheXBhdGg9U3BvcnRoZHNreTEgcGFnZVVybD1odHRwOi8vd3d3LmhkY2FzdC5vcmcvIHRva2VuPSN5dyV0dCN3QGtrdQ=='),''))
        match.append((base64.b64decode('U2tpIFNwb3J0IDIgVjI='),'manual',base64.b64decode('cnRtcGU6Ly80Ni4yNDYuMjkuMTYyOjE5MzUvbGl2ZS8gcGxheXBhdGg9U3BvcnRoZHNreTIgcGFnZVVybD1odHRwOi8vd3d3LmhkY2FzdC5vcmcvIHRva2VuPSN5dyV0dCN3QGtrdQ=='),''))
        match.append((base64.b64decode('U2tpIFNwb3J0IDMgVjI='),'manual',base64.b64decode('cnRtcGU6Ly80Ni4yNDYuMjkuMTYyOjE5MzUvbGl2ZS8gcGxheXBhdGg9U3BvcnRoZHNreTMgcGFnZVVybD1odHRwOi8vd3d3LmhkY2FzdC5vcmcvIHRva2VuPSN5dyV0dCN3QGtrdQ=='),''))
        match.append((base64.b64decode('U2tpIFNwb3J0IDQgVjI='),'manual',base64.b64decode('cnRtcGU6Ly80Ni4yNDYuMjkuMTYyOjE5MzUvbGl2ZS8gcGxheXBhdGg9U3BvcnRoZHNreTQgcGFnZVVybD1odHRwOi8vd3d3LmhkY2FzdC5vcmcvIHRva2VuPSN5dyV0dCN3QGtrdQ=='),''))
        match.append((base64.b64decode('U2tpIFNwb3J0IDUgVjI='),'manual',base64.b64decode('cnRtcGU6Ly80Ni4yNDYuMjkuMTYyOjE5MzUvbGl2ZS8gcGxheXBhdGg9U3BvcnRoZHNreTUgcGFnZVVybD1odHRwOi8vd3d3LmhkY2FzdC5vcmcvIHRva2VuPSN5dyV0dCN3QGtrdQ=='),''))
        match.append((base64.b64decode('U2tpIFNwb3J0IEYxIFYy'),'manual',base64.b64decode('cnRtcGU6Ly80Ni4yNDYuMjkuMTYyOjE5MzUvbGl2ZS8gcGxheXBhdGg9U3BvcnRoZHNreWYxIHBhZ2VVcmw9aHR0cDovL3d3dy5oZGNhc3Qub3JnLyB0b2tlbj0jeXcldHQjd0Bra3U='),''))

#    print match




#    match=sorted(match,key=itemgetter(0)   )
    match=sorted(match,key=lambda s: s[0].lower()   )
    for cname,ctype,curl,imgurl in match:
        if 1==1:#ctype=='liveWMV' or ctype=='manual':
            print curl
            #if ctype<>'': cname+= '[' + ctype+']'
            addDir(Colored(cname.capitalize(),'ZM') ,base64.b64encode(curl) ,11,imgurl, False, True,isItFolder=False)		#name,url,mode,icon
    return
    
def re_me(data, re_patten):
    match = ''
    m = re.search(re_patten, data)
    if m != None:
        match = m.group(1)
    else:
        match = ''
    return match

def revist_dag(page_data):
    final_url = ''
    if '127.0.0.1' in page_data:
        final_url = re_me(page_data, '&ver_t=([^&]+)&') + ' live=true timeout=15 playpath=' + re_me(page_data, '\\?y=([a-zA-Z0-9-_\\.@]+)')
    if re_me(page_data, 'token=([^&]+)&') != '':
        final_url = final_url + '?token=' + re_me(page_data, 'token=([^&]+)&')
    elif re_me(page_data, 'wmsAuthSign%3D([^%&]+)') != '':
        final_url = re_me(page_data, '&ver_t=([^&]+)&') + '?wmsAuthSign=' + re_me(page_data, 'wmsAuthSign%3D([^%&]+)') + '==/mp4:' + re_me(page_data, '\\?y=([^&]+)&')
    else:
        final_url = re_me(page_data, 'HREF="([^"]+)"')

    if 'dag1.asx' in final_url:
        return get_dag_url(final_url)

    if 'devinlivefs.fplive.net' not in final_url:
        final_url = final_url.replace('devinlive', 'flive')
    if 'permlivefs.fplive.net' not in final_url:
        final_url = final_url.replace('permlive', 'flive')
    return final_url

def get_dag_url(page_data):
    print 'get_dag_url',page_data
    if '127.0.0.1' in page_data:
        return revist_dag(page_data)
    elif re_me(page_data, 'wmsAuthSign%3D([^%&]+)') != '':
        final_url = re_me(page_data, '&ver_t=([^&]+)&') + '?wmsAuthSign=' + re_me(page_data, 'wmsAuthSign%3D([^%&]+)') + '==/mp4:' + re_me(page_data, '\\?y=([^&]+)&')
    else:
        final_url = re_me(page_data, 'href="([^"]+)"[^"]+$')
        if len(final_url)==0:
            final_url=page_data
    final_url = final_url.replace(' ', '%20')
    return final_url
    
def PlayOtherUrl ( url ):
    url=base64.b64decode(url)
    if url.startswith('cid:'): url=base64.b64decode('aHR0cDovL2ZlcnJhcmlsYi5qZW10di5jb20vaW5kZXgucGhwLzJfNC9neG1sL3BsYXkvJXM=')%url.replace('cid:','')
    progress = xbmcgui.DialogProgress()
    progress.create('Progress', 'Fetching Streaming Info')
    progress.update( 10, "", "Finding links..", "" )

    direct=False
    if url=='http://live.aryzindagi.tv/':
        req = urllib2.Request(url)
        #req.add_header('User-Agent', 'Verismo-BlackUI_(2.4.7.5.8.0.34)')   
        #req.add_header('User-Agent', 'Mozilla/5.0(iPad; U; CPU iPhone OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B314 Safari/531.21.10')
        req.add_header('User-Agent', 'Verismo-BlackUI_(2.4.7.5.8.0.34)') 
        response = urllib2.urlopen(req)
        link=response.read()
        curlpatth='file: "(htt.*?)"'
        progress.update( 50, "", "Preparing url..", "" )
        dag_url =re.findall(curlpatth,link)[0]
    elif url=='etv':
        req = urllib2.Request('http://m.news18.com/live-tv/etv-urdu')
        #req.add_header('User-Agent', 'Verismo-BlackUI_(2.4.7.5.8.0.34)')   
        req.add_header('User-Agent', 'Mozilla/5.0(iPad; U; CPU iPhone OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B314 Safari/531.21.10')
        #req.add_header('User-Agent', 'Verismo-BlackUI_(2.4.7.5.8.0.34)') 
        response = urllib2.urlopen(req)
        link=response.read()
        curlpatth='<source src="(.*?)"'
        progress.update( 50, "", "Preparing url..", "" )
        dag_url =re.findall(curlpatth,link)[0]
    elif 'dag1.asx' not in url and 'hdcast.org' not in url:
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Verismo-BlackUI_(2.4.7.5.8.0.34)')   
        #req.add_header('User-Agent', 'Mozilla/5.0(iPad; U; CPU iPhone OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B314 Safari/531.21.10')
        response = urllib2.urlopen(req)
        link=response.read()
        curlpatth='<link>(.*?)<\/link>'
        progress.update( 50, "", "Preparing url..", "" )
        dag_url =re.findall(curlpatth,link)
        if '[CDATA' in dag_url:
            dag_url=dag_url.split('CDATA[')[1].split(']')[0]#
        if not (dag_url and len(dag_url)>0 ):
            curlpatth='\<ENTRY\>\<REF HREF="(.*?)"'
            dag_url =re.findall(curlpatth,link)[0]
        else:
            dag_url=dag_url[0]
    else:
        if 'hdcast.org' in url:
            direct=True
        dag_url=url
    if '[CDATA' in dag_url:
        dag_url=dag_url.split('CDATA[')[1].split(']')[0]#

    print 'dag_url',dag_url,name
    
    if 'Dunya news' in name and 'dag1.asx' not in dag_url:
        print 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
        dag_url='http://dag-chi.totalstream.net/dag1.asx?id=ad1!dunya'

    if 'dag1.asx' in dag_url:    
        req = urllib2.Request(dag_url)
        req.add_header('User-Agent', 'Verismo-BlackUI_(2.4.7.5.8.0.34)')   
        response = urllib2.urlopen(req)
        link=response.read()
        dat_pattern='href="([^"]+)"[^"]+$'
        dag_url =re.findall(dat_pattern,link)[0]
    print 'dag_url2',dag_url
    if direct:
        final_url=dag_url
    else:
        final_url=get_dag_url(dag_url)
    progress.update( 100, "", "Almost done..", "" )
    print final_url
    listitem = xbmcgui.ListItem( label = str(name), iconImage = "DefaultVideo.png", thumbnailImage = xbmc.getInfoImage( "ListItem.Thumb" ) )
    print "playing stream name: " + str(name) 
    xbmc.Player( xbmc.PLAYER_CORE_AUTO ).play( final_url, listitem)    

def AddChannelsFromEbound():
	liveURL='http://eboundservices.com/istream_demo.php'
	req = urllib2.Request(liveURL)
	req.add_header('User-Agent','Mozilla/5.0(iPad; U; CPU iPhone OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B314 Safari/531.21.10')
	response = urllib2.urlopen(req)
	link=response.read()
	response.close()
#	print link
#	match=re.compile('<param name="URL" value="(.+?)">').findall(link)
#	match=re.compile('<a href="(.+?)"').findall(link)
#	match=re.compile('onclick="playChannel\(\'(.*?)\'\);">(.*?)</a>').findall(link)
#	match =re.findall('onclick="playChannel\(\'(.*?)\'\);">(.*?)</a>', link, re.DOTALL|re.IGNORECASE)
#	match =re.findall('onclick="playChannel\(\'(.*?)\'\);".?>(.*?)</a>', link, re.DOTALL|re.IGNORECASE)
#	match =re.findall('<div class=\"post-title\"><a href=\"(.*?)\".*<b>(.*)<\/b><\/a>', link, re.IGNORECASE)
#	match =re.findall('<img src="(.*?)" alt=".*".+<\/a>\n*.+<div class="post-title"><a href="(.*?)".*<b>(.*)<\/b>', link, re.UNICODE)

	match =re.findall('<a href=".*?stream=(.*?)".*?src="(.*?)" (.)', link,re.M)

	print match
	expressExists=False
	expressCName='express'
	arynewsAdded=False
	
	if not any('Express Tv' == x[0] for x in match):
		match.append(('Express Tv','express','manual'))
	if not any('Ary News' == x[0] for x in match):
		match.append(('Ary News','arynews','manual'))
	if not any('Ary Digital' == x[0] for x in match):
		match.append(('Ary Digital','aryentertainment','manual'))

	match.append(('Baby Tv','babytv','manual'))
	match.append(('Star Gold','stargold','manual'))
	match.append(('Ten Sports','tensports','manual'))
	match.append(('Discovery','discovery','manual'))
	match.append(('National Geographic','nationalgeographic','manual'))
	match.append(('mecca','mecca','manual'))
	match.append(('madina','madina','manual'))
	match.append(('Qtv','qtv','manual'))
	match.append(('Peace Tv','peacetv','manual'))

	match=sorted(match,key=lambda s: s[0].lower()   )

	#h = HTMLParser.HTMLParser()
	for cname in match:
		if cname[2]=='manual':
			addDir(Colored(cname[0].capitalize(),'EB') ,cname[1] ,9,cname[2], False, True,isItFolder=False)		#name,url,mode,icon
		else:
			addDir(Colored(cname[0].capitalize(),'EB') ,cname[0] ,9,cname[1], False, True,isItFolder=False)		#name,url,mode,icon

		if 1==2:
			if cname[0]==expressCName:
				expressExists=True
			if cname[0]=='arynews':
				arynewsAdded=True

	if 1==2:			
		if not expressExists:
			addDir(Colored('Express Tv','EB') ,'express' ,9,'', False, True,isItFolder=False)		#name,url,mode,icon
		if not arynewsAdded:
			addDir(Colored('Ary News','EB') ,'arynews' ,9,'', False, True,isItFolder=False)		#name,url,mode,icon
			addDir(Colored('Ary Digital','EB') ,'aryentertainment' ,9,'', False, True,isItFolder=False)		#name,url,mode,icon
		addDir(Colored('Baby Tv','EB') ,'babytv' ,9,'', False, True,isItFolder=False)		#name,url,mode,icon
		addDir(Colored('Star Gold','EB') ,'stargold' ,9,'', False, True,isItFolder=False)		#name,url,mode,icon
		addDir(Colored('Ten Sports','EB') ,'tensports' ,9,'', False, True,isItFolder=False)		#name,url,mode,icon
	return		

def Colored(text = '', colorid = '', isBold = False):
	if colorid == 'ZM':
		color = 'FF11b500'
	elif colorid == 'EB':
		color = 'FFe37101'
	elif colorid == 'bold':
		return '[B]' + text + '[/B]'
	else:
		color = colorid
		
	if isBold == True:
		text = '[B]' + text + '[/B]'
	return '[COLOR ' + color + ']' + text + '[/COLOR]'	

def PlayShowLinkDup ( url ): 
#	url = tabURL.replace('%s',channelName);
	req = urllib2.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0(iPad; U; CPU iPhone OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B314 Safari/531.21.10')
	response = urllib2.urlopen(req)
	link=response.read()
	response.close()
#	print url

	line1 = "Playing DM Link"
	time = 5000  #in miliseconds
 	defaultLinkType=0 #0 youtube,1 DM,2 tunepk
	defaultLinkType=selfAddon.getSetting( "DefaultVideoType" ) 
	#print defaultLinkType
	#print "LT link is" + linkType
	# if linktype is not provided then use the defaultLinkType
	linkType="LINK"
	if linkType=="DM" or (linkType=="" and defaultLinkType=="1"):
		print "PlayDM"
		line1 = "Playing DM Link"
		xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(__addonname__,line1, time, __icon__))
#		print link
		playURL= match =re.findall('src="(.*?(dailymotion).*?)"',link)
		playURL=match[0][0]
		print playURL
		playlist = xbmc.PlayList(1)
		playlist.clear()
		listitem = xbmcgui.ListItem(name, iconImage="DefaultVideo.png")
		listitem.setInfo("Video", {"Title":name})
		listitem.setProperty('mimetype', 'video/x-msvideo')
		listitem.setProperty('IsPlayable', 'true')
		stream_url = urlresolver.HostedMediaFile(playURL).resolve()
		print stream_url
		playlist.add(stream_url,listitem)
		xbmcPlayer = xbmc.Player(xbmc.PLAYER_CORE_AUTO)
	        xbmcPlayer.play(playlist)
#src="(.*?(dailymotion).*?)"
	elif  linkType=="LINK"  or (linkType=="" and defaultLinkType=="2"):
		line1 = "Playing Tune.pk Link"
		xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(__addonname__,line1, time, __icon__))

		print "PlayLINK"
		playURL= match =re.findall('<strong>Tune Full<\/strong>\s*.*?src="(.*?(tune\.pk).*?)"', link)
		playURL=match[0][0]# check if not found then try other methods
		print playURL
		playlist = xbmc.PlayList(1)
		playlist.clear()
		listitem = xbmcgui.ListItem(name, iconImage="DefaultVideo.png")
		listitem.setInfo("Video", {"Title":name})
		listitem.setProperty('mimetype', 'video/x-msvideo')
		listitem.setProperty('IsPlayable', 'true')
		stream_url = urlresolver.HostedMediaFile(playURL).resolve()
		print stream_url
		playlist.add(stream_url,listitem)
		xbmcPlayer = xbmc.Player(xbmc.PLAYER_CORE_AUTO)
	        xbmcPlayer.play(playlist)

#src="(.*?(tune\.pk).*?)"
	else:	#either its default or nothing selected
		line1 = "Playing Youtube Link"
		xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(__addonname__,line1, time, __icon__))

		youtubecode= match =re.findall('<strong>Youtube<\/strong>.*?src=\".*?embed\/(.*?)\?.*\".*?<\/iframe>', link,re.DOTALL| re.IGNORECASE)
		youtubecode=youtubecode[0]
		uurl = 'plugin://plugin.video.youtube/?action=play_video&videoid=%s' % youtubecode
#	print uurl
		xbmc.executebuiltin("xbmc.PlayMedia("+uurl+")")
	
	return
def convert(s):
    try:
        return s.group(0).encode('latin1').decode('utf8')
    except:
        return s.group(0)
		
def AddShows(Fromurl):
#	print Fromurl
	req = urllib2.Request(Fromurl)
	req.add_header('User-Agent','Mozilla/5.0(iPad; U; CPU iPhone OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B314 Safari/531.21.10')
	response = urllib2.urlopen(req)
	link=response.read()
	response.close()
#	print link
#	print "addshows"
#	match=re.compile('<param name="URL" value="(.+?)">').findall(link)
#	match=re.compile('<a href="(.+?)"').findall(link)
#	match=re.compile('onclick="playChannel\(\'(.*?)\'\);">(.*?)</a>').findall(link)
#	match =re.findall('onclick="playChannel\(\'(.*?)\'\);">(.*?)</a>', link, re.DOTALL|re.IGNORECASE)
#	match =re.findall('onclick="playChannel\(\'(.*?)\'\);".?>(.*?)</a>', link, re.DOTALL|re.IGNORECASE)
#	match =re.findall('<div class=\"post-title\"><a href=\"(.*?)\".*<b>(.*)<\/b><\/a>', link, re.IGNORECASE)
#	match =re.findall('<img src="(.*?)" alt=".*".+<\/a>\n*.+<div class="post-title"><a href="(.*?)".*<b>(.*)<\/b>', link, re.UNICODE)

	if '<div id="top-articles">' in link:
		link=link.split('<div id="top-articles">')[0]
	match =re.findall('img src="(.*?)".+\s*<div class="post-title">.*?href="(.*?)".*?<b>(.*?)</', link, re.UNICODE)
#	print Fromurl

#	print match
	h = HTMLParser.HTMLParser()

	for cname in match:
		tname=cname[2]
		tname=re.sub(r'[\x80-\xFF]+', convert,tname )
		#tname=repr(tname)
		addDir(tname,cname[1] ,3,cname[0], True,isItFolder=False)
		
#	<a href="http://www.zemtv.com/page/2/">&gt;</a></li>
	match =re.findall('<a class="nextpostslink" rel="next" href="(.*?)">', link, re.IGNORECASE)
	
	if len(match)==1:
		addDir('Next Page' ,match[0] ,2,'',isItFolder=True)
#       print match
	
	return

	
def AddChannels():
	req = urllib2.Request(liveURL)
	req.add_header('User-Agent','Mozilla/5.0(iPad; U; CPU iPhone OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B314 Safari/531.21.10')
	response = urllib2.urlopen(req)
	link=response.read()
	response.close()
#	print link
#	match=re.compile('<param name="URL" value="(.+?)">').findall(link)
#	match=re.compile('<a href="(.+?)"').findall(link)
#	match=re.compile('onclick="playChannel\(\'(.*?)\'\);">(.*?)</a>').findall(link)
#	match =re.findall('onclick="playChannel\(\'(.*?)\'\);">(.*?)</a>', link, re.DOTALL|re.IGNORECASE)
#	match =re.findall('onclick="playChannel\(\'(.*?)\'\);".?>(.*?)</a>', link, re.DOTALL|re.IGNORECASE)
#	match =re.findall('<div class=\"post-title\"><a href=\"(.*?)\".*<b>(.*)<\/b><\/a>', link, re.IGNORECASE)
#	match =re.findall('<img src="(.*?)" alt=".*".+<\/a>\n*.+<div class="post-title"><a href="(.*?)".*<b>(.*)<\/b>', link, re.UNICODE)

	match =re.findall('<div class="epic-cs">\s*<a href="(.+)" rel=.*<img src="(.+)" alt="(.+)" \/>', link, re.UNICODE)

#	print match
	h = HTMLParser.HTMLParser()
	for cname in match:
		addDir(Colored(h.unescape(cname[2].replace("Watch Now Watch ","").replace("Live, High Quality Streaming","").replace("Live &#8211; High Quality Streaming","").replace("Watch Now ","")) ,'ZM'),cname[0] ,4,cname[1],False,True,isItFolder=False)		
	return	

	
	

def PlayShowLink ( url ): 
#	url = tabURL.replace('%s',channelName);
	req = urllib2.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0(iPad; U; CPU iPhone OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B314 Safari/531.21.10')
	response = urllib2.urlopen(req)
	link=response.read()
	response.close()
#	print url

	line1 = "Playing DM Link"
	time = 5000  #in miliseconds
 	defaultLinkType=0 #0 youtube,1 DM,2 tunepk
	defaultLinkType=selfAddon.getSetting( "DefaultVideoType" ) 
	print defaultLinkType
	print "LT link is" + linkType
	# if linktype is not provided then use the defaultLinkType
	
	if linkType.upper()=="SHOWALL" or (linkType.upper()=="" and defaultLinkType=="5"):
		ShowAllSources(url,link)
		return
	if linkType.upper()=="DM" or (linkType=="" and defaultLinkType=="1"):
		print "PlayDM"
		line1 = "Playing DM Link"
		xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(__addonname__,line1, time, __icon__))
#		print link
		playURL= match =re.findall('src="(http.*?(dailymotion.com).*?)"',link)
		if len(playURL)==0:
			line1 = "Daily motion link not found"
			xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(__addonname__,line1, time, __icon__))
			ShowAllSources(url,link)
			return 
		playURL=match[0][0]
		print playURL
		playlist = xbmc.PlayList(1)
		playlist.clear()
		listitem = xbmcgui.ListItem(name, iconImage="DefaultVideo.png")
		listitem.setInfo("Video", {"Title":name})
		listitem.setProperty('mimetype', 'video/x-msvideo')
		listitem.setProperty('IsPlayable', 'true')
		stream_url = urlresolver.HostedMediaFile(playURL).resolve()
		print stream_url
		playlist.add(stream_url,listitem)
		xbmcPlayer = xbmc.Player(xbmc.PLAYER_CORE_AUTO)
		xbmcPlayer.play(playlist)
		#xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, listitem)
		#src="(.*?(dailymotion).*?)"
	elif  linkType.upper()=="EBOUND"  or (linkType=="" and defaultLinkType=="4"):
		line1 = "Playing Ebound Link"
		xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(__addonname__,line1, time, __icon__))
		print "Eboundlink"
		playURL= match =re.findall(' src=".*?ebound\\.tv.*?site=(.*?)&.*?date=(.*?)\\&', link)
		if len(playURL)==0:
			line1 = "EBound link not found"
			xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(__addonname__,line1, time, __icon__))
			ShowAllSources(url,link)
			return 

		playURL=match[0]
		dt=playURL[1]
		clip=playURL[0]
		urli='http://www.eboundservices.com/iframe/new/vod_ugc.php?stream=mp4:vod/%s/%s&width=620&height=350&clip=%s&day=%s&month=undefined'%(dt,clip,clip,dt)
		#req = urllib2.Request(urli)
		#req.add_header('User-Agent', 'Mozilla/5.0(iPad; U; CPU iPhone OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B314 Safari/531.21.10')
		#response = urllib2.urlopen(req)
		#link=response.read()
		#response.close()
		post = {'username':'hash'}
		post = urllib.urlencode(post)
		req = urllib2.Request('http://eboundservices.com/flashplayerhash/index.php')
		req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.117 Safari/537.36')
		response = urllib2.urlopen(req,post)
		link=response.read()
		response.close()
		strval =link;# match[0]

		stream_url='rtmp://cdn.ebound.tv/vod playpath=mp4:vod/%s/%s app=vod?wmsAuthSign=%s swfurl=http://www.eboundservices.com/live/v6/player.swf?domain=www.zemtv.com&channel=%s&country=EU pageUrl=%s tcUrl=rtmp://cdn.ebound.tv/vod?wmsAuthSign=%s live=true timeout=15'	% (dt,clip,strval,clip,urli,strval)

		print stream_url
		playlist = xbmc.PlayList(1)
		playlist.clear()
		listitem = xbmcgui.ListItem(name, iconImage="DefaultVideo.png")
		listitem.setInfo("Video", {"Title":name})
		listitem.setProperty('mimetype', 'video/x-msvideo')
		listitem.setProperty('IsPlayable', 'true')
		playlist.add(stream_url,listitem)
		xbmcPlayer = xbmc.Player(xbmc.PLAYER_CORE_AUTO)
		xbmcPlayer.play(playlist)
	elif  linkType.upper()=="LINK"  or (linkType=="" and defaultLinkType=="2"):
		line1 = "Playing Tune.pk Link"
		xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(__addonname__,line1, time, __icon__))
		print "PlayLINK"
		playURL= match =re.findall('src="(.*?(tune\.pk).*?)"', link)
		if len(playURL)==0:
			line1 = "Link.pk link not found"
			xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(__addonname__,line1, time, __icon__))
			ShowAllSources(url,link)
			return 

		playURL=match[0][0]
		print playURL
		playlist = xbmc.PlayList(1)
		playlist.clear()
		listitem = xbmcgui.ListItem(name, iconImage="DefaultVideo.png")
		listitem.setInfo("Video", {"Title":name})
		listitem.setProperty('mimetype', 'video/x-msvideo')
		listitem.setProperty('IsPlayable', 'true')
		stream_url = urlresolver.HostedMediaFile(playURL).resolve()
		print stream_url
		playlist.add(stream_url,listitem)
		xbmcPlayer = xbmc.Player(xbmc.PLAYER_CORE_AUTO)
		xbmcPlayer.play(playlist)
	elif  linkType.upper()=="PLAYWIRE"  or (linkType=="" and defaultLinkType=="3"):
		line1 = "Playing Playwire Link"
		xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(__addonname__,line1, time, __icon__))
		print "Playwire"
		playURL =re.findall('src=".*?(playwire).*?data-publisher-id="(.*?)"\s*data-video-id="(.*?)"', link)
		V=1
		if len(playURL)==0:
			playURL =re.findall('data-config="(.*?config.playwire.com.*?)"', link)
			V=2
		if len(playURL)==0:
			line1 = "Playwire link not found"
			xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(__addonname__,line1, time, __icon__))
			ShowAllSources(url,link)
			return 
		if V==1:
			(playWireVar,PubId,videoID)=playURL[0]
			cdnUrl="http://cdn.playwire.com/v2/%s/config/%s.json"%(PubId,videoID)
			req = urllib2.Request(cdnUrl)
			req.add_header('User-Agent', 'Mozilla/5.0(iPad; U; CPU iPhone OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B314 Safari/531.21.10')
			response = urllib2.urlopen(req)
			link=response.read()
			response.close()
			playURL ="http://cdn.playwire.com/%s/%s"%(PubId,re.findall('src":".*?mp4:(.*?)"', link)[0])
			print 'playURL',playURL
		else:
			playURL=playURL[0]
			reg='media":\{"(.*?)":"(.*?)"'
			req = urllib2.Request(playURL)
			req.add_header('User-Agent', 'Mozilla/5.0(iPad; U; CPU iPhone OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B314 Safari/531.21.10')
			response = urllib2.urlopen(req)
			link=response.read()
			playURL =re.findall(reg, link)
			if len(playURL)>0:
				playURL=playURL[0]
				ty=playURL[0]
				innerUrl=playURL[1]
				print innerUrl
				req = urllib2.Request(innerUrl)
				req.add_header('User-Agent', 'Mozilla/5.0(iPad; U; CPU iPhone OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B314 Safari/531.21.10')
				response = urllib2.urlopen(req)
				link=response.read()
				reg='baseURL>(.*?)<\/baseURL>\s*?<media url="(.*?)"'
				playURL =re.findall(reg, link)[0]
				playURL=playURL[0]+'/'+playURL[1]
		playlist = xbmc.PlayList(1)
		playlist.clear()
		listitem = xbmcgui.ListItem(name, iconImage="DefaultVideo.png")
		listitem.setInfo("Video", {"Title":name})
		listitem.setProperty('mimetype', 'video/x-msvideo')
		listitem.setProperty('IsPlayable', 'true')
		stream_url = playURL#urlresolver.HostedMediaFile(playURL).resolve()
		print 'stream_url',stream_url
		playlist.add(stream_url,listitem)
		xbmcPlayer = xbmc.Player(xbmc.PLAYER_CORE_AUTO)
		xbmcPlayer.play(playlist)
		#bmcplugin.setResolvedUrl(int(sys.argv[1]), True, listitem)#src="(.*?(tune\.pk).*?)"
	else:	#either its default or nothing selected
		line1 = "Playing Youtube Link"
		xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(__addonname__,line1, time, __icon__))
		youtubecode= match =re.findall('<strong>Youtube<\/strong>.*?src=\".*?embed\/(.*?)\?.*\".*?<\/iframe>', link,re.DOTALL| re.IGNORECASE)
		if len(youtubecode)==0:
			line1 = "Youtube link not found"
			xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(__addonname__,line1, time, __icon__))
			ShowAllSources(url,link)
			return
		youtubecode=youtubecode[0]
		uurl = 'plugin://plugin.video.youtube/?action=play_video&videoid=%s' % youtubecode
#	print uurl
		xbmc.executebuiltin("xbmc.PlayMedia("+uurl+")")
	
	return

def ShowAllSources(url, loadedLink=None):
	global linkType
	print 'show all sources',url
	link=loadedLink
	if not loadedLink:
		req = urllib2.Request(url)
		req.add_header('User-Agent', 'Mozilla/5.0(iPad; U; CPU iPhone OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B314 Safari/531.21.10')
		response = urllib2.urlopen(req)
		link=response.read()
		response.close()
	available_source=[]
	playURL =re.findall('src=".*?(playwire).*?data-publisher-id="(.*?)"\s*data-video-id="(.*?)"', link)
	print 'playURL',playURL
	if not len(playURL)==0:
		available_source.append('Playwire Source')

	playURL =re.findall('data-config="(.*?config.playwire.com.*?)"', link)
	print 'playURL',playURL
	if not len(playURL)==0:
		available_source.append('Playwire Source')

	playURL =re.findall('src="(.*?ebound\\.tv.*?)"', link)
	print 'playURL',playURL
	if not len(playURL)==0:
		available_source.append('Ebound Source')		
		 
	playURL= match =re.findall('src="(.*?(dailymotion).*?)"',link)
	if not len(playURL)==0:
		available_source.append('Daily Motion Source')

	playURL= match =re.findall('src="(.*?(tune\.pk).*?)"', link)
	if not len(playURL)==0:
		available_source.append('Link Source')

	playURL= match =re.findall('<strong>Youtube<\/strong>.*?src=\".*?embed\/(.*?)\?.*\".*?<\/iframe>', link,re.DOTALL| re.IGNORECASE)
	if not len(playURL)==0:
		available_source.append('Youtube Source')

	if len(available_source)>0:
		dialog = xbmcgui.Dialog()
		index = dialog.select('Choose your stream', available_source)
		if index > -1:
			linkType=available_source[index].replace(' Source','').replace('Daily Motion','DM').upper()
			print 'linkType',linkType
			PlayShowLink(url);

def PlayLiveLink ( url ):
	progress = xbmcgui.DialogProgress()
	progress.create('Progress', 'Fetching Streaming Info')
	progress.update( 10, "", "Finding links..", "" )
	if mode==4:
		req = urllib2.Request(url)
		req.add_header('User-Agent', 'Mozilla/5.0(iPad; U; CPU iPhone OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B314 Safari/531.21.10')
		response = urllib2.urlopen(req)
		link=response.read()
		response.close()
		#print link
		#print url
		match =re.findall('"http.*(ebound).*?\?site=(.*?)"',link,  re.IGNORECASE)[0]
		cName=match[1]
		progress.update( 20, "", "Finding links..", "" )
	else:
		cName=url
	import math, random, time
	rv=str(int(5000+ math.floor(random.random()*10000)))
	currentTime=str(int(time.time()*1000))
	#newURL='http://www.eboundservices.com/iframe/newads/iframe.php?stream='+ cName+'&width=undefined&height=undefined&clip=' + cName
	newURL='http://www.eboundservices.com/iframe/new/mainPage.php?stream='+cName+  '&width=undefined&height=undefined&clip=' + cName+'&rv='+rv+'&_='+currentTime
	
	req = urllib2.Request(newURL)
	req.add_header('User-Agent', 'Mozilla/5.0(iPad; U; CPU iPhone OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B314 Safari/531.21.10')
	response = urllib2.urlopen(req)
	link=response.read()
	response.close()
	progress.update( 50, "", "Finding links..", "" )
	
#	match =re.findall('<iframe.+src=\'(.*)\' frame',link,  re.IGNORECASE)
#	print match
#	req = urllib2.Request(match[0])
#	req.add_header('User-Agent', 'Mozilla/5.0(iPad; U; CPU iPhone OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B314 Safari/531.21.10')
#	response = urllib2.urlopen(req)
#	link=response.read()
#	response.close()
	time = 2000  #in miliseconds
	defaultStreamType=0 #0 RTMP,1 HTTP
	defaultStreamType=selfAddon.getSetting( "DefaultStreamType" ) 
	print 'defaultStreamType',defaultStreamType
	if 1==2 and (linkType=="HTTP" or (linkType=="" and defaultStreamType=="1")): #disable http streaming for time being
#	print link
		line1 = "Playing Http Stream"
		xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(__addonname__,line1, time, __icon__))
		
		match =re.findall('MM_openBrWindow\(\'(.*)\',\'ebound\'', link,  re.IGNORECASE)
			
	#	print url
	#	print match
		
		strval = match[0]
		
		#listitem = xbmcgui.ListItem(name)
		#listitem.setInfo('video', {'Title': name, 'Genre': 'Live TV'})
		#playlist = xbmc.PlayList( xbmc.PLAYLIST_VIDEO )
		#playlist.clear()
		#playlist.add (strval)
		
		#xbmc.Player().play(playlist)
		listitem = xbmcgui.ListItem( label = str(cName), iconImage = "DefaultVideo.png", thumbnailImage = xbmc.getInfoImage( "ListItem.Thumb" ), path=strval )
		print "playing stream name: " + str(cName) 
		listitem.setInfo( type="video", infoLabels={ "Title": cName, "Path" : strval } )
		listitem.setInfo( type="video", infoLabels={ "Title": cName, "Plot" : cName, "TVShowTitle": cName } )
		xbmc.Player(PLAYER_CORE_AUTO).play( str(strval), listitem)
	else:
		line1 = "Playing RTMP Stream"
		xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(__addonname__,line1, time, __icon__))
		progress.update( 60, "", "Finding links..", "" )
		post = {'username':'hash'}
        	post = urllib.urlencode(post)
		req = urllib2.Request('http://eboundservices.com/flashplayerhash/index.php')
		req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.117 Safari/537.36')
		response = urllib2.urlopen(req,post)
		link=response.read()
		response.close()
		

        
		print link
		#match =re.findall("=(.*)", link)

		#print url
		#print match

		strval =link;# match[0]

		#listitem = xbmcgui.ListItem(name)
		#listitem.setInfo('video', {'Title': name, 'Genre': 'Live TV'})
		#playlist = xbmc.PlayList( xbmc.PLAYLIST_VIDEO )
		#playlist.clear()
		#playlist.add (strval)

		playfile='rtmp://cdn.ebound.tv/tv?wmsAuthSign=/%s app=tv?wmsAuthSign=%s swfurl=http://www.eboundservices.com/live/v6/jwplayer.flash.swf?domain=www.eboundservices.com&channel=%s&country=EU pageUrl=http://www.eboundservices.com/channel.php?app=tv&stream=%s tcUrl=rtmp://cdn.ebound.tv/tv?wmsAuthSign=%s live=true timeout=15'	% (cName,strval,cName,cName,strval)
		#playfile='rtmp://cdn.ebound.tv/tv?wmsAuthSign=/humtv app=tv?wmsAuthSign=?%s swfurl=http://www.eboundservices.com/live/v6/player.swf?domain=&channel=humtv&country=GB pageUrl=http://www.eboundservices.com/iframe/newads/iframe.php?stream=humtv tcUrl=rtmp://cdn.ebound.tv/tv?wmsAuthSign=?%s live=true'	% (strval,strval)
		progress.update( 100, "", "Almost done..", "" )
		print playfile
		#xbmc.Player().play(playlist)
		listitem = xbmcgui.ListItem( label = str(name), iconImage = "DefaultVideo.png", thumbnailImage = xbmc.getInfoImage( "ListItem.Thumb" ) )
		print "playing stream name: " + str(name) 
		#listitem.setInfo( type="video", infoLabels={ "Title": name, "Path" : playfile } )
		#listitem.setInfo( type="video", infoLabels={ "Title": name, "Plot" : name, "TVShowTitle": name } )
		xbmc.Player( xbmc.PLAYER_CORE_AUTO ).play( playfile, listitem)
		#xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, listitem)
	
	
	return


#print "i am here"
params=get_params()
url=None
name=None
mode=None
linkType=None

try:
	url=urllib.unquote_plus(params["url"])
except:
	pass
try:
	name=urllib.unquote_plus(params["name"])
except:
	pass
try:
	mode=int(params["mode"])
except:
	pass


args = cgi.parse_qs(sys.argv[2][1:])
linkType=''
try:
	linkType=args.get('linkType', '')[0]
except:
	pass


print 	mode,url,linkType

try:
	if mode==None or url==None or len(url)<1:
		print "InAddTypes"
		Addtypes()
	elif mode==2:
		print "Ent url is "+name
		AddEnteries(name)

	elif mode==3:
		print "Play url is "+url
		PlayShowLink(url)

	elif mode==4 or mode==9:
		print "Play url is "+url
		PlayLiveLink(url)
	elif mode==11:
		print "Play url is "+url
		PlayOtherUrl(url)

	elif mode==6 :
		print "Play url is "+url
		ShowSettings(url)
	elif mode==13 :
		print "Play url is "+url
		AddSports(url)
	elif mode==14 or mode==144:
		print "Play url is "+url
		AddSmartCric(url)
	elif mode==15 :
		print "Play url is "+url
		PlaySmartCric(url)
	elif mode==16 :
		print "Play url is "+url
		AddWatchCric(url)
	elif mode==17 :
		print "Play url is "+url
		PlayWatchCric(url)
	elif mode==19 :
		print "Play url is "+url
		AddWillowCric(url)
	elif mode==20:
		print "Play url is "+url
		AddWillSportsOldSeries(url)
	elif mode==21 or mode==22:
		print "Play url is "+url
		PlayWillowMatch(url)        
	elif mode==23:
		print "Play url is "+url
		AddWillowReplayParts(url)        
	elif mode==24:
		print "Play url is "+url
		AddWillSportsOldSeriesMatches(url)        
	elif mode==25 :
		print "Play url is "+url
		AddP3Gtv(url)
	elif mode==26 :
		print "Play url is "+url
		AddPopeLive(url)
	elif mode==27 :
		print "Play url is "+url
		PlayPopeLive(url)                
	elif mode==31 :
		print "Play url is "+url
		AddFlashtv(url)                
	elif mode==30 :
		print "Play url is "+url
		AddP3gSports(url)                
	elif mode==32 :
		print "Play url is "+url
		PlayFlashTv(url)                


        
except:
	print 'somethingwrong'
	traceback.print_exc(file=sys.stdout)
	

if not ( (mode==3 or mode==4 or mode==9 or mode==11 or mode==15 or mode==21 or mode==22 or mode==27)  )  :
	if mode==144:
		xbmcplugin.endOfDirectory(int(sys.argv[1]),updateListing=True)
	else:
		xbmcplugin.endOfDirectory(int(sys.argv[1]))
