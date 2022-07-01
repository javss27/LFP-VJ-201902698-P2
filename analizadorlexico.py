from glob import glob
import os
import ply.lex as lex
result_lexema=[]
reservada = (
    'STRING',
    'INT',
    'DOUBLE',
    'CHAR',
    'BOOLEAN',
    'VOID',
    'RETURN',

     #CILCOS
    'WHILE',
    'DO',

    #condiciones
    'IF',
    'ELSE',
)
contenido = "<!DOCTYPE html>\n"
contenido +="<html lang=\"en\">\n"
contenido += "<head>"
contenido +="<meta charset=\"UTF-8\">"
contenido +="<meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">"
contenido += "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">"
contenido +="<title>Document</title>"
contenido +="</head>"
contenido +="<body>"
contenido += "<table  style=\"margin: 0 auto;\" class=\"default\">"
contenido += "<tr> <td>Linea</td>   <td>tipo</td>    <td>Valor</td>  <td>posicion</td> </tr>"

contenidor = "<!DOCTYPE html>\n"
contenidor +="<html lang=\"en\">\n"
contenidor += "<head>"
contenidor +="<meta charset=\"UTF-8\">"
contenidor +="<meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">"
contenidor += "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">"
contenidor +="<title>Document</title>"
contenidor +="</head>"
contenidor +="<body>"
contenidor += "<table  style=\"margin: 0 auto;\" class=\"default\">"
contenidor += "<tr> <td>Linea</td>   <td>Columna</td>    <td>Tipo</td>  <td>Mensaje</td> </tr>"

tokens = reservada + (
    'COMENTLINE',
    'COMENTLINES',
    'ID',
    'DECIMAL',
    'ENTERO',
    'CADENA',
    'CARACTER',
    
    #operaciones
    'SUMA',
    'RESTA',
    'MULT',
    'DIV',
    'MOD',
    'MENORQUE',
    'MAYORQUE',

    #LOGICA
    'IGUALACION',
    'DIFERENCIACION',
    'MAYOR',
    'MENOR',
    'MAYORIGUAL',
    'MENORIGUAL',
    'AND',
    'OR',
    'NOT',

   

    #SIMBOLOS
    'IGUAL',
    'PARIZQ',
    'PARDER',
    'LLAVEIZQ',
    'LLAVEDER',

    'PUNTO',
    'PUNTOCOMA',
    'COMA',
    'COMILLA',
    'COMDOBLE'

)

#reglas exp regulares
t_SUMA = r'\+'
t_RESTA = r'\-'
t_MULT = r'\*'
t_MOD = r'\%'
t_DIV = r'\/'

t_IGUAL = r'\='
t_AND = r"\&\&"
t_OR = r"\|\|"
t_NOT = r'\!'
t_MENORQUE = r'\<'
t_MAYORQUE = r'\>'

t_PUNTOCOMA = r'\;'
t_PUNTO = r'\.'
t_COMA = r'\,'
t_COMILLA =r'\''
t_COMDOBLE = r'\"'

t_PARIZQ = r'\('
t_PARDER = r'\)'
t_LLAVEIZQ = r'\{'
t_LLAVEDER = r'\}'




#metodo de cada reservada
def t_STRING(t):
    r'string'
    return t

def t_INT(t):
    r'int'
    return t

def t_DOUBLE(t):
    r'double'
    return t

def t_CHAR(t):
    r'char'
    return t

def t_BOOLEAN(t):
    r'boolean'
    return t

def t_VOID(t):
    r'void'
    return t

def t_RETURN(t):
    r'return'
    return t

#CICLOS
def t_WHILE(t):
    r'while'
    return t

def t_DO(t):
    r'do'
    return t

#CONDICIONES
def t_IF(t):
    r'if'
    return t

def t_ELSE(t):
    r'else'
    return t

#expreciones regulares para los tipos de datos
def t_ID(t):
    r'[a-z*|_][_\w]+|[a-z]'
    return t

def t_DECIMAL(t):#hay quever si se corrigue por lo de algun simbolo al final
    r'\-?\d*\.\d+'
    return t

def t_ENTERO(t):
    r'\d+'
    return t

def t_CADENA(t):
    r'\".*\"'
    return t

def t_CARACTER(t):
    r'\'.\''
    return t

#operaciones
def t_IGUALACION(t):
    r'=='
    return t

