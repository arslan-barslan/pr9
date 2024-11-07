def main():
	counter=1
	chtn=0
	nechtn=0
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
		print("Вот количество нечетных и четных чисел в списке")
		for i in range(len(spisok)):
			if i%2==0:
				chtn+=1
			else:
				nechtn+=1
		print("Четных:", chtn)
		print("НЕ Четных:", nechtn)
	else:
		print("список пуст")
main()
