import re
import fileinput
import sys
import os.path


def loadSpritesParse(file):
	i=2
	while True:
		v = str(i)
		tempNeeds = 'img1 = Crafty.e("2D, DOM, needs' + v+ ', Draggable").attr({x:0, y:0, w:0,h: 0});\n'
		tempFeelings = 'img1 = Crafty.e("2D, DOM, feelings' + v+ ', Draggable").attr({x:0, y:0, w:0,h: 0});\n'
		#tempNeeds = 'img1 = Crafty.e("2D, DOM, needs' + v+ ', Draggable")\n' + '     .attr({x:200, y:0, w:0,h: 0})\n' + '    .bind("Click", function(e) {\n' + '    	this.destroy();\n' + '    });\n'
		#tempFeelings = 'img1 = Crafty.e("2D, DOM, feelings' + v+ ', Draggable")\n' + '     .attr({x:500, y:0, w:0,h: 0})\n' + '    .bind("Click", function(e) {\n' +'    	this.destroy();\n' + '    });\n'
		tempNeeds2 = 'stackN.push(img1);\n'
		tempFeelings2 = 'stackF.push(img1);\n'
		file.write(tempNeeds+tempNeeds2)
		file.write(tempFeelings+tempFeelings2)
		i=i+1
		if(i == 71):
			return


def saveStatesParse(file):
	i=1
	while True:
		num = str(i)

		firstL = 'imgx = img' + num+'.x.toString();' + '\n'
		secondL = 'imgy = img' + num+ '.y.toString();' + '\n'
		thirdL = 'imgw = img'+num+'.w.toString();' + '\n'
		fourthL = 'imgh = img'+num+'.h.toString();' + '\n'
		fifthL = 'coordinateValue = imgx + "," +imgy + "," + imgw + "," + imgh;'+ '\n'
		sixthL = 'localStorage.setItem("img' +num + '",coordinateValue);'+ '\n'

		tempCardCoordinates = firstL + secondL + thirdL + fourthL + fifthL + sixthL
		file.write(tempCardCoordinates)
		i=i+1
		if(i == 141):
			return

def loadStatesParse(file):
	i=1
	while True:
		num = str(i)

		firstL =    'if (localStorage.img'+num+ '!== null) {' + '\n'
		secondL =   'var pair = localStorage.getItem("img' + num+ '");' + '\n'
		thirdL = 	'var coords = pair.split(",");'+ '\n'
		fourthL = 	'img'+num+'.x= parseInt(coords[0]);' + '\n'
		fifthL = 	'img'+num+'.y= parseInt(coords[1]);' + '\n'
		sixthL = 	'img'+num+'.w= parseInt(coords[2]);' + '\n'
		seventhL =  'img'+num+'.h= parseInt(coords[3]);'+ 'img'+num+'.z=2;' + '\n'
		eigthL =    'if (img' + num + '.h!==0) {' + '\n onTopPickPileN.push(img' + num+');}\n'
		ninthL =    'else { stackN.push(img'+num+');}\n'
		tenthL =    '}' + '\n'

		tempCardCoordinates = firstL + secondL + thirdL + fourthL + fifthL + sixthL + seventhL + eigthL + ninthL + tenthL
		file.write(tempCardCoordinates)
		i=i+2
		if(i == 141):
			return

def main():
	
	file1 = open("savedState.txt", "w")
	saveStatesParse(file1)
	file1.close()
	file2 = open("loadState.txt", "w")
	loadStatesParse(file2)
	file2.close()


if __name__ == "__main__":
    main()