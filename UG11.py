class RakObat:
    def __init__(self):
        self.size = 5
        self.map = [None] * self.size
        
    def _getHash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size
        
    def _probing(self, key):
        for index in range(self.size):
            probeHash = self._linearProbing(key, index)
            if (self.map[probeHash] is None) or (self.map[probeHash] == 'deleted'):
                return probeHash
        return None
        
    def _linearProbing(self, key, index):
        return (self._getHash(key)+index) % self.size

        
    def tambahObat(self, namaObat, jenisObat):
        key_hash = self._getHash(jenisObat)
        key_value = [jenisObat, namaObat]
        
        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            key_hash = self._probing(jenisObat)
            if key_hash is None:
                print("Rak Obat sudah penuh")
                return False
        self.map[key_hash] = list([key_value])
        return False
        
    def lihatObat(self, jenisObat):
        key_hash = self._getHash(jenisObat)
        if (self.map[key_hash] is not None) and (self.map[key_hash] != 'deleted'):
             for index in range(self.size):
                  key_hash = self._linearProbing(jenisObat, index)
                  if(self.map[key_hash][0][0] == jenisObat):
                      return self.map[key_hash][0][1]
        print("Key ",jenisObat, " tidak ditemukan")
        return "None"
            

    def ambilObat(self, jenisObat):
        key_hash = self._getHash(jenisObat)
        if self.map[key_hash] is None:
            return False
        for index in range(self.size):
            key_hash = self._linearProbing(jenisObat, index)
            if(self.map[key_hash][0][0] == jenisObat):
                print("obat ", jenisObat, "diambil dari rak")
                self.map[key_hash] = "deleted"
                return True
        
        print("Key ",jenisObat, " tidak ditemukan")
        return False
    
    def printAll(self):
        print('==========List Obat==========')
        for item in self.map:
            if item is not None and type(item) == list:
                print("Nama:", (item[0][1]), "<> Jenis: ", (item[0][0]))

if __name__ == "__main__":
    rak1 = RakObat()
    rak1.tambahObat('AstraZeneca (A01)', 'Covid')
    rak1.tambahObat('UltraFlu (A02)', 'Flu')
    rak1.tambahObat('Paramex (A03)', 'Sakit Kepala')
    rak1.tambahObat('Promag (A04)', 'Maag')
    rak1.tambahObat('Bodrex (A05)', 'Sakit Kepala')
    
    rak1.printAll()
    
    print(rak1.lihatObat("Sakit Kepala"))
    print(rak1.lihatObat("Migraine"))
    
    rak1.ambilObat("Flu")
    rak1.ambilObat("Malaria")
    rak1.printAll()
