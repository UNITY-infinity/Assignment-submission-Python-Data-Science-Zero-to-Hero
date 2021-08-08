def rev(s):
   news = ''
   rlt=s.split(' ')
   rlist=rlt.reverse()
   for i in rlist[:-1]:
      news=news+i+' '
   news+=rlist[-1]
   return(news)