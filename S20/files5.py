try:
    with open("practice.txt", "r") as f_in:
        content = f_in.readlines()
except OSError as err:
    print(err)

else:
    print(content)
    try: 
        with open("output.txt", "w") as o_in:
            o_in.writelines(content[:5])
    except OSError as err:
        print(err)