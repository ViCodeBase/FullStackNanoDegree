import webbrowser
import time

startTime = time.ctime()
print "The Program started at - " + startTime
startLoop = 1
endLoop = 5
while(startLoop < endLoop):
	time.sleep(1*60)
	webbrowser.open("https://www.youtube.com/watch?v=hXh35CtnSyU")
	print "Bulleya - Ranbir, Aishwarya Rai and Anushka Rai invoked at - " + time.ctime()
	startLoop=startLoop+1