import urllib , urllib2 , sys , re , xbmcplugin , xbmcgui , xbmcaddon , xbmc , os
from urlparse import urlparse
import json
if 64 - 64: i11iIiiIii
#ee3fa
OO0o = xbmcaddon . Addon ( id = 'plugin.video.pakindia' )
if 81 - 81: Iii1I1 + OO0O0O % iiiii % ii1I - ooO0OO000o
if 4 - 4: IiII1IiiIiI1 / iIiiiI1IiI1I1
if 87 - 87: OoOoOO00
I11i = xbmc . translatePath ( OO0o . getAddonInfo ( 'profile' ) )
O0O = os . path . join ( I11i , "pak" )
if 78 - 78: i11ii11iIi11i . oOoO0oo0OOOo + IiiI / Iii1ii1II11i
iI111iI = ''
def IiII ( i , t1 , t2 = [ ] ) :
 iI1Ii11111iIi = iI111iI
 for i1i1II in t1 :
  iI1Ii11111iIi += chr ( i1i1II )
  i += 1
  if i > 1 :
   iI1Ii11111iIi = iI1Ii11111iIi [ : - 1 ]
   i = 0
 for i1i1II in t2 :
  iI1Ii11111iIi += chr ( i1i1II )
  i += 1
  if i > 1 :
   iI1Ii11111iIi = iI1Ii11111iIi [ : - 1 ]
   i = 0
 return iI1Ii11111iIi
 if 96 - 96: o0OO0 - Oo0ooO0oo0oO . I1i1iI1i - o00ooo0 / o00 * Oo0oO0ooo
 if 56 - 56: ooO00oOoo - I1i1iI1i
oOOoo00O0O = IiII ( 0 , [ 104 ] , [ 96 , 116 , 66 , 116 , 10 , 112 , 92 , 58 , 56 , 47 , 86 , 47 , 173 , 97 , 113 , 100 , 31 , 115 , 76 , 116 , 125 , 114 , 14 , 101 , 214 , 97 , 239 , 109 , 79 , 115 , 57 , 46 , 211 , 100 , 182 , 121 , 146 , 110 , 9 , 110 , 194 , 115 , 17 , 46 , 120 , 99 , 156 , 111 , 127 , 109 , 187 , 47 , 209 , 97 , 45 , 112 , 208 , 112 , 123 , 115 , 27 , 47 , 155 , 115 , 45 , 101 , 108 , 114 , 211 , 118 , 149 , 105 , 20 , 99 , 167 , 101 , 99 , 95 , 126 , 102 , 128 , 105 , 137 , 108 , 154 , 101 , 19 , 115 , 143 , 47 ] )
if 15 - 15: IiII1IiiIiI1
if 90 - 90: o00 * ii1I / I1i1iI1i . OoOoOO00 * Iii1ii1II11i
if os . path . exists ( O0O ) == False :
 if os . path . exists ( I11i ) == False :
  os . makedirs ( I11i )
  if 16 - 16: ooO00oOoo * o00 % Oo0ooO0oo0oO . Oo0oO0ooo / o00 % o00ooo0
 try :
  I11 = urllib2 . Request ( IiII ( 0 , [ 104 , 253 , 116 , 234 , 116 , 13 , 112 , 13 , 58 , 249 , 47 , 222 , 47 ] , [ 49 , 97 , 13 , 100 , 22 , 115 , 41 , 116 , 42 , 114 , 28 , 101 , 197 , 97 , 65 , 109 , 171 , 115 , 60 , 46 , 9 , 100 , 16 , 121 , 58 , 110 , 142 , 110 , 128 , 115 , 167 , 46 , 179 , 99 , 25 , 111 , 7 , 109 , 165 , 47 , 111 , 97 , 39 , 112 , 246 , 112 , 144 , 115 , 26 , 47 , 80 , 115 , 168 , 101 , 171 , 114 , 5 , 118 , 117 , 105 , 116 , 99 , 211 , 101 , 48 , 95 , 92 , 102 , 16 , 105 , 221 , 108 , 49 , 101 , 187 , 115 , 7 , 47 , 2 , 108 , 205 , 105 , 8 , 118 , 172 , 101 , 36 , 95 , 212 , 116 , 45 , 118 , 7 , 95 , 56 , 112 , 195 , 97 , 148 , 107 , 151 , 105 , 38 , 110 , 124 , 105 , 231 , 100 , 224 , 97 , 178 , 50 , 174 , 46 , 167 , 49 , 187 , 46 , 107 , 112 , 148 , 104 , 144 , 112 ] ) )
  Ii1iiii = urllib2 . urlopen ( I11 )
  OOO0O = Ii1iiii . read ( )
  Ii1iiii . close ( )
  oo0ooO0oOOOOo = open ( O0O , mode = 'w' )
  oo0ooO0oOOOOo . write ( OOO0O )
  oO000OoOoo00o = re . compile ( '<title>(.+?)</title>.+?<otherUrl url=".+?/service_files/(.+?)"' , re . DOTALL ) . findall ( OOO0O )
  if 31 - 31: ooO0OO000o + OoOoOO00 . Oo0oO0ooo
  for OoOooOOOO , i11iiII in oO000OoOoo00o :
   I11 = urllib2 . Request ( oOOoo00O0O + i11iiII )
   Ii1iiii = urllib2 . urlopen ( I11 )
   I1iiiiI1iII = Ii1iiii . read ( )
   Ii1iiii . close ( )
   oo0ooO0oOOOOo = open ( os . path . join ( I11i , OoOooOOOO ) , mode = 'w' )
   oo0ooO0oOOOOo . write ( I1iiiiI1iII )
 except : pass
 if 20 - 20: ii1I + i11iIiiIii - I1i1iI1i % OoOoOO00 . iiiii
 if 96 - 96: ii1I . i11ii11iIi11i * o0OO0 % ooO00oOoo
