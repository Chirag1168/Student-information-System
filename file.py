def test():
    f=open("test.txt","w")
    while True:
        a=raw_input("enter sentence")
        f.write(a)
        f.write("\n")
        con=raw_input("want to continue(y/n)")
        if (con=="n"):
            break
    print"data saved in file"
