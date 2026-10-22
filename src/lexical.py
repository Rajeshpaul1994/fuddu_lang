import logging

class Lexical_analysis():
    def __init__(self): # constractor
        self.EXPECTED_START = 'SRK:\n'
        self.EXPECTED_END = ':SRK\n'
        self.msg = ''
    def remove_new_line(self, file:list)->list:
        while '\n' in file:
            file.remove('\n')
        return file
        
    def check_open_close(self, start:str, close:str)-> bool: # instance method
        if start == self.EXPECTED_START and close == self.EXPECTED_END:
            self.msg = 'verified successfully'
            logging.info(self.msg)
            return True
        elif start != self.EXPECTED_START or close != self.EXPECTED_END:
            self.msg = 'syntax Error: starting not ending not matched.'
            logging.error(self.msg)
            return False
        return False
