def ttt():
    print('this is a game of tic tac toe for multi players...... ENJOY!!!!')
    p1=' '
    p2=' '
    p3=' '
    p4=' '
    p5=' '
    p6=' '
    p7=' '
    p8=' '
    p9=' '
    b=' '
    print("""these are the positions to be entered
                 |    |
              1  |  2 |  3
            _____|____|____
                 |    |
               4 |  5 |  6
            _____|____|____
                 |    |
               7 |  8 |  9
                 |    |     """)
    c=input('player 1,enter what you want to be(X/O)')
    while c not in'xXoO':
        try:
            print('enter X or O only')
            c=input('player 1,enter what you want to be(X/O)')
        except ValueError:
            print('since you didnt enter anything')
            c='X'
    if c.upper()=='X':
        b='O'
    elif c.upper()=='O':
        b='X'
    else:
        print('since you didnt enter anything')
        c='X'
        b='O'
    a=c.upper()
    print('so player 1,you are ',a)
    print('and player 2,you are ',b)
    print('player 1,enter your',a,'in')
    m1=int(input(' '))
    valid_choice=False
    while valid_choice:
        try:
            print('you entered a position which is not between 1 and 9 or any other character')
            print('player 1,enter your',a,'in')
            m1=int(input(' '))
        except:
            pass
    if m1==1:
        p1=a
    elif m1==2:
        p2=a
    elif m1==3:
        p3=a
    elif m1==4:
        p4=a
    elif m1==5:
        p5=a
    elif m1==6:
        p6=a
    elif m1==7:
        p7=a
    elif m1==8:
        p8=a
    elif m1==9:
        p9=a
    else:
        print('you didnt enter anything')
    print()
    print(' ',p1,' | ',p2,' | ',p3)
    print('_________________________')
    print(' ',p4,' | ',p5,' | ',p6)
    print('_________________________')
    print(' ',p7,' | ',p8,' | ',p9)
    print() 
    print('player 2,enter your',b,'in')
    m2=int(input(' '))
    while (m1==m2)or(m2>9):
        try:
            print('you entered a position which already exist or not between 1 and 9')
            print('player 2,enter your',b,'in')
            m2=int(input(' '))
        except:
            pass
    if m2==1:
        p1=b
    elif m2==2:
        p2=b
    elif m2==3:
        p3=b
    elif m2==4:
        p4=b
    elif m2==5:
        p5=b
    elif m2==6:
        p6=b
    elif m2==7:
        p7=b
    elif m2==8:
        p8=b
    elif m2==9:
        p9=b
    print()
    print(' ',p1,' | ',p2,' | ',p3)
    print('_________________________')
    print(' ',p4,' | ',p5,' | ',p6)
    print('_________________________')
    print(' ',p7,' | ',p8,' | ',p9)
    print()
    print('player 1,enter your',a,'in')
    m3=int(input(' '))
    while (m3==m1)or(m3==m2)or(m3>9):
        try:
            print('you entered a position which already exist or the position is not between 1 and 9')
            print('player 1,enter your',a,'in')
            m3=int(input(' '))
        except:
            pass
    if m3==1:
        p1=a
    elif m3==2:
        p2=a
    elif m3==3:
        p3=a
    elif m3==4:
        p4=a
    elif m3==5:
        p5=a
    elif m3==6:
        p6=a
    elif m3==7:
        p7=a
    elif m3==8:
        p8=a
    elif m3==9:
        p9=a
    print()
    print(' ',p1,' | ',p2,' | ',p3)
    print('_________________________')
    print(' ',p4,' | ',p5,' | ',p6)
    print('_________________________')
    print(' ',p7,' | ',p8,' | ',p9)
    print() 
    print('player 2,enter your',b,'in')
    m4=int(input(' '))
    while (m4==m3)or(m4==m2)or(m4==m1)or(m4>9):
        try:
            print('you entered a position which already exist or the position is not between 1 and 9')
            print('player 2,enter your',b,'in')
            m4=int(input(' '))
        except:
            pass
    if m4==1:
        p1=b
    elif m4==2:
        p2=b
    elif m4==3:
        p3=b
    elif m4==4:
        p4=b
    elif m4==5:
        p5=b
    elif m4==6:
        p6=b
    elif m4==7:
        p7=b
    elif m4==8:
        p8=b
    elif m4==9:
        p9=b
    print()
    print(' ',p1,' | ',p2,' | ',p3)
    print('_________________________')
    print(' ',p4,' | ',p5,' | ',p6)
    print('_________________________')
    print(' ',p7,' | ',p8,' | ',p9)
    print()
    print('player 1,enter your',a,'in')
    m5=int(input(' '))
    while (m5==m4)or(m5==m3)or(m5==m2)or(m5==m1)or(m5>9):
        try:
            print('you entered a position which already exist or the position is not between 1 and 9')
            print('player 1,enter your',a,'in')
            m5=int(input(' '))
        except:
            pass
    if m5==1:
        p1=a
    elif m5==2:
        p2=a
    elif m5==3:
        p3=a
    elif m5==4:
        p4=a
    elif m5==5:
        p5=a
    elif m5==6:
        p6=a
    elif m5==7:
        p7=a
    elif m5==8:
        p8=a
    elif m5==9:
        p9=a
    print()
    print(' ',p1,' | ',p2,' | ',p3)
    print('_________________________')
    print(' ',p4,' | ',p5,' | ',p6)
    print('_________________________')
    print(' ',p7,' | ',p8,' | ',p9)
    print()
    if((p1==a)and(p1==p2)and(p2==p3))or((p1==a)and(p1==p4)and(p4==p7))or((p1==a)and(p1==p5)and(p5==p9))or((p4==a)and(p4==p5)and(p5==p6))or((p7==p5)and(p5==a)and(p5==p3))or((p7==a)and(p7==p8)and(p8==p9))or((p2==a)and(p2==p5)and(p5==p8))or((p3==a)and(p3==p6)and(p6==p9)):
        print('player 1 wins!!! *claps*')
        rate=input("Rate this program with '*' please :* XD =")
        while rate not in'****************************************************************************************************':
            try:
                print("WOW,I just specified you to rate with '*'")
                rate=input("Rate this program with '*' please :* XD =")
            except:
                pass
        print('THANKS FOR USING!!! :) XOXO')
        return
    else:
        pass
    print('player 2,enter your',b,'in')
    m6=int(input(' '))
    while (m6==m5)or(m6==m4)or(m6==m3)or(m6==m2)or(m6==m1)or(m6>9):
        try:
            print('you entered a position which already exist or the position is not between 1 and 9')
            print('player 2,enter your',b,'in')
            m6=int(input(' '))
        except:
            pass
    if m6==1:
        p1=b
    elif m6==2:
        p2=b
    elif m6==3:
        p3=b
    elif m6==4:
        p4=b
    elif m6==5:
        p5=b
    elif m6==6:
        p6=b
    elif m6==7:
        p7=b
    elif m6==8:
        p8=b
    elif m6==9:
        p9=b
    print()
    print(' ',p1,' | ',p2,' | ',p3)
    print('_________________________')
    print(' ',p4,' | ',p5,' | ',p6)
    print('_________________________')
    print(' ',p7,' | ',p8,' | ',p9)
    print()
    if((p1==b)and(p1==p2)and(p2==p3))or((p1==b)and(p1==p4)and(p4==p7))or((p1==b)and(p1==p5)and(p5==p9))or((p4==b)and(p4==p5)and(p5==p6))or((p7==p5)and(p5==b)and(p5==p3))or((p7==b)and(p7==p8)and(p8==p9))or((p2==b)and(p2==p5)and(p5==p8))or((p3==b)and(p3==p6)and(p6==p9)):
        print('player 2 wins!!! *claps*')
        rate=input("Rate this program with '*' please :* XD =")
        while rate not in'****************************************************************************************************':
            try:
                print("WOW,I just specified you to rate with '*'")
                rate=input("Rate this program with '*' please :* XD =")
            except:
                pass
        print('THANKS FOR USING!!! :) XOXO')
        return
    else:
        pass
    print('player 1,enter your',a,'in')
    m7=int(input(' '))
    while (m7==m6)or(m7==m5)or(m7==m4)or(m7==m3)or(m7==m2)or(m7==m1)or(m7>9):
        try:
            print('you entered a position which already exist or the position is not between 1 and 9')
            print('player 1,enter your',a,'in')
            m7=int(input(' '))
        except:
            pass
    if m7==1:
        p1=a
    elif m7==2:
        p2=a
    elif m7==3:
        p3=a
    elif m7==4:
        p4=a
    elif m7==5:
        p5=a
    elif m7==6:
        p6=a
    elif m7==7:
        p7=a
    elif m7==8:
        p8=a
    elif m7==9:
        p9=a
    print()
    print(' ',p1,' | ',p2,' | ',p3)
    print('_________________________')
    print(' ',p4,' | ',p5,' | ',p6)
    print('_________________________')
    print(' ',p7,' | ',p8,' | ',p9)
    print()
    if((p1==a)and(p1==p2)and(p2==p3))or((p1==a)and(p1==p4)and(p4==p7))or((p1==a)and(p1==p5)and(p5==p9))or((p4==a)and(p4==p5)and(p5==p6))or((p7==p5)and(p5==a)and(p5==p3))or((p7==a)and(p7==p8)and(p8==p9))or((p2==a)and(p2==p5)and(p5==p8))or((p3==a)and(p3==p6)and(p6==p9)):
        print('player 1 wins!!! *claps*')
        rate=input("Rate this program with '*' please :* XD =")
        while rate not in'****************************************************************************************************':
            try:
                print("WOW,I just specified you to rate with '*'")
                rate=input("Rate this program with '*' please :* XD =")
            except:
                pass
        print('THANKS FOR USING!!! :) XOXO')
        return
    else:
        pass
    print('player 2,enter your',b,'in')
    m8=int(input(' '))
    while (m8==m7)or(m8==m6)or(m8==m5)or(m8==m4)or(m8==m3)or(m8==m2)or(m8==m1)or(m8>9):
        try:
            print('you entered a position which already exist or the position is not between 1 and 9')
            print('player 2,enter your',b,'in')
            m8=int(input(' '))
        except:
            pass
    if m8==1:
        p1=b
    elif m8==2:
        p2=b
    elif m8==3:
        p3=b
    elif m8==4:
        p4=b
    elif m8==5:
        p5=b
    elif m8==6:
        p6=b
    elif m8==7:
        p7=b
    elif m8==8:
        p8=b
    elif m8==9:
        p9=b
    print()
    print(' ',p1,' | ',p2,' | ',p3)
    print('_________________________')
    print(' ',p4,' | ',p5,' | ',p6)
    print('_________________________')
    print(' ',p7,' | ',p8,' | ',p9)
    print()
    if((p1==b)and(p1==p2)and(p2==p3))or((p1==b)and(p1==p4)and(p4==p7))or((p1==b)and(p1==p5)and(p5==p9))or((p4==b)and(p4==p5)and(p5==p6))or((p7==p5)and(p5==b)and(p5==p3))or((p7==b)and(p7==p8)and(p8==p9))or((p2==b)and(p2==p5)and(p5==p8))or((p3==b)and(p3==p6)and(p6==p9)):
        print('player 2 wins!!! *claps*')
        rate=input("Rate this program with '*' please :* XD =")
        while rate not in'****************************************************************************************************':
            try:
                print("WOW,I just specified you to rate with '*'")
                rate=input("Rate this program with '*' please :* XD =")
            except:
                pass
        print('THANKS FOR USING!!! :) XOXO')
        return    
    else:
        pass        
    print('player 1,enter your',a,'in')
    m9=int(input(' '))
    if (m9==m8)or(m9==m7)or(m9==m6)or(m9==m5)or(m9==m4)or(m9==m3)or(m9==m2)or(m9==m1)or(m9>9):
        try:
            print('you entered a position which already exist or the position is not between 1 and 9')
            print('player 1,enter your',a,'in')
            m9=int(input(' '))
        except:
            pass
    if m9==1:
        p1=a
    elif m9==2:
        p2=a
    elif m9==3:
        p3=a
    elif m9==4:
        p4=a
    elif m9==5:
        p5=a
    elif m9==6:
        p6=a
    elif m9==7:
        p7=a
    elif m9==8:
        p8=a
    elif m9==9:
        p9=a
    print()
    print(' ',p1,' | ',p2,' | ',p3)
    print('_________________________')
    print(' ',p4,' | ',p5,' | ',p6)
    print('_________________________')
    print(' ',p7,' | ',p8,' | ',p9)
    print()
    if((p1==a)and(p1==p2)and(p2==p3))or((p1==a)and(p1==p4)and(p4==p7))or((p1==a)and(p1==p5)and(p5==p9))or((p4==a)and(p4==p5)and(p5==p6))or((p7==p5)and(p5==a)and(p5==p3))or((p7==a)and(p7==p8)and(p8==p9))or((p2==a)and(p2==p5)and(p5==p8))or((p3==a)and(p3==p6)and(p6==p9)):
        print('player 1 wins!!! *claps*')
    else:
        print(" it's a TIE... :(..better luck next time")
    rate=input("Rate the program with '*' please :* XD =")
    while rate not in'****************************************************************************************************':
        try:
            print("WOW,that wasn't a '*', rate with a '*'")
            rate=input("Rate this program with '*' please :* XD =")
        except:
            pass
    print('THANKS FOR USING!!! :) XOXO')
    
        
ttt()
    
    
           
