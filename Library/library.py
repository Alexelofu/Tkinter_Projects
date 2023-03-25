#import all dependencies
from tkinter import*
from tkinter import ttk

#create the starting class
class LibManSys:
    def __init__(self,root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")

        #creating and styling the top label
        labeltitle = Label(self.root,text ='LIBRARY MANAGEMENT SYSTEM', bg='white', fg='black', bd=20, relief=RIDGE, font=("Calibri", 50, "bold"), padx=2, pady=6)
        
        #loading the label and postioning it
        labeltitle.pack(side=TOP,fill=X)

        #creating first subframe
        frame = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        frame.place(x=0, y=130, width=1550, height=400)

        ##########################################left side second subframe##########################################
        DataFrameLeft = LabelFrame(frame, text="Library Membership Information",bg='powder blue', fg='black', bd=20, relief=RIDGE, font=("Calibri", 15, "bold"), pady=2,padx=10)
        DataFrameLeft.place(x=0, y=5, width=900,height=350)

        lblMember = Label(DataFrameLeft, bg="powder blue", text="Member Type", font=("calibri",12,"bold"),padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=W)

        #dropdown creation#
        comMember = ttk.Combobox(DataFrameLeft, font=("calibri",13,"bold"), width=32,state="readonly") 
        comMember["value"] = ("Admin Staff","Student","Lecturer")
        comMember.grid(row=0,column=1,padx=10, pady=10)

        ###text box##
        lblPRN_No = Label(DataFrameLeft, bg="powder blue", text="PRN No", font=("calibri",12,"bold"),padx=2,pady=4)
        lblPRN_No.grid(row=1,column=0,sticky=W)
        txtPRN_NO = Entry(DataFrameLeft, font=("calibri",13,"bold"), width=34,highlightbackground="grey", highlightthickness=1)
        txtPRN_NO.grid(row=1,column=1)

        lblTitle = Label(DataFrameLeft, bg="powder blue", text="ID No", font=("calibri",12,"bold"),padx=2,pady=4)
        lblTitle.grid(row=2,column=0,sticky=W)
        lblTitle = Entry(DataFrameLeft, font=("calibri",13,"bold"), width=34,highlightbackground="grey", highlightthickness=1)
        lblTitle.grid(row=2,column=1)

        lblFirstName = Label(DataFrameLeft, bg="powder blue", text="First Name", font=("calibri",12,"bold"),padx=2,pady=4)
        lblFirstName.grid(row=3,column=0,sticky=W)
        lblFirstName = Entry(DataFrameLeft, font=("calibri",13,"bold"), width=34,highlightbackground="grey", highlightthickness=1)
        lblFirstName.grid(row=3,column=1)

        lblLastName = Label(DataFrameLeft, bg="powder blue", text="Last Name", font=("calibri",12,"bold"),padx=2,pady=4)
        lblLastName.grid(row=4,column=0,sticky=W)
        lblLastName = Entry(DataFrameLeft, font=("calibri",13,"bold"), width=34,highlightbackground="grey", highlightthickness=1)
        lblLastName.grid(row=4,column=1)

        lblAddress1 = Label(DataFrameLeft, bg="powder blue", text="Address 1", font=("calibri",12,"bold"),padx=2,pady=4)
        lblAddress1.grid(row=5,column=0,sticky=W)
        lblAddress1 = Entry(DataFrameLeft, font=("calibri",13,"bold"), width=34,highlightbackground="grey", highlightthickness=1)
        lblAddress1.grid(row=5,column=1)

        lblAddress2 = Label(DataFrameLeft, bg="powder blue", text="Adderss 2", font=("calibri",12,"bold"),padx=2,pady=4)
        lblAddress2.grid(row=6,column=0,sticky=W)
        lblAddress2 = Entry(DataFrameLeft, font=("calibri",13,"bold"), width=34,highlightbackground="grey", highlightthickness=1)
        lblAddress2.grid(row=6,column=1)

        lblPostCode= Label(DataFrameLeft, bg="powder blue", text="Post Code", font=("calibri",12,"bold"),padx=2,pady=4)
        lblPostCode.grid(row=7,column=0,sticky=W)
        lblPostCode = Entry(DataFrameLeft, font=("calibri",13,"bold"), width=34,highlightbackground="grey", highlightthickness=1)
        lblPostCode.grid(row=7,column=1)

        lblMobile= Label(DataFrameLeft, bg="powder blue", text="Mobile No", font=("calibri",12,"bold"),padx=2,pady=4)
        lblMobile.grid(row=8,column=0,sticky=W)
        lblMobile = Entry(DataFrameLeft, font=("calibri",13,"bold"), width=34,highlightbackground="grey", highlightthickness=1)
        lblMobile.grid(row=8,column=1)




        ############################right side of second frame############################################
        DataFrameRight = LabelFrame(frame, text="Book Details",bg='white', fg='black', bd=20, relief=RIDGE, font=("Calibri", 15, "bold"), pady=2,padx=10)
        DataFrameRight.place(x=920, y=5, width=570,height=350)


        ############################# Buttons Frame #################################################
        framebutton = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        framebutton.place(x=0, y=530, width=1550, height=70)


        ############################# Information Frame #################################################
        frameDetails= Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        frameDetails.place(x=0, y=600, width=1550, height=195)



#load the page
if __name__ == "__main__":
    root = Tk()
    obj = LibManSys(root)
    root.mainloop()