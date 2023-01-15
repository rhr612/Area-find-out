def area():
    shape=int(input('Which shape area you want to find?\n'+'1.Rectangle\n'+'2.Square\n'+'3.Triangle\n'+'4.Circle\n'+'5.Trapezoid\n'))
    if shape==1:
        #Area = l × w
        l=int(input('What is the length of the Rectangle?\n'))
        w=int(input('What is the width of the Rectangle?\n'))
        ans=l*w
        print('The area of the rectangle is '+str(ans))

    elif shape==2:
        #Area = a^2
        a=int(input('What is the side of the square?\n'))
        ans=a*a
        print('The area of the rectangle is '+str(ans))
    elif shape==3:
        #Area = 1/2 b*h  ;b=base ;h=height;
        b=int(input('What is the base of the Triangle?\n'))
        h=int(input('What is the height of the Triangle?\n'))
        ans=0.5*b*h
        print('The area of the rectangle is '+str(ans))
    elif shape==4:
        #Area = Π*r^2
        r=int(input('What is the radius of the Circlle?\n'))
        ans=3.1416*r*r
        print('The area of the rectangle is '+str(ans))
    elif shape==5:
        #Area = 0.5*(a+b)*h
        a=int(input('What is the base1(a) of the Trapezoid?\n'))
        b=int(input('What is the base2(b) of the Trapezoid?\n'))
        h=int(input('What is the height of the Trapezoid?\n'))
        ans=0.5*(a+b)*h
        print('The area of the rectangle is '+str(ans))
    else:
        print('You enter a wrong number')

while True:
    area()
    continue

