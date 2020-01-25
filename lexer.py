#list of tokens:
#datatypes,digits,strings,brackets,assignment,symbols



# command line based test cases   NOT INCLUDED



import ply.lex as lex

tokens=[

    'EQUALSEQUALS',
    'PLUS',
    'MINUS',
    'MULTIPLY',
    'DIVIDE',
    'MODULUS',
    'EQUALS',
    'LPAREN',
    'RPAREN',
    'AND',
    'OR',
    'NOT',
    'NOTEQUALS',
    'GREATERTHAN',
    'LESSTHAN',
    'GREATEREQUALS',
    'LESSEQUALS',
    'TRUE',
    'FALSE',
    'COMMA',
    'STRING',
    'FLOAT',
    'INT',
    'CHAR',
    'BOOL',
    'HEADER',
    'NEWLINE',
    'ID',
    'PLUSPLUS',
    'MINUSMINUS',
    'UNSTABLE',
    'DOT',
    'AT',
    'LSQUARE',
    'RSQUARE',
    'POP',
    'APPEND',
    'RESERVE',






]

reserved={
    'If' : 'If',
    'Else' : 'Else',
    'Print' : 'Print',
    'Slice' : 'Slice',
    'For'   : 'For',
    'Born'  : 'Born',
    'Summon': 'Summon',
    'Db' : 'Db',
    'Obj': 'Obj',
    'Value' : 'Value'



}
tokens +=reserved.values()
states=(
    ('INLINECOMMENT','exclusive'),
    ('SPANINGCOMMENT','exclusive'),
)
def t_INLINECOMMENT(t):
    r'\$\$'
    t.lexer.begin('INLINECOMMENT')
def t_INLINECOMMENT_end(t):
    r'\n'
    t.lexer.begin('INITIAL')
def t_SPANINGCOMMENT(t):
    r'\$\-'
    t.lexer.begin('SPANINGCOMMENT')
def t_SPANINGCOMMENT_end(t):
    r'\-\$'
    t.lexer.begin('INITIAL')

def t_SPANINGCOMMENT_error(t):
    t.lexer.skip(1)
def t_INLINECOMMENT_error(t):
    t.lexer.skip(1)

t_INLINECOMMENT_ignore=r'.'
t_SPANINGCOMMENT_ignore=r'.'

t_ignore=' \t'
t_MINUSMINUS=r'\-\-'
t_PLUSPLUS=r'\+\+'
t_EQUALSEQUALS=r'\=\='
t_PLUS=r'\+'
t_MINUS=r'\-'
t_MULTIPLY=r'\*'
t_DIVIDE=r'\/'
t_MODULUS=r'\%'
t_EQUALS=r'\='
t_GREATERTHAN=r'>'
t_LESSTHAN=r'<'
t_GREATEREQUALS=r'>='
t_LESSEQUALS=r'<='
t_NOT=r'\!'
t_AND=r'&&'
t_OR=r'\|\|'
t_NOTEQUALS=r'\!\='
t_COMMA=r'\,'
r_TRUE=r'true'
r_FALSE=r'false'
r_LSQUARE=r'\['
r_RSQUARE=r'\]'


def t_RESERVE(t):
    r'[A-Z]{1}[a-z]+'
    t.type=reserved.get(t.value,'RESERVE')
    return t


def t_DOT(t):
    r'\.'
    return t
def t_APPEND(t):
    r'append'
    return t

def t_LPAREN(t):
    r'\('
    return t
def t_RPAREN(t):
    r'\)'
    return t

def t_POP(t):
    r'pop'
    return t
def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno+=len(t.value)
    t.lexer.skip(1)
def t_AT(t):
    r'\@'
    return t
def t_UNSTABLE(t):
    r'unstable'
    return t

def t_HEADER(t):
    r'^\bhailhydra\b'
    return(t)


def t_FLOAT(t):
    r'\-*\+*(\d*)(?:\.)\d+'
    t.value=float(t.value)
    return t

def t_INT(t):
    r'\-*\+*\d+'
    t.value=int(t.value)
    return t

def t_CHAR(t):
    r'\'[a-zA-Z0-9]{1}\''
    t.value=t.value[1:-1]
    return(t)

def t_BOOL(t):
    r'true|false'
    if(t.value=='true'):
        t.value=bool(t.value)
    else:
        t.value=not bool(t.value)
    return t
def t_STRING(t):
    r'"[a-z_A-Z0-9]"'
    t.value=t.value[1:-1]
    return t


def t_error(t):
    print("ILLEGAL CHARACTER",t.value[0],"@ position ",t.lexpos," on line no",t.lineno)
    t.lexer.skip(1)

def t_FOR(t):
    r'for'
    return t
def t_WHILE(t):
    r'until'
    return t
def t_DO(t):
    r'do'
    return t



def t_RETURN(t):
    r'send'
    return t
def t_ID(t):
    r'[a-z_A-Z]+([0-9]*?)'
    return t
'''
lexer=lex.lex()
input=input('')
lexer.input(input)
for tok in (lexer):
    print(tok)
'''