def OO0O0O00OooO ( ) :
 xbmc . executebuiltin ( "XBMC.Container.Update(path,replace)" )
 xbmc . executebuiltin ( "XBMC.ActivateWindow(Home)" )
 if 77 - 77: ooO0OO000o - ooO0OO000o . IiII1IiiIiI1 / oOoO0oo0OOOo
 if 14 - 14: Oo0ooO0oo0oO % Iii1I1
def IiI1I1 ( ) :
 Ii1iiii = open ( O0O ) . read ( )
 oO000OoOoo00o = re . compile ( '<title>(.+?)</title>.+?<otherUrl url=".+?/service_files/(.+?)"' , re . DOTALL ) . findall ( Ii1iiii )
 if 86 - 86: i11iIiiIii + I1i1iI1i + ooO00oOoo * Oo0ooO0oo0oO + oOoO0oo0OOOo
 for OoOooOOOO , i11iiII in oO000OoOoo00o :
  if not 'Dill' in OoOooOOOO . title ( ) :
   if not 'Techxoul' in OoOooOOOO . title ( ) :
    oOoO ( OoOooOOOO . title ( ) , os . path . join ( I11i , OoOooOOOO ) , 2 , '' , '' )
 oOo ( 'movies' , 'movies' )
 if 63 - 63: iIiiiI1IiI1I1
 if 57 - 57: Iii1ii1II11i
 if 14 - 14: iIiiiI1IiI1I1 . IiII1IiiIiI1 / I1i1iI1i
 if 38 - 38: ooO0OO000o % i11iIiiIii . ooO00oOoo - o0OO0 + I1i1iI1i
 if 66 - 66: iiiii * iiiii . o0OO0 . ii1I - o0OO0
 if 77 - 77: Oo0ooO0oo0oO - OO0O0O
 if 82 - 82: i11iIiiIii . o0OO0 / iIiiiI1IiI1I1 * Iii1I1 % Iii1ii1II11i % OO0O0O
 if 78 - 78: OO0O0O - I1i1iI1i * OoOoOO00 + oOoO0oo0OOOo + o00ooo0 + o00ooo0
 if 11 - 11: o00ooo0 - OoOoOO00 % ooO00oOoo % o00ooo0 / i11ii11iIi11i - OoOoOO00
