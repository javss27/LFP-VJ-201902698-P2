import ply.yacc as yacc
from analizadorlexico import tokens
from analizadorlexico import analizador

resultado_grmatica = []

precedence = (
    ('left','IGUALACION','DIFERENCIACION')
    ('left','MENORQUE','MAYORQUE','MAYORIGUAL','MENORIGUAL','IGUAL')
    ('left','SUMA','RESTA'),
    ('left','MULT','DIV','MOD')
    ('right','NOT')

)

def p_declaracion(t):
    'declaracion : '