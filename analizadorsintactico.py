import os
import ply.yacc as yacc
import graphviz as graph
import analizadorlexico as an
from analizadorlexico import tokens


resultado_grmatica = []
#graph_attr={'ordering':"in"}
AST = graph.Digraph()

precedence = (
    ('left','IGUALACION','DIFERENCIACION'),
    ('left','MENORQUE','MAYORQUE','MAYORIGUAL','MENORIGUAL','IGUAL'),
    ('left','SUMA','RESTA'),
    ('left','MULT','DIV','MOD'),
    ('right','NOT')

)

def p_declaracion(p):
    '''
    declaracion : VOID ID PARIZQ parametros PARDER LLAVEIZQ instrucciones LLAVEDER
        | INT ID IGUAL ENTERO PUNTOCOMA
        | CHAR ID IGUAL CARACTER PUNTOCOMA
        | DOUBLE ID IGUAL DECIMAL PUNTOCOMA
        | BOOLEAN ID IGUAL ID PUNTOCOMA
        | ID IGUAL identificador PUNTOCOMA
        | STRING ID IGUAL CADENA PUNTOCOMA
    '''

    print("init",len(p),p[0],p[1],p[5])
    print(str(p.lexer.lineno))
    id_padre = str(p.lexer.lineno)+str(p.lexpos)+'declaracion'
    AST.node(id_padre,'declaracion')

    if p[5]==";":

        AST.node(str(p.lexer.lineno)+str(p.lexpos)+p[1],"TIPO DE DATO\n"+p[1])
        AST.node(str(p.lexer.lineno)+str(p.lexpos)+p[2],"ID\n"+p[2])
        AST.node(str(p.lexer.lineno)+str(p.lexpos)+p[3],"DATO\n"+p[3])
        AST.edge(id_padre,str(p.lexer.lineno)+str(p.lexpos)+p[1])
        AST.edge(id_padre,str(p.lexer.lineno)+str(p.lexpos)+p[2])
        AST.edge(id_padre,str(p.lexer.lineno)+str(p.lexpos)+p[3])
        
    elif p[5]==")":

        AST.node(str(p.lexer.lineno)+str(p.lexpos)+p[1],p[1])
        AST.node(str(p.lexer.lineno)+str(p.lexpos)+p[2],"ID\n"+p[2])
        nodo_hijo3 = resultado_grmatica.pop()
        AST.edge(id_padre,str(p.lexer.lineno)+str(p.lexpos)+p[1])
        AST.edge(id_padre,str(p.lexer.lineno)+str(p.lexpos)+p[2])
        AST.edge(id_padre,nodo_hijo3)
        print("por ahora es void -->",p[1])

        p[0]=p[4]
    
    else:
        AST.node(str(p.lexer.lineno)+str(p.lexpos)+p[1],"ID\n"+p[1])
        nodo_hijo2 = resultado_grmatica.pop()
        AST.edge(id_padre,str(p.lexer.lineno)+str(p.lexpos)+p[1])
        AST.edge(id_padre,nodo_hijo2)

        p[0] = p[3]

    resultado_grmatica.append(id_padre)
#p[0] = {"nodo":"operacion", "linea": p.lexer.lineno, "columna": getColumn(p.lexer), "valor": p[1]}

