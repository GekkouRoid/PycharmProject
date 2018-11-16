# Exercise 8-14

def make_car(vendor, model, **paras):
    """simulate to make a car with vendor and model info,
    in addition to any other information introduced."""
    car = {}
    car['vendor'] = vendor
    car['model'] = model
    for key, value in paras.items():
        car[key] = value
    return car


car1 = make_car('Honda', 'access', color='Silver', size='Medium')
print(car1)
car2 = make_car('Subaru', 'outback', color='Blue', tow_package=True)
print(car2)
