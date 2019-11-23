import csv
import matplotlib.pyplot as plt

#
#


categories = []

with open("menhockey.py") as csvfile:
	reader = csv.reader(csvfile)

	line_count = 0

	for row in reader:
		if line_count is 0:
			#
			categories.append(row)
			line_count += 1
		else:
			if row[7] == "Gold":
				print("won gold!")
				golds.append(row[7])

			elif row[7] == "Silver":
				print("won silver!")
				silvers.append(row[7])

			if row[7] == "Bronze":
				print("won bronze. Is that even winning?")
				bronzes.append(row[7])

			line_count += 1
print("gold medals: ", len(golds))
print("silver medals ", len(silvers))
print("bronze medalds ", len(bronzes))