import tkinter as tk 
from tkinter import *
from tkinter import messagebox
import mysql.connector


#login ekranı
root=tk.Tk()
root.title("rENtİS v2.1.3")
root.geometry("500x400")
root.resizable(0,0)
root.configure(bg="#F7F5EB")
loginlbl=Label(root,text="rENt",font="Times 45 bold",fg="#5BC0F8")
loginlbl.place(x=149,y=50)
loginseclbl=Label(root,text="İS",font="Times 45 bold",fg="#FFC93C")
loginseclbl.place(x=280,y=50)
usrnameEntry=Entry(highlightthickness=1)
usrnameEntry.place(x=120,y=180,width=250,height=23)
usrnameEntry.insert(0,"Kullanıcı adı")
usrnameEntry.configure(state="disabled",highlightbackground="#5BC0F8")
passwEntry=Entry(highlightthickness=1,show="●")
passwEntry.place(x=120,y=220,width=250,height=23)
passwEntry.insert(0,"Şifre")
passwEntry.configure(state="disabled",highlightbackground="#5BC0F8")
#müşteriler veri tabanı bağlantısı
def connectcustdb():
    try:
        mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database=""
        )
        mycursor=mydb.cursor()
        mycursor.execute("CREATE DATABASE custdb")
        
        print("Databese yazıldı")
    except:
        print("Bağlantı Başarısız")
def müşteriekle():
    try:
        
        mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="custdb"
        )
        mycursor=mydb.cursor()
        mycursor.execute("CREATE TABLE custtable (adi VARCHAR(255),soyadi VARCHAR(255),tcno VARCHAR(255), dtarihi VARCHAR(255), adress VARCHAR(255),telno VARCHAR(255),meslek VARCHAR(255),ehliyet VARCHAR(255),medenidurum VARCHAR(255),egitimdurumu VARCHAR(255))")
        print("Tablo oluşturuldu")
    except:
        print("Tablo oluşturulamadı")
def inserttable():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="custdb"
        )
    if len(nameEntry.get() and surnameEntry.get() and tcEntry.get() and birthEntry.get() and adresEntry.get() and telEntry.get() and meslekEntry.get and ehliyetEntry.get() and durumEntry.get() and egitimEntry.get())!=0:
        mycursor = mydb.cursor()
        sql = "INSERT INTO custtable (adi, soyadi,tcno,dtarihi,adress,telno,meslek,ehliyet,medenidurum,egitimdurumu) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (f"{nameEntry.get()}",f"{surnameEntry.get()}",f"{tcEntry.get()}",f"{birthEntry.get()}",f"{adresEntry.get()}",f"{telEntry.get()}",f"{meslekEntry.get()}",f"{ehliyetEntry.get()}",f"{durumEntry.get()}",f"{nameEntry.get()}")
        mycursor.execute(sql, val)
        mydb.commit()
        messagebox.showinfo("Başarılı",f"Müşteri başarılı bir şekilde eklendi")
        print(mycursor.rowcount, "Tabloya veri eklendi.")
        
    else:
        print("Eksik bilgi olduğu için veri eklenemedi")

#araclar veri tabanı bağlantısı
def connectcardb():
    try:
        mycardb=mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database=""
        )
        mycarcursor=mycardb.cursor()
        mycarcursor.execute("CREATE DATABASE cardb")
        
        print("Databese yazıldı")
    except:
        print("Bağlantı Başarısız") 
def aracekle():
    try: 
        mycardb=mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="cardb"
        )
        mycarcursor=mycardb.cursor()
        mycarcursor.execute("CREATE TABLE cartable (type VARCHAR(255),marka VARCHAR(255),model VARCHAR(255), üretimyılı VARCHAR(255),yakittürü VARCHAR(255),vites VARCHAR(255),motorgucu VARCHAR(255), kasatipi VARCHAR(255),motorhacmi VARCHAR(255),çekiş VARCHAR(255),kapı VARCHAR(255),renk VARCHAR(255),motorno VARCHAR(255),şaşino VARCHAR(255),bedeli VARCHAR(255),durumu VARCHAR(255))")
        print("Tablo oluşturuldu")
        
    except:
        print("Tablo oluşturulamadı")
def insertcartable():
    mycardb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="cardb"
        )
    if len(typeEntry.get() and markaEntry.get() and modelEntry.get() and yilEntry.get() and yakitEntry.get() and vitesEntry.get() and motorgucuEntry.get() and kasatypeEntry.get() and motorhacmiEntry.get() and çekisEntry.get() and kapiEntry.get() and carrenkEntry.get() and motornoEntry.get() and sasinoEntry.get() and bedelEntry.get() and cardurumuEntry.get())!=0:
        sql = "INSERT INTO cartable (type, marka,model,üretimyılı,yakittürü,vites,motorgucu,kasatipi,motorhacmi,çekiş,kapı,renk,motorno,şaşino,bedeli,durumu) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s,%s, %s)"
        val = (f"{typeEntry.get()}",f"{markaEntry.get()}",f"{modelEntry.get()}",f"{yilEntry.get()}",f"{yakitEntry.get()}",f"{vitesEntry.get()}",f"{motorgucuEntry.get()}",f"{kasatypeEntry.get()}",f"{motorhacmiEntry.get()}",f"{çekisEntry.get()}",f"{kapiEntry.get()}",f"{carrenkEntry.get()}",f"{motornoEntry.get()}",f"{sasinoEntry.get()}",f"{bedelEntry.get()}",f"{cardurumuEntry.get()}")
        mycarcursor = mycardb.cursor()
        mycarcursor.execute(sql, val)
        mycardb.commit()
        messagebox.showinfo("Başarılı",f"Araç başarılı bir şekilde eklendi")
        

        print(mycarcursor.rowcount, "Tabloya veri eklendi.")
    else:
        print("Eksik bilgi olduğu için veri eklenemedi")
        
                                    

