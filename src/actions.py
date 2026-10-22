class Actions():
    def print_func(self,f:list):
        print_size = 8
        for line in f:
            if line.startswith("PRINT:"):
                n = list(line)
                
                print("".join(n[print_size:len(n)-2]))
        
