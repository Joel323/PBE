class Rfid:
	def read_uid(self):
		uid = int(input())
		return hex(uid)

if __name__ == "__main__":
	rf = Rfid()
	while(1):
		uid = rf.read_uid()
		print(uid)
