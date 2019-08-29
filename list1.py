def test():
    f=open("hc","w")
    while True:
        sen=raw_input("enter sentence")
        f.write(sen)
        f.write("\n")
        con=raw_input("want to continue?(y/n)")
        if (con=="n"):
            break
    print"data saved in jha pe krna h"
    f.close()
                
        
