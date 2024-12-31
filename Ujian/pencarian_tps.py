class TPSLocator:
    def __init__(self):
        self.data = {
            "Bogor": "Jl. Raya Bogor KM.43, Bogor",
            "Jakarta": "Jl. Daan Mogot KM.14, Jakarta Barat",
            "Depok": "Jl. Raya Sawangan No.45, Depok",
            "Tangerang": "Jl. Imam Bonjol No.89, Tangerang",
            "Bekasi": "Jl. Narogong KM.13, Bekasi",
            "Bandung": "Jl. Babakan Siliwangi No.15, Bandung"
        }
    
    def cari_tps(self, kota):
        if kota in self.data:
            return self.data[kota]
        else:
            return "Alamat TPS tidak ditemukan untuk kota ini."