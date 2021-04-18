class method_tugas:
#init method
    def __init__(self, modul, kelompok):
        self.modul = modul
        self.kelompok = kelompok
#self parameter
    def penutup(self):
        print(f"Terimakasih sudah mengisi nilai praktiku {self.modul} untuk {self.kelompok}")