def homewithoutpassw():
    home2=tk.Tk()
    home2.title("rENtİs v2.1.3")
    home2.configure(bg="#F7F5EB")
    home2.resizable(0,0)
    home2.geometry("700x500")
    #4buton arayüzler için
    def exithome2():
        home2.destroy()    
    btncustomer2=Button(home2,text="Müşteri Ekle",font="Arial 20 bold",bg="#5BC0F8",fg="#fff",command=lambda:(exithome2(),customerinfo()))
    btncustomer2.place(x=100,y=120,height=65,)
    btncar2=Button(home2,text="Araç Ekle",font="Arial 20 bold",bg="#5BC0F8",fg="#fff",command=lambda:(exithome2(),selectcar()))
    btncar2.place(x=400,y=120,height=65,width=220)
    btnrentcar2=Button(home2,text="Araç Kiralama Bilgisi",font="Arial 17 bold",bg="#5BC0F8",fg="#fff",command=lambda:(exithome2(),meetcustandcars()))
    btnrentcar2.place(x=100,y=300,height=65)
    btnrentedcar2=Button(home2,text="Kiralanmış Araçlar",font="Arial 17 bold",bg="#5BC0F8",fg="#fff",command=lambda:(exithome2(),rentedwcust()))
    btnrentedcar2.place(x=400,y=300,height=65)
    home2.mainloop()

#home ekranına giriş
def home():
    
    if usrnameEntry.get()=="enis" and passwEntry.get()=="enis07":
        home=tk.Tk()
        home.title("rENtİs v2.1.3")
        home.configure(bg="#F7F5EB")
        home.resizable(0,0)
        home.geometry("700x500")
        root.destroy()
        def exithome():
            home.destroy()
        #4buton arayüzler için      
        btncustomer=Button(home,text="Müşteri Ekle",font="Arial 20 bold",bg="#5BC0F8",fg="#fff",command=lambda:(exithome(),customerinfo()))
        btncustomer.place(x=100,y=120,height=65,)
        btncar=Button(home,text="Araç Ekle",font="Arial 20 bold",bg="#5BC0F8",fg="#fff",command=lambda:(exithome(),selectcar()))
        btncar.place(x=400,y=120,height=65,width=220)
        btnrentcar=Button(home,text="Araç Kiralama Bilgisi",font="Arial 17 bold",bg="#5BC0F8",fg="#fff",command=lambda:(exithome(),meetcustandcars()))
        btnrentcar.place(x=100,y=300,height=65)
        btnrentedcar=Button(home,text="Kiralanmış Araçlar",font="Arial 17 bold",bg="#5BC0F8",fg="#fff",command=lambda:(exithome(),rentedwcust()))
        btnrentedcar.place(x=400,y=300,height=65)    
        home.mainloop() 
    elif usrnameEntry.get()=="Kullanıcı adı" or len(usrnameEntry.get())==0:
        messagebox.showwarning("Uyarı",f"Lütfen kullanıcı adını giriniz")
    elif passwEntry.get()=="Şifre" or len(passwEntry.get())==0:
        messagebox.showwarning("Uyarı",f"Lütfen şifreyi giriniz")
    elif usrnameEntry.get()!="enis" and passwEntry.get()!="enis07":
        messagebox.showwarning("Uyarı",f"Kullanıcı adı veya parola yanlış")
    else:
        messagebox.showwarning("Hata",f"Kullanıcı adı veya parola yanlış")            
