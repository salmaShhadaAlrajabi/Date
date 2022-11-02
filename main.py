
    import datetime 


    class Date: 
        
        def __init__(self, day, month, year):    # a (able to instantiate an instance using a constructor)
            self.day = day
            self.month = month
            self.year = year
            self.datetimeObject = datetime.datetime(self.year, self.month, self.day)
            

        def order(self):                        # b (method “order” that returns the order of a specific date in the year) 
            return self.datetimeObject.timetuple().tm_yday  


        def __str__(self):                      # c (print the date in the format dd/mm/yyyy )
            return (self.datetimeObject.date().strftime("%d/%m/%Y"))
        

        def __add__(self, num_days):            # d (use addition to find the date after a number of days )
            datetimeObject = self.datetimeObject + datetime.timedelta(days=num_days)
            return(datetimeObject.date().strftime("%d/%m/%Y"))
        

        def __sub__ (self, AnotherObject):      # e (use subtraction to find the difference (number of days) between two dates )
            AnotherObjectDatetime = datetime.datetime(AnotherObject.year, AnotherObject.month, AnotherObject.day)
            return abs((self.datetimeObject - AnotherObjectDatetime).days)
        

        def __lt__(self, AnotherObject):        # f (use comparison to find if a date precedes the other)
            print(AnotherObject)
            AnotherObjectDatetime = datetime.datetime(AnotherObject.year, AnotherObject.month, AnotherObject.day)
            
            if(self.datetimeObject < AnotherObjectDatetime):
                return True
            else:
                return False
            

    d1 = Date(23,12,2022)
    d3 = Date(15,2,2020)


    print(d3.order())


    print(d1 + 22)


    number_of_days = d3 - d1


    print(number_of_days)


    if d1 < d3:
        print("yes")
        
    input("press Enter to exit....")
