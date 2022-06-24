import ply.lex as lex
result_lexema=[]
reservada = {
    'STRING',
    'INT',
    'DOUBLE',
    'CHAR',
    'BOOLEAN',
    'VOID'
    'RETURN'
}

tokens = reservada + {
    'ID',
    'ENTERO',
    'DECIMAL',
    
    
    #operaciones
    'SUMA',
    'RESTA',
    'MULTIPLICACION',
    'DIVISION',
    'MODULO',
    
    #LOGICA
    'IGUALACION',
    'DIFERENCIACION',
    'MAYOR',
    'MENOR',
    'MAYORIGUAL',
    'MENORIGUAL',
    'AND',
    'OR',
    'NOT'

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

    'PUNTO'
    'PUNTOCOMA',
    'COMA',
    'COMILLA',
    'COMDOBLE'
}

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

t_PUNTOCOMA = r';'
t_PUNTO = r'.'
t_COMA = r','
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