loginbtn=Button(root,text="Giriş",bg="#0081C9",fg="#fff",font="Arial 10 bold",command=home)
loginbtn.place(x=120,y=270,width=250)
#müşteri bilgileri buton1
def customerinfo():
    cust=tk.Tk()
    cust.title("Müşteri Bilgileri")
    cust.geometry("900x600")
    cust.resizable(0,0)
    canvascustinfo=Canvas(cust)
    canvascustinfo.place(x=2,y=5,width=300,height=550)
    canvascustinfo.create_line(5, 40, 200, 40)
    labelcustinfo=Label(canvascustinfo,text="Müşteri Bilgileri",font="Arial 15 bold")
    labelcustinfo.place(x=10,y=10)
    #info entry ve labeller
    #give global 
    global nameEntry,surnameEntry,tcEntry,birthEntry,adresEntry,telEntry,meslekEntry,ehliyetEntry,durumEntry,egitimEntry
    lblname=Label(canvascustinfo,text="Ad:",font="Arial 12")
    lblname.place(x=10,y=60)
    nameEntry=Entry(canvascustinfo)
    nameEntry.place(x=70,y=62)
    lblsurname=Label(canvascustinfo,text="Soyad:",font="Arial 12")
    lblsurname.place(x=10,y=100)
    surnameEntry=Entry(canvascustinfo)
    surnameEntry.place(x=70,y=102)
    lbltc=Label(canvascustinfo,text="TC NO:",font="Arial 12")
    lbltc.place(x=10,y=140)
    tcEntry=Entry(canvascustinfo)
    tcEntry.place(x=70,y=142)
    lblbirth=Label(canvascustinfo,text="D.tarihi:",font="Arial 12")
    lblbirth.place(x=10,y=180)
    birthEntry=Entry(canvascustinfo)
    birthEntry.place(x=70,y=182)
    lbladres=Label(canvascustinfo,text="Adres:",font="Arial 12")
    lbladres.place(x=10,y=220)
    adresEntry=Entry(canvascustinfo)
    adresEntry.place(x=70,y=222)
    lbltel=Label(canvascustinfo,text="Telefon:",font="Arial 12")
    lbltel.place(x=10,y=260)
    telEntry=Entry(canvascustinfo)
    telEntry.place(x=70,y=262)
    lblmeslek=Label(canvascustinfo,text="Meslek:",font="Arial 12")
    lblmeslek.place(x=10,y=300)
    meslekEntry=Entry(canvascustinfo)
    meslekEntry.place(x=70,y=302)
    lblehliyet=Label(canvascustinfo,text="Ehliyet:",font="Arial 12")
    lblehliyet.place(x=10,y=340)
    ehliyetEntry=Entry(canvascustinfo)
    ehliyetEntry.place(x=70,y=342)
    lbldurum=Label(canvascustinfo,text="Medeni Durum:",font="Arial 12")
    lbldurum.place(x=10,y=380)
    durumEntry=Entry(canvascustinfo)
    durumEntry.place(x=70,y=382)
    lblegitim=Label(canvascustinfo,text="Eğitim Durumu:",font="Arial 12")
    lblegitim.place(x=10,y=420)
    egitimEntry=Entry(canvascustinfo)
    egitimEntry.place(x=70,y=422)
    lblrent=Label(cust,text="rENt",font="Times 27 bold",fg="#5BC0F8")
    lblrent.place(x=500,y=10)
    lblis=Label(cust,text="İS",font="Times 27 bold",fg="#FFC93C")
    lblis.place(x=580,y=10)
    custtextarea=Text(cust)
    custtextarea.place(x=400,y=50,width=300,height=400)
    textarealbl=Label(custtextarea,text="Müşteri Bilgileri",font="Times 12 bold",state="disabled",bg="#fff")
    textarealbl.place(x=100,y=10)
    custtextarea.configure(state="normal")
    def exitcustomerinfo(): 
        cust.destroy()
    btnhome=Button(cust,text="Anasayfa",font="Times 13 bold",bg="#0081C9",fg="#fff",command=lambda:(exitcustomerinfo(),homewithoutpassw()))
    btnhome.place(x=460,y=480)
    btnrentegit=Button(cust,text="Araç Seç",font="Times 13 bold",bg="#FFC93C",fg="#333",command=lambda:(exitcustomerinfo(),selectcar())) 
    btnrentegit.place(x=570,y=480)  
    def kayit():
        entryname=nameEntry.get()
        entrysurname=surnameEntry.get()
        entrytc=tcEntry.get()
        entrybirth=birthEntry.get()
        entryadres=adresEntry.get()
        entrytel=telEntry.get()
        entrymeslek=meslekEntry.get()
        entryehliyet=ehliyetEntry.get()
        entrydurum=durumEntry.get()
        entryegitimdurumu=egitimEntry.get()
        if len(nameEntry.get() and surnameEntry.get() and tcEntry.get() and birthEntry.get() and adresEntry.get() and telEntry.get() and meslekEntry.get and ehliyetEntry.get() and durumEntry.get() and egitimEntry.get())==0:
            messagebox.showwarning("Hata",f"Eksik bilgileri doldurun")
        else:      
            custtextarea.insert(END,f"\n\n\n Müşteri Adı:{entryname}")
            custtextarea.insert(END,f"\n\n Müşteri Soyadı:{entrysurname}") 
            custtextarea.insert(END,f"\n\n Müşteri Tc No:{entrytc}")
            custtextarea.insert(END,f"\n\n Müşteri Doğum Tarihi:{entrybirth}")
            custtextarea.insert(END,f"\n\n Müşteri Adresi:{entryadres}")
            custtextarea.insert(END,f"\n\n Müşteri Telefonu:{entrytel}")
            custtextarea.insert(END,f"\n\n Müşteri Mesleği:{entrymeslek}")
            custtextarea.insert(END,f"\n\n Müşteri Ehliyet Durumu:{entryehliyet}")
            custtextarea.insert(END,f"\n\n Müşteri Medeni Durumu:{entrydurum}")
            custtextarea.insert(END,f"\n\n Müşteri Eğitim Durumu:{entryegitimdurumu}")
           
    def clear():
        nameEntry.delete("0",END)
        surnameEntry.delete("0",END)
        tcEntry.delete("0",END)
        birthEntry.delete("0",END)
        adresEntry.delete("0",END)
        telEntry.delete("0",END)
        meslekEntry.delete("0",END)
        ehliyetEntry.delete("0",END)
        durumEntry.delete("0",END)
        egitimEntry.delete("0",END)
        custtextarea.delete("4.0",END)    

        
    btnkayitclear=Button(cust,text="Kaydı Temizle",font="Times 13 bold",bg="#FFC93C",fg="#333",command=clear)
    btnkayitclear.place(x=150,y=480)    
      

       
        
    btnkayitolustur=Button(cust,text="Kaydı oluştur",font="Times 13 bold",bg="#0081C9",fg="#fff",command=lambda:(kayit(),connectcustdb(),müşteriekle(),inserttable()))
    btnkayitolustur.place(x=10,y=480)
    cust.mainloop()    

