#inventory manager


import csv
try:
	with open("inventory.csv","r")as file:
		read = list(csv.reader(file))
		print("last added:",read[-1])
except FileNotFoundError:
	with open("inventory.csv","w",newline='')as file:
		write = csv.writer(file)
		write.writerow(["Name", "Category", "Quantity", "Price"])
while True:
	ask = input("1. Add New Item\n2. View All Items\n3. Search Item by Name or Category\n4. Update Quantity or Price\n5. Delete an Item\n6. Show Total Stock Value\n7. Exit\n enter: ")
	if ask =="1":
		a = input("enter in format(Name, Category, Quantity, Price)")
		with open("inventory.csv","a",newline='')as file:
			write = csv.writer(file)
			write.writerow(a.split(","))
	elif ask =="2":
		with open ("inventory.csv","r") as file:
			read = csv.reader(file)
			for row in read:
				print(row)
	elif ask =="3":
		a = input("enter name or category: ")
		with open("inventory.csv" , "r") as file:
			read = list(csv.reader(file))
			for row in read:
					if any(a.lower() in item.lower() for item in row):
						print(row)
	elif ask =="4":
		a = input("enter which product quentity & price you wanna edit in format: (Name, Category, Quantity, Price)")
		update = a.split(",")
		ntu = update[0].strip().lower()
		with open('inventory.csv','r') as file:
			read = list(csv.reader(file))
		with open("inventory.csv","w", newline ="") as file:
			write = csv.writer(file)
			for row in read:
				if row[0].strip().lower() == ntu:
					write.writerow(update)
				else:
					write.writerow(row)
	elif ask =="5":
		a = input("what do you wanna remove: ")
		with open("inventory.csv","r")as file:
			read = list(csv.reader(file))
		with open("inventory.csv","w",newline="")as file:
			write = csv.writer(file)
			for row in read:
				if a.lower() not in ",".join(row).lower():
					write.writerow(row)
	elif ask =='6':
		totalvalue = 0
		with open("inventory.csv","r") as file:
			read = csv.reader(file)
			next(read)
			for row in read:
				name = row[0]
				price = float(row[-1])
				quentity = int(row[-2])
				value = quentity * price
				totalvalue += value
				print(f"product: {name} , quentity: {quentity}, price: {price} , value: {value}")
			print("total value of all is {totalvalue}")
	elif ask =="7":
		print("thx")
		break
	else:
		print("enter from 1-7")