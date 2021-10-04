import readchar


class Rfid:
    def read_uid(self):       
        uidFromCharacters = self.read_char() 
        uidJoined = self.join_char(uidFromCharacters)
        uid = int(uidJoined)
        uidHex = format(uid, 'x')
        uidUnformatted = str(uidHex)
        uidFormatted = self.format_string(uidUnformatted)
        uidFormatted.reverse() 
        print(uidFormatted)
        
        return ("".join(uidFormatted)).upper()
     
    
    def format_string(self, uidString):
        return [uidString[i:i+2] for i in range(0, len(uidString), 2)]
    
    def read_char(self):
        char_list = []
        p = ''
        for i in range(0,10):
            p = readchar.readchar()
            char_list.append(p)
        return char_list

    def join_char(self, charList):
        uidFromCharacters = ""
        return(uidFromCharacters.join(charList))

        

if __name__ == "__main__":
    rf = Rfid()
    uid = rf.read_uid()
    print(uid, end = '')
