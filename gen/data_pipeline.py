#    Read every line of the file.
file_name = "techcrunch.csv"
#    Split each line into a list of values.
lines = (line for line in open(file_name))
list_line = (s.rstrip().split(",") for s in lines)
#    Extract the column names.
cols = next(list_line)
#    Use the column names and lists to create a dictionary.
company_dict = (dict(zip(cols,data)) for data in list_line)
#    Filter out the rounds you aren’t interested in.
funding = (

    int(company_dict["raisedAmt"])

    for company_dict in company_dict

    if company_dict["round"] == "a"

)
#    Calculate the total and average values for the rounds you are interested in.
total_series_a = sum(funding)

print(f"Total series A fundraising: ${total_series_a}")