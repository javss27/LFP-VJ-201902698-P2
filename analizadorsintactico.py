import os
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
    declaracion : STRING ID IGUAL CADENA PUNTOCOMA
        | INT ID IGUAL ENTERO PUNTOCOMA
        | CHAR ID IGUAL CARACTER PUNTOCOMA
        | DOUBLE ID IGUAL DECIMAL PUNTOCOMA
        | BOOLEAN ID IGUAL ID PUNTOCOMA
        | ID IGUAL identificador PUNTOCOMA
        | VOID ID PARIZQ parametros PARDER 
    '''
    
    print("init",len(p),p[0],p[1],p[5])

    if p[5]==";":
        print('alguna declaracion ',p[4])
        resultado_grmatica.append(p[4])
        
    elif p[4]==")":
        print("por ahora es void -->",p[1])
        resultado_grmatica.append(p[1])#podria ser para agregar al ast
        p[0]=p[4]
#p[0] = {"nodo":"operacion", "linea": p.lexer.lineno, "columna": getColumn(p.lexer), "valor": p[1]}
def p_identificador(p):
    '''
    identificador : DECIMAL
        | CARACTER 
        | ID 
        | CADENA 
    '''
def p_parametros(p):
    '''
    parametros : STRING ID 
        | STRING ID COMA
        | INT ID
        | INT ID COMA parametros
        | DOUBLE ID
        | DOUBLE ID COMA parametros
        | CHAR ID
        | CHAR ID COMA parametros
    '''
    print("parametros",len(p))
    if len(p)== 3:
        print("un parametro")
    if len(p) == 4:
        print("recursividad")
        p[0]=p[3]
    #hacer validacion si viene mas de un parametro

""" def p_logica(p):
    '''
    logica : IGUALACION 
        | DIFERENCIACION
        | MAYOR
        | MENOR
        | MAYORIGUAL
        | MENORIGUAL
        | AND
        | OR 
        | NOT
    ''' """
#| VOID ID PARIZQ parametros PARDER LLAVEIZQ instrucciones LLAVEDER 
""" print("etamos en la declaracion",len(p))
if len(p)==5:
    print('aber la p',p[1]) """




""" 



def p_instruccion(p):
    '''
    instruccion : validacion
    '''

def p_if(p):
    '''
    if : PARIZQ instruccion PARDER LLAVEIZQ instruccion LLAVEDER 
    '''
def p_else(p):
    '''
    else : LLAVEIZQ instruccion LLAVEDER
    '''

def p_dowhile(p):
    '''
    do : LLAVEIZQ instruccion LLAVEDER WHILE PARIZQ validacion PARDERECHO PUNTOCOMA 
    ''' """


    
    
def p_error(p):
    print("error sintactico xd:",p)

parser = yacc.yacc()

def prueba_sintactico(data):
    global resultado_grmatica
    resultado_grmatica.clear()
    
    ast = parser.parse(data, analizador)
    import json
    print("el yison",json.dumps(ast, indent=4, sort_keys=False))

""" if __name__ =='__main__':
    while True:
        try:
            s = input('ingresar:')
        except EOFError:
            continue
        if not s: continue
        preuba_sintactico(s) """

def lecturaArchivo(ruta):     # validacion de la extension correcta  
    global fila,colum
    nombre_archivo, extension = os.path.splitext(ruta)
    if extension == ".sc":
        archivo = open(ruta, "r")

        prueba_sintactico(archivo.read())
        print(len(resultado_grmatica))
        archivo.close()
        
        for x in resultado_grmatica:
            print(x)
    else:
        print("la ruta ingresada es incorrecta")

def menu():
    fin = True
    while fin:
        print("\n1. Cargar Archivo    \n2. Reporte Tokens \n3. Reporte AST \n4. Reporte Errores \n5. Salir \n")
        opc = input("Ingrese el número de la opción: ")
        if opc == "1":
            print("Ingrese la ruta del archivo")
            ruta = input() 
            #lecturaArchivo(ruta)
        elif opc =="2":
            print("Generando reporte de tokens")
        elif opc =="3":
            print("Generando reporte de AST")
        elif opc =="4":
            print("Generando reporte de Errores")
        elif opc =="5":
            fin = False

lecturaArchivo("C:/Users/otrop/Desktop/LFP-JV-201902689-P2/prueba2.sc")     