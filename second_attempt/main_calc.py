from scanner import *
from sys import argv
from calculator import *


class main():
    
    
    def print_as_lines(self):
        for line_index in range(1, self.scan.line + 1):
            result = ""
            for token in self.scan.token_array:
                if token.line == line_index:
                    result += token.__str__()
                    result += " "
            print("line ", line_index, ": ", result)
    
    def get_file_as_array_of_lines(self, filepath):
        '''opens the file and reads the lines of it'''
        
        
        with open(filepath, "r", newline="\n") as file:
            
            text = list(file.readlines())
            
            # removes the "\n" newline character from the end of each entry in the array of lines
            text = [line.strip("\n") for line in text]
        return text
    
    def scan_from_file(self, filepath):
        '''reads the file from the filepath specified in the fucntion'''
        
        #reads the file form the filepath into an appropriate format
        text = self.get_file_as_array_of_lines(filepath)
        
        # iterates throught each line and adds the tokens from that to the array of tokens
        for i in range(len(text)):
            # updates the position to zero for the start of the new line
            self.scan.position = 0
            
            # updates the line number as well
            self.scan.line += 1
            
            # if this is the last line in the file then the EOF token is added to the end of the array
            if i == len(text) - 1:
                self.scan.is_last_line = True
            
            # renews what line we are reading from
            line = text[i]
            
            # runs the main function of scan, which scans from the file and produces an array of tokens
            self.scan.main(line)
            
        # prints out the token array
        self.print_as_lines()
        print("there are ", self.scan.line, "lines in this file")
    
    def main(self):
        # initialises a new scanner object
        self.scan = scanner()
        
        
        if len(argv) == 1:
            print("no file given")
            exit()
        elif len(argv) == 2:
            self.scan_from_file(str(argv[1]))
        self.calc_parser = cal_parser(self.scan.token_array)
        self.calc_parser.main()

program = main()
program.main()