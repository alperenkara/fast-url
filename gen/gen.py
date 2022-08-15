
# 
# def csv_reader(file_name):
#     file = (file_open)
#     result = file.read().split("\n")
#     return result 
# 

row_count = 0

file_name = "techcrunch.csv"




def csv_reader(file_name):
    for row in open(file_name,"r"):
        yield row

# csv_gen = csv_reader(file_name)

csv_gen = (row for row in open(file_name))

for row in csv_gen:
    row_count +=1 
    

print(f"Row count is {row_count}")


