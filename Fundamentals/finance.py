# we are creating a series of functions called the finance module

def addTax(price, tax):
    ''' create addtax function'''
    newPrice = price / 100 * (100 + tax)
    return newPrice

def addVat(price,vat):
    ''' create newprice function'''
    newPrice = vat/100 + price
    return newPrice
