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
		if(i == 140):
			return

def loadStatesParseOdd(file):
	i=1
	while True:
		num = str(i)

		firstL =    'if (localStorage.img'+num+ '!== null) {' + '\n'
		secondL =   'var pair = localStorage.getItem("img' + num+ '");' + '\n'
		thirdL = 	'var coords = pair.split(",");'+ '\n'
		fourthL = 	'img'+num+ '.attr({x:parseInt(coords[0]), y:parseInt(coords[1]),w: parseInt(coords[2]), h:parseInt(coords[3])}).bind("MouseOver", function(e) {if(!dragging){this.attr({x:this._x, y:this._y, w:cardWidth+200,h: cardHeight+200});this.z = 3;}}).bind("MouseOut", function(e) {if(!dragging){this.attr({x:this._x, y:this._y, w:cardWidth,h: cardHeight});this.z=2;}}).bind("DoubleClick", function(e){var j = onTopPickPileN.indexOf(this);stackN.unshift(this);onTopPickPileN.splice(j,1);this.attr({x:800, y:500, w:0,h: 0});if(stackN.length > 0){imgNB.attr({x:bgWidth-68, y:0, w:cardWidth,h: cardHeight});}}).bind("StartDrag", function(e){dragging = true;})	.bind("StopDrag", function(e){dragging = false;if(checkContained(this._x,this._y)){var coordinates = coordinatesContained(this._x,this._y);this.attr({x:coordinates.x-5,y:coordinates.y+5,w:cardWidth,h:cardHeight});}});' + '\n'
		fifthL =    'img'+num+'.z=2;'+'if(img'+num+'.x!==0){onTopPickPileN.push(img'+num+');\nvar j = stackF.indexOf(img'+num+');\nstackF.splice(j,1);}' + '\n'
		sixthL =    '}' + '\n'

		tempCardCoordinates = firstL + secondL + thirdL + fourthL+ fifthL + sixthL
		file.write(tempCardCoordinates)
		i=i+2
		if(i == 141):
			return

def loadStatesParseEven(file):
	i=2
	while True:
		num = str(i)

		firstL =    'if (localStorage.img'+num+ '!== null) {' + '\n'
		secondL =   'var pair = localStorage.getItem("img' + num+ '");' + '\n'
		thirdL = 	'var coords = pair.split(",");'+ '\n'
		fourthL = 	'img'+num+ '.attr({x:parseInt(coords[0]), y:parseInt(coords[1]),w: parseInt(coords[2]), h:parseInt(coords[3])}).bind("MouseOver", function(e) {if(!dragging){this.attr({x:this._x, y:this._y, w:cardWidth+200,h: cardHeight+200});this.z = 3;}}).bind("MouseOut", function(e) {if(!dragging){this.attr({x:this._x, y:this._y, w:cardWidth,h: cardHeight});this.z=2;}}).bind("DoubleClick", function(e){var j = onTopPickPileF.indexOf(this);stackF.unshift(this);onTopPickPileF.splice(j,1);this.attr({x:800, y:500, w:0,h: 0});if(stackF.length > 0){imgFB.attr({x:bgWidth-68, y:0, w:cardWidth,h: cardHeight});}}).bind("StartDrag", function(e){dragging = true;})	.bind("StopDrag", function(e){dragging = false;if(checkContained(this._x,this._y)){var coordinates = coordinatesContained(this._x,this._y);this.attr({x:coordinates.x-5,y:coordinates.y+5,w:cardWidth,h:cardHeight});}});' + '\n'
		fifthL =    'img'+num+'.z=2;'+'if(img'+num+'.x!==0){onTopPickPileF.push(img'+num+');\nvar j = stackF.indexOf(img'+num+');\nstackF.splice(j,1);}' + '\n'
		sixthL =    '}' + '\n'

		tempCardCoordinates = firstL + secondL + thirdL + fourthL + fifthL + sixthL
		file.write(tempCardCoordinates)
		i=i+2
		if(i == 142):
			return

def main():
	
	file1 = open("saveState.txt", "w")
	saveStatesParse(file1)
	file1.close()



if __name__ == "__main__":
    main()

