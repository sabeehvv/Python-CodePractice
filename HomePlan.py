class Home:
    def __init__(self):
          pass 
    def room1(self):
        width=100 
        breadth = 100 
        print('are of room1',width*breadth)
    def officeRoom(self):
        width = 1234
        breadth = 4668 
        print('are of officeRoom',width*breadth) 
    def kitchen(self):
        width = 1222
        breadth = 4888 
        print('are of kitchen',width*breadth)
    def bathroom(self):
        width = 1222
        breadth = 4888 
        print('are of bathroom',width*breadth)
    def prayerRoom(self):
        width = 1242
        breadth = 4788 
        print('are of prayerRoom',width*breadth)


class FirstHome(Home):
    def __init__(self):
            pass
    def studyRoom(self):
        width = 1772
        breadth = 4238 
        print('are of studyRoom',width*breadth)

class SecondHome(Home):
    def __init__(self):
        pass
    def work_area(self):
        width = 1772
        breadth = 4238 
        print('are of work_area',width*breadth)

CommenHome = Home()
model1Home = FirstHome()
model2Home = SecondHome()

print("Commen model Home")
CommenHome.room1()
CommenHome.prayerRoom()
CommenHome.bathroom()
CommenHome.kitchen()
CommenHome.officeRoom()
print("HOme Model 1")
model1Home.room1()
model1Home.bathroom()
model1Home.kitchen()
model1Home.prayerRoom()
model1Home.officeRoom()
model1Home.studyRoom()

print("HOME Model 2")
model2Home.room1()
model1Home.prayerRoom()
model2Home.bathroom()
model2Home.kitchen()
model2Home.officeRoom()
model2Home.work_area()