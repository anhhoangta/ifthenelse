import random

listPlayer= [["Marc-André ter Stegen", "Jordi Masip", "Claudio Bravo"], ["Douglas", "Gerard Piqué", "Dani Alves",
             "Marc Bartra", "Jordi Alba", "Adriano", "Thomas Vermaelen", "Jérémy Mathieu"], ["Ivan Rakitić",
             "Sergio Busquets", "Andrés Iniesta", "Rafinha", "Javier Mascherano", "Sergi Roberto", "Alex Song",
             "Arda Turan", "Aleix Vidal"], ["Luis Suárez", "Neymar", "Lionel Messi", "Munir El Haddadi", "Sandro Ramírez"]]
	
GK = random.choice(listPlayer[0])
DF = random.sample(listPlayer[1], 4)
MF = random.sample(listPlayer[2], 4)
FW = random.sample(listPlayer[3], 2)

print("{0} - {1} - {2} - {3}" .format(GK, ', '.join(DF), ', '.join(MF), ', '.join(FW)))