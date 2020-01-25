import numpy as np
import ply.lex as lex
import lexer
import ply.yacc as yacc

from lexer import tokens

precedence=(
    ('left','AND','OR'),
    ('left','GREATERTHAN','LESSTHAN','GREATEREQUALS','LESSEQUALS'),
    ('left','PLUS','MINUS'),
    ('left','MULTIPLY','DIVIDE','MODULUS'),



)
start="statements"






def p_single(p):
    '''
    statements : statement


    '''
    print(run(p[1]))
def p_statement(p):
    '''
    statement : UNSTABLE ID EQUALS expr


    '''
    p[0]=('=',p[2],p[4])
def p_print(p):
    '''
    statement : Print LPAREN statement RPAREN


    '''
    p[0]=('display',p[3])
def p_factors(p):
    '''
    expr : LPAREN expr RPAREN


    '''

    p[0]=p[2]
def p_empty(p):
    'empty :'
    pass

def p_state_empty(p):
    'statements : empty'
    pass

def p_lists(p):
    '''
    statement : ID INT EQUALS entries

    '''
    p[0]=('array',p[1],p[4],p[2])

def p_entries(p):
    '''
   entries : entries entry
           | entry



    '''
    if len(p)==2:
        p[0]=p[1]

    else:
     p[0]= p[1] + p[2]


def p_entry(p):
    '''
    entry : INT
          | FLOAT
          | STRING
          | CHAR
    '''
    p[0]=[p[1]]

def p_binary_opr(p):
    '''
    expr : expr PLUS expr
         | expr MINUS expr
         | expr MULTIPLY expr
         | expr DIVIDE expr
         | expr MODULUS expr
         | expr EQUALSEQUALS expr
         | expr GREATERTHAN expr
         | expr LESSTHAN expr
         | expr AND expr
         | expr OR expr
         | expr NOTEQUALS expr
         | expr GREATEREQUALS expr
         | expr LESSEQUALS expr


    '''
    p[0]=(p[2],p[1],p[3])

def p_unary_opr(p):
    '''
    expr : expr PLUSPLUS
         | expr MINUSMINUS

    '''
    p[0]=(p[2],p[1])

def p_expr_ID(p):
    '''
    expr : ID

    '''

def p_funborn(p):
    '''
    statement : Born ID LPAREN RPAREN statement

    '''
    p[0]= ('born',p[2],p[5])

def p_summon(p):
    '''
    statement : Summon ID LPAREN RPAREN

    '''
    p[0]=('summon',p[2])


def p_born_Db(p):
    '''
    statement : Born Db ID statement

    '''
    p[0]=('born-db',p[3],p[4])
def p_obj(p):
    '''
    statement : ID ID LPAREN Obj RPAREN

    '''
    p[0]=('obj',p[1],p[2])

def p_val(p):
    '''
    statement : ID DOT Value

    '''
    p[0]=('val',p[1])
def p_num(p):
    '''
    expr : INT
         | FLOAT
         | STRING
         | CHAR
         | BOOL
    '''
    p[0]=('number',p[1])

def p_exp(p):
    'statement : expr'
    p[0]=p[1]


def p_mutable(p):
    '''
    statement : ID EQUALS expr


    '''
    p[0]=('var',p[1],p[3])

def p_access_arr(p):
    '''
    expr : AT ID INT

    '''
    p[0]=('get_aval',p[2],p[3])

def p_get_value(p):
    '''
    expr : AT ID

    '''
    p[0]=('get',p[2])

def p_arr_pop(p):
    '''
    expr : ID DOT POP

    '''
    p[0]=('pop',p[1])

def p_conditionals(p):
    '''
    statement : If expr statement Else statement

    '''
    p[0]=('if-else',p[2],p[3],p[5])

def for_loop(p):
    '''
    expr : For expr

    '''
    print(p[1])

def p_number(p):
    '''
    number : INT
           | FLOAT
           | STRING
           | CHAR
           | BOOL

    '''
    p[0]=p[1]
def p_arr_append(p):
    '''
    expr : ID DOT APPEND number

    '''
    p[0]=('append',p[1],p[4])

def p_slice(p):
    '''
    expr : ID Slice INT INT

    '''
    p[0]=('slice',p[1],p[3],p[4])



def p_error(p):
    print("SYNTAX ERROR ON LINENO",p.lineno)

