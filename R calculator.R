#1
fact<-function(a)
{
  if (a<0)
  {
    "infinite"
  }
  if (a==0)
  {
    1
  }
  else
  {
    a*fact(a-1)
  }
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
  a/b
}

#6
exponent<-function(a,b)
{
  if (a==0 && b<=0)
  {
    "Error"
  }
  a^b
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
    "a complex number"
  }
  a^(1/2)
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


#12
root<-function(a,b)
{
  if (a==0 && (1/b)<1)
  {
    return ("Error")
  }
  if (a<0 && (b%2)==1)								
  {
    return (-(-a)^(1.0/b))
  }
  if (a<0 && (b%2)==0)
  {
    return ("a complex number")
  }
  if (b>=1)
  {
    return (a^(1.0/b))
  }
  return ("Error")
}

#1
fact(-3)
fact(0)
fact(1)
fact(5)
fact(6)
fact(10)

#2
add(-3,5)
add(0,-1)
add(1,0)
add(5,10.1)
add(6,25)
add(-3.05,-4)

#3


#4


#5


#6
exponent(0,.5)

#7


#8


#9


#10
cubeRoot(27)
cubeRoot(-27)

#11


#12
root(81,4)