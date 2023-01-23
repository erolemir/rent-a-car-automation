from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector


class otoKiralama:
    def __init__(self):

        self.pencere = Tk()
        self.pencere.title("Oto Kiralama")
        self.pencere.geometry("850x650+350+50")
        self.pencere.resizable(FALSE,FALSE)
        self.pencere.configure(background="grey10")
        self.database()
        self.musteriKayit()
        self.musteriBilgi()
        self.arabaBilgi()
        self.musteriler1()
        self.araclar1()
        self.kiraGunu1()

    def database(self):
        self.mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "") 

        # Bağlantıyı kontrol edin
        if self.mydb.is_connected():
            print("Veritabanına bağlantı başarılı bir şekilde sağlandı.")
            
            
        self.dbcursor=self.mydb.cursor()
        self.dbcursor.execute("CREATE DATABASE IF NOT EXISTS aracKiralama")
        self.dbcursor.execute("USE aracKiralama")
        self.dbcursor.execute("""
        CREATE TABLE IF NOT EXISTS musteri_bilgileri (id INT AUTO_INCREMENT PRIMARY KEY, ad VARCHAR(255), soyad VARCHAR(255), tc_kimlik VARCHAR(255), dogum_tarihi VARCHAR(255), adres VARCHAR(255), telefon VARCHAR(255), meslek VARCHAR(255), ehliyet_sinifi VARCHAR(255), medeni_durum VARCHAR(255), egitim_durumu VARCHAR(255))""")
        

        # Araç bilgileri tablosunu oluştur
        self.dbcursor.execute("CREATE TABLE IF NOT EXISTS arac_bilgileri (id INT AUTO_INCREMENT PRIMARY KEY, marka VARCHAR(255),  uretim_yili VARCHAR(255), yakit_turu VARCHAR(255), vites VARCHAR(255), motor_gucu VARCHAR(255), kasa_tipi VARCHAR(255), motor_hacmi VARCHAR(255), kapi VARCHAR(255), renk VARCHAR(255), motor_no VARCHAR(255), sasi_no VARCHAR(255), gunluk_kiralama_bedeli VARCHAR(255), kirada_mi VARCHAR(255), kullanim_disi_mi VARCHAR(255))")
        
        # Araç kiralama bilgi tablosu
        self.dbcursor.execute("CREATE TABLE IF NOT EXISTS kiralanan_arac(id INT AUTO_INCREMENT PRIMARY KEY, musteri varchar(255), arac varchar(255), kira_gunu VARCHAR(255))")
        
        
    
   