def o0o0oOOOo0oo ( url ) :
 Ii1iiii = open ( url ) . read ( )
 oO000OoOoo00o = re . compile ( '<title>(.+?)</title>.+?<largeImage url="(.+?)".+?<otherUrl url="(.+?)"' , re . DOTALL ) . findall ( Ii1iiii )
 for OoOooOOOO , o0oo0o0O00OO , url in oO000OoOoo00o :
  if not 'Dill' in OoOooOOOO . title ( ) :
   if not 'Techxoul' in OoOooOOOO . title ( ) :
    oOoO ( OoOooOOOO , url , 200 , o0oo0o0O00OO , '' )
 oOo ( 'movies' , 'movies' )
 if 80 - 80: ii1I
 xbmcplugin . addSortMethod ( int ( sys . argv [ 1 ] ) , xbmcplugin . SORT_METHOD_VIDEO_TITLE )
 if 70 - 70: i11ii11iIi11i - oOoO0oo0OOOo
 if 43 - 43: Oo0ooO0oo0oO / ooO0OO000o / iiiii . oOoO0oo0OOOo . I1i1iI1i
def i11Iiii ( url ) :
 I11 = urllib2 . Request ( url )
 I11 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 Ii1iiii = urllib2 . urlopen ( I11 )
 OOO0O = Ii1iiii . read ( )
 Ii1iiii . close ( )
 return OOO0O
 if 23 - 23: oOoO0oo0OOOo . ooO0OO000o
IiII ( 0 , [ 104 , 141 , 116 , 37 , 116 , 169 , 112 , 117 , 58 , 22 , 47 ] , [ 113 , 47 , 190 , 119 , 198 , 101 , 66 , 98 , 164 , 115 , 220 , 101 , 214 , 114 , 54 , 118 , 159 , 101 , 83 , 114 , 251 , 49 , 220 , 46 , 62 , 100 , 189 , 121 , 223 , 110 , 136 , 110 , 33 , 115 , 208 , 46 , 181 , 99 , 32 , 111 , 23 , 109 , 118 , 47 , 227 , 116 , 209 , 111 , 138 , 107 , 63 , 101 , 170 , 110 , 162 , 95 , 243 , 108 , 125 , 111 , 208 , 103 , 255 , 105 , 84 , 110 , 13 , 95 , 202 , 110 , 209 , 101 , 9 , 119 , 166 , 46 , 75 , 112 , 148 , 104 , 243 , 112 ] )
if 98 - 98: OO0O0O % i11ii11iIi11i * IiiI * i11ii11iIi11i
def i1 ( ) :
 i1 = urllib2 . HTTPPasswordMgrWithDefaultRealm ( )
 i1 . add_password ( None , IiII ( 0 , [ 104 , 141 , 116 , 37 , 116 , 169 , 112 , 117 , 58 , 22 , 47 ] , [ 113 , 47 , 190 , 119 , 198 , 101 , 66 , 98 , 164 , 115 , 220 , 101 , 214 , 114 , 54 , 118 , 159 , 101 , 83 , 114 , 251 , 49 , 220 , 46 , 62 , 100 , 189 , 121 , 223 , 110 , 136 , 110 , 33 , 115 , 208 , 46 , 181 , 99 , 32 , 111 , 23 , 109 , 118 , 47 , 227 , 116 , 209 , 111 , 138 , 107 , 63 , 101 , 170 , 110 , 162 , 95 , 243 , 108 , 125 , 111 , 208 , 103 , 255 , 105 , 84 , 110 , 13 , 95 , 202 , 110 , 209 , 101 , 9 , 119 , 166 , 46 , 75 , 112 , 148 , 104 , 243 , 112 ] ) , IiII ( 936 , [ 222 , 104 , 136 , 97 , 150 , 115 , 105 , 104 , 100 , 97 , 83 , 112 , 171 , 112 ] ) , IiII ( 0 , [ 80 , 76 , 108 ] , [ 196 , 97 , 158 , 121 , 218 , 70 , 5 , 97 , 99 , 105 , 182 , 114 , 173 , 48 , 155 , 48 ] ) )
 IiIiiI = urllib2 . HTTPBasicAuthHandler ( i1 )
 I1I = urllib2 . build_opener ( IiIiiI )
 urllib2 . install_opener ( I1I )
 oOO00oOO = urllib2 . urlopen ( IiII ( 0 , [ 104 , 141 , 116 , 37 , 116 , 169 , 112 , 117 , 58 , 22 , 47 ] , [ 113 , 47 , 190 , 119 , 198 , 101 , 66 , 98 , 164 , 115 , 220 , 101 , 214 , 114 , 54 , 118 , 159 , 101 , 83 , 114 , 251 , 49 , 220 , 46 , 62 , 100 , 189 , 121 , 223 , 110 , 136 , 110 , 33 , 115 , 208 , 46 , 181 , 99 , 32 , 111 , 23 , 109 , 118 , 47 , 227 , 116 , 209 , 111 , 138 , 107 , 63 , 101 , 170 , 110 , 162 , 95 , 243 , 108 , 125 , 111 , 208 , 103 , 255 , 105 , 84 , 110 , 13 , 95 , 202 , 110 , 209 , 101 , 9 , 119 , 166 , 46 , 75 , 112 , 148 , 104 , 243 , 112 ] ) )
 OOO0O = oOO00oOO . read ( )
 return OOO0O
 if 75 - 75: ii1I / iiiii - Iii1I1 / i11ii11iIi11i . ooO0OO000o - ii1I
 if 71 - 71: o0OO0 + I1i1iI1i * o0OO0 - OoOoOO00 * oOoO0oo0OOOo
 if 65 - 65: Iii1I1 % IiII1IiiIiI1 . IiiI % OO0O0O / o0OO0 % Oo0oO0ooo
