
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from sqlshot import sqlqueryselecttbl, sqlquerytitlesearch, sqlquerysaverecord, \
     sqlqueryisbnsearch, sqlquerysaveupdateentry, sqlquerycountlastid, sqlqueryidsearchset, \
     sqlquerydeleterec
import time


app = QtWidgets.QApplication([])
loginform = uic.loadUi("loginui.ui")
mymain = uic.loadUi("mainui.ui")
nofoundnote = uic.loadUi("nofoundnote.ui")

def reloadgrid():
    
    mymain.tbllibrary.clear()
    
    re = sqlqueryselecttbl()
    
    for row in re:
        inx = re.index(row)
        mymain.tbllibrary.insertRow(inx)
        # add more if there is more columns in the database.
        mymain.tbllibrary.setItem(inx, 0, QTableWidgetItem(str(row[0])))
        mymain.tbllibrary.setItem(inx, 1, QTableWidgetItem(str(row[1])))
        mymain.tbllibrary.setItem(inx, 2, QTableWidgetItem(row[2]))
        mymain.tbllibrary.setItem(inx, 3, QTableWidgetItem(row[3]))
        mymain.tbllibrary.setItem(inx, 4, QTableWidgetItem(row[4]))
        mymain.tbllibrary.setItem(inx, 5, QTableWidgetItem(row[5]))
        
def myloginsetfocustopass(): loginform.editpass.setFocus()
def myloginsetfocustouser(): loginform.edituser.setFocus()
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
        
        
def mainformuifunc():    #main form of this program
    mymain.show()
    
    mymain.tbllibrary.update()
    
    re = sqlqueryselecttbl()
    
    reloadgrid()
    
    """mymain.tbllibrary.setItem(0,0, QTableWidgetItem(str(re[0])))
    mymain.tbllibrary.setItem(0,1, QTableWidgetItem(str(re[1])))
    mymain.tbllibrary.setItem(0,2, QTableWidgetItem(re[2]))
    mymain.tbllibrary.setItem(0,3, QTableWidgetItem(re[3]))
    mymain.tbllibrary.setItem(0,4, QTableWidgetItem(re[4]))
    mymain.tbllibrary.setItem(0,5, QTableWidgetItem(re[5]))"""
    
    try:
        mymain.editid.setText(str(re[0][0]))
        mymain.editisbn.setText(str(re[0][1]))
        mymain.edittitle.setText(re[0][2])
        mymain.editauthor.setText(re[0][3])
        mymain.editborrowedtime.setText(re[0][4])
        mymain.editborrower.setText(re[0][5])
    except:
        mymain.editid.clear()
        mymain.editisbn.clear()
        mymain.edittitle.clear()
        mymain.editauthor.clear()
        mymain.editborrowedtime.clear()
        mymain.editborrower.clear()

    mymain.editsearch.setFocus()
    mymain.pbupdate.setHidden(True)
    mymain.editidhideover.setHidden(True)

def cancellogin(): # loginform
    exit()

def mainsaveentry():
    
    tosearchserved = mymain.edittitle.text()
    
    mymain.editidhideover.setHidden(True)
    mymain.editid.setHidden(False)
    
    mymain.pbcancel.setEnabled(False)
    mymain.pbsave.setEnabled(False)
    mymain.pbdelete.setEnabled(True)
    mymain.pbaddnew.setEnabled(True)
    mymain.pbedit.setEnabled(True)
    
    mymain.edittitle.setReadOnly(True)
    mymain.editisbn.setReadOnly(True)
    mymain.editborrowedtime.setReadOnly(True)
    mymain.editauthor.setReadOnly(True)
    mymain.editborrower.setReadOnly(True)
    
    isbn = mymain.editisbn.text()
    title = mymain.edittitle.text()
    borrowed = mymain.editborrowedtime.text()
    author = mymain.editauthor.text()
    borrower = mymain.editborrower.text()
    
    sqlquerysaverecord(isbn, title, borrowed, author, borrower)
    
    searched = sqlqueryisbnsearch(isbn)
    
    reloadgrid()
    
    searched = sqlquerytitlesearch(tosearchserved)
    mymain.tbllibrarysearched.setItem(0,0, QTableWidgetItem(str(searched[0])))
    mymain.tbllibrarysearched.setItem(0,1, QTableWidgetItem(str(searched[1])))
    mymain.tbllibrarysearched.setItem(0,2, QTableWidgetItem(searched[2]))
    mymain.tbllibrarysearched.setItem(0,3, QTableWidgetItem(searched[3]))
    mymain.tbllibrarysearched.setItem(0,4, QTableWidgetItem(searched[4]))
    mymain.tbllibrarysearched.setItem(0,5, QTableWidgetItem(searched[5]))
    
    mymain.editid.setText(str(searched[0]))
    mymain.editisbn.setText(str(searched[1]))
    mymain.edittitle.setText(searched[2])
    mymain.editauthor.setText(searched[3])
    mymain.editborrowedtime.setText(searched[4])
    mymain.editborrower.setText(searched[5])