def p_identificador(p):
    '''
    identificador : DECIMAL
        | CARACTER 
        | ID 
        | CADENA
    '''
    global AST

    id_padre = str(p.lexer.lineno)+str(p.lexpos)+'identificador'
    AST.node(id_padre,'identificador')

    AST.node(str(p.lexer.lineno)+str(p.lexpos)+p[1],p[1])
    AST.edge(id_padre,str(p.lexer.lineno)+str(p.lexpos)+p[1])

    resultado_grmatica.append(id_padre)

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
    global AST

    id_padre = str(p.lexer.lineno)+str(p.lexpos)+'parametros'
    AST.node(id_padre,'parametros')

    print("parametros",len(p))
    if len(p)<= 4:
        AST.node(str(p.lexer.lineno)+str(p.lexpos)+p[1],"TIPO DE DATO\n"+p[1])
        AST.node(str(p.lexer.lineno)+str(p.lexpos)+p[2],"ID\n"+p[2])
        AST.edge(id_padre,str(p.lexer.lineno)+str(p.lexpos)+p[1])
        AST.edge(id_padre,str(p.lexer.lineno)+str(p.lexpos)+p[2])
    else:
        AST.node(str(p.lexer.lineno)+str(p.lexpos)+p[1],"TIPO DE DATO\n"+p[1])
        AST.node(str(p.lexer.lineno)+str(p.lexpos)+p[2],"ID\n"+p[2])
        nodo_hijo3 = resultado_grmatica.pop()
        AST.edge(id_padre,str(p.lexer.lineno)+str(p.lexpos)+p[1])
        AST.edge(id_padre,str(p.lexer.lineno)+str(p.lexpos)+p[2])
        AST.edge(id_padre,nodo_hijo3)
        print("recursividad")
        p[0]=p[4]

    resultado_grmatica.append(id_padre)
    #hacer validacion si viene mas de un parametro

def p_llamada(p):
    '''
    llamada : ID PARDER argumentos PARIZQ
    '''
    global AST

    id_padre = str(p.lexer.lineno)+str(p.lexpos)+'llamada'
    AST.node(id_padre,'llamada')
    AST.node(str(p.lexer.lineno)+str(p.lexpos)+p[1],"ID\n"+p[1])
    hijo2 = resultado_grmatica.pop()
    AST.edge(id_padre,str(p.lexer.lineno)+str(p.lexpos)+p[1])
    AST.edge(id_padre,hijo2)

    resultado_grmatica.append(id_padre)

def p_retorno(p):
    '''
    retorno : RETURN PUNTOCOMA
            | RETURN identificador PUNTOCOMA
    '''
    global AST

    id_padre = str(p.lexer.lineno)+str(p.lexpos)+'retorno'
    AST.node(id_padre,'retorno')

    if len(p) = 4:
        hijo1 = resultado_grmatica.pop()
        AST.edge(id_padre,str(p.lexer.lineno)+str(p.lexpos)+p[1])
        p[0] = p[2]

    resultado_grmatica.append(id_padre)
    
def p_argumentos(p):
    '''
    argumentos : ID 
               | ID COMA argumentos
    '''

    global AST

    id_padre = str(p.lexer.lineno)+str(p.lexpos)+'argumentos'
    AST.node(id_padre,'argumentos')

    if len(p)== 1:
        AST.node(str(p.lexer.lineno)+str(p.lexpos)+p[1],"ID\n"+p[1])
        AST.edge(id_padre,str(p.lexer.lineno)+str(p.lexpos)+p[1])
    else:
        AST.node(str(p.lexer.lineno)+str(p.lexpos)+p[1],"ID\n"+p[1])
        nodo_hijo2 = resultado_grmatica.pop()
        AST.edge(id_padre,str(p.lexer.lineno)+str(p.lexpos)+p[1])
        AST.edge(id_padre,nodo_hijo3)
        print("recursividad")
        p[0]=p[3]

    resultado_grmatica.append(id_padre)

