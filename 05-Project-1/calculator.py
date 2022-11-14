moneysb4tip = float(input())
numguests = int(input())
if (numguests) >= 8:
    print ("A 20% tip is automatically added to parties of 8 or more.")
    TipOptions8 = "Your bill is {}"
    print(TipOptions8.format(round(moneysb4tip * 1.2, 2)))
else:
    print ("Your tip options are:")
    TipOptions = "15%: {} 20%: {} 25% {}"
    print(TipOptions.format(round(moneysb4tip * 1.15, 2), round(moneysb4tip * 1.20, 2), round(moneysb4tip * 1.25, 2)))