# ------------------------------------------Müşteri Kayıt Ekranı------------------------------------------
    def musteriKayitEkran(self):
        self.kayitEkran= Tk()
        self.kayitEkran.title("Müşteri Kayıt")
        self.kayitEkran.geometry("450x650+300+30")
        self.kayitEkran.resizable(FALSE,FALSE)
        self.kayitEkran.configure(background="grey10")
        
        self.baslik1 = Label(self.kayitEkran,text="Müşteri Bilgileri", fg="White",bg="grey10", font="Fixedsys 10 bold")
        self.baslik1.place(x=90,y=60)
        
        self.tcNo= Label(self.kayitEkran,text="Tc No:",fg="#EEEEEE",bg="grey10") 
        self.tcNo.place(x=50,y=100)
        self.tcNoEntry= Entry(self.kayitEkran,bg="lavender",bd=5, relief=RAISED)
        self.tcNoEntry.place(x=150,y=100)
        
        self.ad= Label(self.kayitEkran,text="Ad:",fg="#EEEEEE",bg="grey10")
        self.ad.place(x=50,y=135)
        self.adEntry= Entry(self.kayitEkran,bg="lavender",bd=5, relief=RAISED)
        self.adEntry.place(x=150,y=135)
        
        self.soyad= Label(self.kayitEkran,text="Soyad:",fg="#EEEEEE",bg="grey10")
        self.soyad.place(x=50,y=170)
        self.soyadEntry= Entry(self.kayitEkran,bg="lavender",bd=5, relief=RAISED)
        self.soyadEntry.place(x=150,y=170)
        
        self.dogumTarihi= Label(self.kayitEkran,text="Doğum Tarihi:",fg="#EEEEEE",bg="grey10")
        self.dogumTarihi.place(x=50,y=205)
        self.dogumTarihiEntry= Entry(self.kayitEkran,bg="lavender",bd=5, relief=RAISED)
        self.dogumTarihiEntry.place(x=150,y=205)
        
        self.adres= Label(self.kayitEkran,text="Adres:",fg="#EEEEEE",bg="grey10")
        self.adres.place(x=50,y=240)
        self.adresEntry= Entry(self.kayitEkran,bg="lavender",bd=5, relief=RAISED)
        self.adresEntry.place(x=150,y=240)
        
        self.telNo= Label(self.kayitEkran,text="Telefon No:",fg="#EEEEEE",bg="grey10")
        self.telNo.place(x=50,y=275)
        self.telNoEntry= Entry(self.kayitEkran,bg="lavender",bd=5, relief=RAISED)
        self.telNoEntry.place(x=150,y=275)
        
        self.meslek= Label(self.kayitEkran,text="Meslek:",fg="#EEEEEE",bg="grey10")
        self.meslek.place(x=50,y=310)
        self.meslekEntry= Entry(self.kayitEkran,bg="lavender",bd=5, relief=RAISED)
        self.meslekEntry.place(x=150,y=310)
        
        self.ehliyetSinifi= Label(self.kayitEkran,text="Ehliyet Sınıfı:",fg="#EEEEEE",bg="grey10")
        self.ehliyetSinifi.place(x=50,y=345)
        self.ehliyetSinifiEntry= Entry(self.kayitEkran,bg="lavender",bd=5, relief=RAISED)
        self.ehliyetSinifiEntry.place(x=150,y=345)
        
        self.medeniDurum= Label(self.kayitEkran,text="Medeni Durum:",fg="#EEEEEE",bg="grey10")
        self.medeniDurum.place(x=50,y=380)
        self.medeniDurumEntry= Entry(self.kayitEkran,bg="lavender",bd=5, relief=RAISED)
        self.medeniDurumEntry.place(x=150,y=380)
        
        self.egitimDurumu= Label(self.kayitEkran,text="Eğitim Durumu:",fg="#EEEEEE",bg="grey10")
        self.egitimDurumu.place(x=50,y=415)
        self.egitimDurumuEntry= Entry(self.kayitEkran,bg="lavender",bd=5, relief=RAISED)
        self.egitimDurumuEntry.place(x=150,y=415)
        
        
        
        self.Kaydet = Button(self.kayitEkran,bd=5, fg="black", font=('Fixedsys', 14, 'bold'), width=14, text="Kaydet", bg="white", cursor="hand2", overrelief="solid", height=2,command=self.musteri_bilgileri_kaydet)
        self.Kaydet.place(x=100,y=500)


    def musteri_bilgileri_kaydet(self):
        self.dbcursor=self.mydb.cursor()
        self.dbcursor.execute(f"INSERT INTO musteri_bilgileri (tc_kimlik,ad,soyad,dogum_tarihi,adres,telefon,meslek,ehliyet_sinifi,medeni_durum,egitim_durumu) VALUES ('{self.tcNoEntry.get()}','{self.adEntry.get()}','{self.soyadEntry.get()}','{self.dogumTarihiEntry.get()}','{self.adresEntry.get()}','{self.telNoEntry.get()}','{self.meslekEntry.get()}','{self.ehliyetSinifiEntry.get()}','{self.medeniDurumEntry.get()}','{self.egitimDurumuEntry.get()}')")
        self.mydb.commit()

        
