ph=int(input("svp entrer le nobre de photocopie:"))
if ph==10 or ph<10:
    prix=ph*0.30
elif ph==30 or ph<30:
    prix=10*0.30+(ph-30)*0.20+20*0.25
else:
    prix=10*0.30+20*0.25+(ph-30)+20*0.20
print("le prix total:",prix)
