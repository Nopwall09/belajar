def input_biodata():
    print("\n================Selamat Datang================")  
    print("\n==============Silahkan Registrasi==============")
    registrasi()
  
def registrasi():
    email1 = input("Masukkan email anda            : ")
    nama = input("Masukkan nama anda             : ")
    umur = int(input("Masukkan Umur Anda             : "))
    if umur <=18 :
        print("Umur Anda Belum Cukup")
        input_biodata()
    elif umur >=18:
        biodata2(nama,umur,email1)

def biodata2(nama,umur,email1):
    ttl = input("Masukkan Tanggal Lahir dd/mm/yy: ")
    ktp = int(input("Masukkan Nomer KTP(16 Digit)   : "))
    print("="*20, "Masukkan Alamat Anda", "="*20)
    alamat = desa = input("Desa     : "); kec = input("Kecamatan: "); kab = input("Kabupaten: ")
    pin(pin,nama,umur,ttl,ktp,desa,kec,kab,email1)

def pin(pin,nama,umur,ttl,ktp,desa,kec,kab,email1):
    while True:
        print("====================Buat Pin Anda====================")
        pin = int(input('Buat Pin Anda "4 digit": '))
        konfirm = int(input("Konfirmasi Pin Anda    : "))
        if konfirm == pin:
            cek_pin = input("Apakah Pin Anda Sudah Benar?sudah/belum: ")
            if cek_pin == "sudah":
                login(pin,nama,umur,ttl,ktp,desa,kec,kab,email1)
                break               
            elif cek_pin == "belum":
                continue
            else:
                print("Input Tidak Dikenali")
                input_biodata()
        else:
            print("\n======>Pin Anda Salah")
            pin(pin,nama,umur,ttl,ktp,desa,kec,kab,email1)

def login(pin,nama,umur,ttl,ktp,desa,kec,kab,email1):
    print("\n================Silahkan Login================")
    email = input("Masukkan email anda: ")
    if email == email1:
        sandi_pin(pin,nama,umur,ttl,ktp,desa,kec,kab,email1)
    else:
        print("Maaf Email Anda Salah")
        login(pin,nama,umur,ttl,ktp,desa,kec,kab,email1)

def sandi_pin(pin,nama,umur,ttl,ktp,desa,kec,kab,email1):
    sandi_pin = int(input("Masukkan pin anda  : "))
    if sandi_pin == pin:
        rumus_rekening = 2024 + umur + pin + (ktp//1000)
        konfirmasi_semua = input("Apakah Data Anda Sudah Benar?sudah/belum: ")
        if konfirmasi_semua == "sudah":
            print_biodata(nama,umur,ttl,ktp,pin, desa, kec, kab,rumus_rekening,email1)
        elif konfirmasi_semua == "belum":
            input_biodata()
        else:
            print("Input Tidak Dikenal")
            login(pin,nama,umur,ttl,ktp,desa,kec,kab,email1)
    else:
        print("Pin Anda Salah")
        login(pin,nama,umur,ttl,ktp,desa,kec,kab,email1)
        

def print_biodata(nama,umur,ttl,ktp,pin, desa, kec, kab,rumus_rekening,email1):
    print("\n============= Data Registrasi Anda =============")
    print(f"Email Anda          :{email1}")
    print(f"Nama Anda           :{nama}")
    print(f"Umur Anda           :{umur}")
    print(f"TTL                 :{ttl}")
    print(f"NIK                 :{ktp}")
    print(f"Alamat              :Desa {desa}, Kecamatan {kec},Kabupaten {kab}")
    print(f"Nomer Rekening Anda :{rumus_rekening}")
    print(f"Pin Anda            :{pin}")
    
input_biodata()