# --------------------------------------------Oto Kayıt------------------------------------------
    def otoKayit(self):
        self.otoKayitEkran= Tk()
        self.otoKayitEkran.title("Otomobil Kayıt")
        self.otoKayitEkran.geometry("550x650+300+30")
        self.otoKayitEkran.resizable(FALSE,FALSE)
        self.otoKayitEkran.configure(background="grey10")
        
        self.baslik11 = Label(self.otoKayitEkran,text="Otomobil Kayit", fg="White",bg="grey10", font="Fixedsys 10 bold")
        self.baslik11.place(x=90,y=60)
        
        self.marka = Label(self.otoKayitEkran,text="Marka:",fg="#EEEEEE",bg="grey10")
        self.marka.place(x=50,y=100)
        self.markaCombobox = ttk.Combobox(self.otoKayitEkran,values=["Audi","BMW","Citroen","Fiat","Ford","Honda","Hyundai","Kia","Mercedes","Nissan","Opel","Peugeot","Renault","Skoda","Toyota","Volkswagen","Volvo"])        
        self.markaCombobox.place(x=150,y=100)
        
        
        self.aracTipi = Label(self.otoKayitEkran,text="Araç Tipi:",fg="#EEEEEE",bg="grey10")
        self.aracTipi.place(x=50,y=135)
        self.aracTipiCombobox = ttk.Combobox(self.otoKayitEkran,values=["Sedan","Hatchback","Station Wagon","SUV","Crossover","Coupe","Convertible","MPV","Pickup","Van","Minivan","Cabriolet","Roadster","Limousine","Sports Car","Super Car","Semi-Trailer","Truck","Tractor","Bus","Motorcycle","Bicycle","Tricycle","Quad Bike","ATV","Boat","Yacht","Jet Ski","Scooter","Snowmobile","Go Kart","Golf Cart","Hovercraft","Hoverboard","Segway","Unicycle","Other"])
        self.aracTipiCombobox.place(x=150,y=135)
        
        self.UretimYili = Label(self.otoKayitEkran,text="Üretim Yılı:",fg="#EEEEEE",bg="grey10")
        self.UretimYili.place(x=50,y=170)
        self.UretimYiliCombobox = ttk.Combobox(self.otoKayitEkran,values=["2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020","2021"])
        self.UretimYiliCombobox.place(x=150,y=170)
        
        self.yakitTuru = Label(self.otoKayitEkran,text="Yakıt Türü:",fg="#EEEEEE",bg="grey10")
        self.yakitTuru.place(x=50,y=205)
        self.yakitTuruCombobox = ttk.Combobox(self.otoKayitEkran,values=["Benzin","Dizel","LPG","Elektrik","Hibrit"])
        self.yakitTuruCombobox.place(x=150,y=205)
        
        self.vitesTuru = Label(self.otoKayitEkran,text="Vites Türü:",fg="#EEEEEE",bg="grey10")
        self.vitesTuru.place(x=50,y=240)
        self.vitesTuruCombobox = ttk.Combobox(self.otoKayitEkran,values=["Manuel","Otomatik"])
        self.vitesTuruCombobox.place(x=150,y=240)
        
        self.motorGucu = Label(self.otoKayitEkran,text="Motor Gücü:",fg="#EEEEEE",bg="grey10")
        self.motorGucu.place(x=50,y=275)
        self.motorGucuCombobox = ttk.Combobox(self.otoKayitEkran,values=["50 HP","75 HP","100 HP","125 HP","150 HP","175 HP","200 HP","225 HP","250 HP","275 HP","300 HP","325 HP","350 HP","375 HP","400 HP","425 HP","450 HP","475 HP","500 HP"])
        self.motorGucuCombobox.place(x=150,y=275)
        
        self.motorHacmi = Label(self.otoKayitEkran,text="Motor Hacmi:",fg="#EEEEEE",bg="grey10")
        self.motorHacmi.place(x=50,y=310)
        self.motorHacmiCombobox = ttk.Combobox(self.otoKayitEkran,values=["1000 cc","1250 cc","1500 cc","1750 cc","2000 cc","2250 cc","2500 cc","2750 cc","3000 cc","3250 cc","3500 cc","3750 cc","4000 cc","4250 cc","4500 cc","4750 cc","5000 cc"])
        self.motorHacmiCombobox.place(x=150,y=310)
        
        self.cekis = Label(self.otoKayitEkran,text="Çekiş:",fg="#EEEEEE",bg="grey10")
        self.cekis.place(x=50,y=345)
        self.cekisCombobox = ttk.Combobox(self.otoKayitEkran,values=["Önden Çekiş","Arkadan Çekiş","4 Çeker"])
        self.cekisCombobox.place(x=150,y=345)
        
        self.kapıSayisi = Label(self.otoKayitEkran,text="Kapı Sayısı:",fg="#EEEEEE",bg="grey10")
        self.kapıSayisi.place(x=50,y=380)
        self.kapıSayisiCombobox = ttk.Combobox(self.otoKayitEkran,values=["2","3","4","5"])
        self.kapıSayisiCombobox.place(x=150,y=380)
        
        self.renk = Label(self.otoKayitEkran,text="Renk:",fg="#EEEEEE",bg="grey10")
        self.renk.place(x=50,y=415)
        self.renkCombobox = ttk.Combobox(self.otoKayitEkran,values=["Beyaz","Siyah","Gri","Kırmızı","Mavi","Yeşil","Sarı","Turuncu","Bordo","Lacivert","Mor","Pembe","Burgu","Bej","Altın","Gümüş","Bordo","Beyaz","Siyah","Gri","Kırmızı","Mavi","Yeşil","Sarı","Turuncu","Bordo","Lacivert","Mor","Pembe","Burgu","Bej","Altın","Gümüş","Bordo"])
        self.renkCombobox.place(x=150,y=415)
        
        self.motorNo = Label(self.otoKayitEkran,text="Motor No:",fg="#EEEEEE",bg="grey10")
        self.motorNo.place(x=50,y=450)
        self.motorNoEntry= Entry(self.otoKayitEkran,width=23)
        self.motorNoEntry.place(x=150,y=450)
        
        self.şasiNo = Label(self.otoKayitEkran,text="Şasi No:",fg="#EEEEEE",bg="grey10")
        self.şasiNo.place(x=50,y=485)
        self.şasiNoEntry= Entry(self.otoKayitEkran,width=23)
        self.şasiNoEntry.place(x=150,y=485)
        
        self.kiralamaBedeli = Label(self.otoKayitEkran,text="Kiralama Günü:",fg="#EEEEEE",bg="grey10")   
        self.kiralamaBedeli.place(x=50,y=520)
        self.kiralamaBedeliEntry= Entry(self.otoKayitEkran,width=23)
        self.kiralamaBedeliEntry.place(x=150,y=520)
        
        self.kiradaMi = Label(self.otoKayitEkran,text="Kirada mı?",fg="#EEEEEE",bg="grey10")
        self.kiradaMi.place(x=50,y=555)
        self.kiradaMiCombobox = ttk.Combobox(self.otoKayitEkran,values=["Evet","Hayır"])
        self.kiradaMiCombobox.place(x=150,y=555)
        
        self.kullanimDişiMi = Label(self.otoKayitEkran,text="Kullanım Dışı mı?",fg="#EEEEEE",bg="grey10")
        self.kullanimDişiMi.place(x=50,y=590)
        self.kullanimDişiMiCombobox = ttk.Combobox(self.otoKayitEkran,values=["Evet","Hayır"])
        self.kullanimDişiMiCombobox.place(x=150,y=590)
        
        
        self.Kaydet1 = Button(self.otoKayitEkran,bd=5, fg="black", font=('Fixedsys', 14, 'bold'), width=14, text="Kaydet", bg="white", cursor="hand2", overrelief="solid", height=2,command=self.otomobilBilgileriKaydet)
        self.Kaydet1.place(x=350,y=300)
        

        
        
    def otomobilBilgileriKaydet(self):
        self.dbcursor=self.mydb.cursor()
        self.dbcursor.execute(f"INSERT INTO arac_bilgileri (marka,uretim_yili,yakit_turu,vites,motor_gucu,kasa_tipi,motor_hacmi,kapi,renk,motor_no,sasi_no,gunluk_kiralama_bedeli,kirada_mi,kullanim_disi_mi) VALUES ('{self.markaCombobox.get()}','{self.UretimYiliCombobox.get()}','{self.yakitTuruCombobox.get()}','{self.vitesTuruCombobox.get()}','{self.motorGucuCombobox.get()}','{self.aracTipiCombobox.get()}','{self.motorHacmiCombobox.get()}','{self.kapıSayisiCombobox.get()}','{self.renkCombobox.get()}','{self.motorNoEntry.get()}','{self.şasiNoEntry.get()}','{self.kiralamaBedeliEntry.get()}','{self.kiradaMiCombobox.get()}','{self.kullanimDişiMiCombobox.get()}')")
        self.mydb.commit()
        
