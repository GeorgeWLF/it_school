# context manager


try:
    with open("google_logo.png", "rb") as f_in:
        content = f_in.read()
except OSError as err:
    print(err)

else:
    print(content)
    # for i in content:
    #     print(f"{i:08b}", end="")

print("END")