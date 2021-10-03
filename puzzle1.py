class Rfid:
	def read_uid(self):
		uid = int(input())
		uidHex = hex(uid)
		return uidHex.upper()

if __name__ == "__main__":
	rf = Rfid()
	while(1):
		uid = rf.read_uid()
		print(uid)