# ------------------------------------------------Kiralama Ekranı-------------------------------------------------------
    def kiralamaEkranı(self):
        self.kiralaKayitEkran= Tk()
        self.kiralaKayitEkran.title("Araç Kiralama")
        self.kiralaKayitEkran.geometry("450x350+300+30")
        self.kiralaKayitEkran.resizable(FALSE,FALSE)
        self.kiralaKayitEkran.configure(background="grey10")
        
        self.baslik111 = Label(self.kiralaKayitEkran, text="Araç Kiralama", fg="#EEEEEE", bg="grey10", font=("Fixedsys", 25, "bold"))
        self.baslik111.place(x=80,y=30)
        
        self.musteriBilgi1 = Label(self.kiralaKayitEkran,text="Müşteri:",fg="#EEEEEE",bg="grey10")
        self.musteriBilgi1.place(x=50,y=135)
        self.musteriBilgi1Combobox = ttk.Combobox(self.kiralaKayitEkran,values=self.musteriListe)
        self.musteriBilgi1Combobox.place(x=150,y=135)
        
        self.aracBilgi = Label(self.kiralaKayitEkran,text="Araç:",fg="#EEEEEE",bg="grey10")
        self.aracBilgi.place(x=50,y=180)
        self.aracBilgiCombobox = ttk.Combobox(self.kiralaKayitEkran,values=self.arabaListe)
        self.aracBilgiCombobox.place(x=150,y=180)
        
        self.kacgGunKiralanacak = Label(self.kiralaKayitEkran,text="Kaç Gün Kiralanacak:",fg="#EEEEEE",bg="grey10")
        self.kacgGunKiralanacak.place(x=35,y=225)
        
        self.kacgGunKiralanacakEntry= Entry(self.kiralaKayitEkran,width=23)
        self.kacgGunKiralanacakEntry.place(x=150,y=225)
        
        self.musteriBilgiBtn = Button(self.kiralaKayitEkran,bd=5, fg="black", font=('Fixedsys', 14, 'bold'), width=18, text="Kaydet", bg="white", cursor="hand2", overrelief="solid", height=2,command=self.kiralananAracKaydet)
        self.musteriBilgiBtn.place(x=150,y=250)
        
        self.veritabaniBtn = Button(self.kiralaKayitEkran,bd=5, fg="black", font=('Fixedsys', 14, 'bold'), width=18, text="Veritabanı Güncelle", bg="white", cursor="hand2", overrelief="solid", height=2,command=self.kiralananAracGuncelle)
        self.veritabaniBtn.place(x=150,y=300)
        
    def musteriBilgi(self):
        self.musteriListe = []
        self.dbcursor=self.mydb.cursor()
        self.dbcursor.execute("SELECT ad,soyad FROM musteri_bilgileri")
        self.musteriler = self.dbcursor.fetchall()
        
        for veri in self.musteriler:
            self.musteriListe.append(veri)
            
    def arabaBilgi(self):
        self.arabaListe = []
        self.arabacursor=self.mydb.cursor()
        self.arabacursor.execute("SELECT marka FROM arac_bilgileri")
        self.arabalar = self.arabacursor.fetchall()
        
        for veri1 in self.arabalar:
            self.arabaListe.append(veri1)
            print(veri1)
            
    def kiralananAracKaydet(self):
        self.kaydetcursor=self.mydb.cursor()
        self.kaydetcursor.execute(f"INSERT INTO kiralanan_arac (musteri,arac,kira_gunu) VALUES ('{self.musteriBilgi1Combobox.get()}','{self.aracBilgiCombobox.get()}','{self.kacgGunKiralanacakEntry.get()}')")
        self.mydb.commit()
        
    def kiralananAracGuncelle(self):
        self.kiralaKayitEkran.destroy()
        self.musteriBilgi()
        self.arabaBilgi()
        self.kiralamaEkranı()
        
        
        
