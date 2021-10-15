from datetime import timedelta, datetime
#
#
# now = datetime.now()
# print(f"    Сейчас : {now}")
#
# d = dict()
#
#
# print("Сейчас.")
#
# amount_of_ads = int(input('Enter amount of ads: '))
#
# for i in range(1,amount_of_ads+1):
#     date_entry = input('Enter a first date (i.e. 2017,7,1): ')
#     day, month = map(int, date_entry.split(','))
#     d['num_%s' % i]= datetime(2021, month, day)
#
#
# a = d['num_1']
# b = d['num_2']
# c = d['num_3']
# d = d['num_4']


delta = timedelta(15)
deltaMinus = timedelta(-15)
delta7plus = timedelta(7)
deltaNull = timedelta(0)


a = datetime(2021, 10, 1)
b = datetime(2021, 10, 1)
c = datetime(2021, 10, 1)
d = datetime(2021, 10, 1)
today = datetime(2021, 10, 18)
diff_date = b - a

dateOneAct, dateTwoAct = a + delta + delta, b + delta + delta

amount_of_ads = 4

dif_delta = 30 / amount_of_ads


# first sitation a = 1, b = 17, now = 18
if diff_date > delta:
    dateOneAct = b + delta

# second sitation a = 17, b = 1, now = 18
if diff_date < deltaMinus:
    dateTwoAct = a + delta

# third sitation a = 1, b = 10, now = 18
if deltaNull < diff_date < delta:
    dateOneAct = b + delta * 2
    dateTwoAct = b + delta

# four sitation a = 10, b = 1, now = 18
if deltaMinus < diff_date < deltaNull:
    dateOneAct = a + delta
    dateTwoAct = a + delta * 2

dateThirdAct = dateOneAct + delta7plus
dateForthAct = dateTwoAct + delta7plus

branch = 'ФИЛИАЛ'
#
print(f"{branch}  {'дата акт'}                   {'дата след.акт.'}")
print(f"{'      '}{a}    {dateOneAct}   {''}")
print(f"{'      '}{b}    {dateTwoAct}   {'  '}")
print(f"{'      '}{c}    {dateThirdAct}   {''}")
print(f"{'      '}{d}    {dateForthAct}   {'  '}")

# if __name__ == '__main__':
#     main()











# import time
#
# now = time.strftime("%d %b %Y")
#
# def times(date):
#
#     return print(f'   Today:{date}')
#
#
# def main():
#     while True:
#
#         times(now)
#         print("INPUT DATE OF BEGIING YOUR VACATION: ")
#
#         dat_vac = int(input("FORMAT OF INPUTING DD,MM, YY:  "))
#         dat_vac = int(input("FORMAT OF INPUTING DD,MM, YY:  "))
#
#         if InputCommands == 'e':
#             print('Программа завершена')
#             break
#
#         elif InputCommands == 'r':
#             pass
#
#         elif InputCommands == 'w':
#             print("Запись в файл сделано")
#
#         else:
#             print("Ошибка!!! Это неверная команда. Попробуйте еще")
#
#
# if __name__ == '__main__':
#     main()
#     #inputCommand()
#
#
#
#
#
#     # def __str__(self):
#     #     return (
#     #         f'Date: {self.created}\n'
#     #         f'Category: {self.category}\n'
#     #         f'Text: {self.text}\n\n'
#     #     )
#
#
#
#

#
#
#
#
#
