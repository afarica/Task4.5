# AK-47
# Soldier Ryan has an AK47
# Soldiers can fire ("tigi-tigitishh").
# Guns can fire bullets.
# Guns can fill bullets - increase the number of bullets(reloads)

# Create class Act_of_Shooting, which will inheritates from class Soldier, class Guns.
# Where soldier will fire from a gun and reload, and fire one more time.

class Guns:
	def __init__(self,name_of_guns='AK-47'):
		self.name_ofgGuns=name_of_guns

class Soldiers:
	def __init__(self,name_of_soldiers='Rayan'):
		self.name_of_goldiers=name_of_soldiers

class Act_of_Shooting(Guns,Soldiers):
	def __init__(self,name_of_guns,name_of_soldiers):
		self.name_of_guns=name_of_guns
		self.name_of_soldiers=name_of_soldiers

	def data(self):
		print("У солдата ",self.name_of_soldiers,"есть", self.name_of_guns)

	def fire(self):
		hey=input('Огооонь?:').lower()
		if hey == 'yes':
			print('тиги-тигидиш')


	def repload(self,fire):
		 reploads=input("Введи GO! чтобы перезарядить!:")
		 if reploads=='GO!':
		 	return self.fire

a=Act_of_Shooting('АК-47','Rayan')
a.data()
a.fire()
a.repload()