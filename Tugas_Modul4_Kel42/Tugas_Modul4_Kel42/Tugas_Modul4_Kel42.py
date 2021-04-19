import method_Tugas_Modul4_Kel42

print("Sebutkan Nama dan NIM kelompok 42 praktikum DKP 2021!!!")

def identitas(i, nama, nim):
    print("Praktikan : "+i)
    print("Nama : "+nama)
    print("NIM  : "+nim)

def nilai():
    print("\n")
    print("Pilihan Nilai : ")
    print("[1] A")
    print("[2] B")
    print("[3] C")
    print("[4] D")
    print("[5] E")

    for a in range(1,5):
        print("Pilih nilai yang diinginkan Praktikan",a," : ")
        nilai = int(input())
        if nilai == 1:
            print("Nilai Praktikan",a,": A")
        elif nilai == 2:
            print("Nilai Praktikan",a,": B")
        elif nilai == 3:
            print("Nilai Praktikan",a,": C")
        elif nilai == 4:
            print("Nilai Praktikan",a,": D")
        elif nilai == 5:
            print("Nilai Praktikan",a,": E")
        else:
            print("Pilihan nilai hanya 1-5!!")
     
        if nilai < 4:
            print("Praktikan",a,"lulus matkul praktikum DKP")
        else:
            print("Praktikan",a,"harus mengulang")
        print("\n")

    
identitas("1", "Kanzu Khairon Adli", "21120118130063")
identitas("2", "Kanina Nadia Andriyani", "21120120130053")
identitas("3", "Novita Auliya", "2112012040114")
identitas("4", "Ahmad Aldani Herlangga", "21120120140168")
nilai()

pl = method_Tugas_Modul4_Kel42.method_tugas("Modul 4", "Kelompok 42")

pl.penutup()