def mainupdateentry():
    mainid = mymain.editid.text()
    isbn = mymain.editisbn.text()
    title = mymain.edittitle.text()
    author = mymain.editauthor.text()
    btime = mymain.editborrowedtime.text()
    borrower = mymain.editborrower.text()
    
    mymain.pbcancel.setEnabled(False)
    mymain.pbupdate.setEnabled(False)
    mymain.pbdelete.setEnabled(True)
    mymain.pbaddnew.setEnabled(True)
    mymain.pbedit.setEnabled(True)
    
    mymain.edittitle.setReadOnly(True)
    mymain.editisbn.setReadOnly(True)
    mymain.editborrowedtime.setReadOnly(True)
    mymain.editauthor.setReadOnly(True)
    mymain.editborrower.setReadOnly(True)
    
    sqlquerysaveupdateentry(mainid, isbn, title, author, btime, borrower)
    
    reloadgrid()
    
    searched = sqlquerytitlesearch(title)
    mymain.tbllibrarysearched.setItem(0,0, QTableWidgetItem(str(searched[0])))
    mymain.tbllibrarysearched.setItem(0,1, QTableWidgetItem(str(searched[1])))
    mymain.tbllibrarysearched.setItem(0,2, QTableWidgetItem(searched[2]))
    mymain.tbllibrarysearched.setItem(0,3, QTableWidgetItem(searched[3]))
    mymain.tbllibrarysearched.setItem(0,4, QTableWidgetItem(searched[4]))
    mymain.tbllibrarysearched.setItem(0,5, QTableWidgetItem(searched[5]))

def mainaddnewentry():     #mymain
    
    mymain.editborrowedtime.setText(time.asctime())
    
    mymain.pbsave.setHidden(False)
    mymain.pbupdate.setHidden(True)
    
    gmainid = mymain.editid.text()
    gisbn = mymain.editisbn.text()
    gtitle = mymain.edittitle.text()
    gbtime = mymain.editborrowedtime.text()
    gauthor = mymain.editauthor.text()
    gborrower = mymain.editborrower.text()
    
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
    
    mymain.editidhideover.setHidden(False)
    mymain.editid.setHidden(True)
    mymain.edittitle.clear()
    mymain.editisbn.clear()
    #mymain.editborrowedtime.clear()
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
    mysearchid = mymain.editid.text()
    
    mymain.editidhideover.setHidden(True)
    mymain.editid.setHidden(False)
    mymain.pbupdate.setHidden(True)
    mymain.pbsave.setHidden(False)
    
    mymain.pbcancel.setEnabled(False)
    mymain.pbaddnew.setEnabled(True)
    mymain.pbdelete.setEnabled(True)
    mymain.pbedit.setEnabled(True)
    mymain.pbsave.setEnabled(False)
    mymain.pbupdate.setEnabled(True)
    
    mymain.edittitle.setReadOnly(True)
    mymain.editisbn.setReadOnly(True)
    mymain.editborrowedtime.setReadOnly(True)
    mymain.editauthor.setReadOnly(True)
    mymain.editborrower.setReadOnly(True)
    
    toset = sqlqueryidsearchset(mysearchid)
    
    mymain.editid.setText(str(toset[0]))
    mymain.editisbn.setText(str(toset[1]))
    mymain.edittitle.setText(toset[2])
    mymain.editauthor.setText(toset[3])
    mymain.editborrowedtime.setText(toset[4])
    mymain.editborrower.setText(toset[5])
    
