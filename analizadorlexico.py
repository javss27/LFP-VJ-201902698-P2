import ply.lex as lex
result_lexema=[]
reservada = (
    'STRING',
    'INT',
    'DOUBLE',
    'CHAR',
    'BOOLEAN',
    'VOID'
    'RETURN'
)

tokens = reservada + (
    'ID',
    'DECIMAL',
    'ENTERO',
    
    
    
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

    #CILCOS
    'WHILE',
    'DO',

    #condiciones
    'IF',
    'ELSE',

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
    'COMDOBLE',

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

#expreciones regulares para los tipos de datos
def t_ID(t):
    r'[a-z*|_][_\w]+'
    return t

def t_ENTERO(t):
    r'\d+'
    return t

def t_DECIMAL(t):#hay quever si se corrigue por lo de algun simbolo al final
    r'\-?\d*\.\d+'
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

#COMENTARIOS
def t_COMENTLINE(t):
    r'\/\/(.)*\n'
    t.lexer.lineno +=1

t_ignore= ' \t'

def t_error(t):
    global result_lexema
    estado = "Toke no valido en la linea {:4} Valor {:6}".format(str(t.lineno),str(t.value),str(t.lexpos))
    result_lexema.append(estado)
    t.lexer.skip(1)


def prueba(data):
    global result_lexema

    analizador = lex.lex()
    analizador.input(data)

    result_lexema.clear()
    while True:
        tok = analizador.token()
        if not tok:
            break
        estado = "Linea {:4} Tipo {:6} Valor {:16} Posicion {:4}".format(str(tok.lineno),str(tok.type),str(tok.value),str(tok.lexpos))
        result_lexema.append(estado)
    return result_lexema                            

analizado = lex.lex()
if __name__ == '__main__':
    while True:
        data = input("ingrese:").lower()
        prueba(data)
        print(result_lexema)
        print(len(result_lexema))