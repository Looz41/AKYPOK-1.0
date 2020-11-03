# Доработанная версия

import re
import os
import datetime
import pickle
from colorama import init
from colorama import Fore, Back, Style

init()

class AKYPOK:
	def __init__(self, name, number):
		self.name = name
		self.number = number
	def ShowNumber():
		print(Back.GREEN)
		print(Fore.BLACK)

		with open('AdressBook.txt', 'r') as f:
			text = f.read()
			print(text)

		Begining()
	def Search(self):
		print(Back.GREEN)
		print(Fore.BLACK)
	def AddNumber(self):
		print(Back.WHITE)
		print(Fore.BLACK)

		try:
			inp = int(self.number)

			print('Вы ввели {0} : {1}. Продолжить? '.format(self.name, self.number))
			work13 = input().lower()
			if work13 == 'да':
				f = open('AdressBook.txt', 'a')
				f.write('Имя: {0} : {1}\n'.format(self.name, self.number))
				f.close()

				print(Back.GREEN)
				print(Fore.BLACK)
				print('Успешно!')
				Work32()
			else:
				Begining()
		except:
			print('Введите НОМЕР!!!')
			Work32()

	def DelNumber():
		print(Back.WHITE)
		print(Fore.BLACK)
		
		NumBer = input('Введите номер: ')

		print('Вы ввели {0}. Продолжить?'.format(NumBer))
		work12 = input().lower()
		if work12 == 'да':
			with open('AdressBook.txt') as f:
				lines = f.readlines()

			str = NumBer

			if NumBer == '89182072558':
				print(Back.RED)
				print(Fore.BLACK)

				print('Не не не!')
				Work32()
			else:
				pattern = re.compile(re.escape(str))
				with open('AdressBook.txt', 'w') as f:
					for line in lines:
						delimister = line
						result = pattern.search(line)
						if result is None:
							f.write(line)
				print(Back.GREEN)
				print(Fore.BLACK)
				print('Успешно!')
				Work32()
		else:
			Begining()
	
	def Change():
		word = input('Введите номер: ')
		print('Вы ввели {0}.'.format(word))
		
		with open('AdressBook.txt') as f:
			for line in f:
				if word in line:
					print('Вы хотите изменить {0} ?'.format(line.splitlines()))
					work4343 = input('Продолжить? ').lower()
					if work4343 == 'да':

						with open('AdressBook.txt') as f:
							lines = f.readlines()
						
							old_data = line

							new_Name = input('Введите новое имя: ')
							new_Num = input('Введите новый номер: ')
							new_line = new_Name + " : " + new_Num
								

							str = word

							print(new_line)

							new_data = old_data.replace(line, new_line)

							pattern = re.compile(re.escape(str))

						with open('AdressBook.txt', 'w') as f:
							for line in lines:
								delimister = line
								result = pattern.search(line)
								if result is None:
									f.write(line)

						f = open('AdressBook.txt', 'a')
						f.write('Имя: {0} : {1}\n'.format(new_Name, new_Num))
						f.close()
						Work32()
					else:
						Begining()

def Begining():
	print(Back.WHITE)
	print(Fore.BLACK)
	print("Выберите дейтсвие: Просмотреть 'АКУРОК' - 0	Выход - 1	Добавить контакт - 2	Удалить контакт - 3  Изменить контакт - 4")
	work = input()
	if work == "1":
		print('Пока!')
		input()
	elif work == "0":
		AKYPOK.ShowNumber()
	elif work == "2":
		a = input('Введите имя: ')
		b = input('Введите номер: ')
		adress = AKYPOK(a, b)
		adress.AddNumber()
	elif work == "3":
		AKYPOK.DelNumber()
	elif work == '4':
		AKYPOK.Change()
	else:
		print(Back.RED)
		print(Fore.BLACK)
		print('Ошибка')

def Work32():
		print(Back.WHITE)
		print(Fore.BLACK)
		work32 = input('Вернуться в меню?  ').lower()
		if work32 == 'да':
			Begining()
		else:
			print('Пока!')
			input()

def Enter():
	print(Back.WHITE)
	print(Fore.BLACK)
	print("Добро пожаловать в 'АКУРОК'(Адресная Книга Учебная Разработанная Очередным Клешнеруким)")
	password = input("Введите пароль: ")
	if password != "0000":
			print(Back.RED)
			print(Fore.BLACK)
			print('Доступ запрещен!')
	else:
		print('\nУспех!')
		Begining()

f = open('AdressBook.txt', 'a')
f.close()
Enter()
