def main():

	try:
		a = int(input("Введите число a: "))
		b = int(input("Введите число b: "))
	except ValueError:
		print("Неверный ввод, попробуте снова")
		return main()

	spisok = []
	for i in range(a, b + 1):
		spisok.append(i ** 2)
	print("Квадраты целых чисел от",a," до",b)
	print(spisok)
	return 0
main()
