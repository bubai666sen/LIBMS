import tkinter as tk
from tkinter import *
from turtle import *
import sqlite3 as sql
import datetime

now = datetime.datetime.now()

db = sql.connect('USER_DB.db')
db1 = sql.connect('LIB_DB.db')
cur = db.cursor()
cur1 = db1.cursor()


def welcome():
    def create_user_db():

        sql_q = """create table if not exists USER_DB(
                    name varchar2(500) Not null,
                    username varchar2(100) primary key,
                    email varchar2(100) not null,
                    phone number(12) not null,
                    password varchar2(100000) not null,
                    address varchar2(100) not null)"""
        cur.execute(sql_q)

    def create_lib_db():

        sql_q = """create table if not exists LIB_DB(
                    bid varchar2(11) primary key check(bid like 'B%'),
                    bname varchar2(100) not null,
                    author varchar2(100) not null,
                    publisher varchar2(100) not null,
                    price number(10,2) not null,
                    br_by varchar2(11),
                    doi varchar2(10),
                    dos varchar2(10))"""
        cur1.execute(sql_q)
        
    def close():
        db.close()

    def close1():
        db1.close()

    create_user_db()
    create_lib_db()

    # close()
    # close1()
    def msg(s1, s2):
        error = tk.Tk()
        error.resizable(0, 0)
        error.title(s1)
        lab = tk.Label(error,
                       text=s2,
                       font=('Agency FB', 18))

        lab.pack()
        but = tk.Button(error, text='Close', font=('Agency FB', 10), bg='tomato', height=3, width=25,
                        command=error.destroy)
        but.pack()
        lab = tk.Label(error)
        lab.pack()
        error.mainloop()

    def msg_small(s1, s2):
        error1 = tk.Tk()
        error1.resizable(0, 0)
        error1.title(s1)
        lab = tk.Label(error1,
                       text=s2,
                       font=('Agency FB', 12))

        lab.pack()
        but = tk.Button(error1, text='Close', font=('Agency FB', 10), bg='tomato', height=3, width=25,
                        command=error1.destroy)
        but.pack()
        lab = tk.Label(error1)
        lab.pack()
        error1.mainloop()

    """def ask(s1,s2):
                error2 = tk.Tk()
                error2.resizable(0, 0)
                error2.title(s1)
                lab = tk.Label(error2,
                               text=s2,
                               font=('Agency FB', 18))

                lab.pack()
                frame3 = tk.Frame(error2)
                but = tk.Button(frame3, text='Yes', font=('Agency FB', 12),bg='tomato', height=3, width=35,
                                    command=yes)
                but.pack(side='right')
                but = tk.Button(frame3, text='Cancel', font=('Agency FB', 12),bg='light cyan',
                                      height=3, width=35, command=error2.destroy)
                but.pack(side='left')
                frame3.pack()
                error2.mainloop()"""

    def not_found_error():
        nf = tk.Tk()
        nf.resizable(0, 0)
        nf.title("Not Found Error!")
        lab = tk.Label(nf,
                       text="No such record found!\n",
                       font=('Agency FB', 18))

        lab.pack()
        but = tk.Button(nf, text='Close', font=('Agency FB', 10), bg='tomato', height=3, width=25,
                        command=nf.destroy)
        but.pack()
        lab = tk.Label(nf)
        lab.pack()
        nf.mainloop()

    def pwd_mismatch_error():
        pme = tk.Tk()
        pme.resizable(0, 0)
        pme.title("Password Mismatch Error!")
        lab = tk.Label(pme,
                       text="Password Mismatch Error!\n",
                       font=('Agency FB', 18))

        lab.pack()
        but = tk.Button(pme, text='Close', font=('Agency FB', 10), bg='tomato', height=3, width=25,
                        command=pme.destroy)
        but.pack()
        lab = tk.Label(pme)
        lab.pack()
        pme.mainloop()

    def db_in_error():
        er = tk.Tk()
        er.resizable(0, 0)
        er.title("Database Insertion Error!")
        lab = tk.Label(er,
                       text="Database Insertion Error!\n",
                       font=('Agency FB', 18))

        lab.pack()
        but = tk.Button(er, text='Close', font=('Agency FB', 10), bg='tomato', height=3, width=25,
                        command=er.destroy)
        but.pack()
        lab = tk.Label(er)
        lab.pack()
        er.mainloop()

    def db_in_success():
        ss = tk.Tk()
        ss.resizable(0, 0)
        ss.title("Record added successfully!")
        lab = tk.Label(ss,
                       text="Record added successfully!\n",
                       font=('Agency FB', 18))

        lab.pack()
        but = tk.Button(ss, text='Close', font=('Agency FB', 10), bg='tomato', height=3, width=25,
                        command=ss.destroy)
        but.pack()
        lab = tk.Label(ss)
        lab.pack()
        ss.mainloop()

    def reset():
        blank.set('')
        blank1.set('')

    def sure():
        def yes():
            s.destroy()
            root.destroy()

        def cancel():
            s.destroy()

        s = tk.Tk()
        # s.geometry("800x400")
        s.resizable(0, 0)
        s.title("Are you Sure you want to exit?")
        lab = tk.Label(s, text='Are you Sure you want to exit?', font=('Agency FB', 26))
        lab.pack()
        frame3 = tk.Frame(s)
        but = tk.Button(frame3, text='Yes', font=('Agency FB', 12), bg='tomato', height=3, width=35,
                        command=yes)
        but.pack(side='right')
        but = tk.Button(frame3, text='Cancel', font=('Agency FB', 12), bg='light cyan',
                        height=3, width=35, command=cancel)
        but.pack(side='right')
        frame3.pack()
        s.mainloop()
    # encription
    def sencript(s):
        string = ''
        char = ''
        for ch in s:
            temp = ord(ch)
            if temp % 2 == 0:
                temp = temp // 6
            else:
                temp = temp * 3
            temp = (bin(temp)[2:])
            for ch1 in temp:
                if ch1 == '1':
                    char = char + '#'
                elif ch1 == '0':
                    char = char + ' '
            string = string + char
        return string

    def add_book():
        def add_book_submit():
            fg = 0
            try:
                b1 = e1.get()
                b2 = e2.get()
                b3 = e3.get()
                b4 = e4.get()
                b5 = float(e5.get())
                val = []
                val.append(b1)
                val.append(b2)
                val.append(b3)
                val.append(b4)
                val.append(b5)
                val.append('None')
                val.append('N/A')
                val.append('N/A')
                sql_q = "insert into LIB_DB values(?,?,?,?,?,?,?,?)"
                cur1.execute(sql_q, val)
                db1.commit()
            except:
                db1.rollback()
                #db_in_error()
                msg("Database Insertion Error","Check your input!\nBook ID may be already taken or you have given some invalid input!\nCheck input restrictions for help")
                fg = 1
            bid.set('B')
            bname.set('')
            author.set('')
            publisher.set('')
            price.set('')
            # br_by.set('')
            if fg == 0:
                db_in_success()

        addbook = tk.Tk()
        addbook.title("Add Book")
        addbook.geometry("1000x700")
        addbook.resizable(0, 0)
        addbook.configure(bg="royal blue1")

        bid = tk.StringVar(addbook)
        bid.set('B')
        bname = tk.StringVar(addbook)
        author = tk.StringVar(addbook)
        publisher = tk.StringVar(addbook)
        price = tk.StringVar(addbook)
        # br_by=tk.StringVar(addbook)

        frame1 = tk.Frame(addbook, pady=30, bg='royal blue1')
        lable1 = tk.Label(frame1, text='       Enter Book Id : ', fg='white', bg='royal blue1', font=('Agency FB', 24),
                          padx=25)
        lable1.pack(side='left')
        e1 = tk.Entry(frame1, textvariable=bid, font=('Agency FB', 24))
        e1.pack(side='left')
        lab = tk.Label(frame1, text="Start with B", fg='white', bg='royal blue1', font=('Agency FB', 24))
        lab.pack(side='left')
        frame1.pack()

        frame2 = tk.Frame(addbook, pady=30, bg='royal blue1')
        lable2 = tk.Label(frame2, text='      Enter Book Name      : ', fg='white', bg='royal blue1',
                          font=('Agency FB', 24), padx=25)
        lable2.pack(side='left')
        e2 = tk.Entry(frame2, textvariable=bname, font=('Agency FB', 24))
        e2.pack(side='left')
        frame2.pack()

        frame3 = tk.Frame(addbook, pady=30, bg='royal blue1')
        lable3 = tk.Label(frame3, text='       Enter Author Name    : ', fg='white', bg='royal blue1',
                          font=('Agency FB', 24), padx=25)
        lable3.pack(side='left')
        e3 = tk.Entry(frame3, textvariable=author, font=('Agency FB', 24))
        e3.pack(side='left')
        frame3.pack()

        frame4 = tk.Frame(addbook, pady=30, bg='royal blue1')
        lable4 = tk.Label(frame4, text='       Enter Publisher name : ', fg='white', bg='royal blue1',
                          font=('Agency FB', 24), padx=25)
        lable4.pack(side='left')
        e4 = tk.Entry(frame4, textvariable=publisher, font=('Agency FB', 24))
        e4.pack(side='left')
        frame4.pack()

        frame5 = tk.Frame(addbook, pady=30, bg='royal blue1')
        lable5 = tk.Label(frame5, text='             Enter Price          : ', fg='white', bg='royal blue1',
                          font=('Agency FB', 24), padx=25)
        lable5.pack(side='left')
        e5 = tk.Entry(frame5, textvariable=price, font=('Agency FB', 24))
        e5.pack(side='left')
        frame5.pack()

        lab = tk.Label(addbook, text="", bg='royal blue1')
        lab.pack()

        frame4 = tk.Frame(addbook, bg='royal blue1')
        but_register = tk.Button(frame4, text='Add', fg='black', bg='tomato', font=('Agency FB', 16), height=3,
                                 width=30, command=add_book_submit)
        but_register.pack(side='right')
        lab1 = tk.Label(frame4, padx=25, bg='royal blue1')
        lab1.pack(side='right')
        but = tk.Button(frame4, text='Input Restrictions', fg='black', bg='light cyan', font=('Agency FB', 16), height=3,
                        width=30, command=show_constraints)
        but.pack(side='right')
        lab1 = tk.Label(frame4, padx=25, bg='royal blue1')
        lab1.pack(side='right')
        but_exit = tk.Button(frame4, text='Close', fg='black', bg='tomato', font=('Agency FB', 16), height=3, width=30,
                             command=addbook.destroy)
        but_exit.pack(side='right')
        frame4.pack()

    def show_all_books_user(unsh):
        shbu = tk.Tk()
        shbu.title('Show all books')
        shbu.resizable(0, 0)
        shbu.configure(bg='white')
        st = tk.StringVar(shbu)
        sp = tk.StringVar(shbu)
        st = ''
        sp = '     '
        sh=' '
        result = cur1.execute('select * from LIB_DB')
        data = result.fetchall()
        '''st =format(
            'BOOK ID', '11') + sp + format('BOOK NAME', '15') + sp + format('AUTHOR NAME', '15') + sp + format(
            'PUBLISHER NAME', '15') + sp + format('PRICE', '13') + sp + format('BORROWER', '15') + sp + format(
            'ISSUE DATE', '10') + sp + format('SUBMISSION DATE','10')'''
        st = 'book id'.ljust(11,sh) + sp + 'book name'.ljust(15,sh) + sp + 'author name'.ljust(15,sh) + sp + 'publisher name'.ljust(15,sh) + sp + 'price'.ljust(13,sh) + sp + 'borrower'.ljust(15,sh)+ sp + 'issue'.ljust(10,sh)+ sp + 'submission'.ljust(10,sh)
        ###
        f1 = tk.Frame(shbu)
        scrollbar = tk.Scrollbar(shbu)
        scrollbar.pack(side='right', fill='y')
        scrollbar1 = tk.Scrollbar(shbu)
        scrollbar1.pack(side='bottom',fill='x')
        mylist = tk.Listbox(f1,height=20,width=90, yscrollcommand=scrollbar.set,xscrollcommand=scrollbar1.set)
        #mylist = tk.Listbox(f1, height=20, width=90, yscrollcommand=scrollbar.set)
        mylist.config(font=('Agency FB', '16'))
        mylist.insert(END, "__________________________________________________________________________________________________________________________")
        mylist.insert(END,'')
        mylist.insert(END,st)
        mylist.insert(END,"___________________________________________________________________________________________________________________________")
        for row in data:
            if row == None:
                shbu.destroy()
                msg("No Books!","No Books!\nNeed to add some books...\n")
            elif row[5] == 'None':
                st = format(row[0], '11') + sp + format(row[1], '15') + sp + format(row[2], '15') + sp + format(
                    row[3], '15') + sp + format(row[4], '13') + sp + format(row[5], '15') + sp + format(row[6],
                                                                                                        '10') + sp + format(
                    row[7], '10')
                mylist.insert(END,st)
                mylist.insert(END,'')
            elif row[5] == unsh:
                st = format(row[0], '11') + sp + format(row[1], '15') + sp + format(row[2], '15') + sp + format(
                    row[3], '15') + sp + format(row[4], '13') + sp + format('You!', '15') + sp + format(row[6],
                                                                                                        '10') + sp + format(
                    row[7], '10')
                mylist.insert(END,st)
                mylist.insert(END,'')
            else:
                st = format(row[0], '11') + sp + format(row[1], '15') + sp + format(row[2], '15') + sp + format(
                    row[3], '15') + sp + format(row[4], '13') + sp + format('Another User', '15') + sp + format(row[6],
                                                                                                                '10') + sp + format(
                    row[7], '10')
                mylist.insert(END,st)
                mylist.insert(END,'')
            #st = bid.ljust(11,sh) + sp + bname.ljust(15,sh) + sp + author.ljust(15,sh) + sp + publisher.ljust(15,sh) + sp + price.ljust(13,sh) + sp + br_by.ljust(15,sh) + sp + doi.ljust(10,sh)+ sp + dos.ljust(10,sh)
            '''st=format(row[0], '11') + sp + format(row[1], '15') + sp + format(row[2], '15') + sp + format(row[3],
                                                                                                       '15') + sp + format(
                row[4], '12') + sp + format(row[5], '15') + sp + format(row[6], '10') + sp + format(row[7], '10')'''
            #l=len(st)
            #print('line=',l)
            #mylist.insert(END,st)
            #mylist.insert(END, '')
            #print(st)
        mylist.pack(side='left', fill='both')
        scrollbar.config(command=mylist.yview)
        scrollbar1.config(orient=HORIZONTAL,command=mylist.xview)
        f1.pack()
        ###
        '''for row in data:
            if row == None:
                st = "No Books!\nNeed to add some books...\n"
            elif row[5] == 'None':
                st = st + format(row[0], '11') + sp + format(row[1], '15') + sp + format(row[2], '15') + sp + format(
                    row[3], '15') + sp + format(row[4], '13') + sp + format(row[5], '15') + sp + format(row[6],
                                                                                                        '10') + sp + format(
                    row[7], '10') + "\n"
            elif row[5] == unsh:
                st = st + format(row[0], '11') + sp + format(row[1], '15') + sp + format(row[2], '15') + sp + format(
                    row[3], '15') + sp + format(row[4], '13') + sp + format('You!', '15') + sp + format(row[6],
                                                                                                        '10') + sp + format(
                    row[7], '10') + "\n"
            else:
                st = st + format(row[0], '11') + sp + format(row[1], '15') + sp + format(row[2], '15') + sp + format(
                    row[3], '15') + sp + format(row[4], '13') + sp + format('Another User', '15') + sp + format(row[6],
                                                                                                                '10') + sp + format(
                    row[7], '10') + "\n"
        lab = tk.Label(shbu, text=st, fg='blue', bg='white', font=('Agency FB', 18))
        lab.pack()'''
        lab = tk.Label(shbu, bg='white')
        lab.pack()
        but_exit = tk.Button(shbu, text='Close', fg='black', bg='tomato', font=('Agency FB', 12), height=3, width=30,
                             command=shbu.destroy)
        but_exit.pack()
        lab = tk.Label(shbu, bg='white')
        lab.pack()
        shbu.mainloop()

    def show_all_books():
        shb = tk.Tk()
        shb.title('Show all books')
        # shb.geometry("1000x700")
        shb.resizable(0, 0)
        shb.configure(bg='white')
        st = tk.StringVar(shb)
        sp = tk.StringVar(shb)
        st = ''
        sp = '     '
        sh = ' '
        result = cur1.execute('select * from LIB_DB')
        data = result.fetchall()
        st = 'book id'.ljust(11, sh) + sp + 'book name'.ljust(15, sh) + sp + 'author name'.ljust(15,
                                                                                                 sh) + sp + 'publisher name'.ljust(
            15, sh) + sp + 'price'.ljust(13, sh) + sp + 'borrower'.ljust(15, sh) + sp + 'issue'.ljust(10,
                                                                                                      sh) + sp + 'submission'.ljust(
            10, sh)
        '''st = format(
                'book id', '15') + sp + format('book name', '15') + sp + format('author', '15') + sp + format(
                'publisher', '15') + sp + format('price', '12') + sp + format('borrower', '15') + sp + format(
                'issue', '10') + sp + format('submission','10')'''
        # l = len(st)
        # print('line -1=',l,st)
        # print(st)
        f1 = tk.Frame(shb)
        scrollbar = tk.Scrollbar(shb)
        scrollbar.pack(side='right', fill='y')
        scrollbar1 = tk.Scrollbar(shb)
        scrollbar1.pack(side='bottom', fill='x')
        mylist = tk.Listbox(f1, height=20, width=90, yscrollcommand=scrollbar.set, xscrollcommand=scrollbar1.set)
        # mylist = tk.Listbox(f1, height=20, width=90, yscrollcommand=scrollbar.set)
        mylist.config(font=('Agency FB', '16'))
        mylist.insert(END,
                      "__________________________________________________________________________________________________________________________")
        mylist.insert(END, '')
        mylist.insert(END, st)
        mylist.insert(END,
                      "___________________________________________________________________________________________________________________________")
        for row in data:
            bid = str(row[0])
            bname = str(row[1])
            author = str(row[2])
            publisher = str(row[3])
            price = str(row[4])
            br_by = str(row[5])
            doi = str(row[6])
            dos = str(row[7])
            st = bid.ljust(11, sh) + sp + bname.ljust(15, sh) + sp + author.ljust(15, sh) + sp + publisher.ljust(15,
                                                                                                                 sh) + sp + price.ljust(
                13, sh) + sp + br_by.ljust(15, sh) + sp + doi.ljust(10, sh) + sp + dos.ljust(10, sh)
            '''st=format(row[0], '11') + sp + format(row[1], '15') + sp + format(row[2], '15') + sp + format(row[3],
                                                                                                       '15') + sp + format(
                row[4], '12') + sp + format(row[5], '15') + sp + format(row[6], '10') + sp + format(row[7], '10')'''
            # l=len(st)
            # print('line=',l)
            mylist.insert(END, st)
            mylist.insert(END, '')
            # print(st)
        mylist.pack(side='left', fill='both')
        scrollbar.config(command=mylist.yview)
        scrollbar1.config(orient=HORIZONTAL, command=mylist.xview)
        f1.pack()
        # lab = tk.Label(shb, text=st, fg='blue', bg='white', font=('Agency FB', 18))
        # lab.pack()

        lab = tk.Label(shb, bg='white')
        lab.pack()
        but_exit = tk.Button(shb, text='Close', fg='black', bg='tomato', font=('Agency FB', 12), height=3, width=30,
                             command=shb.destroy)
        but_exit.pack()
        lab = tk.Label(shb, bg='white')
        lab.pack()
        shb.mainloop()
    def search_book_user(uns):
        def searching_booku():
            shb1u = tk.Tk()
            nonlocal uns
            shb1u.title('Search Result')
            shb1u.resizable(0, 0)
            shb1u.configure(bg='white')
            st = tk.StringVar(shb1u)
            sp = tk.StringVar(shb1u)
            st = ''
            sp = '     '
            sh=' '
            biu = bidddu.get()
            val = []
            for i in range(0, 5):
                val.append(biu)
            sql_q = 'select * from LIB_DB where bid=? or bname=? or author=? or publisher=? or price=?'
            result = cur1.execute(sql_q, val)
            data = result.fetchall()
            if len(data) == 0:
                shb1u.destroy()
                msg('Not Found!','No Such Record Found!')
            else:
                '''st=    format(
                    'BOOK ID', '11') + sp + format('BOOK NAME', '15') + sp + format('AUTHOR NAME', '15') + sp + format(
                    'PUBLISHER NAME', '15') + sp + format('PRICE', '13') + sp + format('BORROWER', '15') + sp + format(
                    'ISSUE DATE', '10') + sp + format('SUBMISSION DATE','10')'''
                st = 'book id'.ljust(11,sh) + sp + 'book name'.ljust(15,sh) + sp + 'author name'.ljust(15,sh) + sp + 'publisher name'.ljust(15,sh) + sp + 'price'.ljust(13,sh) + sp + 'borrower'.ljust(15,sh)+ sp + 'issue'.ljust(10,sh)+ sp + 'submission'.ljust(10,sh)
                ###
                f1 = tk.Frame(shb1u)
                scrollbar = tk.Scrollbar(shb1u)
                scrollbar.pack(side='right', fill='y')
                scrollbar1 = tk.Scrollbar(shb1u)
                scrollbar1.pack(side='bottom',fill='x')
                mylist = tk.Listbox(f1,height=20,width=90, yscrollcommand=scrollbar.set,xscrollcommand=scrollbar1.set)
                #mylist = tk.Listbox(f1, height=20, width=90, yscrollcommand=scrollbar.set)
                mylist.config(font=('Agency FB', '16'))
                mylist.insert(END, "__________________________________________________________________________________________________________________________")
                mylist.insert(END,'')
                mylist.insert(END,st)
                mylist.insert(END,"___________________________________________________________________________________________________________________________")
                for row in data:
                    if row[5] == 'None':
                        st = format(row[0], '15') + sp + format(row[1], '15') + sp + format(row[2],
                                                                                                 '15') + sp + format(
                            row[3], '15') + sp + format(row[4], '13') + sp + format(row[5], '15') + sp + format(row[6],
                                                                                                                '10') + sp + format(
                            row[7], '10')
                        mylist.insert(END,st)
                        mylist.insert(END,'')
                    elif row[5] == uns:
                        st = format(row[0], '15') + sp + format(row[1], '15') + sp + format(row[2],
                                                                                                 '15') + sp + format(
                            row[3], '15') + sp + format(row[4], '13') + sp + format('You!', '15') + sp + format(row[6],
                                                                                                                '10') + sp + format(
                            row[7], '10')
                        mylist.insert(END,st)
                        mylist.insert(END,'')
                    else:
                        st = format(row[0], '15') + sp + format(row[1], '15') + sp + format(row[2],
                                                                                                 '15') + sp + format(
                            row[3], '15') + sp + format(row[4], '13') + sp + format('Another User', '15') + sp + format(
                            row[6], '10') + sp + format(row[7], '10')
                        mylist.insert(END,st)
                        mylist.insert(END,'')
                mylist.pack(side='left', fill='both')
                scrollbar.config(command=mylist.yview)
                scrollbar1.config(orient=HORIZONTAL,command=mylist.xview)
                f1.pack()
                ###
                '''for row in data:
                    if row[5] == 'None':
                        st = st + format(row[0], '15') + sp + format(row[1], '15') + sp + format(row[2],
                                                                                                 '15') + sp + format(
                            row[3], '15') + sp + format(row[4], '13') + sp + format(row[5], '15') + sp + format(row[6],
                                                                                                                '10') + sp + format(
                            row[7], '10') + "\n"
                    elif row[5] == uns:
                        st = st + format(row[0], '15') + sp + format(row[1], '15') + sp + format(row[2],
                                                                                                 '15') + sp + format(
                            row[3], '15') + sp + format(row[4], '13') + sp + format('You!', '15') + sp + format(row[6],
                                                                                                                '10') + sp + format(
                            row[7], '10') + "\n"
                    else:
                        st = st + format(row[0], '15') + sp + format(row[1], '15') + sp + format(row[2],
                                                                                                 '15') + sp + format(
                            row[3], '15') + sp + format(row[4], '13') + sp + format('Another User', '15') + sp + format(
                            row[6], '10') + sp + format(row[7], '10') + "\n"
            lab = tk.Label(shb1u, text=st, fg='blue', bg='white', font=('Agency FB', 18))
            lab.pack()'''
            lab = tk.Label(shb1u, bg='white')
            lab.pack()
            but_exit = tk.Button(shb1u, text='Close', fg='black', bg='tomato', font=('Agency FB', 12), height=3,
                                 width=30,
                                 command=shb1u.destroy)
            but_exit.pack()
            lab = tk.Label(shb1u, bg='white')
            lab.pack()
            shb1u.mainloop()

        searchbku = tk.Tk()
        searchbku.title("Search Book")
        searchbku.geometry("800x400")
        searchbku.resizable(0, 0)
        searchbku.configure(bg='royal blue1')
        biddu = tk.StringVar(searchbku)
        frame1 = tk.Frame(searchbku, pady=30, bg='royal blue1')
        lable1 = tk.Label(frame1, text='Enter something to search: ', fg='white', bg='royal blue1',
                          font=('Agency FB', 24))
        lable1.pack(side='left')
        bidddu = tk.Entry(frame1, textvariable=biddu, font=('Agency FB', 24))
        bidddu.pack(side='left')
        frame1.pack()
        lable1 = tk.Label(searchbku, text="Note: Enter proper Book Id only to get unique result.  \n\
                        If you don't know the Book Id then you can search with   \n\
                        any other attribute like book name,author,publisher,   \n\
                        price etc but it may show multiple results.   ", fg='white', bg='royal blue1',
                          font=('Agency FB', 24))
        lable1.pack()
        frame4 = tk.Frame(searchbku, bg='royal blue1')
        but_register = tk.Button(frame4, text='Search', fg='black', bg='light cyan', font=('Agency FB', 14), height=3,
                                 width=30, command=searching_booku)
        but_register.pack(side='right')
        lab1 = tk.Label(frame4, padx=25, bg='royal blue1')
        lab1.pack(side='right')
        but_exit = tk.Button(frame4, text='Close', fg='black', bg='tomato', font=('Agency FB', 14), height=3, width=30,
                             command=searchbku.destroy)
        but_exit.pack(side='right')
        frame4.pack()

        searchbku.mainloop()

    def search_book():
        def searching_book():
            shb1 = tk.Tk()
            shb1.title('Search Result')
            shb1.resizable(0, 0)
            shb1.configure(bg='white')
            st = tk.StringVar(shb1)
            sp = tk.StringVar(shb1)
            st = ''
            sp = '     '
            sh=' '
            bi = biddd.get()
            val = []
            for i in range(0, 8):
                val.append(bi)
            sql_q = 'select * from LIB_DB where bid=? or bname=? or author=? or publisher=? or price=? or br_by=? or doi=? or dos=?'
            result = cur1.execute(sql_q, val)
            data = result.fetchall()
            if len(data) == 0:
                shb1.destroy()
                msg('Not Found!','No Such Record Found!')
            else:
                '''st=    format(
                    'BOOK ID', '11') + sp + format('BOOK NAME', '15') + sp + format('AUTHOR NAME', '15') + sp + format(
                    'PUBLISHER NAME', '15') + sp + format('PRICE', '13') + sp + format('BORROWER', '15') + sp + format(
                    'ISSUE DATE', '10') + sp + format('SUBMISSION DATE','10')'''
                st = 'book id'.ljust(11,sh) + sp + 'book name'.ljust(15,sh) + sp + 'author name'.ljust(15,sh) + sp + 'publisher name'.ljust(15,sh) + sp + 'price'.ljust(13,sh) + sp + 'borrower'.ljust(15,sh)+ sp + 'issue'.ljust(10,sh)+ sp + 'submission'.ljust(10,sh)
                f1 = tk.Frame(shb1)
                scrollbar = tk.Scrollbar(shb1)
                scrollbar.pack(side='right', fill='y')
                scrollbar1 = tk.Scrollbar(shb1)
                scrollbar1.pack(side='bottom',fill='x')
                mylist = tk.Listbox(f1,height=20,width=90, yscrollcommand=scrollbar.set,xscrollcommand=scrollbar1.set)
                #mylist = tk.Listbox(f1, height=20, width=90, yscrollcommand=scrollbar.set)
                mylist.config(font=('Agency FB', '16'))
                mylist.insert(END, "__________________________________________________________________________________________________________________________")
                mylist.insert(END,'')
                mylist.insert(END,st)
                mylist.insert(END,"___________________________________________________________________________________________________________________________")
                for row in data:
                    bid=str(row[0])
                    bname=str(row[1])
                    author=str(row[2])
                    publisher=str(row[3])
                    price=str(row[4])
                    br_by=str(row[5])
                    doi=str(row[6])
                    dos=str(row[7])
                    st = bid.ljust(11,sh) + sp + bname.ljust(15,sh) + sp + author.ljust(15,sh) + sp + publisher.ljust(15,sh) + sp + price.ljust(13,sh) + sp + br_by.ljust(15,sh) + sp + doi.ljust(10,sh)+ sp + dos.ljust(10,sh)
                    '''st=format(row[0], '11') + sp + format(row[1], '15') + sp + format(row[2], '15') + sp + format(row[3],
                                                                                                               '15') + sp + format(
                        row[4], '12') + sp + format(row[5], '15') + sp + format(row[6], '10') + sp + format(row[7], '10')'''
                    #l=len(st)
                    #print('line=',l)
                    mylist.insert(END,st)
                    mylist.insert(END, '')
                    #print(st)
                mylist.pack(side='left', fill='both')
                scrollbar.config(command=mylist.yview)
                scrollbar1.config(orient=HORIZONTAL,command=mylist.xview)
                f1.pack()
            #lab = tk.Label(shb1, text=st, fg='blue', bg='white', font=('Agency FB', 18))
            #lab.pack()
            lab = tk.Label(shb1, bg='white')
            lab.pack()
            but_exit = tk.Button(shb1, text='Close', fg='black', bg='tomato', font=('Agency FB', 12), height=3,
                                 width=30,
                                 command=shb1.destroy)
            but_exit.pack()
            lab = tk.Label(shb1, bg='white')
            lab.pack()
            shb1.mainloop()

        searchbk = tk.Tk()
        searchbk.title("Search Book")
        searchbk.geometry("800x400")
        searchbk.resizable(0, 0)
        searchbk.configure(bg='royal blue1')
        bidd = tk.StringVar(searchbk)
        frame1 = tk.Frame(searchbk, pady=30, bg='royal blue1')
        lable1 = tk.Label(frame1, text='Enter something to search: ', fg='white', bg='royal blue1',
                          font=('Agency FB', 24))
        lable1.pack(side='left')
        biddd = tk.Entry(frame1, textvariable=bidd, font=('Agency FB', 24))
        biddd.pack(side='left')
        frame1.pack()
        lable1 = tk.Label(searchbk, text="Note: Enter proper Book Id only to get unique result.  \n\
                        If you don't know the Book Id then you can search with   \n\
                        any other attribute like book name,author,publisher,   \n\
                        price,borrower's name,date of issue or date of submission\n\
                        etc but it may show multiple results.                      ", fg='white', bg='royal blue1',
                          font=('Agency FB', 24))
        lable1.pack()
        frame4 = tk.Frame(searchbk, bg='royal blue1')
        but_register = tk.Button(frame4, text='Search', fg='black', bg='light cyan', font=('Agency FB', 14), height=3,
                                 width=30, command=searching_book)
        but_register.pack(side='right')
        lab1 = tk.Label(frame4, padx=25, bg='royal blue1')
        lab1.pack(side='right')
        but_exit = tk.Button(frame4, text='Close', fg='black', bg='tomato', font=('Agency FB', 14), height=3, width=30,
                             command=searchbk.destroy)
        but_exit.pack(side='right')
        frame4.pack()

        searchbk.mainloop()
        ##def update_book():                ############################################
        pass

    def delete_book():
        def del_book():
            def deleting_book():
                nonlocal bi
                val = []
                val.append(bi)
                sql_q = 'delete from LIB_DB where bid=?'
                cur1.execute(sql_q, val)
                db1.commit()
                msg("Successfully deleted!", bi + " book deleted successfully!")

            shb11 = tk.Tk()
            shb11.title('Are you sure you want to delete it?')
            shb11.geometry("1000x700")
            shb11.resizable(0, 0)
            shb11.configure(bg='white')
            st = tk.StringVar(shb11)
            sp = tk.StringVar(shb11)
            st = ''
            sp = '     '
            bi = biddd0.get()
            val = []
            # for i in range(0,6):
            val.append(bi)
            sql_q = 'select * from LIB_DB where bid=?'
            result = cur1.execute(sql_q, val)
            data = result.fetchall()
            if len(data) == 0:
                shb11.title('Not Found!')
                shb11.geometry("400x150")
                lab = tk.Label(shb11, text='   Book Id not found!   ', fg='blue', bg='white', font=('Agency FB', 18))
                lab.pack()
                but_exit10 = tk.Button(shb11, text='Close', fg='black', bg='tomato', font=('Agency FB', 12), height=3,
                                       width=30,
                                       command=shb11.destroy)
                but_exit10.pack()
            else:
                st = "\nFound a record!\nAre you sure you want to delete it?\n\n"
                st = st + "________________________________________________________________________________________________________________________________________________________________\n\n" + format(
                    'BOOK ID', '11') + sp + format('BOOK NAME', '15') + sp + format('AUTHOR NAME', '15') + sp + format(
                    'PUBLISHER NAME', '15') + sp + format('PRICE', '13') + sp + format('BORROWER', '15') + sp + format(
                    'ISSUE DATE', '10') + sp + format('SUBMISSION DATE',
                                                      '10') + "\n________________________________________________________________________________________________________________________________________________________________\n\n"
                for row in data:
                    st = st + format(row[0], '11') + sp + format(row[1], '15') + sp + format(row[2],
                                                                                             '15') + sp + format(row[3],
                                                                                                                 '15') + sp + format(
                        row[4], '13') + sp + format(row[5], '15') + sp + format(row[6], '10') + sp + format(row[7],
                                                                                                            '10') + "\n"
                lab = tk.Label(shb11, text=st, fg='blue', bg='white', font=('Agency FB', 18))
                lab.pack()
                lab = tk.Label(shb11, bg='white')
                lab.pack()
                frame400 = tk.Frame(shb11, bg='white')
                but = tk.Button(frame400, text="Delete Book", fg='black', bg='tomato', font=('Agency FB', 12), height=3,
                                width=30,
                                command=deleting_book)
                but.pack(side='right')
                lab = tk.Label(frame400, text='          ', bg='white')
                lab.pack(side='right')
                but_exit = tk.Button(frame400, text='Close', fg='black', bg='tomato', font=('Agency FB', 12), height=3,
                                     width=30,
                                     command=shb11.destroy)
                but_exit.pack(side='right')
                frame400.pack()

            lab = tk.Label(shb11, bg='white')
            lab.pack()
            shb11.mainloop()

        searchbk11 = tk.Tk()
        searchbk11.title("Delete Book")
        searchbk11.geometry("600x360")
        searchbk11.resizable(0, 0)
        searchbk11.configure(bg='royal blue1')
        bidd0 = tk.StringVar(searchbk11)
        frame1 = tk.Frame(searchbk11, pady=30, bg='royal blue1')
        lable1 = tk.Label(frame1, text='Enter Book Id : ', fg='white', bg='royal blue1', font=('Agency FB', 24))
        lable1.pack(side='left')
        biddd0 = tk.Entry(frame1, textvariable=bidd0, font=('Agency FB', 24))
        biddd0.pack(side='left')
        frame1.pack()
        lable1 = tk.Label(searchbk11, text="   ", bg='royal blue1')
        lable1.pack()
        frame4 = tk.Frame(searchbk11, bg='royal blue1')
        lab1 = tk.Label(frame4, padx=25, bg='royal blue1')
        lab1.pack(side='right')

        but_register = tk.Button(frame4, text='Search Book', fg='black', bg='light cyan', font=('Agency FB', 14),
                                 height=3,
                                 width=30, command=search_book)
        but_register.pack(side='right')
        lab1 = tk.Label(frame4, padx=25, bg='royal blue1')
        lab1.pack(side='right')

        but_register = tk.Button(frame4, text='Show all books', fg='black', bg='light cyan', font=('Agency FB', 14),
                                 height=3,
                                 width=30, command=show_all_books)
        but_register.pack(side='right')
        lab1 = tk.Label(frame4, padx=25, bg='royal blue1')
        lab1.pack(side='right')
        frame4.pack()
        lab = tk.Label(searchbk11, bg='royal blue1')
        lab.pack()
        frame5 = tk.Frame(searchbk11, bg='royal blue1')
        lab1 = tk.Label(frame5, padx=25, bg='royal blue1')
        lab1.pack(side='right')
        but_register = tk.Button(frame5, text='Delete', fg='black', bg='tomato', font=('Agency FB', 14), height=3,
                                 width=30, command=del_book)
        but_register.pack(side='right')
        lab1 = tk.Label(frame5, padx=25, bg='royal blue1')
        lab1.pack(side='right')
        but_exit = tk.Button(frame5, text='Close', fg='black', bg='tomato', font=('Agency FB', 14), height=3, width=30,
                             command=searchbk11.destroy)
        but_exit.pack(side='right')
        lab1 = tk.Label(frame5, padx=25, bg='royal blue1')
        lab1.pack(side='right')

        frame5.pack()

        searchbk11.mainloop()

    def show_constraints():
        sc = tk.Tk()
        sc.geometry("1000x600")
        sc.resizable(0, 0)
        sc.title("Input Restrictions")
        lab = tk.Label(sc,
                       text="There are two tables.One is for user details and the another one is for library contents.    \n\
                             For library contents:Book Id should be unique and it should start with B.Book Id should      \n\
                             have minimum 1 to maximum 11 characters.Book name can have maximum 100 characters and        \n\
                             should not be null.Author name can have maximum 100 characters and should not be null.       \n\
                             Publisher name can have maximum 100 characters and should not be null.Price should be        \n\
                             number 10 digits are allowed before point and 2 digits after point and it should not be null     \n\
                             In case of issueing a book date of issue and date of submission should be dates in dd/mm/yyyy\n\
                             format(eg:20/12/2018).Now for another table which is for User details:                       \n\
                             Name can be maximum 500 characters long and should not be null                               \n\
                             Username can be minimum 6 to maximum 100 characters long and                                 \n\
                             should not be null and it should be unique.If the username already                           \n\
                             exists then database insertion error will occur.Email Id can be maximum                      \n\
                             100 characters long and should not be null.Phone number should be 12                         \n\
                             characters long and should not be null and it should contain numbers                         \n\
                             only.Password should be minimum 6 to maximum 16 characters long and                          \n\
                             should not be null.Address can be maximum 100 characters and should                          \n\
                             not be null                                                                                  \n",
                       font=('Agency FB', 18))

        lab.pack()
        but = tk.Button(sc, text='Close', font=('Agency FB', 12), bg='tomato', height=3, width=35,
                        command=sc.destroy)
        but.pack()
        sc.mainloop()

    def show_constraints_user():
        scu = tk.Tk()
        # scu.geometry("1000x500")
        scu.resizable(0, 0)
        scu.title("Input Restrictions")
        lab = tk.Label(scu,
                       text="\
Name can be maximum 500 characters long and should not be null         \n\
Username can be minimum 6 to maximum 100 characters long and           \n\
should not be null and it should be unique.If the username already     \n\
exists then database insertion error will occur.Email Id can be maximum\n\
100 characters long and should not be null.Phone number should be 12   \n\
characters long and should not be null and it should contain numbers   \n\
only.Password should be minimum 6 to maximum 16 characters long and    \n\
should not be null.Address can be maximum 100 characters and should    \n\
not be null\n"
                       , font=('Agency FB', 18))

        lab.pack()
        but = tk.Button(scu, text='Close', font=('Agency FB', 12), bg='tomato', height=3, width=35,
                        command=scu.destroy)
        but.pack()
        scu.mainloop()

    def register():
        reset()

        def reg_submit():
            fg = 0
            try:
                rg1 = u1.get()
                rg2 = u2.get()
                rg3 = u3.get()
                rg4 = int(u4.get())
                rg5 = u5.get()
                rg6 = u6.get()
                rg7 = u7.get()
                if rg5 == rg6:
                    l = len(rg5)
                    l1 = len(rg2)
                    if (l <= 16 and l >= 6) and (l1 >= 6 and l1 <= 100):

                        rg5 = sencript(rg5)
                        val = []
                        val.append(rg1)
                        val.append(rg2)
                        val.append(rg3)
                        val.append(rg4)
                        val.append(rg5)
                        val.append(rg7)
                        sql_q = "insert into USER_DB values(?,?,?,?,?,?)"
                        cur.execute(sql_q, val)
                        db.commit()
                    else:
                        fg = 1
                        plh = tk.Tk()
                        plh.resizable(0, 0)
                        plh.title("Username or Password Length Error!")
                        lab = tk.Label(plh,
                                       text="Username or Password Length Error!\nUsername should be minimum 6 to maximum 100 characters long...\nPassword should be minimum 6 to maximum 16 characters long...\n",
                                       font=('Agency FB', 18))

                        lab.pack()
                        but = tk.Button(plh, text='Close', font=('Agency FB', 10), bg='tomato', height=3, width=25,
                                        command=plh.destroy)
                        but.pack()
                        lab = tk.Label(plh)
                        lab.pack()
                        plh.mainloop()
                else:
                    fg = 1
                    pwd_mismatch_error()
            except:
                fg = 1
                db.rollback()
                #db_in_error()
                msg("Database Insertion Error","Check your input!\nUsername may be already taken or you have given some invalid input!\nCheck input restrictions for help")

            if (fg == 0):
                db_in_success()

        reg = tk.Tk()
        reg.geometry("1000x800")
        reg.resizable(0, 0)
        reg.configure(bg='royal blue1')
        reg.title("Register")
        name = tk.StringVar(reg)
        uname = tk.StringVar(reg)
        email = tk.StringVar(reg)
        phone = tk.StringVar(reg)
        pwd = tk.StringVar(reg)
        cpwd = tk.StringVar(reg)
        add = tk.StringVar(reg)
        frame1 = tk.Frame(reg, pady=10, bg='royal blue1')
        lable1 = tk.Label(frame1, text='Enter Name           : ', fg='white', bg='royal blue1', font=('Agency FB', 24),
                          padx=25)
        lable1.pack(side='left')
        u1 = tk.Entry(frame1, textvariable=name, font=('Agency FB', 24))
        u1.pack(side='left')
        frame1.pack()

        frame2 = tk.Frame(reg, pady=10, bg='royal blue1')
        lable1 = tk.Label(frame2, text='Enter Unique Username: ', fg='white', bg='royal blue1', font=('Agency FB', 24),
                          padx=25)
        lable1.pack(side='left')
        u2 = tk.Entry(frame2, textvariable=uname, font=('Agency FB', 24))
        u2.pack(side='left')
        frame2.pack()

        frame3 = tk.Frame(reg, pady=10, bg='royal blue1')
        lable1 = tk.Label(frame3, text='Enter Email Id       : ', fg='white', bg='royal blue1', font=('Agency FB', 24),
                          padx=25)
        lable1.pack(side='left')
        u3 = tk.Entry(frame3, textvariable=email, font=('Agency FB', 24))
        u3.pack(side='left')
        frame3.pack()

        frame4 = tk.Frame(reg, pady=10, bg='royal blue1')
        lable1 = tk.Label(frame4, text='Enter Phone Number   : ', fg='white', bg='royal blue1', font=('Agency FB', 24),
                          padx=25)
        lable1.pack(side='left')
        u4 = tk.Entry(frame4, textvariable=phone, font=('Agency FB', 24))
        u4.pack(side='left')
        frame4.pack()

        frame5 = tk.Frame(reg, pady=10, bg='royal blue1')
        lable2 = tk.Label(frame5, text='Enter Password       : ', fg='white', bg='royal blue1', font=('Agency FB', 24),
                          padx=25)
        lable2.pack(side='left')
        u5 = tk.Entry(frame5, show='*', textvariable=pwd, font=('Agency FB', 24))
        u5.pack(side='left')
        frame5.pack()

        frame6 = tk.Frame(reg, pady=10, bg='royal blue1')
        lable2 = tk.Label(frame6, text='Confirm Password     : ', fg='white', bg='royal blue1', font=('Agency FB', 24),
                          padx=25)
        lable2.pack(side='left')
        u6 = tk.Entry(frame6, show='*', textvariable=cpwd, font=('Agency FB', 24))
        u6.pack(side='left')
        frame6.pack()

        frame48 = tk.Frame(reg, pady=10, bg='royal blue1')
        lable1 = tk.Label(frame48, text='Enter address       : ', fg='white', bg='royal blue1', font=('Agency FB', 24),
                          padx=25)
        lable1.pack(side='left')
        u7 = tk.Entry(frame48, textvariable=add, font=('Agency FB', 24))
        u7.pack(side='left')
        frame48.pack()

        frame7 = tk.Frame(reg, bg='royal blue1')
        but_register = tk.Button(frame7, text='Submit', fg='black', bg='tomato', font=('Agency FB', 16), height=3,
                                 width=30, command=reg_submit)
        but_register.pack(side='right')
        lab1 = tk.Label(frame7, padx=25, bg='royal blue1')
        lab1.pack(side='right')
        but = tk.Button(frame7, text='Show Input Restrictions', fg='black', bg='light cyan', font=('Agency FB', 16),
                        height=3,
                        width=30, command=show_constraints_user)
        but.pack(side='right')
        lab1 = tk.Label(frame7, padx=25, bg='royal blue1')
        lab1.pack(side='right')
        but_exit = tk.Button(frame7, text='Close', fg='black', bg='tomato', font=('Agency FB', 16), height=3, width=30,
                             command=reg.destroy)
        but_exit.pack(side='right')
        frame7.pack()
        reg.mainloop()

    def show_all_users():
        shu = tk.Tk()
        shu.title('Show all Users')
        shu.resizable(0, 0)
        shu.configure(bg='white')
        st = tk.StringVar(shu)
        sp = tk.StringVar(shu)
        st = ''
        sp = '     '
        result = cur.execute('select name,username,email,phone,address from USER_DB')
        data = result.fetchall()
        f1 = tk.Frame(shu)
        scrollbar = tk.Scrollbar(shu)
        scrollbar.pack(side='right', fill='y')
        scrollbar1 = tk.Scrollbar(shu)
        scrollbar1.pack(side='bottom',fill='x')
        mylist = tk.Listbox(f1,height=20,width=90, yscrollcommand=scrollbar.set,xscrollcommand=scrollbar1.set)
        mylist.config(font=('Agency FB', '16'))
        st = format('NAME', '15') + sp + format('USERNAME', '15') + sp + format('EMAIL ID', '15') + sp + format('PHONE NUMBER','12') + sp + format('ADDRESS','15')
        mylist.insert(END, "__________________________________________________________________________________________________________________________")
        mylist.insert(END,'')
        mylist.insert(END,st)
        mylist.insert(END,"___________________________________________________________________________________________________________________________")
        for row in data:
            st = format(row[0], '15') + sp + format(row[1], '15') + sp + format(row[2], '15') + sp + format(row[3],'15') + sp + format(row[4], '15')
            mylist.insert(END,st)
            mylist.insert(END,'')
        mylist.pack(side='left', fill='both')
        scrollbar.config(command=mylist.yview)
        scrollbar1.config(command=mylist.xview,orient=HORIZONTAL)
        f1.pack()
        lab = tk.Label(shu, bg='white')
        lab.pack()
        but_exit = tk.Button(shu, text='Close', fg='black', bg='tomato', font=('Agency FB', 12), height=3, width=30,
                             command=shu.destroy)
        but_exit.pack()
        lab = tk.Label(shu, bg='white')
        lab.pack()
        shu.mainloop()

    def search_user():
        def searching_user():
            shb2 = tk.Tk()
            shb2.title('Search Result')
            shb2.resizable(0, 0)
            shb2.configure(bg='white')
            st = tk.StringVar(shb2)
            sp = tk.StringVar(shb2)
            st = ''
            sp = '     '
            # bn1=bnameee1.get()
            bi1 = biddd1.get()
            val = []
            for i in range(0, 5):
                val.append(bi1)
            sql_q = 'select name,username,email,phone,address from USER_DB where username=? or name=? or email=? or phone=? or address=?'
            result = cur.execute(sql_q, val)
            data = result.fetchall()
            if len(data) == 0:
                st = 'No Such Record Found!'
            else:
                f1 = tk.Frame(shb2)
                scrollbar = tk.Scrollbar(shb2)
                scrollbar.pack(side='right', fill='y')
                scrollbar1 = tk.Scrollbar(shb2)
                scrollbar1.pack(side='bottom',fill='x')
                mylist = tk.Listbox(f1,height=20,width=90, yscrollcommand=scrollbar.set,xscrollcommand=scrollbar1.set)
                #mylist = tk.Listbox(f1, height=20, width=90, yscrollcommand=scrollbar.set)
                mylist.config(font=('Agency FB', '16'))
                st = format('NAME', '15') + sp + format('USERNAME', '15') + sp + format('EMAIL ID', '15') + sp + format('PHONE NUMBER','12') + sp + format('ADDRESS','15')
                mylist.insert(END, "__________________________________________________________________________________________________________________________")
                mylist.insert(END,'')
                mylist.insert(END,st)
                mylist.insert(END,"___________________________________________________________________________________________________________________________")
                for row in data:
                    st = format(row[0], '15') + sp + format(row[1], '15') + sp + format(row[2], '15') + sp + format(row[3],
                                                                                                                         '15') + sp + format(
                        row[4], '15')

                    #l=len(st)
                    #print('line=',l)
                    mylist.insert(END,st)
                    mylist.insert(END,'')
                    #print(st)
                mylist.pack(side='left', fill='both')
                scrollbar.config(command=mylist.yview)
                scrollbar1.config(command=mylist.xview,orient=HORIZONTAL)
                f1.pack()
            but_exit = tk.Button(shb2, text='Close', fg='black', bg='tomato', font=('Agency FB', 12), height=3,
                                         width=30,
                                         command=shb2.destroy)
            but_exit.pack()
            lab = tk.Label(shb2, bg='white')
            lab.pack()
            shb2.mainloop()

        searchbk1 = tk.Tk()
        searchbk1.title("Search User")
        searchbk1.geometry("800x400")
        searchbk1.resizable(0, 0)
        searchbk1.configure(bg='royal blue1')
        bidd1 = tk.StringVar(searchbk1)
        frame1 = tk.Frame(searchbk1, pady=30, bg='royal blue1')
        lable1 = tk.Label(frame1, text='Enter something to search: ', fg='white', bg='royal blue1',
                          font=('Agency FB', 24))
        lable1.pack(side='left')
        biddd1 = tk.Entry(frame1, textvariable=bidd1, font=('Agency FB', 24))
        biddd1.pack(side='left')
        frame1.pack()
        lable1 = tk.Label(searchbk1, text="Note: Enter proper Username only to get unique result.  \n\
                        If you don't know the username then you can search with   \n\
                        any other attribute like name,email id,phone number   \n\
                        but it may show multiple results.   ", fg='white', bg='royal blue1', font=('Agency FB', 24))
        lable1.pack()
        frame4 = tk.Frame(searchbk1, bg='royal blue1')
        but_register = tk.Button(frame4, text='Search', fg='black', bg='light cyan', font=('Agency FB', 14), height=3,
                                 width=30, command=searching_user)
        but_register.pack(side='right')
        lab1 = tk.Label(frame4, padx=25, bg='royal blue1')
        lab1.pack(side='right')
        but_exit = tk.Button(frame4, text='Close', fg='black', bg='tomato', font=('Agency FB', 14), height=3, width=30,
                             command=searchbk1.destroy)
        but_exit.pack(side='right')
        frame4.pack()

        searchbk1.mainloop()

    def update_user():
        def set_update():
            def updating():
                nonlocal uname_up
                phn1 = phn.get()
                em1 = em.get()
                ad1 = ad.get()
                sql_q = 'update USER_DB set phone=?,email=?,address=? where username=?'
                val = []
                val.append(phn1)
                val.append(em1)
                val.append(ad1)
                val.append(uname_up)
                cur.execute(sql_q, val)
                db.commit()
                msg("Successfully updated!", "The account was successfully updated!")

            uname_up = uname.get()
            v = []
            v.append(uname_up)
            sql_q = 'select phone,email,address from USER_DB where username=?'
            result1 = cur.execute(sql_q, v)
            data1 = result1.fetchone()
            if data1 != None:
                uu1 = tk.Tk()
                uu1.title("Enter new values to update:")
                uu1.resizable(0, 0)
                uu1.configure(bg='royal blue1')
                old_phn = tk.StringVar(uu1)
                old_email = tk.StringVar(uu1)
                old_address = tk.StringVar(uu1)
                old_phn.set(data1[0])
                old_email.set(data1[1])
                old_address.set(data1[2])
                lab = tk.Label(uu1, bg='royal blue1', text=' ')
                lab.pack()

                frame1 = tk.Frame(uu1, bg='royal blue1')
                lab = tk.Label(frame1, bg='royal blue1', fg='white', text='  Enter New Phone Number : ',
                               font=("Agency FB", 20))
                lab.pack()
                phn = tk.Entry(frame1, textvariable=old_phn, font=('Agency FB', 20))
                phn.pack()
                lab = tk.Label(frame1, bg='royal blue1', text='  ')
                lab.pack()
                frame1.pack()

                lab = tk.Label(uu1, bg='royal blue1', text='  ')
                lab.pack()

                frame2 = tk.Frame(uu1, bg='royal blue1')
                lab = tk.Label(frame2, bg='royal blue1', fg='white', text='  Enter New Email Id : ',
                               font=("Agency FB", 20))
                lab.pack()
                em = tk.Entry(frame2, textvariable=old_email, font=('Agency FB', 20))
                em.pack()
                lab = tk.Label(frame2, bg='royal blue1', text='  ')
                lab.pack()
                frame2.pack()

                frame3 = tk.Frame(uu1, bg='royal blue1')
                lab = tk.Label(frame3, bg='royal blue1', fg='white', text='  Enter New Address : ',
                               font=("Agency FB", 20))
                lab.pack()
                ad = tk.Entry(frame3, textvariable=old_address, font=('Agency FB', 20))
                ad.pack()
                lab = tk.Label(frame3, bg='royal blue1', text='  ')
                lab.pack()
                frame3.pack()

                lab = tk.Label(uu1, bg='royal blue1', text='  ')
                lab.pack()

                frame4 = tk.Frame(uu1, bg='royal blue1')
                but = tk.Button(frame4, text='Close', fg='black', bg='light cyan', font=('Agency FB', 14), height=3,
                                width=30, command=uu1.destroy)
                but.pack()
                lab = tk.Label(frame4, bg='royal blue1', text='  ')
                lab.pack()
                but = tk.Button(frame4, text='Update', fg='black', bg='tomato', font=('Agency FB', 14), height=3,
                                width=30, command=updating)
                but.pack()
                frame4.pack()
                uu1.mainloop()
            else:
                msg("Username not found!", "Username not found!")

        uu = tk.Tk()
        uu.title("Enter username to update:")
        uu.resizable(0, 0)
        lab = tk.Label(uu, text=' ')
        lab.pack()
        uname1 = tk.StringVar(uu)
        frame1 = tk.Frame(uu)
        lab = tk.Label(frame1, text='  Enter Username : ', font=("Agency FB", 20))
        lab.pack(side='left')
        uname = tk.Entry(frame1, textvariable=uname1, font=('Agency FB', 20))
        uname.pack(side='left')
        frame1.pack()

        lab = tk.Label(uu, text=' ')

        frame2 = tk.Frame(uu)
        lab.pack()
        but = tk.Button(frame2, text='Close', fg='black', bg='tomato', font=('Agency FB', 14), height=3, width=30,
                        command=uu.destroy)
        but.pack(side='left')
        but = tk.Button(frame2, text='Update', fg='black', bg='light cyan', font=('Agency FB', 14), height=3, width=30,
                        command=set_update)
        but.pack(side='left')
        frame2.pack()
        lab = tk.Label(uu, text=' ')
        lab.pack()
        uu.mainloop()

    def delete_user():
        def del_user():
            def deleting_user():
                nonlocal bii
                val = []
                val.append(bii)
                sql_q = 'delete from USER_DB where username=?'
                cur.execute(sql_q, val)
                db.commit()
                msg("Account deleted Successfully!", bii + " was deleted successfully!")

            shb111 = tk.Tk()
            shb111.title('Are you sure you want to delete this account?')
            shb111.geometry("1000x700")
            shb111.resizable(0, 0)
            shb111.configure(bg='white')
            st = tk.StringVar(shb111)
            sp = tk.StringVar(shb111)
            st = ''
            sp = '     '
            bii = biddd00.get()
            val = []
            # for i in range(0,6):
            val.append(bii)
            sql_q = 'select Name,username,email,phone,address from USER_DB where username=?'
            result = cur.execute(sql_q, val)
            data = result.fetchall()
            if len(data) == 0:
                shb111.title('Not Found!')
                shb111.geometry("400x150")
                lab = tk.Label(shb111, text='   Username not found!   ', fg='blue', bg='white', font=('Agency FB', 18))
                lab.pack()
                but_exit10 = tk.Button(shb111, text='Close', fg='black', bg='tomato', font=('Agency FB', 12), height=3,
                                       width=30,
                                       command=shb111.destroy)
                but_exit10.pack()
            else:
                st = "\nFound a record!\nAre you sure you want to delete this account?\n\n_______________________________________________________________________________________________________\n\n" + format(
                    'NAME', '15') + sp + format('USERNAME', '15') + sp + format('EMAIL ID', '15') + sp + format(
                    'PHONE NUMBER', '15') + sp + format("ADDRESS",
                                                        "15") + "\n_______________________________________________________________________________________________________\n\n"
                for row in data:
                    st = st + format(row[0], '15') + sp + format(row[1], '15') + sp + format(row[2],
                                                                                             '15') + sp + format(row[3],
                                                                                                                 '15') + sp + format(
                        row[4], '15') + "\n"
                lab = tk.Label(shb111, text=st, fg='blue', bg='white', font=('Agency FB', 18))
                lab.pack()
                lab = tk.Label(shb111, bg='white')
                lab.pack()
                frame400 = tk.Frame(shb111, bg='white')
                but = tk.Button(frame400, text="Delete Account", fg='black', bg='tomato', font=('Agency FB', 12),
                                height=3, width=30,
                                command=deleting_user)
                but.pack(side='right')
                lab = tk.Label(frame400, text='          ', bg='white')
                lab.pack(side='right')
                but_exit = tk.Button(frame400, text='Close', fg='black', bg='tomato', font=('Agency FB', 12), height=3,
                                     width=30,
                                     command=shb111.destroy)
                but_exit.pack(side='right')
                frame400.pack()

            lab = tk.Label(shb111, bg='white')
            lab.pack()
            shb111.mainloop()

        searchbk111 = tk.Tk()
        searchbk111.title("Delete User")
        searchbk111.geometry("600x360")
        searchbk111.resizable(0, 0)
        searchbk111.configure(bg='royal blue1')
        bidd00 = tk.StringVar(searchbk111)
        frame1 = tk.Frame(searchbk111, pady=30, bg='royal blue1')
        lable1 = tk.Label(frame1, text='Enter Username : ', fg='white', bg='royal blue1', font=('Agency FB', 24))
        lable1.pack(side='left')
        biddd00 = tk.Entry(frame1, textvariable=bidd00, font=('Agency FB', 24))
        biddd00.pack(side='left')
        frame1.pack()
        lable1 = tk.Label(searchbk111, bg='royal blue1')
        lable1.pack()
        frame4 = tk.Frame(searchbk111, bg='royal blue1')
        lab1 = tk.Label(frame4, padx=25, bg='royal blue1')
        lab1.pack(side='right')

        but_register = tk.Button(frame4, text='Search user', fg='black', bg='light cyan', font=('Agency FB', 14),
                                 height=3,
                                 width=30, command=search_user)
        but_register.pack(side='right')
        lab1 = tk.Label(frame4, padx=25, bg='royal blue1')
        lab1.pack(side='right')

        but_register = tk.Button(frame4, text='Show all users', fg='black', bg='light cyan', font=('Agency FB', 14),
                                 height=3,
                                 width=30, command=show_all_users)
        but_register.pack(side='right')
        lab1 = tk.Label(frame4, padx=25, bg='royal blue1')
        lab1.pack(side='right')
        frame4.pack()
        lab = tk.Label(searchbk111, bg='royal blue1')
        lab.pack()
        frame5 = tk.Frame(searchbk111, bg='royal blue1')
        lab1 = tk.Label(frame5, padx=25, bg='royal blue1')
        lab1.pack(side='right')
        but_register = tk.Button(frame5, text='Delete', fg='black', bg='tomato', font=('Agency FB', 14), height=3,
                                 width=30, command=del_user)
        but_register.pack(side='right')
        lab1 = tk.Label(frame5, padx=25, bg='royal blue1')
        lab1.pack(side='right')
        but_exit = tk.Button(frame5, text='Close', fg='black', bg='tomato', font=('Agency FB', 14), height=3, width=30,
                             command=searchbk111.destroy)
        but_exit.pack(side='right')
        lab1 = tk.Label(frame5, padx=25, bg='royal blue1')
        lab1.pack(side='right')

        frame5.pack()

        searchbk111.mainloop()

    def show_all_issued_book():
        val = []
        val.append("None")
        sql_q = 'select * from LIB_DB where br_by!=?'
        result = cur1.execute(sql_q, val)
        data = result.fetchall()
        st = ''
        sp = '     '
        if len(data) == 0:
            msg('No book is borrowed or issued!','No book is borrowed or issued!')
        else:
                shb = tk.Tk()
                shb.title('Show all issued books')
                #shb.geometry("1000x700")
                shb.resizable(0, 0)
                shb.configure(bg='white')
                st = tk.StringVar(shb)
                sp = tk.StringVar(shb)
                st = ''
                sp = '     '
                sh = ' '
                st = 'book id'.ljust(11,sh) + sp + 'book name'.ljust(15,sh) + sp + 'author name'.ljust(15,sh) + sp + 'publisher name'.ljust(15,sh) + sp + 'price'.ljust(13,sh) + sp + 'borrower'.ljust(15,sh)+ sp + 'issue'.ljust(10,sh)+ sp + 'submission'.ljust(10,sh)
                '''st = format(
                        'book id', '15') + sp + format('book name', '15') + sp + format('author', '15') + sp + format(
                        'publisher', '15') + sp + format('price', '12') + sp + format('borrower', '15') + sp + format(
                        'issue', '10') + sp + format('submission','10')'''
                #l = len(st)
                #print('line -1=',l,st)
                #print(st)
                f1 = tk.Frame(shb)
                scrollbar = tk.Scrollbar(shb)
                scrollbar.pack(side='right', fill='y')
                scrollbar1 = tk.Scrollbar(shb)
                scrollbar1.pack(side='bottom',fill='x')
                mylist = tk.Listbox(f1,height=20,width=90, yscrollcommand=scrollbar.set,xscrollcommand=scrollbar1.set)
                #mylist = tk.Listbox(f1, height=20, width=90, yscrollcommand=scrollbar.set)
                mylist.config(font=('Agency FB', '16'))
                mylist.insert(END, "__________________________________________________________________________________________________________________________")
                mylist.insert(END,'')
                mylist.insert(END,st)
                mylist.insert(END,"___________________________________________________________________________________________________________________________")
                for row in data:
                    bid=str(row[0])
                    bname=str(row[1])
                    author=str(row[2])
                    publisher=str(row[3])
                    price=str(row[4])
                    br_by=str(row[5])
                    doi=str(row[6])
                    dos=str(row[7])
                    st = bid.ljust(11,sh) + sp + bname.ljust(15,sh) + sp + author.ljust(15,sh) + sp + publisher.ljust(15,sh) + sp + price.ljust(13,sh) + sp + br_by.ljust(15,sh) + sp + doi.ljust(10,sh)+ sp + dos.ljust(10,sh)
                    '''st=format(row[0], '11') + sp + format(row[1], '15') + sp + format(row[2], '15') + sp + format(row[3],
                                                                                                               '15') + sp + format(
                        row[4], '12') + sp + format(row[5], '15') + sp + format(row[6], '10') + sp + format(row[7], '10')'''
                    #l=len(st)
                    #print('line=',l)
                    mylist.insert(END,st)
                    mylist.insert(END, '')
                    #print(st)
                mylist.pack(side='left', fill='both')
                scrollbar.config(command=mylist.yview)
                scrollbar1.config(orient=HORIZONTAL,command=mylist.xview)
                f1.pack()
                #lab = tk.Label(shb, text=st, fg='blue', bg='white', font=('Agency FB', 18))
                #lab.pack()

                lab = tk.Label(shb, bg='white')
                lab.pack()
                but_exit = tk.Button(shb, text='Close', fg='black', bg='tomato', font=('Agency FB', 12), height=3, width=30,
                                     command=shb.destroy)
                but_exit.pack()
                lab = tk.Label(shb, bg='white')
                lab.pack()
                shb.mainloop()
    

    def show_user_issued_book(u):
        val = []
        val.append(u)
        sql_q = 'select * from LIB_DB where br_by==?'
        result = cur1.execute(sql_q, val)
        data = result.fetchall()
        st = ''
        sp = '     '
        if len(data) == 0:
            msg("All Issued Books!", 'No book is borrowed by ' + u + '!')
        else:
                shb = tk.Tk()
                shb.title('All issued books')
                #shb.geometry("1000x700")
                shb.resizable(0, 0)
                shb.configure(bg='white')
                st = tk.StringVar(shb)
                sp = tk.StringVar(shb)
                st = ''
                sp = '     '
                sh = ' '
                st = 'book id'.ljust(11,sh) + sp + 'book name'.ljust(15,sh) + sp + 'author name'.ljust(15,sh) + sp + 'publisher name'.ljust(15,sh) + sp + 'price'.ljust(13,sh) + sp + 'borrower'.ljust(15,sh)+ sp + 'issue'.ljust(10,sh)+ sp + 'submission'.ljust(10,sh)
                '''st = format(
                        'book id', '15') + sp + format('book name', '15') + sp + format('author', '15') + sp + format(
                        'publisher', '15') + sp + format('price', '12') + sp + format('borrower', '15') + sp + format(
                        'issue', '10') + sp + format('submission','10')'''
                #l = len(st)
                #print('line -1=',l,st)
                #print(st)
                f1 = tk.Frame(shb)
                scrollbar = tk.Scrollbar(shb)
                scrollbar.pack(side='right', fill='y')
                scrollbar1 = tk.Scrollbar(shb)
                scrollbar1.pack(side='bottom',fill='x')
                mylist = tk.Listbox(f1,height=20,width=90, yscrollcommand=scrollbar.set,xscrollcommand=scrollbar1.set)
                #mylist = tk.Listbox(f1, height=20, width=90, yscrollcommand=scrollbar.set)
                mylist.config(font=('Agency FB', '16'))
                mylist.insert(END, "__________________________________________________________________________________________________________________________")
                mylist.insert(END,'')
                mylist.insert(END,st)
                mylist.insert(END,"___________________________________________________________________________________________________________________________")
                for row in data:
                    bid=str(row[0])
                    bname=str(row[1])
                    author=str(row[2])
                    publisher=str(row[3])
                    price=str(row[4])
                    br_by=str(row[5])
                    doi=str(row[6])
                    dos=str(row[7])
                    st = bid.ljust(11,sh) + sp + bname.ljust(15,sh) + sp + author.ljust(15,sh) + sp + publisher.ljust(15,sh) + sp + price.ljust(13,sh) + sp + br_by.ljust(15,sh) + sp + doi.ljust(10,sh)+ sp + dos.ljust(10,sh)
                    '''st=format(row[0], '11') + sp + format(row[1], '15') + sp + format(row[2], '15') + sp + format(row[3],
                                                                                                               '15') + sp + format(
                        row[4], '12') + sp + format(row[5], '15') + sp + format(row[6], '10') + sp + format(row[7], '10')'''
                    #l=len(st)
                    #print('line=',l)
                    mylist.insert(END,st)
                    mylist.insert(END, '')
                    #print(st)
                mylist.pack(side='left', fill='both')
                scrollbar.config(command=mylist.yview)
                scrollbar1.config(orient=HORIZONTAL,command=mylist.xview)
                f1.pack()
                #lab = tk.Label(shb, text=st, fg='blue', bg='white', font=('Agency FB', 18))
                #lab.pack()

                lab = tk.Label(shb, bg='white')
                lab.pack()
                but_exit = tk.Button(shb, text='Close', fg='black', bg='tomato', font=('Agency FB', 12), height=3, width=30,
                                     command=shb.destroy)
                but_exit.pack()
                lab = tk.Label(shb, bg='white')
                lab.pack()
                shb.mainloop()
    
        

    def issue_book_admin():
        def issuing_book_admin():
            un2 = un1.get()
            bk2 = bk1.get()
            did2 = did1.get()
            dim2 = dim1.get()
            diy2 = diy1.get()
            dsd2 = dsd1.get()
            dsm2 = dsm1.get()
            dsy2 = dsy1.get()
            issdate = did2 + '/' + dim2 + '/' + diy2
            subdate = dsd2 + '/' + dsm2 + '/' + dsy2
            sql_q = 'select username from USER_DB where username=?'
            val = []
            val.append(un2)
            result = cur.execute(sql_q, val)
            data = result.fetchone()
            sql_q1 = 'select br_by from LIB_DB where bid=?'
            val1 = []
            val1.append(bk2)
            result1 = cur1.execute(sql_q1, val1)
            data1 = result1.fetchone()
            if data == None:

                msg("Username not found!", "Username not found!")
            elif data1 == None:
                msg("Book Id not found!", "Book Id not found!")
            elif data1[0] != 'None':
                if data1[0] == un2:
                    msg("Oops!", "The user already borrowed this book!")
                else:
                    msg("Oops!", "The book is borrowed by another user!")
            elif data1[0] == 'None':
                sql_q = 'update LIB_DB set br_by=?,doi=?,dos=? where bid=?'
                v = []
                v.append(un2)
                v.append(issdate)
                v.append(subdate)
                v.append(bk2)
                cur1.execute(sql_q, v)
                db1.commit()
                msg("Updated!", "Book Issued Successfuly!")

        p = (str(now))
        p = p[:10]
        d = p.split('-')
        ib = tk.Tk()
        ib.title("Issue Book")
        ib.configure(bg='royal blue1')
        ib.geometry("1100x500")
        ib.resizable(0, 0)
        un = tk.StringVar(ib)
        bk = tk.StringVar(ib)
        did = tk.StringVar(ib)
        dim = tk.StringVar(ib)
        diy = tk.StringVar(ib)
        dsd = tk.StringVar(ib)
        dsm = tk.StringVar(ib)
        dsy = tk.StringVar(ib)
        did.set(d[2])
        dim.set(d[1])
        diy.set(d[0])
        lab = tk.Label(ib, text='  ', bg='royal blue1')
        lab.pack()
        frame1 = tk.Frame(ib, bg='royal blue1')
        lab = tk.Label(frame1, text='Enter Username :  ', fg='white', bg='royal blue1', font=('Agency FB', 20))
        lab.pack(side='left')
        un1 = tk.Entry(frame1, textvariable=un, font=('Agency FB', 20))
        un1.pack(side='left')
        lab = tk.Label(frame1, text='             Enter Book Id :  ', fg='white', bg='royal blue1',
                       font=('Agency FB', 20))
        lab.pack(side='left')
        bk1 = tk.Entry(frame1, textvariable=bk, font=('Agency FB', 20))
        bk1.pack(side='left')
        frame1.pack()

        lab = tk.Label(ib, text='\n\nEnter Date of Issue (DD/MM/YYYY) :  (Autogenerated by system)', fg='white',
                       bg='royal blue1', font=('Agency FB', 20))
        lab.pack()

        frame2 = tk.Frame(ib, bg='royal blue1')
        lab = tk.Label(frame2, text=' Day:  ', fg='white', bg='royal blue1', font=('Agency FB', 18))
        lab.pack(side='left')
        did1 = tk.Entry(frame2, textvariable=did, font=('Agency FB', 18))
        did1.pack(side='left')
        lab = tk.Label(frame2, text='     Month:  ', fg='white', bg='royal blue1', font=('Agency FB', 18))
        lab.pack(side='left')
        dim1 = tk.Entry(frame2, textvariable=dim, font=('Agency FB', 18))
        dim1.pack(side='left')
        lab = tk.Label(frame2, text='     Year:  ', fg='white', bg='royal blue1', font=('Agency FB', 18))
        lab.pack(side='left')
        diy1 = tk.Entry(frame2, textvariable=diy, font=('Agency FB', 18))
        diy1.pack(side='left')
        frame2.pack()

        lab = tk.Label(ib, text='\n\nEnter Date of Submission (DD/MM/YYYY) :  ', fg='white', bg='royal blue1',
                       font=('Agency FB', 20))
        lab.pack()

        frame3 = tk.Frame(ib, bg='royal blue1')
        lab = tk.Label(frame3, text=' Day:  ', fg='white', bg='royal blue1', font=('Agency FB', 18))
        lab.pack(side='left')
        dsd1 = tk.Entry(frame3, textvariable=dsd, font=('Agency FB', 18))
        dsd1.pack(side='left')
        lab = tk.Label(frame3, text='     Month:  ', fg='white', bg='royal blue1', font=('Agency FB', 18))
        lab.pack(side='left')
        dsm1 = tk.Entry(frame3, textvariable=dsm, font=('Agency FB', 18))
        dsm1.pack(side='left')
        lab = tk.Label(frame3, text='     Year:  ', fg='white', bg='royal blue1', font=('Agency FB', 18))
        lab.pack(side='left')
        dsy1 = tk.Entry(frame3, textvariable=dsy, font=('Agency FB', 18))
        dsy1.pack(side='left')
        frame3.pack()

        lab = tk.Label(ib, text='  \n', bg='royal blue1')
        lab.pack()

        frame4 = tk.Frame(ib, bg='royal blue1')
        but_register = tk.Button(frame4, text='Issue', fg='black', bg='tomato', font=('Agency FB', 14), height=3,
                                 width=30, command=issuing_book_admin)
        but_register.pack(side='right')
        lab1 = tk.Label(frame4, padx=25, bg='royal blue1')
        lab1.pack(side='right')
        but_exit = tk.Button(frame4, text='Close', fg='black', bg='light cyan', font=('Agency FB', 14), height=3,
                             width=30,
                             command=ib.destroy)
        but_exit.pack(side='right')
        frame4.pack()

    def return_book_admin():
        def returning_book_admin():
            n2 = n.get()
            b2 = b.get()
            sql_q = 'select br_by from LIB_DB where bid=?'
            val = []
            val.append(b2)
            result = cur1.execute(sql_q, val)
            data = result.fetchone()
            if data == None:
                msg("Book Id not found!", "Book Id not found!")
            elif data[0] == 'None':
                msg("The book is not borrowed!",
                    "The book is not borrowed by anyone at this time!\nWe already have the book!\n")
            elif data[0] == n2:
                sql_q = 'update LIB_DB set br_by=?,doi=?,dos=? where bid=?'
                val1 = []
                val1.append('None')
                val1.append('N/A')
                val1.append('N/A')
                val1.append(b2)
                cur1.execute(sql_q, val1)
                db1.commit()
                msg("Book Returned Successfully!", "Book Returned Successfully!")
            else:
                msg("Wrong username!", "Wrong username!\nThe book was borrowed by another user!\n")

        rt = tk.Tk()
        rt.title("Return book")
        rt.configure(bg='royal blue1')
        rt.resizable(0, 0)
        n1 = tk.StringVar(rt)
        b1 = tk.StringVar(rt)
        lab = tk.Label(rt, text='  \n', bg='royal blue1')
        lab.pack()
        frame1 = tk.Frame(rt, bg='royal blue1')
        lab = tk.Label(frame1, text='  Enter Username :  ', fg='white', bg='royal blue1', font=('Agency FB', 20))
        lab.pack(side='left')
        n = tk.Entry(frame1, textvariable=n1, font=('Agency FB', 20))
        n.pack(side='left')
        lab = tk.Label(frame1, text='             Enter Book Id :  ', fg='white', bg='royal blue1',
                       font=('Agency FB', 20))
        lab.pack(side='left')
        b = tk.Entry(frame1, textvariable=b1, font=('Agency FB', 20))
        b.pack(side='left')
        lab = tk.Label(frame1, text='  ', bg='royal blue1')
        lab.pack()
        frame1.pack()
        lab = tk.Label(rt, text='  \n', bg='royal blue1')
        lab.pack()
        frame4 = tk.Frame(rt, bg='royal blue1')
        but_register = tk.Button(frame4, text='Return', fg='black', bg='tomato', font=('Agency FB', 14), height=3,
                                 width=30, command=returning_book_admin)
        but_register.pack(side='right')
        lab1 = tk.Label(frame4, padx=25, bg='royal blue1')
        lab1.pack(side='right')
        but_exit = tk.Button(frame4, text='Close', fg='black', bg='light cyan', font=('Agency FB', 14), height=3,
                             width=30,
                             command=rt.destroy)
        but_exit.pack(side='right')
        frame4.pack()
        lab = tk.Label(rt, text='  \n', bg='royal blue1')
        lab.pack()
        rt.mainloop()

    def login():
        def proceed_user_choice():
            nonlocal u
            # unm=u
            chu = tk.StringVar(user)
            chu = choice_user.get()
            if chu == '1':
                show_all_books_user(u)
            elif chu == '2':
                search_book_user(u)


            elif chu == '3':
                val = []
                val.append(u)
                sql_q = 'select name,username,email,phone,address from USER_DB where username=?'
                result = cur.execute(sql_q, val)
                data = result.fetchone()
                sp = '    '
                s = "\n_______________________________________________________________________________________________________\n\n" + format(
                    'NAME', '15') + sp + format('USERNAME', '15') + sp + format('EMAIL ID', '15') + sp + format(
                    'PHONE NUMBER', '12') + sp + format('ADDRESS',
                                                        '15') + "\n_______________________________________________________________________________________________________\n\n"
                s = s + format(data[0], '15') + sp + format(data[1], '15') + sp + format(data[2], '15') + sp + format(
                    data[3], '12') + sp + format(data[4], '15') + "\n"
                msg("Details of " + u + "!", "Your details are following!\n" + s)
                """elif chu == '6':
                #update own details
                pass
                elif chu == '7':
                #delete own account
                pass"""
            elif chu == '4':
                show_user_issued_book(u)
            else:
                msg(" Invalid Input!", "Invalid Input!Please enter a value from 1 to 4 ")

        try:
            u = username.get()
            p = password.get()
            v = []
            v.append(u)
            # v.append(p)
            sql_q = "Select password from USER_DB where username=?"  # and password=?"
            result = cur.execute(sql_q, v)
            data = result.fetchone()
            if sencript(p) == data[0]:
                reset()
                s = "Welcome " + u + "!"
                user = tk.Tk()
                user.title("Login Successfull!")
                user.resizable(0, 0)
                user.geometry("1000x700")
                user.configure(bg='royal blue1')
                lab = tk.Label(user, text=s, fg='white', bg='royal blue1', font=("Agency FB", 36))
                lab.pack()
                lab = tk.Label(user, text='\
1.See all books            \n\
2.Search book              \n\
3.See your details         \n\
4.See your borrowed books  \n\n\
Note: If you want to borrow/return a book or if you want to update\n\
anything then visit the library and request the administrator.\n', fg='white', bg='royal blue1', font=("Agency FB", 24))
                lab.pack()
                uchoice = tk.StringVar(user)
                frame2 = tk.Frame(user, pady=5, bg='royal blue1')
                lable2 = tk.Label(frame2, text='Enter your choice(1 to 4): ', fg='white', bg='royal blue1',
                                  font=('Agency FB', 28), padx=25)
                lable2.pack(side='left')
                choice_user = tk.Entry(frame2, textvariable=uchoice, font=('Agency FB', 28))
                choice_user.pack(side='left')
                lable2 = tk.Label(frame2, text='  ', bg='royal blue1')
                lable2.pack(side='left')
                but = tk.Button(frame2, text='Proceed', fg='black', bg='light cyan', font=('Agency FB', 16),
                                height=2, width=20, command=proceed_user_choice)
                but.pack(side='left')
                frame2.pack()
                but = tk.Button(user, text='Logout', fg='black', bg='tomato', font=('Agency FB', 16),
                                height=2, width=20, command=user.destroy)
                but.pack()
                user.mainloop()
            else:
                pwd_mismatch_error()
        except:
            not_found_error()
        reset()

    def login_admin():
        reset()

        def proceed():
            def proceed_admin_choice():
                ch = tk.StringVar(admin)
                ch = choice_admin.get()
                if ch == '1':
                    add_book()
                elif ch == '2':
                    show_all_books()
                elif ch == '3':
                    search_book()
                elif ch == '4':
                    # update_book()
                    return_book_admin()
                elif ch == '5':
                    delete_book()
                elif ch == '6':
                    show_constraints()
                elif ch == '7':
                    show_all_issued_book()
                elif ch == '8':
                    def proceed_():
                        user = un_.get()
                        show_user_issued_book(user)
                        # lal.destroy()

                    lal = tk.Tk()
                    lal.resizable(0, 0)
                    lal.title("Select an user")
                    adminpass_ = tk.StringVar(lal)
                    frame2 = tk.Frame(lal, pady=5)
                    lable2 = tk.Label(frame2, text='  Enter Username: ', font=('Agency FB', 24), padx=25)
                    lable2.pack(side='left')
                    un_ = tk.Entry(frame2, textvariable=adminpass_, font=('Agency FB', 24))
                    un_.pack(side='left')
                    lab = tk.Label(frame2, text='  ')
                    lab.pack()
                    frame2.pack()

                    frame3 = tk.Frame(lal)
                    but = tk.Button(frame3, text='Proceed', font=('Agency FB', 12), bg='light cyan', height=3, width=35,
                                    command=proceed_)
                    but.pack(side='right')
                    lab = tk.Label(frame3, text=" ")
                    lab.pack(side='right')
                    but = tk.Button(frame3, text='Close', font=('Agency FB', 12), bg='tomato',
                                    height=3, width=35, command=lal.destroy)
                    but.pack(side='right')
                    frame3.pack()
                    lab = tk.Label(lal, text="")
                    lab.pack(side='right')
                    lal.mainloop()

                elif ch == '9':
                    register()
                elif ch == '10':
                    show_all_users()
                elif ch == '11':
                    search_user()
                elif ch == '12':
                    update_user()
                elif ch == '13':
                    delete_user()
                elif ch == '14':
                    issue_book_admin()
                    """elif ch=='15':
                    return_book_admin()"""

                else:
                    d = tk.Tk()
                    # sc.geometry("900x600")
                    d.resizable(0, 0)
                    d.title("Invalid Input!")
                    lab = tk.Label(d,
                                   text="\nInvalid Input!\n    Please enter a value from 1 to 14   \n",
                                   font=('Agency FB', 24))

                    lab.pack()
                    but = tk.Button(d, text='Close', font=('Agency FB', 12), bg='tomato', height=3, width=35,
                                    command=d.destroy)
                    but.pack()
                    lab = tk.Label(d,
                                   text="\n",
                                   )

                    lab.pack()
                    d.mainloop()

            admin_pass = password_admin.get()
            if sencript(
                    admin_pass) == "##    ####    ###    ##    ###    # #   #####    ###    # #   ####  ###    ###    # #   ####  ##  ###    ###    # #   ####  ##  ##  #":
                admin = tk.Tk()
                admin.geometry("1000x700")
                admin.resizable(0, 0)
                admin.configure(bg="royal blue1")
                admin.title("Logged in as Admin")
                la.destroy()
                lab = tk.Label(admin, text='Welcome Admin!', fg='white', bg='royal blue1', font=('Agency FB', 36))
                lab.pack()
                lab = tk.Label(admin, text='', bg='royal blue1')
                lab.pack()

                lab = tk.Label(admin, text='1.Add a book                     9.Register an account\n'
                                           '2.Show all books                 10.Show all users     \n'
                                           '3.Search book                    11.Search user        \n'
                                           '4.Return a book                  12.Update an user    \n'
                                           '5.Delete a book                  13.Delete an user    \n'
                                           '6.Show Input Restriction         14.Issue book        \n'
                                           '7.Show all issued books                               \n'
                                           '8.Show issued books by an user                        \n', fg='white',
                               bg='royal blue1', font=('Agency FB', 28))
                lab.pack()
                choice = tk.StringVar(admin)
                frame2 = tk.Frame(admin, pady=5, bg='royal blue1')
                lable2 = tk.Label(frame2, text='Enter your choice(1 to 14): ', fg='white', bg='royal blue1',
                                  font=('Agency FB', 28), padx=25)
                lable2.pack(side='left')
                choice_admin = tk.Entry(frame2, textvariable=choice, font=('Agency FB', 28))
                choice_admin.pack(side='left')
                lable2 = tk.Label(frame2, text='  ', bg='royal blue1')
                lable2.pack(side='left')
                but = tk.Button(frame2, text='Proceed', fg='black', bg='light cyan', font=('Agency FB', 16),
                                height=2, width=20, command=proceed_admin_choice)
                but.pack(side='left')
                frame2.pack()
                but = tk.Button(admin, text='Logout', fg='black', bg='tomato', font=('Agency FB', 16),
                                height=2, width=20, command=admin.destroy)
                but.pack()

                admin.mainloop()
            else:
                la.destroy()
                msg = tk.Tk()
                msg.geometry("400x120")
                msg.resizable(0, 0)
                msg.title("Password mismatch!")
                lab = tk.Label(msg, text='Wrong Password!', font=('Agency FB', 24))
                lab.pack()
                but = tk.Button(msg, text='Close', font=('Agency FB', 12), bg='tomato', height=2, width=30,
                                command=msg.destroy)
                but.pack()

        la = tk.Tk()
        la.resizable(0, 0)
        la.title("Login as Admin")
        adminpass = tk.StringVar(la)
        frame2 = tk.Frame(la, pady=5)
        lable2 = tk.Label(frame2, text='  Enter Admin Password: ', font=('Agency FB', 24), padx=25)
        lable2.pack(side='left')
        password_admin = tk.Entry(frame2, show='*', textvariable=adminpass, font=('Agency FB', 24))
        password_admin.pack(side='left')
        lab = tk.Label(frame2, text='  ')
        lab.pack()
        frame2.pack()

        frame3 = tk.Frame(la)
        but = tk.Button(frame3, text='Proceed', font=('Agency FB', 12), bg='tomato', height=3, width=35,
                        command=proceed)
        but.pack(side='right')
        lab = tk.Label(frame3, text=" ")
        lab.pack(side='right')
        but = tk.Button(frame3, text='Cancel', font=('Agency FB', 12), bg='light cyan',
                        height=3, width=35, command=la.destroy)
        but.pack(side='right')
        frame3.pack()
        lab = tk.Label(la, text="")
        lab.pack(side='right')
        la.mainloop()

    root = tk.Tk()
    root.geometry("700x700")
    root.title("Library Management System")
    root.resizable(0, 0)
    root.configure(bg='royal blue1')

    lab = tk.Label(root, text='', bg='royal blue1', fg='white', font=('Arial', 28))
    lab.pack()
    lab = tk.Label(root, text='Welcome to The Library Management System!', bg='royal blue1', fg='white',
                   font=('Agency FB', 28))
    lab.pack()
    lab = tk.Label(root, text='', bg='royal blue1')
    lab.pack()

    blank = tk.StringVar(root)
    blank.set('')
    blank1 = tk.StringVar(root)
    blank1.set('')

    frame1 = tk.Frame(root, pady=30, bg='royal blue1')
    lable1 = tk.Label(frame1, text='Enter Username: ', fg='white', bg='royal blue1', font=('Agency FB', 24), padx=25)
    lable1.pack(side='left')
    username = tk.Entry(frame1, textvariable=blank, font=('Agency FB', 24))
    username.pack(side='left')
    frame1.pack()

    frame2 = tk.Frame(root, pady=5, bg='royal blue1')
    lable2 = tk.Label(frame2, text='Enter Password: ', fg='white', bg='royal blue1', font=('Agency FB', 24), padx=25)
    lable2.pack(side='left')
    password = tk.Entry(frame2, show='*', textvariable=blank1, font=('Agency FB', 24))
    password.pack(side='left')
    frame2.pack()

    lab = tk.Label(root, text='', bg='royal blue1')
    lab.pack()

    frame3 = tk.Frame(root, bg='royal blue1')
    but_log = tk.Button(frame3, text='LOGIN', fg='black', bg='light cyan', font=('Agency FB', 14), height=3, width=30,
                        command=login)
    but_log.pack(side='right')
    lab1 = tk.Label(frame3, padx=25, bg='royal blue1')
    lab1.pack(side='right')
    but_reset = tk.Button(frame3, text='RESET', fg='black', bg='light cyan', font=('Agency FB', 14), height=3, width=30,
                          command=reset)
    but_reset.pack(side='right')
    frame3.pack()

    lab = tk.Label(root, text='', bg='royal blue1')
    lab.pack()

    frame4 = tk.Frame(root, bg='royal blue1')
    but_register = tk.Button(frame4, text='REGISTER', fg='black', bg='light cyan', font=('Agency FB', 14), height=3,
                             width=30, command=register)
    but_register.pack(side='right')
    lab1 = tk.Label(frame4, padx=25, bg='royal blue1')
    lab1.pack(side='right')
    but_exit = tk.Button(frame4, text='EXIT', fg='black', bg='light cyan', font=('Agency FB', 14), height=3, width=30,
                         command=sure)
    but_exit.pack(side='right')
    frame4.pack()

    lab = tk.Label(root, text='', bg='royal blue1')
    lab.pack()

    but = tk.Button(root, text='LOGIN AS ADMIN', fg='black', bg='light cyan', font=('Agency FB', 14), height=3,
                    width=69,
                    command=login_admin)
    but.pack()

    root.mainloop()


def splashscreen():
    t = Turtle()
    t.speed(10)
    t.hideturtle()
    t.write("SEN PRODUCTION", move=True, align="center", font=("Agency FB", 50, "bold", "underline"))
    t.goto(-200, 0)
    t.penup()
    t.goto(-200, 10)
    t.bk(70)
    t.pendown()
    for i in range(20):
        t.pensize(2)
        t.fd(60)
        t.lt(90)
        t.left(10)
    welcome()

splashscreen()