#Araç seçme ekranı
def selectcar():
    car=tk.Tk()
    car.title("Araç Seçme Ekranı")
    car.geometry("1000x900")
    canvascarinfo=Canvas(car)
    canvascarinfo.place(x=2,y=5,width=300,height=800)
    canvascarinfo.create_line(5, 40, 250, 40)
    labelcarinfo=Label(canvascarinfo,text="Araç Bilgileri",font="Arial 15 bold")
    labelcarinfo.place(x=10,y=10)
    #info entry ve labeller
    #global car entries
    global typeEntry,markaEntry,modelEntry,yilEntry,yakitEntry,vitesEntry,motorgucuEntry,kasatypeEntry,motorhacmiEntry,   çekisEntry,carrenkEntry,motornoEntry,kapiEntry,sasinoEntry,bedelEntry,cardurumuEntry
    lblcartype=Label(canvascarinfo,text="Araç Türü:",font="Arial 12")
    lblcartype.place(x=10,y=60)
    typeEntry=Entry(canvascarinfo)
    typeEntry.place(x=110,y=62)
    lblmarka=Label(canvascarinfo,text="Marka:",font="Arial 12")
    lblmarka.place(x=10,y=100)
    markaEntry=Entry(canvascarinfo)
    markaEntry.place(x=110,y=102)
    lblmodel=Label(canvascarinfo,text="Model:",font="Arial 12")
    lblmodel.place(x=10,y=140)
    modelEntry=Entry(canvascarinfo)
    modelEntry.place(x=110,y=142)
    lblyil=Label(canvascarinfo,text="Üretim Yılı:",font="Arial 12")
    lblyil.place(x=10,y=180)
    yilEntry=Entry(canvascarinfo)
    yilEntry.place(x=110,y=182)
    lblyakittype=Label(canvascarinfo,text="Yakıt Türü:",font="Arial 12")
    lblyakittype.place(x=10,y=220)
    yakitEntry=Entry(canvascarinfo)
    yakitEntry.place(x=110,y=222)
    lblvites=Label(canvascarinfo,text="Vites:",font="Arial 12")
    lblvites.place(x=10,y=260)
    vitesEntry=Entry(canvascarinfo)
    vitesEntry.place(x=110,y=262)
    lblmotorgucu=Label(canvascarinfo,text="Motor Gücü:",font="Arial 12")
    lblmotorgucu.place(x=10,y=300)
    motorgucuEntry=Entry(canvascarinfo)
    motorgucuEntry.place(x=110,y=302)
    lblkasatype=Label(canvascarinfo,text="Kasa Tipi:",font="Arial 12")
    lblkasatype.place(x=10,y=340)
    kasatypeEntry=Entry(canvascarinfo)
    kasatypeEntry.place(x=110,y=342)
    lblmotorhacmi=Label(canvascarinfo,text="Motor Hacmi:",font="Arial 12")
    lblmotorhacmi.place(x=10,y=380)
    motorhacmiEntry=Entry(canvascarinfo)
    motorhacmiEntry.place(x=110,y=382)
    lblçekis=Label(canvascarinfo,text="Çekiş:",font="Arial 12")
    lblçekis.place(x=10,y=420)
    çekisEntry=Entry(canvascarinfo)
    çekisEntry.place(x=110,y=422)
    lblkapi=Label(canvascarinfo,text="Kapı:",font="Arial 12")
    lblkapi.place(x=10,y=460)
    kapiEntry=Entry(canvascarinfo)
    kapiEntry.place(x=110,y=462)
    lblcarrenk=Label(canvascarinfo,text="Renk:",font="Arial 12")
    lblcarrenk.place(x=10,y=500)
    carrenkEntry=Entry(canvascarinfo)
    carrenkEntry.place(x=110,y=502)
    lblmotorno=Label(canvascarinfo,text="Motor No:",font="Arial 12")
    lblmotorno.place(x=10,y=540)
    motornoEntry=Entry(canvascarinfo)
    motornoEntry.place(x=110,y=542)
    lblsasino=Label(canvascarinfo,text="Şaşi No:",font="Arial 12")
    lblsasino.place(x=10,y=580)
    sasinoEntry=Entry(canvascarinfo)
    sasinoEntry.place(x=110,y=582)
    lblbedel=Label(canvascarinfo,text="K.Bedeli:",font="Arial 12")
    lblbedel.place(x=10,y=620)
    bedelEntry=Entry(canvascarinfo)
    bedelEntry.place(x=110,y=622)
    lblcardurumu=Label(canvascarinfo,text="Araç Durumu:",font="Arial 12")
    lblcardurumu.place(x=10,y=660)
    cardurumuEntry=Entry(canvascarinfo)
    cardurumuEntry.place(x=110,y=662) 
    lblcarrent=Label(car,text="rENt",font="Times 27 bold",fg="#5BC0F8")
    lblcarrent.place(x=500,y=10)
    lblcaris=Label(car,text="İS",font="Times 27 bold",fg="#FFC93C")
    lblcaris.place(x=580,y=10)
    cartextarea=Text(car)
    cartextarea.place(x=400,y=50,width=350,height=550)
    textarealbl=Label(cartextarea,text="Araç Bilgileri",font="Times 12 bold",state="disabled",bg="#fff")
    textarealbl.place(x=100,y=10)
    cartextarea.configure(state="normal")
    #araç register function
    def arackayit():
        entryType=typeEntry.get()
        entryMarka=markaEntry.get()
        entryModel=modelEntry.get()
        entryYil=yilEntry.get()
        entryYakit=yakitEntry.get()
        entryVites=vitesEntry.get()
        entryMotorgücü=motorgucuEntry.get()
        entryKasa=kasatypeEntry.get()
        entryMotorhacmi=motorhacmiEntry.get()
        entryCekis=çekisEntry.get()
        entryKapi=kapiEntry.get()
        entryRenk=carrenkEntry.get()
        entryMotorno=motornoEntry.get()
        entrySasi=sasinoEntry.get()
        entryBedel=bedelEntry.get()
        entryDurum=cardurumuEntry.get()
        if len(typeEntry.get() and markaEntry.get() and modelEntry.get() and yilEntry.get() and yakitEntry.get() and vitesEntry.get() and motorgucuEntry.get() and kasatypeEntry.get() and motorhacmiEntry.get() and çekisEntry.get() and kapiEntry.get() and carrenkEntry.get() and motornoEntry.get() and sasinoEntry.get() and bedelEntry.get() and cardurumuEntry.get())==0:
            messagebox.showwarning("Hata",f"Eksik bilgileri doldurun")
        else:
            cartextarea.insert(END,f"\n\n\n Araç Türü:{entryType}")
            cartextarea.insert(END,f"\n\n Araç Markası:{entryMarka}") 
            cartextarea.insert(END,f"\n\n Araç Modeli:{entryModel}")
            cartextarea.insert(END,f"\n\n Üretim Yılı:{entryYil}")
            cartextarea.insert(END,f"\n\n Yakıt Türü:{entryYakit}")
            cartextarea.insert(END,f"\n\n Vitesi:{entryVites}")
            cartextarea.insert(END,f"\n\n Motor Gücü:{entryMotorgücü}")
            cartextarea.insert(END,f"\n\n Kasa Tipi:{entryKasa}")
            cartextarea.insert(END,f"\n\n Motor Hacmi:{entryMotorhacmi}")
            cartextarea.insert(END,f"\n\n Araç Çekişi:{entryCekis}")
            cartextarea.insert(END,f"\n\n Araç Kapı:{entryKapi}")
            cartextarea.insert(END,f"\n\n Araç Rengi:{entryRenk}") 
            cartextarea.insert(END,f"\n\n Motor No:{entryMotorno}")
            cartextarea.insert(END,f"\n\n Şaşi No'su:{entrySasi}")
            cartextarea.insert(END,f"\n\n Kiralama Bedeli:{entryBedel}")
            cartextarea.insert(END,f"\n\n Araç Durumu:{entryDurum}")
           

    btncarkayitekle=Button(car,text="Aracı Ekle",font="Times 13 bold",bg="#FFC93C",fg="#333",command=lambda:(arackayit(),connectcardb(),aracekle(),insertcartable()))
    btncarkayitekle.place(x=280,y=620)

    def carclear():
        typeEntry.delete("0",END)
        markaEntry.delete("0",END)
        modelEntry.delete("0",END)
        yilEntry.delete("0",END)
        yakitEntry.delete("0",END)
        vitesEntry.delete("0",END)
        motorgucuEntry.delete("0",END)
        kasatypeEntry.delete("0",END)
        motorhacmiEntry.delete("0",END)
        çekisEntry.delete("0",END)
        kapiEntry.delete("0",END)
        carrenkEntry.delete("0",END)
        motornoEntry.delete("0",END)
        sasinoEntry.delete("0",END)
        bedelEntry.delete("0",END)
        cardurumuEntry.delete("0",END)
        cartextarea.delete("1.0",END)          
    def exitselectcar():
        car.destroy()    
    btncarkayitclear=Button(car,text="Kaydı Temizle",font="Times 13 bold",bg="#0081C9",fg="#fff",command=carclear)
    btncarkayitclear.place(x=420,y=620)    
    btncarkayitinfopage=Button(car,text="Aracı Kirala",font="Times 13 bold",bg="#FFC93C",fg="#333",command=lambda:(exitselectcar(),meetcustandcars()))
    btncarkayitinfopage.place(x=560,y=620) 
    btncarkayithome=Button(car,text="Anasayfa",font="Times 13 bold",bg="#FFC93C",fg="#333",command=lambda:(exitselectcar(),homewithoutpassw()))
    btncarkayithome.place(x=700,y=620)                                 
    car.mainloop()
