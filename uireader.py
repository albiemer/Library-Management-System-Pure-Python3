
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from sqlshot import sqlquerysearch


app = QtWidgets.QApplication([])
loginform = uic.loadUi("loginui.ui")
mymain = uic.loadUi("mainui.ui")

def mylogin():   #loginform
    myuser = loginform.edituser.text()
    mypass = loginform.editpass.text()
    if myuser == 'albiemer' and mypass == 'albi3mer' or myuser == 'gwen' and mypass == 'gw3n':
        print("Success")
        loginform.lblnote.setHidden(False)
        loginform.lblnote.setText("successfull login")
        loginform.setHidden(True)
        mainformuifunc()    # to launch main window
    elif myuser == '' and mypass == '':
        loginform.lblnote.setHidden(False)
        loginform.lblnote.setText("!Fill The Text box")
    else:
        loginform.edituser.clear()
        loginform.editpass.clear()
        loginform.lblnote.setHidden(False)
        loginform.lblnote.setText("!Wrong Password")
        

def mainformuifunc():
    mylist = [1,2,3,4,5,6]
    mymain.show()
    re = sqlquerysearch('mybullshit')
    mymain.tbllibrary.setRowCount(1)
    mymain.tbllibrary.setItem(0,0, QTableWidgetItem(str(re[0])))
    mymain.tbllibrary.setItem(0,1, QTableWidgetItem(str(re[1])))
    mymain.tbllibrary.setItem(0,2, QTableWidgetItem(re[2]))
    mymain.tbllibrary.setItem(0,3, QTableWidgetItem(re[3]))
    mymain.tbllibrary.setItem(0,4, QTableWidgetItem(re[4]))
    mymain.tbllibrary.setItem(0,5, QTableWidgetItem(re[5]))
    
    mymain.editid.setText(str(re[0]))
    mymain.editisbn.setText(str(re[1]))
    mymain.edittitle.setText(re[2])
    mymain.editauthor.setText(re[3])
    mymain.editborrowedtime.setText(re[4])
    mymain.editborrower.setText(re[5])

def cancellogin(): # loginform
    exit()

def mainsaveentry():
    mymain.pbcancel.setEnabled(False)
    mymain.pbsave.setEnabled(False)
    mymain.pbdelete.setEnabled(True)
    mymain.pbaddnew.setEnabled(True)
    mymain.pbedit.setEnabled(True)

def mainaddnewentry():     #mymain
    mymain.pbcancel.setEnabled(True)
    mymain.pbaddnew.setEnabled(False)
    mymain.pbdelete.setEnabled(False)
    mymain.pbedit.setEnabled(False)
    mymain.pbsave.setEnabled(True)
    
    mymain.edittitle.setReadOnly(False)
    mymain.editisbn.setReadOnly(False)
    mymain.editborrowedtime.setReadOnly(False)
    mymain.editauthor.setReadOnly(False)
    mymain.editborrower.setReadOnly(False)
    
    mymain.edittitle.clear()
    mymain.editisbn.clear()
    mymain.editborrowedtime.clear()
    mymain.editauthor.clear()
    mymain.editborrower.clear()
    
def mainlogout():
    mymain.setHidden(True)
    loginform.show()
    loginform.edituser.clear()
    loginform.editpass.clear()
    loginform.lblnote.setHidden(False)
    loginform.lblnote.setText("Are You Off Now You Asshole?")

def maincancelentry():
    mymain.pbcancel.setEnabled(False)
    mymain.pbaddnew.setEnabled(True)
    mymain.pbdelete.setEnabled(True)
    mymain.pbedit.setEnabled(True)
    mymain.pbsave.setEnabled(False)
    
    mymain.edittitle.setReadOnly(True)
    mymain.editisbn.setReadOnly(True)
    mymain.editborrowedtime.setReadOnly(True)
    mymain.editauthor.setReadOnly(True)
    mymain.editborrower.setReadOnly(True)
    
def maineditentry():
    mymain.pbsave.setEnabled(True)
    mymain.pbaddnew.setEnabled(False)
    mymain.pbcancel.setEnabled(True)
    mymain.pbedit.setEnabled(False)
    mymain.pbdelete.setEnabled(False)
    
    mymain.edittitle.setReadOnly(False)
    mymain.editisbn.setReadOnly(False)
    mymain.editborrowedtime.setReadOnly(False)
    mymain.editauthor.setReadOnly(False)
    mymain.editborrower.setReadOnly(False)

##############################################################################
loginform.pblogin.clicked.connect(mylogin)####################################
loginform.pbcancel.clicked.connect(cancellogin)####### LOGIN FORM BUTTON #####
##############################################################################

##############################################################################
mymain.pblogout.clicked.connect(mainlogout)###################################
mymain.pbaddnew.clicked.connect(mainaddnewentry)##############################
mymain.pbcancel.clicked.connect(maincancelentry)###### MAIN FORM BUTTON ######
mymain.pbsave.clicked.connect(mainsaveentry)##################################
mymain.pbedit.clicked.connect(maineditentry)##################################
##############################################################################

if __name__ == '__main__':
    loginform.show()
    app.exec()
