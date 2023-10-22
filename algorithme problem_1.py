algorithme problem_1
variable
NP1,NP2,NP3:chain de caractere
n1,n2,n3,i,j,g:entier
s1,s2,s3,t1,t2,t3,a,b,c,tableau tab1(),tableau tab3():,tableau tab3()::reel
debut
ecrire("Donner le nom et prénom du client 1 :")
lire(NP1)
ecrire("Donner le nombre darticle pour le client 1 :")
lire(n1)
t1 <= 0
s1 <= 0
pour i <= 0 an n1 pas 1 faire:
ecrire("Donnez le prix de l'article ",i+1," :")
lire(a)
    tab1[i] <= a
finpour
pour i <= 0 an n1 pas 1 faire
    t1<=tab1[i]*(1+0.15-0.02)
    s1<=s1+t1
finpour
ecrire("Donner le nom et prénom du client 2 :")
lire(NP2)
ecrire("Donner le nombre darticle pour le client 2 :")
lire(n2)
t2 <= 0
s2 <= 0
pour j <= 0 an n2 pas 1 faire:
ecrire("Donnez le prix de l'article ",j+1," :")
lire(b)
    tab2[j] <= a
finpour
pour j <= 0 an n2 pas 1 faire
    t2<=tab2[j]*(1+0.15-0.02)
    s2<=s2+t2
finpour
ecrire("Donner le nom et prénom du client 3 :")
lire(NP3)
ecrire("Donner le nombre darticle pour le client 3 :")
lire(n3)
t3 <= 0
s3 <= 0
pour g <= 0 an n3 pas 1 faire:
ecrire("Donnez le prix de l'article ",g+1," :")
lire(c)
    tab2[g] <= c
finpour
pour g <= 0 an n3 pas 1 faire
    t3<=tab3[g]*(1+0.15-0.02)
    s3<=s3+t3
finpour
ecrire("Facture est : ")    
ecrire("Le Total à payer pour le client",NP1," est :",s1,"DH")
ecrire("Le Total à payer pour le client",NP2," est :",s2,"DH")
ecrire("Le Total à payer pour le client",NP3," est :",s3,"DH")
fin