def meetcustandcars():
    #fetch cars from cartable
    
    def fetchcars():
        try:
            mydb=mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="cardb"
        )
            mycursor=mydb.cursor()
            fetchcarquery= "SELECT * FROM cartable"
            mycursor.execute(fetchcarquery)
            records = mycursor.fetchall()
            for row in records:
                labelbigcarname=Label(canvasaddcar,text=f"1-{row[1]} {row[2]}",font="Times 13 bold")
                labelbigcarname.place(x=22,y=40)
                labelinsertcartype=Label(canvasaddcar,text=f"{row[0]}",bg="red")
                labelinsertcartype.place(x=150,y=42,width=60)
                labelinsertmarka=Label(canvasaddcar,text=f"{row[1]}",bg="yellow")
                labelinsertmarka.place(x=220,y=42,width=60)
                labelinsertmodel=Label(canvasaddcar,text=f"{row[2]}",bg="red")
                labelinsertmodel.place(x=280,y=42,width=60)
                labelinsertyil=Label(canvasaddcar,text=f"{row[3]}",bg="yellow")
                labelinsertyil.place(x=342,y=42,width=60)
                labelinsertyakitürü=Label(canvasaddcar,text=f"{row[4]}",bg="red")
                labelinsertyakitürü.place(x=402,y=42,width=60)
                labelinsertvites=Label(canvasaddcar,text=f"{row[5]}",bg="yellow")
                labelinsertvites.place(x=460,y=42,width=60)
                labelinsertmotorgucu=Label(canvasaddcar,text=f"{row[6]}",bg="red")
                labelinsertmotorgucu.place(x=520,y=42,width=60)
                labelinsertktipi=Label(canvasaddcar,text=f"{row[7]}",bg="yellow")
                labelinsertktipi.place(x=520,y=42,width=60)
                labelinsertmhacmi=Label(canvasaddcar,text=f"{row[8]}",bg="red")
                labelinsertmhacmi.place(x=580,y=42,width=60)
                labelinsertcekis=Label(canvasaddcar,text=f"{row[9]}",bg="yellow")
                labelinsertcekis.place(x=640,y=42,width=60)
                labelinsertkapi=Label(canvasaddcar,text=f"{row[10]}",bg="red")
                labelinsertkapi.place(x=702,y=42,width=60)
                labelinsertrenk=Label(canvasaddcar,text=f"{row[11]}",bg="yellow")
                labelinsertrenk.place(x=763,y=42,width=60)
                labelinsertmotorno=Label(canvasaddcar,text=f"{row[12]}",bg="red")
                labelinsertmotorno.place(x=820,y=42,width=60)
                labelinsertsasino=Label(canvasaddcar,text=f"{row[13]}",bg="yellow")
                labelinsertsasino.place(x=880,y=42,width=60)
                labelinsertdurumu=Label(canvasaddcar,text=f"{row[13]}",bg="yellow")
                labelinsertdurumu.place(x=940,y=42,width=60)
                labelinsertbedeli=Label(canvasaddcar,text=f"{row[13]}",bg="yellow")
                labelinsertbedeli.place(x=1000,y=42,width=60)
        except:
            messagebox.showwarning("Hata",f"Kiralanacak araç bulunamadı")
            print("Veri getirilmedi")
    def carselectbtn():
        btncarselect=Button(canvasaddcar,text="Seç",font="Arial 10 bold",fg="#333",bg="#5BC0F8",command=addtocarinfo)
        btncarselect.place(x=1065,y=42,width=30,height=20) 
    def addtocarinfo():
        try:
            mydb=mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="cardb"
                )
            mycursor=mydb.cursor()
            fetchcarquery= "SELECT * FROM cartable"
            mycursor.execute(fetchcarquery)
            records = mycursor.fetchall()
            for row in records:
                global labelbigname
                labelbigname=Label(canvaskirala,text=f"{row[1]} {row[2]}",font="Times 11 bold")
                labelbigname.place(x=300,y=50)
        except:
            print("İsim Bulunamadı")   

    def fetchcust():
        try:
            mydb=mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="custdb"
        )
            mycursor=mydb.cursor()
            fetchcustquery= "SELECT * FROM custtable"
            mycursor.execute(fetchcustquery)
            recordscust = mycursor.fetchall()
            for row in recordscust:
                labelbigname=Label(canvasaddcust,text=f"1-{row[0]} {row[1]}",font="Times 13 bold")
                labelbigname.place(x=30,y=40)
                labelinsertadi=Label(canvasaddcust,text=f"{row[0]}",bg="red")
                labelinsertadi.place(x=185,y=42,width=60)
                labelinsertsoyad=Label(canvasaddcust,text=f"{row[1]}",bg="yellow")
                labelinsertsoyad.place(x=240,y=42,width=60)
                labelinserttcno=Label(canvasaddcust,text=f"{row[2]}",bg="red")
                labelinserttcno.place(x=293,y=42,width=80)
                labelinsertdtarihi=Label(canvasaddcust,text=f"{row[3]}",bg="yellow")
                labelinsertdtarihi.place(x=365,y=42,width=80)
                labelinsertadres=Label(canvasaddcust,text=f"{row[4]}",bg="red")
                labelinsertadres.place(x=442,y=42,width=50)
                labelinserttel=Label(canvasaddcust,text=f"{row[5]}",bg="yellow")
                labelinserttel.place(x=490,y=42,width=60)
                labelinsertmeslek=Label(canvasaddcust,text=f"{row[6]}",bg="red")
                labelinsertmeslek.place(x=550,y=42,width=60)
                labelinsertehliyet=Label(canvasaddcust,text=f"{row[7]}",bg="yellow")
                labelinsertehliyet.place(x=610,y=42,width=60)
                labelinsertmdurumu=Label(canvasaddcust,text=f"{row[8]}",bg="red")
                labelinsertmdurumu.place(x=675,y=42,width=60)
                labelinsertedurumu=Label(canvasaddcust,text=f"{row[9]}",bg="yellow")
                labelinsertedurumu.place(x=730,y=42,width=60)
        except:
            messagebox.showwarning("Hata",f"Müşteri bulunamadı")
            print("Veri getirilmedi")
    def custelectbtn():      
        btncarselect=Button(canvasaddcust,text="Seç",font="Arial 10 bold",fg="#333",bg="#5BC0F8",command=addtocustinfo)
        btncarselect.place(x=1065,y=42,width=30,height=20)
    def addtocustinfo():
        try:
            mydb=mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="custdb"
                )
            mycursor=mydb.cursor()
            fetchcustquery= "SELECT * FROM custtable"
            mycursor.execute(fetchcustquery)
            recordscust = mycursor.fetchall()
            for row in recordscust:
                global labelbigcustname
                labelbigcustname=Label(canvaskirala,text=f"{row[0]} {row[1]}",font="Times 11 bold")
                labelbigcustname.place(x=420,y=50)
        except:
            print("İsim Bulunamadı")  

    def infocarclear():
        labelbigname.destroy()
    def infocustclear():
        labelbigcustname.destroy()
    def entryinfoclear():
        entrygunsayı.delete("0",END)
        entryrota.delete("0",END)       

                    
            
    meet=tk.Tk()
    meet.geometry("1100x800")
    meet.resizable(0,0)
    meet.title("rENtİs v2.1.3")
    def exitmeet():
        meet.destroy()
    canvasaddcar=Canvas(meet)
    canvasaddcar.place(x=0,y=0,width=1100,height=250)
    canvasaddcar.create_line(5, 40, 1100, 40)
    labeladdcar=Label(canvasaddcar,text="Eklenen Araçlar",font="Arial 12 bold")
    labeladdcar.place(x=2,y=7)
    #eklenen araçlar bilgi menüsü
    labeladdedcarname=Label(canvasaddcar,text="Tür")
    labeladdedcarname.place(x=140,y=18,width=70)
    labeladdedcarmarka=Label(canvasaddcar,text="Marka")
    labeladdedcarmarka.place(x=220,y=18,width=60)
    labeladdedcarmodel=Label(canvasaddcar,text="Model")
    labeladdedcarmodel.place(x=280,y=18,width=60)
    labeladdedcaryil=Label(canvasaddcar,text="Ü.Yılı")
    labeladdedcaryil.place(x=340,y=18,width=60)
    labeladdedcaryakit=Label(canvasaddcar,text="Y.Türü")
    labeladdedcaryakit.place(x=400,y=18,width=60)
    labeladdedcarvites=Label(canvasaddcar,text="Vites")
    labeladdedcarvites.place(x=460,y=18,width=60)
    labeladdedcarmotorgucu=Label(canvasaddcar,text="M.Gücü")
    labeladdedcarmotorgucu.place(x=520,y=18,width=60)
    labeladdedcarkasa=Label(canvasaddcar,text="K.Tipi")
    labeladdedcarkasa.place(x=580,y=18,width=60)
    labeladdedcarhacim=Label(canvasaddcar,text="Hacim")
    labeladdedcarhacim.place(x=
    640,y=18,width=60)
    labeladdedcarcekis=Label(canvasaddcar,text="Çekiş")
    labeladdedcarcekis.place(x=700,y=18,width=60)
    labeladdedcarkapi=Label(canvasaddcar,text="Kapı")
    labeladdedcarkapi.place(x=760,y=18,width=60)
    labeladdedcarrenk=Label(canvasaddcar,text="Renk")
    labeladdedcarrenk.place(x=820,y=18,width=60)
    labeladdedcarmno=Label(canvasaddcar,text="M.No")
    labeladdedcarmno.place(x=880,y=18,width=60)
    labeladdedcarsasino=Label(canvasaddcar,text="Şaşi")
    labeladdedcarsasino.place(x=940,y=18,width=60)
    labeladdedcardurumu=Label(canvasaddcar,text="Durumu")
    labeladdedcardurumu.place(x=1000,y=18,width=60)
    

    canvasaddcust=Canvas(meet)
    canvasaddcust.place(x=0,y=250,width=1100,height=250)
    canvasaddcust.create_line(5, 40, 1100, 40)
    labeladdcust=Label(canvasaddcust,text="Eklenen Müşteriler",font="Arial 12 bold")
    labeladdcust.place(x=2,y=10)
    labeladdedcustname=Label(canvasaddcust,text="Adı")
    labeladdedcustname.place(x=180,y=18,width=70)
    labeladdedcustmarka=Label(canvasaddcust,text="Soyadı")
    labeladdedcustmarka.place(x=240,y=18,width=60)
    labeladdedcustmodel=Label(canvasaddcust,text="Tc.No")
    labeladdedcustmodel.place(x=300,y=18,width=60)
    labeladdedcustyil=Label(canvasaddcust,text="D.Tarihi")
    labeladdedcustyil.place(x=360,y=18,width=60)
    labeladdedcustyakit=Label(canvasaddcust,text="Adres")
    labeladdedcustyakit.place(x=420,y=18,width=60)
    labeladdedcustvites=Label(canvasaddcust,text="Telefon")
    labeladdedcustvites.place(x=480,y=18,width=60)
    labeladdedcustmotorgucu=Label(canvasaddcust,text="Meslek")
    labeladdedcustmotorgucu.place(x=540,y=18,width=60)
    labeladdedcustkasa=Label(canvasaddcust,text="Ehliyet")
    labeladdedcustkasa.place(x=600,y=18,width=60)
    labeladdedcusthacim=Label(canvasaddcust,text="M.Durumu")
    labeladdedcusthacim.place(x=
    660,y=18,width=60)
    labeladdedcusthacim=Label(canvasaddcust,text="E.Durumu")
    labeladdedcusthacim.place(x=740,y=18,width=60)

    canvaskirala=Canvas(meet)
    canvaskirala.place(x=0,y=500,width=1100,height=250)
    canvaskirala.create_line(5, 40, 1100, 40)
    labeladdkirala=Label(canvaskirala,text="Kira Bilgisi",font="Arial 15 bold")
    labeladdkirala.place(x=2,y=8)
    labelselectedcar=Label(canvaskirala,text="Seçilen Araç")
    labelselectedcar.place(x=300,y=15)
    labelselectedcust=Label(canvaskirala,text="Seçilen Müşteri")
    labelselectedcust.place(x=420,y=15)
    global entrygunsayı,entryrota
    labelgunsayi=Label(canvaskirala,text="Gün Sayısı",font="Times 12 bold")
    labelgunsayi.place(x=2,y=50)
    entrygunsayı=Entry(canvaskirala)
    entrygunsayı.place(x=120,y=50)
    labelrota=Label(canvaskirala,text="Yolculuk Rotası",font="Times 12 bold")
    labelrota.place(x=2,y=85)
    entryrota=Entry(canvaskirala)
    entryrota.place(x=120,y=85)
    btnkkiralananaraçlar=Button(canvaskirala,text="Kiralanan Araçlar",font="Times 13 bold",bg="#FFC93C",fg="#333",command=lambda:(exitmeet(),rentedwcust()))
    btnkkiralananaraçlar.place(x=600,y=160)
    btnfetch=Button(canvaskirala,text="Eklenenleri getir",font="Times 13 bold",bg="#5BC0F8",fg="#fff",command=lambda:(fetchcars(),fetchcust(),carselectbtn(),custelectbtn()))
    btnfetch.place(x=800,y=160)
    btnanahome=Button(canvaskirala,text="Anasayfa",font="Times 13 bold",bg="#FFC93C",fg="#333",command=lambda:(exitmeet(),homewithoutpassw()))
    btnanahome.place(x=1000,y=160)
    def kirala():
        gunentry=entrygunsayı.get()
        rotaentry=entryrota.get()
        try:
            mydb=mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="custdb"
                )
            mycursor=mydb.cursor()
            fetchcustquery= "SELECT * FROM custtable"
            mycursor.execute(fetchcustquery)
            recordscust = mycursor.fetchall()
            for row in recordscust:
              selectsecreen=messagebox.askyesno("Uyarı",f"{row[0]} {row[1]} isimli müşteriye seçtiğiniz araç {gunentry} günlüğüne kiralansın mı?")
              #create database for rentedcarandcustomers
            if selectsecreen>0:
                try:
                    mydb=mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="",
                        database=""
                    )
                    mycursor=mydb.cursor()
                    mycursor.execute("CREATE DATABASE rented2")
                    
                    print("Databese yazıldı")
                except:
                    print("Bağlantı Başarısız")
        except:
            print("İsim Bulunamadı")          
    def createrentedtable():
        try:
            mydb=mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="rented2"
            )
            mycursor=mydb.cursor()
            mycursor.execute("CREATE TABLE rentedtable (müsteriadi VARCHAR(255),müsterisoyadi VARCHAR(255),arabamarkası VARCHAR(255),arabamodeli VARCHAR(255),rota VARCHAR(255),gün VARCHAR(255))")
            print("Tablo oluşturuldu")
        except:
            print("Tablo oluşturulamadı")
          
    btnkirala=Button(canvaskirala,text="Kirala",font="Times 13 bold",bg="#5BC0F8",fg="#fff",command=lambda:(kirala(),createrentedtable(),insertrentedtable()))
    btnkirala.place(x=2,y=160)
    btntemizle=Button(canvaskirala,text="Sil",font="Times 13 bold",bg="#ff0505",fg="#fff",command=lambda:(infocarclear(),infocustclear(),entryinfoclear()))
    btntemizle.place(x=100,y=160)    
    meet.mainloop()
