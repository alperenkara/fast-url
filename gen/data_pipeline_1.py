with open("techcrunch.csv") as file:
    total_raised=0
    cols=file.readline().rstrip().split(",")

    try:
        while True:
            single_line=file.readline().rstrip().split(",")
            company_dicts=dict(zip(cols,single_line))
            if company_dicts['round']=="a":total_raised=total_raised+int(company_dicts["raisedAmt"])
    except:
        print("Error")
    print(total_raised)