# ------------------------------------------------Bilgi Ekranı-------------------------------------------------------
    def bilgiEkran7(self):
        self.bilgiEkran= Tk()
        self.bilgiEkran.title("Bilgi Ekranı")
        self.bilgiEkran.geometry("450x350+300+30")
        self.bilgiEkran.resizable(FALSE,FALSE)
        self.bilgiEkran.configure(background="grey10")
        
        self.baslik1111 = Label(self.bilgiEkran, text="Bilgi Ekranı", fg="#EEEEEE", bg="grey10", font=("Fixedsys", 25, "bold"))
        self.baslik1111.place(x=80,y=30)
        
        self.musteriNe = Label(self.bilgiEkran,text="Müşteri İsmi:",fg="#EEEEEE",bg="grey10")
        self.musteriNe.place(x=50,y=135)
        
        self.musteriNe1 = Label(self.bilgiEkran,text=self.musterilerr,fg="#EEEEEE",bg="grey10")
        self.musteriNe1.place(x=150,y=135)
        
        self.aracNe = Label(self.bilgiEkran,text="Araç Markası:",fg="#EEEEEE",bg="grey10")
        self.aracNe.place(x=50,y=170)
        
        self.aracNe1 = Label(self.bilgiEkran,text=self.araclarr,fg="#EEEEEE",bg="grey10")
        self.aracNe1.place(x=150,y=170)
        
        self.kiraGun = Label(self.bilgiEkran,text="Kiralanan Gün",fg="#EEEEEE",bg="grey10")
        self.kiraGun.place(x=50,y=205)
        
        self.kiraGun1 = Label(self.bilgiEkran,text=self.kiraa,fg="#EEEEEE",bg="grey10")
        self.kiraGun1.place(x=150,y=205)
        
        self.veriGuncelle = Button(self.bilgiEkran, bd=5, fg="black", font=('VerdanaPro', 14, 'bold'), width=14,
                                    text="Güncelle", bg="white", cursor="hand2", overrelief="solid",
                                    height=1, command=self.Guncellee)
        self.veriGuncelle.place(x=150, y=275)
        
    def musteriler1(self):
        self.musterilerr = []
        self.mustericursor=self.mydb.cursor()
        self.mustericursor.execute("SELECT musteri FROM kiralanan_arac")
        self.musteri1 = self.mustericursor.fetchall()
        
        
        for veri2 in self.musteri1:
            veri2_str = " ".join(str(x) for x in veri2)
            self.musterilerr.append(veri2_str)
            print(veri2_str)
            

    def araclar1(self):
        self.araclarr = []
        self.araccursor=self.mydb.cursor()
        self.araccursor.execute("SELECT arac FROM kiralanan_arac")
        self.arac1 = self.araccursor.fetchall()
        
        
        for veri3 in self.arac1:
            veri3_str = " ".join(str(x) for x in veri3)
            self.araclarr.append(veri3_str)
            print(veri3_str)    

    def kiraGunu1(self):
        self.kiraa = []
        self.kiracursor=self.mydb.cursor()
        self.kiracursor.execute("SELECT kira_gunu FROM kiralanan_arac")
        self.kira1 = self.kiracursor.fetchall()
        
        
        for veri4 in self.kira1:
            veri4_str = " ".join(str(x) for x in veri4)
            self.kiraa.append(veri4_str)
            print(veri4_str)


    def Guncellee(self):
        self.bilgiEkran.destroy()
        self.musteriler1()
        self.araclar1()
        self.kiraGunu1()
        self.bilgiEkran7()
    