dic={}
arr_dic={}
fun_dic={}
db_dic={}
obj_dic={}
def run(p):
    if type(p) == tuple:
        #get number
        if p[0]=='number':
            return p[1]
        #get value
        elif p[0]=='get':
            key =p[1]
            if key in dic.keys():
                return dic[key]
            else:
                print("NO VALUE ASSIGNED TO VARIABLE <<",key,'>>')
                return


        ##assigment
        elif p[0]=='=':
            key =p[1]
            if key in dic.keys():
                print('ERROR!! REDECLARATION OF VARIABLE <<',p[1],'>>')
                return
            if key in arr_dic.keys():
                print('ERROR!! REDECLARATION OF VARIABLE <<', p[1], '>>')
                return
            else:
                dic[p[1]]=run(p[2])
                return dic[p[1]]
        elif p[0]=='var':
            key =p[1]
            if key in dic.keys():
                dic[p[1]]=run(p[2])
                return dic[p[1]]
            else:
                print("ERROR!!  VARIABLE NOT DECLARED YET <<",'p[1]','>>')
                return

        #binary ops
        elif p[0]=='+':
            return run(p[1]) + run(p[2])

        elif p[0]=='-':
            return run(p[1]) - run(p[2])

        elif p[0] == '*':
            return run(p[1]) * run(p[2])

        elif p[0] == '/':
            return run(p[1]) / run(p[2])

        elif p[0]=='%':
            return run(p[1]) % run(p[2])
        elif p[0]=='&&':
            return run(p[1]) & run(p[2])
        elif p[0]=='||':
            return run(p[1]) | run(p[2])
        elif p[0]=='==':
            return run(p[1]) == run(p[2])
        elif p[0]=='>':
            return run(p[1]) > run(p[2])
        elif p[0]=='<':
            return run(p[1]) < run(p[2])
        elif p[0]=='!=':
            return run(p[1]) != run(p[2])
        elif p[0]=='>=':
            return run(p[1]) >= run(p[2])
        elif p[0]=='<=':
            return run(p[1]) <= run(p[2])


        #unary ops
        elif p[0]=='display':
            return run(p[1])
        elif p[0]=='++':
            a =run(p[1])
            a+=1
            return a
        elif p[0]=='--':
            a = run(p[1])
            a -= 1
            return a

        #arrays
        elif p[0]=='array':
            key = p[1]
            arr=p[2]
            if key in arr_dic.keys():
                print("ERROR !! REDECLARATION OF ARRAY VARIABLE <<",p[1],">>")
                return
            elif key in dic.keys():
                print("ERROR !! REDECLARATION OF ARRAY VARIABLE <<", p[1], ">>")
                return

            elif len(arr)> p[3]:
                print("INDEX OUT OF RANGE ")
                return
            else:
                arr_dic[key]=arr
                return

        elif p[0]=='get_aval':
            key =p[1]

            if key not in arr_dic.keys():
                print("ERROR !! VARIABLE NOT DECLARED YET <<",p[1],">>")
            elif p[2]>=len(arr_dic[key]):
                print("ERROR !! INDEX OUT OF RANGE ")
            else:
                arr=(arr_dic[key])
                return arr[p[2]]

        elif p[0]=='pop':
            key =p[1]
            if key in arr_dic.keys():
                arr=arr_dic[key]

                arr.pop()
                return
        elif p[0]=='append':
            key =p[1]
            if key in arr_dic.keys():
                arr=arr_dic[key]
                arr.append(p[2])
                print(arr)
                return
            else:
                print('ARRAY NOT DECLARED YET <<',key,'>>')
                return
        elif p[0]== 'slice':

            key = p[1]
            if key in arr_dic.keys():
                arr=arr_dic[key]
                in1=p[2]
                in2=p[3]
                if in1 >= len(arr) | in2>= len(arr) | in1< 0 | in1 > in2 :
                    print("ERROR IN SPLICING INDEX ")
                    return
                sObject=slice(in1,in2)
                print (arr[sObject])
            else:
                print('ARRAY NOT DECLARED YET <<', key, '>>')
                return
        #IF-ELse
        elif p[0]=='if-else':
            a=run(p[1])

            if(a):
                return run(p[2])
            else:
                return run(p[3])
            #for loop
        elif p[0]=='born':
            if p[1] in fun_dic.keys():
                print("ERROR REDECLARATION ")
                return
            else:
                fun_dic[p[1]]=p[2]
            return

        elif p[0]=='summon':
            key =p[1]
            if key not in fun_dic.keys():
                print("Error NOT A VALID FUNC CALL  !")
                return
            else:
                return run(fun_dic[p[1]])
        elif p[0]=='born-db':
            print(p[2])
            db_dic[p[1]]=p[2]
            return

        elif p[0]=='obj':
            print(p[2],p[1])
            obj_dic[p[2]]=db_dic[p[1]]
            return
        elif p[0]=='val':
            a=run(obj_dic[p[1]])
            return a



















    else:
        return p



l=lex.lex(module=lexer)
parser=yacc.yacc()

while True:
    try:
        s=input('<<)(>> \n')
    except EOFError:
        break
    res=parser.parse(s)




