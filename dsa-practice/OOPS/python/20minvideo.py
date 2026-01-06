# https://www.youtube.com/watch?v=rLyYb7BFgQI

#Classes are blueprint for creating objects

class Microwave:    #use PascalCase 
    #... #placeholder called Ellipsis simillar to pass

    def __init__(self, brand : str , power: str ) -> None:
        self.brand = brand 
        self.power = power       
        self.statuscheck_on:bool = True

    def run(self,seconds:int) -> None :
        if self.status_on :
            print(f'running {self.brand} for {seconds} ')
        else :
            print(f'Turn on your microwave first')

    
    # def get_brand(self) -> str:
    #     # -> str means this function returns a string
    #     return self.brand 

    def status_on(self)-> None :
        if self.statuscheck_on :
            print(f'Microwave ({self.brand}) is running alredy')
        else :
            self.statuscheck_on = True
            print(f'Micorwave ({self.brand}) is now turned on')

    def status_off(self)-> None :
        if self.statuscheck_on :
            self.statuscheck_on = False
            print(f'Micorwave ({self.brand}) is now turned on')

        else :
            print(f'Microwave ({self.brand}) is running alredy')

        
        #Dunder method because can run >>> print(philphs + samsung)

    def __add__(self,other):
        return f'{self.brand} + {other.brand}'
    
    def __str__(self) -> str:
        return f'{self.brand} Rating = {self.power}'




philips: Microwave= Microwave("philiphs","A++")
samsung: Microwave = Microwave(brand = "samsung",power = "A+")
# print(samsung)
# print(samsung.brand)
# print(samsung.power)

# samsung.status_on()
# samsung.status_off()
# samsung.run(10)

print(samsung)
