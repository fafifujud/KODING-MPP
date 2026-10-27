class KarakterSurfer:
	def __init__(self,nama):
		self.nama = nama
		self.skor = 0
		self.koin = 0
		self.is_running = True

	def berlari(self):
		self.is_running = True
		print(f"-----{self.nama} Mulai berlari!-----")

	def ambil_koin(self,jumlah):
		self.koin += jumlah
		print(f"Jumlah Koin Saat Ini = {self.koin}")

	def tabrak_rintangan(self):
		self.is_running = False
		print(f"-> {self.nama} Menabrak Kereta!")

	def info_player(self):
		print("-----Info Player Saat Ini!-----")
		print(f"Nama		: {self.nama}")
		print(f"Jumlah Koin	: {self.koin}")
		print(f"Status Berlari	: {self.is_running}")

	def info_player_final(self):
		print("-----Game Over!-----")
		print("-> Info Akhir Player!")
		print(f"Nama		: {self.nama}")
		print(f"Jumlah Koin	: {self.koin}")
		print(f"Status Berlari	: {self.is_running}")

player1 = KarakterSurfer("Angel")

player1.info_player()

player1.berlari()
player1.ambil_koin(100)
player1.tabrak_rintangan()

player1.info_player_final()
