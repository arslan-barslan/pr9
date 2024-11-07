def main():
	counter=1
	spisok=[]
	while True:
		print("Введите", counter, "число списка")
		try:
			a=input()
			if a=="end":
				break
			a=int(a)
		except ValueError:
			print("Неверный ввод, попробуйте снова")
			continue
		spisok.append(a)
		counter+=1
	if counter>1:
		print("Вот все нечетные числа в списке")
		for i in range(0,len(spisok),2):
				print(spisok[i])
	else:
		print("список пуст")
main()
