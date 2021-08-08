def armstrong(n):
   comp=0
   for i in str(n):
      comp = comp + int(i)**3
   if comp==n:
      print('Yes ',n,' is an Armstrong number.')
   else:
      print('No ',n,' is not an Armstrong numbers.')