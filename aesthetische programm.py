# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 21:07:07 2019

@author: Agando
"""
#w=1
#if w==1:
#    z=t=x=y=k='{}'
#else:
#    z='z: Z ist ein Zeichen'
#    t='t: t ist eine Abbildung t:Z->Z'
#    x='x:...?'
#    y='y:...?'
#    k='k:...?'
#
#Z={z}
#T={t}
#a={x}
#b={y}
#K={k}

#print('Das "ästhetische" Programm ist das Quintupel P:=(Zeichenrepertoire Z =',Z,', Menge der Tranformationen T =',T,', Ablauf-Funktion a =',a,', Bewertungs-Funktion b =',b,', Zielmenge der Bewertungen K =',K,')')

def prod(A,B):
        result= set()
        for a in A:
            for b in B:
                result.add((a,b))
        return result
    
def prodn(A,B,n):
        result= prod(A,B)
        while n>=0:
            result=prod(result,prod(A,B))
            n=n-1
        return result

def P_1(p,n):
    if 0.00000001<=p:
        z_1=0
        z_2=1
        Z={z_1,z_2}
        T=prod({z_1},{z_2})
        a=prod(prod({1,2,3,4,5,6,7,8,9,10},prodn(Z,T,n)),prod(Z,T))
        b=prod(prodn(Z,T,n),{x for x in range(1,10)})
        K= b-{(((((((((((('{}', ('{}', '{}')), ('{}', ('{}', '{}'))), ('{}', ('{}', '{}'))), ('{}', ('{}', '{}'))), ('{}', ('{}', '{}'))), ('{}', ('{}', '{}'))), ('{}', ('{}', '{}'))), ('{}', ('{}', '{}'))), ('{}', ('{}', '{}'))), ('{}', ('{}', '{}'))), ('{}', ('{}', '{}'))), 3)}
        print('************************************ \n EIN ÄSTHETISCHES PROGRAMM VON POPO \n************************************\n\n\n Das "ästhetische" Programm ist das Quintupel P:=(Zeichenrepertoire Z =',Z,', Menge der Tranformationen T =',T,', Ablauf-Funktion a =',a,', Bewertungs-Funktion b =',b,', Zielmenge der Bewertungen K =',K,')')
        print('\n Im folgenden führen wir das ästhetische Programm aus, das heißt wir bilden ein "ästhetisches Objekt" \n\n ===================================================')
        print('ZEICHEN:\n\n', Z,'\n\n=\n\n'
              ,list(Z),'\n\n')
        print('TRANSFORMATIONEN: \n\n', T,'\n\n=\n\n',list(T),'\n\n')
        print('ABLAUF:\n\n', a,'\n\n=\n\n',list(a),'\n\n')
        print('BEWERTUNG:\n\n', b,'\n\n=\n\n',list(b),'\n\n')
        print('GESUCHT:\n\n', K,'\n\n=\n\n',list(K),'\n\n')
    else:
        z='z: Z ist ein Zeichen'
        t='t: t ist eine Abbildung t:Z->Z'
        x='x:...?'
        y='y:...?'
        k='k:...?'
        Z={z}
        T={t}
        a={x}
        b={y}
        K={k}
        print('************************************ \n EIN ÄSTHETISCHES PROGRAMM VON POPO \n************************************\n\n\n Das "ästhetische" Programm ist das Quintupel P:=(Zeichenrepertoire Z =',Z,', Menge der Tranformationen T =',T,', Ablauf-Funktion a =',a,', Bewertungs-Funktion b =',b,', Zielmenge der Bewertungen K =',K,')')
        print('\n Im folgenden führen wir das ästhetische Programm aus, das heißt wir bilden ein "ästhetisches Objekt" \n\n ===================================================')
        z='{}'
        Z={z}
        T=prod({z},{z})
        a=prod(prod({1,2,3,4,5,6,7,8,9,10},prodn(Z,T,n)),prod(Z,T))
        b=prod(prodn(Z,T,n),{x for x in range(1,10)})
        K= b-{(((((((((((('{}', ('{}', '{}')), ('{}', ('{}', '{}'))), ('{}', ('{}', '{}'))), ('{}', ('{}', '{}'))), ('{}', ('{}', '{}'))), ('{}', ('{}', '{}'))), ('{}', ('{}', '{}'))), ('{}', ('{}', '{}'))), ('{}', ('{}', '{}'))), ('{}', ('{}', '{}'))), ('{}', ('{}', '{}'))), 3)}
        print('ZEICHEN:\n\n', Z,'\n\n')
        print('TRANSFORMATIONEN: \n\n', T,'\n\n')
        print('ABLAUF:\n\n', a,'\n\n')
        print('BEWERTUNG:\n\n', b,'\n\n')
        print('GESUCHT:\n\n', K,'\n\n')
        
        
        
###############################################################################
############################################################################### 

###############################################################################    

###############################################################################
###############################################################################    


import matplotlib.pyplot as plt

# ZEICHENREPERTOIRE 'Z'
# Funktion für das Generieren der Menge der Zeichen ("Zeichenrepertoire").

def Z(n):
    Z=set()
    while n>=0:
        Z.add(n)
        n=n-1         
    return frozenset(Z)

# TRANSFORMATIONEN 'T'
# Funktion für das Generieren der Menge T der Transformationen t
    
def T(n):
    T=prod(Z(n),Z(n))
    return frozenset(T)

# ABLAUFFUNKTION 'a'   
# Funktion für das Generieren der Menge der A    
def a(z,t,n,k):
    a=set()
    N=set()
    K=prod(Z(z),T(t))
    while n>=0:
        N.add(n)
        n=n-1
    while k>=0:
        K=prod(K,K)
        k=k-1
    a.add(frozenset(prod(prod(N,K),K)))
#    a.add(frozenset(frozenset(prod(N,K)),frozenset(prod(Z(z),T(t)))))
    return frozenset(a)

# BEWERTUNGSFUNKTION b
    
def b(z,t,k,m):
    b=set()
    K=prod(Z(z),T(t))
    R=set()
    while k>=0:
        K=prod(K,K)
        k=k-1
    while m>=0:
        R.add(m)
        m=m-1
    b.add(frozenset(prod(K,R)))
    return frozenset(b)

# ZIELMENGE K
def K(l,m):
    K=set()
    R=set()
    
    while l>=0:
        K.add(l)
        l=l-1
        
    while m>=0:
        R.add(m)
        m=m-1
    if K.issubset(R)==True:
        return K
    else:
        return False
    
def P_ART(z,t,n,k,m,l): 
    ART=tuple() 
    ART=ART+(Z(z),T(t),a(z,t,n,k),b(z,t,k,m), K(l,m))
    return tuple(ART)


def plot():
    PLOT=[[1,2],[3,2]]
    return plt.matshow(PLOT) 

A={0,1,2,3,4,5,6,7,8,9}
B={0,1,2,3,4,5,6,7,8,9}



def f(A,B,V):
    AA=set()
    while A>=0:
        AA.add(A)
        A=A-1
    BB=set()
    while B>=0:
        BB.add(A)
        B=A-1
    VV=set()
    
    return frozenset(AA),frozenset(B),frozenset(V)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    