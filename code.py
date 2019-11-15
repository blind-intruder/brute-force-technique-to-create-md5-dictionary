import hashlib
char=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","!","@","#","$","%","^","&","*","(",")",",",".","/",";",":"]
save = open("md5.txt", "a")
for a in char:
  for b in char:
    for c in char:
      for d in char:
        for e in char:
          for f in char:
            for g in char:
              for h in char:
                for i in char:
                  for j in char:
                    for k in char:
                      for l in char:
                        hash_obj = hashlib.md5((a+b+c+d+e+f+g+h+i+j+k+l).encode('utf-8'))
                        save.write(hash_obj.hexdigest()+"<<<<<>>>>>"+(a+b+c+d+e+f+g+h+i+j+k+l)+"\n")
save.close()