def p_logica(p):
    '''
    logica : operacion IGUALACION logica
        | operacion DIFERENCIACION logica
        | operacion MAYOR logica
        | operacion MENOR logica
        | operacion MAYORIGUAL logica
        | operacion MENORIGUAL logica
        | operacion AND logica
        | operacion OR logica
        | identificador
        | operacion

    '''
    global AST

    id_padre = str(p.lexer.lineno)+str(p.lexpos)+'logica'
    AST.node(id_padre,'logica')
    

    if len(p) == 4:
        AST.node(str(p.lexer.lineno)+str(p.lexpos)+p[2],"SIMBOLO\n"+p[2])
        hijo3 = resultado_grmatica.pop()
        hijo1 = resultado_grmatica.pop()
        AST.edge(id_padre,str(p.lexer.lineno)+str(p.lexpos)+p[2])
        AST.edge(id_padre,hijo3)
        AST.edge(id_padre,hijo1)
        p[0] = [p[1],p[3]]
    else:
        hijo1 = resultado_grmatica.pop()
        AST.edge(id_padre,hijo1)
        p[0] = p[1]

    resultado_grmatica.append(id_padre)

def p_operacion(p):
    '''
    operacion : identificador SUMA operacion
        | identificador RESTA operacion
        | identificador MULT operacion
        | identificador DIV operacion
        | identificador MOD operacion
        | identificador
    '''
    global AST

    id_padre = str(p.lexer.lineno)+str(p.lexpos)+'operacion'
    AST.node(id_padre,'operacion')

    if len(p) == 4:
        AST.node(str(p.lexer.lineno)+str(p.lexpos)+p[2],"SIMBOLO\n"+p[2])
        hijo3 = resultado_grmatica.pop()
        hijo1 = resultado_grmatica.pop()
        AST.edge(id_padre,str(p.lexer.lineno)+str(p.lexpos)+p[2])
        AST.edge(id_padre,hijo3)
        AST.edge(id_padre,hijo1)
        p[0] = [p[1],p[3]]
    else:
        hijo1 = resultado_grmatica.pop()
        AST.edge(id_padre,hijo1)
        p[0] = p[1]

    resultado_grmatica.append(id_padre)
def p_instrucciones(p):
    '''
    instrucciones : instruccion instrucciones
                  | instruccion
    '''
    global AST
    id_padre = str(p.lexer.lineno)+str(p.lexpos)+'instrucciones'
    AST.node(id_padre,'instrucciones')
    if len(p) == 3:
        hijo1 = resultado_grmatica.pop()
        hijo2 = resultado_grmatica.pop()
        AST.edge(id_padre,hijo1)
        AST.edge(id_padre,hijo2)
    else:
        hijo1 = resultado_grmatica.pop()
        AST.edge(id_padre,hijo1)
    resultado_grmatica.append(id_padre)
    
def p_instruccion(p):
    '''
    instruccion : declaracion 
                | if
                | dowhile
                | while
                | COMENTLINE
                | COMENTLINES
                | llamada
    '''
    global AST
    id_padre = str(p.lexer.lineno)+str(p.lexpos)+'instruccion'
    AST.node(id_padre,'instruccion')
    
    if len(resultado_grmatica) != 0:
        hijo1 = resultado_grmatica.pop()
        AST.edge(id_padre,hijo1)
    else:
        AST.node(str(p.lexer.lineno)+str(p.lexpos)+p[1],p[1])
        AST.edge(id_padre,str(p.lexer.lineno)+str(p.lexpos)+p[1])

    resultado_grmatica.append(id_padre)

def p_if(p):
    '''
    if : IF PARIZQ logica PARDER LLAVEIZQ instrucciones LLAVEDER 
       | if ELSE LLAVEIZQ instrucciones LLAVEDER
    '''
    global AST

    id_padre = str(p.lexer.lineno)+str(p.lexpos)+'if'
    AST.node(id_padre,'if')

    if len(p) == 8:
        AST.node(str(p.lexer.lineno)+str(p.lexpos)+p[1],"CONDICIONAL\n"+p[1])
        hijo3 = resultado_grmatica.pop()
        hijo2 = resultado_grmatica.pop()
        AST.edge(id_padre,hijo3)
        AST.edge(id_padre,hijo2)
        AST.edge(id_padre,str(p.lexer.lineno)+str(p.lexpos)+p[1])
        p[0] = [p[3],p[6]]
    else:
        AST.node(str(p.lexer.lineno)+str(p.lexpos)+p[2],"CONDICIONAL\n"+p[2])
        hijo3 = resultado_grmatica.pop()
        hijo1 = resultado_grmatica.pop()
        AST.edge(id_padre,hijo3)
        AST.edge(id_padre,hijo1)
        AST.edge(id_padre,str(p.lexer.lineno)+str(p.lexpos)+p[2])

    resultado_grmatica.append(id_padre)