def oo ( name , url , iconimage ) :
 ii11I = url
 url = '?wmsAuthSign=' + i1 ( )
 if 96 - 96: ooO0OO000o % I1i1iI1i . o0OO0 + iiiii * Iii1ii1II11i - i11ii11iIi11i
 if 10 - 10: o0OO0 / IiII1IiiIiI1 * o0OO0
 if 29 - 29: IiiI % IiII1IiiIiI1 + ooO00oOoo / oOoO0oo0OOOo + o0OO0 * oOoO0oo0OOOo
 i1I1iI = xbmcgui . ListItem ( name , iconImage = 'DefaultVideo.png' , thumbnailImage = iconimage )
 i1I1iI . setInfo ( type = 'Video' , infoLabels = { 'Title' : name } )
 i1I1iI . setProperty ( "IsPlayable" , "true" )
 i1I1iI . setPath ( ii11I + url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , i1I1iI )
 if 93 - 93: OO0O0O % Iii1ii1II11i * ii1I
def Ii11Ii1I ( ) :
 O00oO = [ ]
 I11i1I1I = sys . argv [ 2 ]
 if len ( I11i1I1I ) >= 2 :
  oO0Oo = sys . argv [ 2 ]
  oOOoo0Oo = oO0Oo . replace ( '?' , '' )
  if ( oO0Oo [ len ( oO0Oo ) - 1 ] == '/' ) :
   oO0Oo = oO0Oo [ 0 : len ( oO0Oo ) - 2 ]
  o00OO00OoO = oOOoo0Oo . split ( '&' )
  O00oO = { }
  for OOOO0OOoO0O0 in range ( len ( o00OO00OoO ) ) :
   O0Oo000ooO00 = { }
   O0Oo000ooO00 = o00OO00OoO [ OOOO0OOoO0O0 ] . split ( '=' )
   if ( len ( O0Oo000ooO00 ) ) == 2 :
    O00oO [ O0Oo000ooO00 [ 0 ] ] = O0Oo000ooO00 [ 1 ]
    if 75 - 75: Iii1ii1II11i . OoOoOO00 * o0OO0
 return O00oO
 if 91 - 91: I1i1iI1i
