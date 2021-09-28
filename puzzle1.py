class Rfid:
	def read_uid(self):
		uid = int(input())
		return hex(uid)

if __name__ == "__main__":
	rf = Rfid()
	uid = rf.read_uid()
	print(uid)