# ------------------------------------------Arama Penceresi(Final)------------------------------------------
    
    def aramaEkran(self):
        self.aramaEkranPencere=Tk()
        self.aramaEkranPencere.geometry('500x250')
        self.aramaEkranPencere.title('Arama Penceresi(Terminale yazar)')
        self.aramaEkranPencere.config(bg='grey10')
        self.Label15=Label(self.aramaEkranPencere,text="İsme Göre Arama",fg="#EEEEEE",bg="grey10",font=("Fixedsys", 20, "bold"))
        self.Label15.place(x=140,y=10)
        self.aramaEntry=Entry(self.aramaEkranPencere,width=35)
        self.aramaEntry.place(x=150,y=90)

        self.AramaBtnnu=Button(self.aramaEkranPencere)
        self.AramaBtnnu.config(text="Ara",bg="white",fg="black",font=('VerdanaPro', 14, 'bold'),width=14)
        self.AramaBtnnu.config(command=self.aramaFonksiyonu)
        # Terminale yazdırıyor
        self.AramaBtnnu.place(x=170,y=150)
       
    def aramaFonksiyonu(self):
        self.arananKelime=self.aramaEntry.get()
        self.Sorguu = self.mydb.cursor()
        self.Sorguu.execute("SELECT  * FROM musteri_bilgileri where ad=%s", (self.arananKelime,))
        self.data = self.Sorguu.fetchall()
        print('Arama Sonucu: ')
        print(self.data)


        
 # ------------------------------------------Ana Ekran------------------------------------------
    def musteriKayit(self):
        self.baslik = Label(self.pencere,text="Araç Kiralama Otomasyonu", fg="White",bg="grey10", font="Fixedsys 22 bold")
        self.baslik.place(x=220,y=60)
        self.kayitEkranBtn = Button(self.pencere,bd=5, fg="black", font=('Fixedsys', 14, 'bold'), width=14, text="Müşteri Kayıt", bg="white", cursor="hand2", overrelief="solid", height=3,command=self.musteriKayitEkran)
        self.kayitEkranBtn.place(x=350,y=150)
        
        self.otoKayitEkranBtn = Button(self.pencere,bd=5, fg="black", font=('Fixedsys', 14, 'bold'), width=14, text="Otomobil Kayıt", bg="white", cursor="hand2", overrelief="solid", height=3,command=self.otoKayit)
        self.otoKayitEkranBtn.place(x=350,y=250)
        
        self.kiralaKayitEkranBtn = Button(self.pencere,bd=5, fg="black", font=('Fixedsys', 14, 'bold'), width=14, text="Araç Kirala", bg="white", cursor="hand2", overrelief="solid", height=3,command=self.kiralamaEkranı)
        self.kiralaKayitEkranBtn.place(x=350,y=350)
        
        self.bilgilerBtn = Button(self.pencere,bd=5, fg="black", font=('Fixedsys', 14, 'bold'), width=14, text="Bilgileri Gör", bg="white", cursor="hand2", overrelief="solid", height=3,command=self.bilgiEkran7)
        self.bilgilerBtn.place(x=350,y=450)
        
        self.aramaBtn = Button(self.pencere,bd=5, fg="black", font=('Fixedsys', 14, 'bold'), width=14, text="Arama Ekranı", bg="white", cursor="hand2", overrelief="solid", height=3,command=self.aramaEkran)
        self.aramaBtn.place(x=350,y=550)

        
        
        
emir = otoKiralama()
emir.pencere.mainloop()