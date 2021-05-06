sen = 'these are words i wrote'
count = 1
for s in sen.split(" "):
    if count % 3 != 0:
        print(s + " ")
    count+=1