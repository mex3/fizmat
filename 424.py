#http://informatics.mccme.ru/moodle/mod/statements/view.php?chapterid=424#1

#вы можете писать комментарии, что именно вы реализовали
MonthNames = ('', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
DayOfTheWeek = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
MonthNums = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}
DayNums = {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5, 'Saturday': 6, 'Sunday': 7}


fin = open("input.txt", "r")
fout = open("output.txt", "w")

a,b,c = map(int,input().split())
k = []
l = 1
for i in range(1,13):
    c = []
    if i in [1,3,5,7,8,10,12]:
        day = 32
        for i in range(1,32):
            c.append('0')
    k.append(c)
print(k)

fin.close()
fout.close()
