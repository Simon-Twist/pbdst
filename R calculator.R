#1
fact<-function(a)
{
  if (a==0)
  {
    return (1)
  }
  
  if (a<0)
  {
    return ("infinite")
  }

  return (a*fact(a-1))
}

#2
add<-function(a,b)
{
  a+b
}

#3
subtract<-function(a,b)
{
  a-b
}

#4
multiply<-function(a,b)
{
  a*b
}

#5
divide<-function(a,b)
{
  if (b!=0)
  {
    return (a/b)
  }
  return ("Cannot divide by zero")
}

#6
exponent<-function(a,b)
{
  if (a==0 && b<=0)
  {
    return ("Error")
  }
  return (a^b)
}

#7
square<-function(a)
{
  a*a
}

#8
cube<-function(a)
{
  a*a*a
}

#9
sqrRoot<-function(a)
{
  if (a<0)
  {
    return ("a complex number")
  }
  return (a^(1/2))
}

#10
cubeRoot<-function(a)
{
  if (a<0)
  {
    return (-((-a)^(1/3)))
  }
  return (a^(1/3))
}

#11
mode<-function(a)
{
  counts=c()
  i=1
  while (i<=length(a))
  {
    counts=c(counts,0)
    
    k=1
    while (k<=length(a))
    {
      if (a[i]==a[k])
      {
        counts[i]=counts[i]+1
      }
      k=k+1
    }
    i=i+1
  }
  
  modelist=c()
  m=1
  while (m<=length(a))
  {
    if (counts[m]==max(counts))
    {
      modelist=c(modelist,a[m])
    }
    m=m+1
  }
  
  #  norepeats=c()
  #  norepeats=c(norepeats,modelist[1])
  norepeats=modelist[1]
  n=1
  while (n<=length(modelist))
  {
    onlist=FALSE
    
    g=1
    while (g<=length(norepeats))
    {
      if (modelist[n]==norepeats[g])
      {
        onlist=TRUE
      }
      g=g+1
    }
    if (onlist==FALSE)
    {
      norepeats=c(norepeats,modelist[n])
    }
    n=n+1
  }
  return (norepeats)
}

#12
root<-function(a,b)
{
  if (((a==0) && ((1/b)<=0)) || (b==0))
  {
    return ("Dividing by zero")
  }

  if ((a<0) && ((b%%2)==1))
  {
    return (-(-a)^(1/b))
  }
  
  if ((a<0) && ((b%%2)==0))
  {
    return ("a complex number")
  }
  
  return (a^(1/b))
}

#1
"infinite"==fact(-3)
1==fact(0)
1==fact(1)
120==fact(5)
720==fact(6)
3628800==fact(10)

#2
2==add(-3,5)
-1==add(0,-1)
1==add(1,0)
15.1==add(5,10.1)
31==add(6,25)
-7.05==add(-3.05,-4)

#3
-8==subtract(-3,5)
1==subtract(0,-1)
1==subtract(1,0)
-5==subtract(5,10)
-19==subtract(6,25)
1==subtract(-3,-4)

#4
-15==multiply(-3,5)
0==multiply(0,-1)
0==multiply(1,0)
50==multiply(5,10)
150==multiply(6,25)
12==multiply(-3,-4)

#5
-0.6==divide(-3,5)
0==divide(0,-1)
"Cannot divide by zero"==divide(1,0)
0.5==divide(5,10)
0.24==divide(6,25)
4/3==divide(-4,-3)

#6
0==exponent(0,.5)
-243==exponent(-3,5)
"Error"==exponent(0,-1)
1==exponent(1,0)
9765625==exponent(5,10)
244140625==exponent(25,6)
(-3)^(-4)==exponent(-3,-4)

#7
9==square(-3)
0==square(0)
1==square(1)
25==square(5)
625==square(25)
1==square(-1)

#8
-27==cube(-3)
0==cube(0)
1==cube(1)
125==cube(5)
15625==cube(25)
-1==cube(-1)

#9
"a complex number"==sqrRoot(-3)
0==sqrRoot(0)
1==sqrRoot(1)
5^(1/2.0)==sqrRoot(5)
5==sqrRoot(25)
"a complex number"==sqrRoot(-1)

#10
3==cubeRoot(27)
-3==cubeRoot(-27)
-(3)^(1/3.0)==cubeRoot(-3)
0==cubeRoot(0)
1==cubeRoot(1)
5^(1/3.0)==cubeRoot(5)
25^(1/3.0)==cubeRoot(25)
-1==cubeRoot(-1)

#11
4==mode(c(1,2,3,4,4,4,5,6,7,7,8))
c(1,2,3)==mode(c(1,2,3))
8==mode(c(8,4,5,6,3,8,7))
6==mode(c(2,5,6,36,7,6,7,8.2,3,4.4,5,6))
1.2==mode(c(1.1,1.2,1.4,1.2,1.5,1.2,1.4,1.3))
"a"==mode(c("a","b","c","a","d"))
c("a",2)==mode(c("a",1,2,2,2,"a",1,"a"))
c(3,"b")==mode(c(3,1,"b","b","b",3,1,3))

#12
3==root(81,4)
-1.24573==round(root(-3,5),5)
"Dividing by zero"==root(0,-1)
"Dividing by zero"==root(1,0)
1.17462==round(root(5,10),5)
1.70998==round(root(25,6),5)
"a complex number"==root(-3,-4)
