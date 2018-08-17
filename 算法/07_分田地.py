def ftd(wight,height):
    if wight%height==0:
        return height
    else:
        return ftd(height,(wight-(wight//height)*height))
print(ftd(73,30))