def p_dowhile(p):
    '''
    dowhile : DO LLAVEIZQ instrucciones LLAVEDER WHILE PARIZQ logica PARDER PUNTOCOMA 
    ''' 
    global AST

    id_padre = str(p.lexer.lineno)+str(p.lexpos)+'dowhile'
    AST.node(id_padre,'dowhile')
    AST.node(str(p.lexer.lineno)+str(p.lexpos)+p[1],"BUCLE\n"+p[1])
    hijo3 = resultado_grmatica.pop()
    hijo2 = resultado_grmatica.pop()
    AST.edge(id_padre,hijo3)
    AST.edge(id_padre,hijo2)
    AST.edge(id_padre,str(p.lexer.lineno)+str(p.lexpos)+p[1])

    resultado_grmatica.append(id_padre)
    p[0] = [p[3],p[7]]

def p_while(p):
    '''
    while : WHILE PARIZQ logica PARDER LLAVEIZQ instrucciones LLAVEDER 
    ''' 
    global AST

    id_padre = str(p.lexer.lineno)+str(p.lexpos)+'while'
    AST.node(id_padre,'while')
    AST.node(str(p.lexer.lineno)+str(p.lexpos)+p[1],"BUCLE\n"+p[1])
    hijo3 = resultado_grmatica.pop()
    hijo2 = resultado_grmatica.pop()
    AST.edge(id_padre,hijo3)
    AST.edge(id_padre,hijo2)
    AST.edge(id_padre,str(p.lexer.lineno)+str(p.lexpos)+p[1])

    resultado_grmatica.append(id_padre)
    p[0] = [p[3],p[6]]

def p_codigo(p):
    '''
    codigo : instrucciones codigo
           | instrucciones
    '''
    global AST
    print(resultado_grmatica)
    id_padre = str(p.lexer.lineno)+str(p.lexpos)+'codigo'
    AST.node(id_padre,'codigo')

    if len(p) == 3:
        p[0] = [p[1],p[2]]
        hijo2 = resultado_grmatica.pop()
        hijo1 = resultado_grmatica.pop()
        AST.edge(id_padre,hijo1)
        AST.edge(id_padre,hijo2)
        
    else:
        hijo1=resultado_grmatica.pop()
        AST.edge(id_padre,hijo1)
        p[0] = p[1]

    resultado_grmatica.append(id_padre)

Error_sintactico = False 
    
def p_error(p):
    global Error_sintactico
    Error_sintactico == True
    print("error sintactico xd:",p)
    


parser = yacc.yacc(start='codigo')

def prueba_sintactico(data):
    global resultado_grmatica, Error_sintactico
    resultado_grmatica.clear()
    ast = parser.parse(data.lower(), an.analizador)
    s = graph.Source(AST.source, filename="r-ast", format="pdf")
    if Error_sintactico:
        print('HA OCURRIDO UN ERROR SINTACTICO, IGUALMENTE SE MOSTRARA EL AST, PERO CONTENDRA ERRORES')
    s.view()

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
        archivo = open(ruta, encoding="utf8").read()
        prueba_sintactico(archivo)

def menu():
    fin = True
    while fin:
        print("\n1. Cargar Archivo    \n2. Salir \n")
        opc = input("Ingrese el número de la opción: ")
        if opc == "1":
            ruta = input("Ingrese la ruta del archivo:")
            
            lecturaArchivo(ruta)
            an.lecturaArchivo(ruta)
            
        elif opc =="3":
            fin = False

menu()  
