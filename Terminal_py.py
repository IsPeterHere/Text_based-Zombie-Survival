import shutil
from threading import Thread
from time import sleep
import os
  
class Terminal():

    def __init__(self):
        self.size = shutil.get_terminal_size()
        self()

        self.width = self.size.columns
        self.height = self.size.lines-2

        self.last_text = [[" " for x in range(self.size.columns)] for x in range(self.size.lines-2)]
        self.text = [[" " for x in range(self.size.columns)] for x in range(self.size.lines-2)]

        self.calling = None
        self.dependencies = []

        t = Thread(target=self.__Keeper)
        t.start()

    def __Keeper(self):
        while True:
            sleep(0.1)
            if self.calling != None:
                
                self.calling()
            
            if ["".join(x) for x in self.text] != self.last_text:
                self.last_text = []
                
                self()
                for line in self.text:
                    line_out = "".join(line)[:self.size.columns]
                    print(line_out)
                    self.last_text.append(line_out)

            for item in self.dependencies:
                self.text = item.update(self.text)
                
    def __call__(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.last_text = []

    def text_box(self,line_start,line_end,start,end, text = "", left = "", right = "",top = "", bottom = ""):
        new_text_box = Text_box(line_start,line_end,start,end,text,left,right,top,bottom)
        self.dependencies.append(new_text_box)
        
        return new_text_box



class Text_box:

    def __init__(self,line_start,line_end,start,end,text,left,right,top,bottom):
        self.line_start = line_start
        self.line_end = line_end
        self.start = start
        self.end = end
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom

        self.last_text = None
        self.text = text

    def update(self,main_text):

        if self.text != self.last_text:
            
            if self.top != "":
                for columns in range(self.start+1,self.end):
                    main_text[self.line_start-1][columns] = self.top

            if self.bottom != "":
                for columns in range(self.start+1,self.end):
                    main_text[self.line_end+1][columns] = self.bottom

            if self.left != "":
                for line in range(self.line_start,self.line_end+1):
                    main_text[line][self.start] = self.left

            if self.right != "":
                for line in range(self.line_start,self.line_end+1):
                    main_text[line][self.end] = self.right


            count = 0
            for line in range(self.line_start,self.line_end+1):
                g = True
                for index in range(self.start+1,self.end):
                    if g:
                    
                        if count < len(self.text):
                            if self.text[count] == "|":
                                g = False
                                main_text[line][index] = " "
                                count += 1
                            else:
                                main_text[line][index] = self.text[count]
                                count += 1
                        else:
                            main_text[line][index] = " "
                            count += 1

                    else:
                        main_text[line][index] = " "
                        
            self.last_text = self.text

        return main_text
    
