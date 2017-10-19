#Mendapatkan waktu saat ini
#Untuk menerjemahkan waktu instan dari satu detik sejak nilai floating-point ke waktu menjadi tupel waktu, lewati nilai floating-point ke fungsi (mis., Localtime) yang mengembalikan waktu tupel dengan semua sembilan item valid.
import time;
localtime = time.localtime(time.time())
print "Waktu lokal saat ini :", localtime


#Mendapatkan waktu yang berformat
#Anda dapat memformat kapan saja sesuai kebutuhan Anda, namun metode sederhana untuk mendapatkan waktu dalam format yang mudah dibaca adalah asctime ()
import time;
localtime = time.asctime( time.localtime(time.time()) )
print "Waktu lokal saat ini :", localtime

#Mendapatkan kalender dalam sebulan
#Modul kalender memberikan berbagai macam metode untuk dimainkan dengan kalender tahunan dan bulanan. Di sini, kami mencetak kalender untuk bulan tertentu (Jan 2008)
import calendar
cal = calendar.month(2008, 1)
print "Dibawah ini adalah kalender:"
print cal
