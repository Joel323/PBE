class Rfid:
    def read_uid(self):       
        uidString = input()
        uidBytes = bytearray(uidString,'utf-8')
        print(uidBytes)
        uidBytes.reverse()
        print(uidBytes)
        uid = int(uidString)
        uidHex = hex(uid)
        return uidHex.upper()
     
    

        

if __name__ == "__main__":
    rf = Rfid()
    uid = rf.read_uid()
    print(uid)
        