def maineditentry():
    
    mymain.pbsave.setHidden(True)
    mymain.pbupdate.setHidden(False)
    
    mymain.pbupdate.setEnabled(True)
    mymain.pbsave.setEnabled(False)
    mymain.pbaddnew.setEnabled(False)
    mymain.pbcancel.setEnabled(True)
    mymain.pbedit.setEnabled(False)
    mymain.pbdelete.setEnabled(False)
    
    mymain.edittitle.setReadOnly(False)
    mymain.editisbn.setReadOnly(False)
    mymain.editborrowedtime.setReadOnly(False)
    mymain.editauthor.setReadOnly(False)
    mymain.editborrower.setReadOnly(False)

def mainsearchentry():
    
    mysearch = mymain.editsearch.text()
    searched = sqlquerytitlesearch(mysearch)
    
    if searched == None:
        nofoundnote.show()
    else:
        mymain.tbllibrarysearched.setItem(0,0, QTableWidgetItem(str(searched[0])))
        mymain.tbllibrarysearched.setItem(0,1, QTableWidgetItem(str(searched[1])))
        mymain.tbllibrarysearched.setItem(0,2, QTableWidgetItem(searched[2]))
        mymain.tbllibrarysearched.setItem(0,3, QTableWidgetItem(searched[3]))
        mymain.tbllibrarysearched.setItem(0,4, QTableWidgetItem(searched[4]))
        mymain.tbllibrarysearched.setItem(0,5, QTableWidgetItem(searched[5]))
        
        mymain.editid.setText(str(searched[0]))
        mymain.editisbn.setText(str(searched[1]))
        mymain.edittitle.setText(searched[2])
        mymain.editauthor.setText(searched[3])
        mymain.editborrowedtime.setText(searched[4])
        mymain.editborrower.setText(searched[5])
        
        del mysearch, searched
    
        mymain.tbllibrary.update()
    
def mymaindeleterec():
    todeleteid = mymain.editid.text()
    sqlquerydeleterec(todeleteid)
    
    re = sqlqueryselecttbl()
    
    reloadgrid()
    
    try:
        mymain.editid.setText(str(re[0][0]))
        mymain.editisbn.setText(str(re[0][1]))
        mymain.edittitle.setText(re[0][2])
        mymain.editauthor.setText(re[0][3])
        mymain.editborrowedtime.setText(re[0][4])
        mymain.editborrower.setText(re[0][5])
    except:
        mymain.editid.clear()
        mymain.editisbn.clear()
        mymain.edittitle.clear()
        mymain.editauthor.clear()
        mymain.editborrowedtime.clear()
        mymain.editborrower.clear()
    
    mymain.tbllibrary.update()

def unloadnofoundnote():
    nofoundnote.setHidden(True)
    mymain.tbllibrary.update()

##############################################################################
loginform.pblogin.clicked.connect(mylogin)####################################
loginform.pbcancel.clicked.connect(cancellogin)####### LOGIN FORM BUTTON #####
loginform.editpass.returnPressed.connect(mylogin)#############################
loginform.edituser.returnPressed.connect(myloginsetfocustopass)###############
loginform.editpass.returnPressed.connect(myloginsetfocustouser)###############
##############################################################################

##############################################################################
mymain.pblogout.clicked.connect(mainlogout)###################################
mymain.pbaddnew.clicked.connect(mainaddnewentry)##############################
mymain.pbcancel.clicked.connect(maincancelentry)###### MAIN FORM BUTTON ######
mymain.pbsave.clicked.connect(mainsaveentry)##################################
mymain.pbedit.clicked.connect(maineditentry)##################################
mymain.pbsearch.clicked.connect(mainsearchentry)##############################
mymain.pbupdate.clicked.connect(mainupdateentry)##############################
mymain.editsearch.returnPressed.connect(mainsearchentry)######################
mymain.pbdelete.clicked.connect(mymaindeleterec)##############################
##############################################################################

####################################################################################
nofoundnote.pbnoteok.clicked.connect(unloadnofoundnote)## NOFOUNDNOTE FORM BUTTON ##
####################################################################################

if __name__ == '__main__':
    loginform.show()
    loginform.edituser.setFocus()
    app.exec()
