from tkinter import *
from tkinter import filedialog
from extract_tables import process_file
from extract_tables import process_dir
import os
import sys

class Root(Tk):
    def __init__(self):
        super(Root,self).__init__()

        self.title('Extract tables from PDF')
        self.minsize(300,300)

        #file path variables
        self.dir = StringVar()
        self.filePath = StringVar()

        #create mex button
        self.dirButton = Button(self, text='Select directory', command=self.dirButton_click)
        self.dirButton.pack(pady=10)

        #create bpcs button
        self.fileButton = Button(self, text='Select file', command=self.fileButton_click)
        self.fileButton.pack(pady=10)

        #create the process button
        self.processButton = Button(self,text='Process Files',command=self.processButton_click,state=DISABLED)
        self.processButton.pack(pady=80)


    def dirButton_click(self):
        a = filedialog.askdirectory(title='Select directory')
        if a:
            self.dir.set(a)
            self.check_validity()
        #print(m)
    
    def fileButton_click(self):
        a = filedialog.askopenfilename(title='Select PDF file', filetypes=(("PDF files","*.pdf"),("All files","*.*")))
        if a:
            self.filePath.set(a)
            self.check_validity()
        #print(b)

    def processButton_click(self):
        a = self.get_file_path()
        try:
            print(a)
            if os.path.isdir(a):
                process_dir(a)
            elif os.path.isfile(a):
                process_file(a)
            
        except:
            self.processButton.config(bg='red')
        else:
            self.processButton.config(bg='green')
        

    def get_file_path(self):
        if self.dir.get():
            a = self.dir.get()
        if self.filePath.get():
            a = self.filePath.get()
        return a


    def check_validity(self):
        if self.dir.get() or self.filePath.get():
            self.processButton["state"] = NORMAL
        else:
            self.processButton["state"] = DISABLED




if __name__ == "__main__":

    if len(sys.argv) == 1:
        # no arguments passed, use the GUI.
        root = Root()
        root.mainloop()
    elif len(sys.argv) == 2:
        # cli argument passed.
        a=os.path.normpath(os.path.join(sys.argv[1]))
        
        if os.path.isdir(a):
            process_dir(a)
        elif os.path.isfile(a):
            process_file(a)
        else:
            sys.exit(1)
    else:
        sys.exit(1)
