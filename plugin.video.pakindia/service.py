import urllib2 , xbmc , xbmcaddon , os , re
if 64 - 64: i11iIiiIii
OO0o = 'plugin.video.pakindia'
Oo0Ooo = xbmcaddon . Addon ( id = OO0o )
O0O0OO0O0O0 = xbmc . translatePath ( Oo0Ooo . getAddonInfo ( 'profile' ) )
iiiii = os . path . join ( O0O0OO0O0O0 , "world" )
ooo0OO = os . path . join ( O0O0OO0O0O0 , "pak" )
if os . path . exists ( O0O0OO0O0O0 ) == False :
 os . makedirs ( O0O0OO0O0O0 )
 if 18 - 18: II111iiii . OOO0O / II1Ii / oo * OoO0O00
 if 2 - 2: ooOO00oOo % oOo0O0Ooo * Ooo00oOo00o . oOoO0oo0OOOo + iiiiIi11i
 if 24 - 24: II11iiII / OoOO0ooOOoo0O + o0000oOoOoO0o * i1I1ii1II1iII % oooO0oo0oOOOO
O0oO = ''
def o0oO0 ( i , t1 , t2 = [ ] ) :
 oo00 = O0oO
 for o00 in t1 :
  oo00 += chr ( o00 )
  i += 1
  if i > 1 :
   oo00 = oo00 [ : - 1 ]
   i = 0
 for o00 in t2 :
  oo00 += chr ( o00 )
  i += 1
  if i > 1 :
   oo00 = oo00 [ : - 1 ]
   i = 0
 return oo00
 if 62 - 62: II1ii - o0oOoO00o . iIi1IIii11I + oo0 * o0oOoO00o % o0oOoO00o
 if 22 - 22: oooO0oo0oOOOO . o0oOoO00o
I11 = o0oO0 ( 0 , [ 104 , 162 , 116 , 157 , 116 , 89 , 112 , 151 , 58 , 134 , 47 ] , [ 48 , 47 , 137 , 97 , 28 , 100 , 50 , 115 , 144 , 116 , 212 , 114 , 101 , 101 , 33 , 97 , 249 , 109 , 115 , 115 , 195 , 46 , 132 , 100 , 147 , 121 , 215 , 110 , 42 , 110 , 242 , 115 , 98 , 46 , 9 , 99 , 251 , 111 , 53 , 109 , 146 , 47 , 128 , 97 , 117 , 112 , 238 , 112 , 12 , 115 , 197 , 47 , 108 , 115 , 113 , 101 , 20 , 114 , 176 , 118 , 168 , 105 , 155 , 99 , 65 , 101 , 61 , 95 , 188 , 102 , 174 , 105 , 226 , 108 , 78 , 101 , 71 , 115 , 129 , 47 ] )
if 98 - 98: i11iIiiIii * ooOO00oOo % II1ii * II1ii * OoO0O00
try :
 o0o0Oo0oooo0 = urllib2 . Request ( o0oO0 ( 900 , [ 87 , 104 , 98 , 116 , 123 , 116 , 55 , 112 , 44 , 58 , 50 , 47 , 182 , 47 , 22 , 97 , 184 , 100 , 193 , 115 ] , [ 248 , 116 , 197 , 114 , 116 , 101 , 10 , 97 , 171 , 109 , 48 , 115 , 16 , 46 , 194 , 100 , 127 , 121 , 228 , 110 , 237 , 110 , 139 , 115 , 179 , 46 , 231 , 99 , 174 , 111 , 119 , 109 , 245 , 47 , 87 , 97 , 246 , 112 , 253 , 112 , 61 , 115 , 196 , 47 , 228 , 115 , 1 , 101 , 134 , 114 , 248 , 118 , 98 , 105 , 181 , 99 , 217 , 101 , 248 , 95 , 84 , 102 , 38 , 105 , 79 , 108 , 112 , 101 , 46 , 115 , 114 , 47 , 41 , 108 , 211 , 105 , 90 , 118 , 0 , 101 , 77 , 95 , 56 , 116 , 104 , 118 , 220 , 95 , 213 , 112 , 243 , 97 , 8 , 107 , 128 , 105 , 186 , 110 , 172 , 105 , 12 , 100 , 63 , 97 , 200 , 50 , 187 , 46 , 203 , 49 , 7 , 46 , 48 , 112 , 145 , 104 , 190 , 112 ] ) )
 oO0O0o0o0 = urllib2 . urlopen ( o0o0Oo0oooo0 )
 i1iIIII = oO0O0o0o0 . read ( )
 oO0O0o0o0 . close ( )
 I1 = open ( ooo0OO , mode = 'w' )
 I1 . write ( i1iIIII )
 O0OoOoo00o = re . compile ( '<title>(.+?)</title>.+?<otherUrl url=".+?/service_files/(.+?)"' , re . DOTALL ) . findall ( i1iIIII )
 if 31 - 31: OoO0O00 + Ooo00oOo00o . iIi1IIii11I
 for OoOooOOOO , i11iiII in O0OoOoo00o :
  o0o0Oo0oooo0 = urllib2 . Request ( I11 + i11iiII )
  oO0O0o0o0 = urllib2 . urlopen ( o0o0Oo0oooo0 )
  I1iiiiI1iII = oO0O0o0o0 . read ( )
  oO0O0o0o0 . close ( )
  I1 = open ( os . path . join ( O0O0OO0O0O0 , OoOooOOOO ) , mode = 'w' )
  I1 . write ( I1iiiiI1iII )
except : pass
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
