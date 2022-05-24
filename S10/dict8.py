# Remove all the items from months dict with value greater then 6

months = {
'January': 1,
'February': 2,
'April': 4,
'May': 5,
'March': 3,
'October': 10,
'July': 7,
'August': 8,
'June': 6,
'September': 9,
'November': 11,
'December': 12
}

# for k in list(months.keys()):
#     if months[k] > 6:
#         del months[k]
# print(months)

def trim_by_six(n):
    for k in list(n.keys()):
        if n[k] > 6:
            del n[k]
    print(n)

trim_by_six(months)

