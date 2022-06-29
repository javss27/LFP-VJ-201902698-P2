import ply.yacc as yacc
from analizadorlexico import tokens
from analizadorlexico import analizador

resultado_grmatica = []

precedence = (
    ('left','IGUALACION','DIFERENCIACION'),
    ('left','MENORQUE','MAYORQUE','MAYORIGUAL','MENORIGUAL','IGUAL'),
    ('left','SUMA','RESTA'),
    ('left','MULT','DIV','MOD'),
    ('right','NOT')

)

def p_declaracion(p):
    '''
    declaracion : STRING ID IGUAL CADENA
        | CHAR ID IGUAL CARACTER
        | INT ID IGUAL ENTERO
        | DOUBLE ID IGUAL DECIMAL
        | BOOLEAN ID IGUAL ID
    '''
    print("etamos en la declaracion",len(p))
    if len(p)==5:
        print('aber la p',p[1])
def p_instruccion(p):

def p_if(p):

def p_else(p):
    
def p_dowhile(p):


    
    
def p_error(p):
    print("error sintactico xd:",p)

parser = yacc.yacc()

def preuba_sintactico(data):
    global resultado_grmatica
    resultado_grmatica.clear()
    ast = parser.parse(data, analizador)
    import json
    print("el yiso",json.dumps(ast, indent=4, sort_keys=False))

if __name__ =='__main__':
    while True:
        try:
            s = input('ingresar:')
        except EOFError:
            continue
        if not s: continue
        preuba_sintactico(s)

    
    
     