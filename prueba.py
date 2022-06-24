import re
cadena = " 33.   . 34.3 .33 -0.43 +33.3 -.42-"
ids= "_274urhd739 _e _d2_2_2 32_ 89 id ide4 ___id2 s78565 _"
#para decimales
print(re.findall(r'\-?\d*\.\d+\s',cadena))

#para ids
print("\n",re.findall(r'[a-z*|_][_\w]+',ids))