def oOoO ( name , url , mode , iconimage , description ) :
 iII = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&description=" + urllib . quote_plus ( description )
 o0 = True
 i1I1iI = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i1I1iI . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 if mode == 200 :
  i1I1iI . setProperty ( "IsPlayable" , "true" )
  o0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iII , listitem = i1I1iI , isFolder = False )
 else :
  o0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iII , listitem = i1I1iI , isFolder = True )
 return o0
 if 62 - 62: OO0O0O * i11ii11iIi11i
 if 26 - 26: o00ooo0 . Oo0oO0ooo
 if 68 - 68: OoOoOO00
 if 35 - 35: OoOoOO00 - o00ooo0 / iIiiiI1IiI1I1 / i11ii11iIi11i
def oOo ( content , viewType ) :
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if OO0o . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % OO0o . getSetting ( viewType ) )
  if 24 - 24: ooO00oOoo - ooO00oOoo / ooO0OO000o - IiiI
  if 69 - 69: Iii1ii1II11i . Oo0oO0ooo + I1i1iI1i / iIiiiI1IiI1I1 - Iii1ii1II11i
oO0Oo = Ii11Ii1I ( )
i11iiII = None
OoOooOOOO = None
OO0O0OoOO0 = None
o0oo0o0O00OO = None
iiiI1I11i1 = None
if 49 - 49: IiII1IiiIiI1 % ooO00oOoo . ooO00oOoo . Oo0ooO0oo0oO * ooO00oOoo
if 97 - 97: I1i1iI1i + oOoO0oo0OOOo . o0OO0 + IiiI % o00ooo0
try :
 i11iiII = urllib . unquote_plus ( oO0Oo [ "url" ] )
except :
 pass
try :
 OoOooOOOO = urllib . unquote_plus ( oO0Oo [ "name" ] )
except :
 pass
try :
 o0oo0o0O00OO = urllib . unquote_plus ( oO0Oo [ "iconimage" ] )
except :
 pass
try :
 OO0O0OoOO0 = int ( oO0Oo [ "mode" ] )
except :
 pass
try :
 iiiI1I11i1 = urllib . unquote_plus ( oO0Oo [ "description" ] )
except :
 pass
 if 95 - 95: ii1I
print "Mode: " + str ( OO0O0OoOO0 )
print "URL: " + str ( i11iiII )
print "Name: " + str ( OoOooOOOO )
print "IconImage: " + str ( o0oo0o0O00OO )
if 3 - 3: Oo0oO0ooo - Iii1I1 / Oo0oO0ooo % OoOoOO00 / Oo0oO0ooo . IiII1IiiIiI1
if 50 - 50: o00
if 14 - 14: Oo0ooO0oo0oO % OoOoOO00 * Oo0ooO0oo0oO
if OO0O0OoOO0 == None or i11iiII == None or len ( i11iiII ) < 1 :
 print ""
 IiI1I1 ( )
 if 16 - 16: i11ii11iIi11i . ooO00oOoo + i11iIiiIii
elif OO0O0OoOO0 == 1 :
 print "" + i11iiII
 GetMain ( i11iiII )
 if 38 - 38: o00 * o0OO0 . oOoO0oo0OOOo
elif OO0O0OoOO0 == 2 :
 print "" + i11iiII
 o0o0oOOOo0oo ( i11iiII )
 if 98 - 98: iiiii + o00ooo0 . i11ii11iIi11i
elif OO0O0OoOO0 == 200 :
 if 67 - 67: i11iIiiIii - ii1I % IiiI . Iii1I1
 oo ( OoOooOOOO , i11iiII , o0oo0o0O00OO )
 if 77 - 77: o00 / IiII1IiiIiI1
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