def t_DIFERENCIACION(t):
    r'!='
    return t

def t_MAYORIGUAL(t):
    r'>='
    return t

def t_MENORIGUAL(t):
    r'<='
    return t 



#COMENTARIOS
def t_COMENTLINE(t):
    r'\/\/(.)*'
    #print("cometariolinea:",t.lexpos,"linea",t.lineno)
    return t

def t_COMENTLINES(t):
    r'(\/\*(.|\n)*?\*\/)'
    """ print("aber la t:",t) son valores que lleva la 't' osea el lexema
    print("aber la t:",t.type) tipo de token
    print("aber la t:",t.value) el contenido del lexema
    print("aber la t:",t.lexer.lineno) linea leida
    print("aber la t:",t.lexer.lexpos) posicion general (no tocar)"""

    for x in t.value:
        if x == "\n":
            t.lexer.lineno+=1        
    return t
    #t.lexer.lineno+=1
    #print("cometariolineasss:",t.lexpos,"linea",t.lineno)

def t_newline(t):
    r'\n+'
    t.lexer.lineno+=len(t.value)
    #print("saltos----------:",t.lexpos,"linea",t.lineno)
    
t_ignore= ' \t\r'

def t_error(t):
    global result_lexema, contenidor
    contenidor += "<tr> <td>"+str(t.lineno)+"</td><td>"+str(getColumn(t))+"</td>  <td>"+'lexico'+"</td>  <td>No se pudo reconocer el lexema: "+str(t.value)+"</td> </tr>\n"
    #result_lexema.append(estado)
    #print(estado)
    t.lexer.skip(1)

def getColumn(t):
    global data1,columna
    line_start = data1.rfind('\n', 0, t.lexpos) + 1
    columna=(t.lexpos-line_start)+1
    return (t.lexpos-line_start)+1

data1=""
columna=0

def prueba(data):
    global result_lexema,data1,contenido,contenidor
    
    data1 = data.lower()
    analizador = lex.lex()
    analizador.input(data.lower())
    for tok in analizador:
        estado = "Linea {:4} Tipo {:6} Valor {:16} Posicion {:4}".format(str(tok.lineno),str(tok.type),str(tok.value),str(getColumn(tok)))
        contenido += "<tr> <td>"+str(tok.lineno)+"</td><td>"+str(tok.type)+"</td>  <td>"+str(tok.value)+"</td>  <td>"+str(getColumn(tok))+"</td> </tr>\n"

    contenido += " </table>"
    contenido += "<style>"
    contenido += "table,th,td{"
    contenido += "border: 1px solid black;"
    contenido += "}"
    contenido += "    th,td{"
    contenido += " padding: 5px;"
    contenido += "}"
    contenido += "</style>"
    contenido += "</body>"
    contenido += "</html>"
    contenidor += " </table>"
    contenidor += "<style>"
    contenidor += "table,th,td{"
    contenidor += "border: 1px solid black;"
    contenidor += "}"
    contenidor += "    th,td{"
    contenidor += " padding: 5px;"
    contenidor += "}"
    contenidor += "</style>"
    contenidor += "</body>"
    contenidor += "</html>"
    contenido = str.encode(contenido)
    contenidor = str.encode(contenidor)
    reporte= os.open("reporte-tokens.html", os.O_CREAT|os.O_RDWR)
    os.write(reporte,contenido)
    os.close(reporte)
    reporter= os.open("reporte-errores.html", os.O_CREAT|os.O_RDWR)
    os.write(reporter,contenidor)
    os.close(reporter)


        #print("Linea:",str(tok.lineno), tok,"columna:",tok.lexpos,getColumn(tok))                          

analizador = lex.lex()
""" if __name__ == '__main__':
    while True:
        data = input("ingrese:").lower()
        prueba(data)
        #print(result_lexema)
        for x in result_lexema:
            print(x)
        print(len(result_lexema)) """

def lecturaArchivo(ruta):     # validacion de la extension correcta  
    global fila,colum
    nombre_archivo, extension = os.path.splitext(ruta)
    if extension == ".sc":
        archivo = open(ruta, "r")
        #print(archivo.readable())
        prueba(archivo.read())
        print(len(result_lexema))
        archivo.close()
        for x in result_lexema:
            print(x)
    else:
        print("la ruta ingresada es incorrecta")


#C:/Users/otrop/Desktop/LFP-JV-201902689-P1/pruebita.sc
