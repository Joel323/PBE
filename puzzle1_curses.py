import curses

class Rfid:
    def read_uid(self):
        stdsrc = curses.initscr()

        curses.noecho()
        
       
        uidString = stdsrc.getstr(0,0)
        uid = str(uidString.decode("utf-8"))
        uidByteArray = bytearray(uid,'utf-8').reverse()
        uidInt = int(uidByteArray)
        uidHex = hex(uidInt)
        curses.echo()
        curses.endwin()
        return uidHex.upper()
     
    

        

if __name__ == "__main__":
    rf = Rfid()
    uid = rf.read_uid()
    print(uid)
        

