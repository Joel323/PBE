class Rfid:
    def read_uid(self):       
        uidString = input()
        uid = int(uidString)
        uidHex = format(uid, 'x')
        uidUnformatted = str(uidHex)
        uidFormatted = self.format_string(uidUnformatted)
        uidFormatted.reverse()
        
        return ("".join(uidFormatted)).upper()
     
    
    def format_string(self, uidString):
        return [uidString[i:i+2] for i in range(0, len(uidString), 2)]
        

if __name__ == "__main__":
    rf = Rfid()
    uid = rf.read_uid()
    print(uid)
        