def insertrentedtable():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="rented2"
        )
    mycursor = mydb.cursor()
    sql = "INSERT INTO rentedtable (müsteriadi, müsterisoyadi,arabamarkası,arabamodeli,rota,gün) VALUES (%s, %s, %s, %s, %s, %s)"
    val = ("Enis","Yılmaz","Superb","Skoda",f"{entryrota.get()}",f"{entrygunsayı.get()}")
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Tabloya veri eklendi.")    
    #kirada olan araçlar
def rentedwcust():
    rented=tk.Tk()
    rented.geometry("900x600")
    rented.resizable(0,0)
    rented.title("rENtİS v2.1.3")
    def exitrented():
        rented.destroy()
    canvasrented=Canvas(rented)
    canvasrented.place(x=0,y=0,width=900,height=90)
    canvasrented.create_line(5, 40, 1100, 40)
    labeladdrented=Label(canvasrented,text="Kiralanmış Araçlar",font="Arial 12 bold")
    labeladdrented.place(x=2,y=13)
    lblcarrented=Label(canvasrented,text="rENt",font="Times 27 bold",fg="#5BC0F8")
    lblcarrented.place(x=390,y=10)
    lblcarrentis=Label(canvasrented,text="İS",font="Times 27 bold",fg="#FFC93C")
    lblcarrentis.place(x=470,y=10)
    canvasleft=Canvas(rented)
    canvasleft.place(x=2,y=45,width=400,height=430)
    labelalanmusteriad=Label(canvasleft,text=" Aracı alan müşteri adı:",font="Arial 12 bold")
    labelalanmusteriad.place(x=0,y=10)
    labelalanmusterisoyad=Label(canvasleft,text="Aracı alan müşteri soyadı:",font="Arial 12 bold")
    labelalanmusterisoyad.place(x=0,y=50)
    labelrentedcarname=Label(canvasleft,text=" Kiralanan aracın modeli:",font="Arial 12 bold")
    labelrentedcarname.place(x=0,y=100)
    labelrentedcarmarka=Label(canvasleft,text="Kiralanan aracın markası:",font="Arial 12 bold")
    labelrentedcarmarka.place(x=0,y=150)
    labelrentedrota=Label(canvasleft,text=" Yolculuk Rotası:",font="Arial 12 bold")
    labelrentedrota.place(x=0,y=200)
    labelrentedgün=Label(canvasleft,text="Toplam kiralanan gün:",font="Arial 12 bold")
    labelrentedgün.place(x=0,y=250)
    labelrentedcharge=Label(canvasleft,text="Bu araba için günlük ücret:",font="Arial 12 bold")
    labelrentedcharge.place(x=0,y=300)
    def addtorented():
        #yolculuk verisi
        try:
            mydb=mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="rented2"
                )
            mycursor=mydb.cursor()
            fetchrentedquery= "SELECT * FROM rentedtable"
            mycursor.execute(fetchrentedquery)
            recordsrented = mycursor.fetchall()
            for row in recordsrented:
                
                labelrentedrota=Label(canvasleft,text=f"{row[4]}",font="Times 13")
                labelrentedrota.place(x=135,y=200)
                labelrentedrota.configure(anchor="center")
                labelrentedday=Label(canvasleft,text=f"{row[5]}",font="Times 13")
                labelrentedday.place(x=180,y=250)
        except:            
            print("İsim Bulunamadı")
            #müşterinin verisi
        try:
            mydb=mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="custdb"
                )
            mycursor=mydb.cursor()
            fetchcustquery= "SELECT * FROM custtable"
            mycursor.execute(fetchcustquery)
            recordscust = mycursor.fetchall()
            for custrow in recordscust:
                
                labelrentedrota=Label(canvasleft,text=f"{custrow[0]}",font="Times 13")
                labelrentedrota.place(x=180,y=10)
                labelrentedrota.configure(anchor="center")
                labelrentedday=Label(canvasleft,text=f"{custrow[1]}",font="Times 13")
                labelrentedday.place(x=200,y=50)
        except:
            print("İsim Bulunamadı") 

            #arabanın verisi           
        try:
            mydb=mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="cardb"
                )
            mycursor=mydb.cursor()
            fetchcarquery= "SELECT * FROM cartable"
            mycursor.execute(fetchcarquery)
            recordscar = mycursor.fetchall()
            for carrow in recordscar:
                
                labelrentedrota=Label(canvasleft,text=f"{carrow[2]}",font="Times 13")
                labelrentedrota.place(x=193,y=100)
                labelrentedrota.configure(anchor="center")
                labelrentedday=Label(canvasleft,text=f"{carrow[1]}",font="Times 13")
                labelrentedday.place(x=204,y=150)
                labelucrettext=Label(canvasleft,text=f"{carrow[14]} TL",font="Times 13")
                labelucrettext.place(x=210,y=300)
                labelrenteducret=Label(canvasleft,text=f"{row[5]} günlük için toplam ücret :{int(row[5])*int(carrow[14])}TL",font="Arial 14 bold",bg="red")
                labelrenteducret.place(x=10,y=380)
                
        except:
            print("İsim Bulunamadı")         

    
    btnview=Button(rented,text="Kiradaki Araçları Görüntüle",font="Times 13 bold",bg="#6cc070",fg="#fff",command=addtorented) 
    btnview.place(x=20,y=500)
    btnrentedhome=Button(rented,text="Anasayfa",font="Times 13 bold",bg="#0081C9",fg="#fff",command=lambda:(exitrented(),homewithoutpassw())) 
    btnrentedhome.place(x=270,y=500) 
     
    

    rented.mainloop()



def on_click(event):
    usrnameEntry.configure(state="normal")
    usrnameEntry.delete(0,END)
    usrnameEntry.unbind('<Button-1>',on_click_id)
    
on_click_id=usrnameEntry.bind('<Button-1>',on_click)

def on_click2(event2):
    passwEntry.configure(state="normal")
    passwEntry.delete(0,END)
    passwEntry.unbind('<Button-1>',on_click_id2)
    
on_click_id2=passwEntry.bind('<Button-1>',on_click2)      


root.mainloop()

    
        