import sys
from src.lexical import Lexical_analysis
from src.actions import Actions
FILE = sys.argv[1]

with open(FILE,'r') as file:
    f = file.readlines()
    lex = Lexical_analysis()
    clean_code = lex.remove_new_line(f)
    
    if lex.check_open_close(clean_code[0], clean_code[-1]):
        a = Actions()
        a.print_func(clean_code[1:len(clean_code)-1])
