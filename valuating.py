def run():
    print("""This app will help you to valuate a company according to Buffetology book. 
    This is only a reference, but we advise you to investigate by yourself before taking any decision.

    Please, follow the steps to valuate a company.""")

    stock = input("Write the stock ticker or number: ")
    last_eps = float(input("Write the last annual EPS: "))
    share_price = float(input("Write today's share price: "))
    rate_return = last_eps / share_price * 100
    print("The rate of return for this share is " + str(round(rate_return, 2)) + "%")



if __name__ == "__main__":
    run()