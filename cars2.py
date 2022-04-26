def make_car(brand,model,**kwarg):
    """Describe a car"""
    kwarg['brand'] = brand
    kwarg['model'] = model
    return kwarg

car = make_car('subaru','outback',color = 'blue',tow_package=True)
print(car)