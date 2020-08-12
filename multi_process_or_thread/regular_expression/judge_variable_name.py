import re 

def main():
    names = ["age", "_age", "1age", "a_age", "age1", "age!", "age#1", "age_1_", "_______"]
    for name in names:
        ret = re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*$", name)
        if ret:
            print("%s is ok" %name)
        else:
            print("%s is not right" %name)

if __name__ == "__main__":
    main()
