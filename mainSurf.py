from surfsUp import getHein
from emailText import sendSurfText

#hein = getHein()


dir,spd,ht,prd = getHein()



greeting = "Surfs Up! Here are today's conditions:"
#surfStatement = "Surfs Up! Here are today's conditions:" + "\n"+dir + "\n"+spd + "\n"+ht + "\n"+prd
#surfStatement = "Surfs Up! Here are today's conditions:" + dir + spd + ht + prd
surfReport = dir + spd + ht + prd

surfStatement = greeting + surfReport
#print(surfStatement)
sendSurfText(surfStatement)

