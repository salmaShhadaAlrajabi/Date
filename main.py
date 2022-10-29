class Date:
    def __init__(self,day,month,year):
        self.day = day
        self.month = month
        self.year = year


    DateCount =0
    def __init__(self):
        self.day = input("Enter day:")
        self.month = input("Enter month:")
        self.year = input("Enter year")
        Date.dateCount +=1




    def print__info(self):
        print("day:"+str(self.day))
        print("month:"+str(self.month))
        print("year:"+str(self.year))


    d1=Date()
    d1.print__info()


   class d2 (Date):
       def__init__(self,day,month,year,add_number_of_day):
       Date __init__ (self,day,month,year)
       self.add_number_of_day=add_number_of_day


       def __init__(self):
           self.add_number_of_day=input('Enter the number of day : ')


       def __print__ info(self)
       print('add number of day :' + str(self.add_number_of_day))


       def __add__(self,add_number_of_day)
           d2 = self.Date + self.add_number_of_day
           return d2