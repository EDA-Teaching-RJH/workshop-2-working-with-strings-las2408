def main():
    pounds = pounds_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to charge? "))
    charge = pounds * percent
    print(f"Charge £{charge:.2f}")


def pounds_to_float(pounds):
    x = (pounds.replace("£",""))
    d = float(x)
    return(d)

def percent_to_float(percent):
    y = (percent.replace("%",""))
    p = (float(y) / 100)
    return(p)

main()
