import curses

class Rfid:
    def read_uid(self):
        stdsrc = curses.initscr()
        curses.noecho()
        uidString = stdsrc.getstr(0,0)
        uid = int(uidString)
        uidHex = hex(uid)
        curses.echo()
        curses.endwin()
        return uidHex.upper()
         
        

if __name__ == "__main__":
    rf = Rfid()
    uid = rf.read_uid()
    print(uid)

        

