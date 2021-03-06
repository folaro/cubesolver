#算法参考:https://ruwix.com/the-rubiks-cube/how-to-solve-the-rubiks-cube-beginners-method/

from random import randint #用以随机打乱魔方
import sys #使用sleep ()方法做暂停
from vpython import * # For 3D

moveNbr = 0 # 转动的步数
fps = 24 # 一秒24帧

# d = Down     
# u = Up	
# f = Face    
# b = Back   
# r = Right
# l = Left 

# 面与向量的关系
faces = {'F': (color.red, vector(0, 0, 1)),
		 'B': (color.orange, vector(0, 0, -1)),
		 'U': (color.yellow, vector(0, 1, 0)),
		 'L': (color.blue, vector(-1, 0, 0)),
		 'D': (color.white, vector(0, -1, 0)),
		 'R': (color.green, vector(1, 0, 0))}
# 坐标系z轴方向从纸面指向我们，x轴从左到右，y轴从下到上
# 每个面逐一上色共6个9宫格，54个sticker
stickers = []
for face_color, axis in faces.values():
	for x in (-1, 0, 1):
		for y in (-1, 0, 1):
			sticker = box(color=face_color, pos=vector(x, y, 1.5),length=0.98, height=0.98, width=0.05)
			cos_angle = dot(vector(0, 0, 1), axis)#两垂直向量点积为0
			if cos_angle == 0:#两垂直单位向量叉积方向为右手法则
				pivot = cross(vector(0, 0, 1), axis)  
			else:
				pivot=vector(1, 0, 0) 
			sticker.rotate(angle=acos(cos_angle), axis=pivot, origin=vector(0, 0, 0))
			stickers.append(sticker)

# ６面转动方法
def rotate3D(key):
	if key[0] in faces:
		face_color, axis = faces[key[0]]
		angle = ((pi / 2) if len(key)>1 else -pi / 2)
		for r in arange(0, angle, angle / fps):
			rate(fps)
			for sticker in stickers:
				if dot(sticker.pos, axis) > 0.5:
					sticker.rotate(angle=angle / fps, axis=axis,origin=vector(0, 0, 0))
	elif key[0] == 'E':
		axis = vector(0, 0.5, 0)
		angle = ((pi / 2) if len(key)>1 else -pi / 2)
		for r in arange(0, angle, angle / fps):
			rate(fps)
			for sticker in stickers:
				sticker.rotate(angle=angle / fps, axis=axis,origin=vector(0, 0, 0))




# 'w' = White  
# 'y' = Yellow 
# 'r' = Red	
# 'o' = Orange 
# 'g' = Green  
# 'b' = Blue  

#中心块着色
d   = 'w' 
u   = 'y' 
f   = 'r' 
b   = 'o' 
r   = 'g' 
l   = 'b' 

# 棱块两面着色
uf = {'u': 'y', 'd': '', 'f': 'r', 'b': '', 'r': '', 'l': ''} 
ur = {'u': 'y', 'd': '', 'f': '', 'b': '', 'r': 'g', 'l': ''} 
ub = {'u': 'y', 'd': '', 'f': '', 'b': 'o', 'r': '', 'l': ''} 
ul = {'u': 'y', 'd': '', 'f': '', 'b': '', 'r': '', 'l': 'b'} 
df = {'u': '', 'd': 'w', 'f': 'r', 'b': '', 'r': '', 'l': ''} 
dr = {'u': '', 'd': 'w', 'f': '', 'b': '', 'r': 'g', 'l': ''} 
db = {'u': '', 'd': 'w', 'f': '', 'b': 'o', 'r': '', 'l': ''} 
dl = {'u': '', 'd': 'w', 'f': '', 'b': '', 'r': '', 'l': 'b'} 
fr = {'u': '', 'd': '', 'f': 'r', 'b': '', 'r': 'g', 'l': ''} 
fl = {'u': '', 'd': '', 'f': 'r', 'b': '', 'r': '', 'l': 'b'} 
br = {'u': '', 'd': '', 'f': '', 'b': 'o', 'r': 'g', 'l': ''} 
bl = {'u': '', 'd': '', 'f': '', 'b': 'o', 'r': '', 'l': 'b'} 

# 角块三面着色
ufr = {'u': 'y', 'd': '', 'f': 'r','b': '', 'r': 'g', 'l': ''} 
ufl = {'u': 'y', 'd': '', 'f': 'r', 'b': '', 'r': '', 'l': 'b'} 
ubr = {'u': 'y', 'd': '', 'f': '', 'b': 'o', 'r': 'g', 'l': ''} 
ubl = {'u': 'y', 'd': '', 'f': '', 'b': 'o', 'r': '', 'l': 'b'} 
dfr = {'u': '', 'd': 'w', 'f': 'r', 'b': '', 'r': 'g', 'l': ''} 
dfl = {'u': '', 'd': 'w', 'f': 'r', 'b': '', 'r': '', 'l': 'b'} 
dbr = {'u': '', 'd': 'w', 'f': '', 'b': 'o', 'r': 'g', 'l': ''} 
dbl = {'u': '', 'd': 'w', 'f': '', 'b': 'o', 'r': '', 'l': 'b'}


#转动方法，默认显示
def move(face, show=1):


	global d, u, f, b, r, l, uf, ur, ub, ul, df, dr, db, dl, fr, fl, br, bl, ufr, ufl, ubr, ubl, dfr, dfl, dbr, dbl
	global moveNbr
	moveNbr += 1
	if show == 1:
		sys.stdout.write(face + ", ") 

	if face == "R": # 右面顺时针转
		ufr['u'], ufr['f'], ufr['r'], ubr['u'], ubr['b'], ubr['r'], dbr['d'], dbr['b'], dbr['r'], dfr['d'], dfr['f'], dfr['r'],  = \
		dfr['f'], dfr['d'], dfr['r'], ufr['f'], ufr['u'], ufr['r'], ubr['b'], ubr['u'], ubr['r'], dbr['b'], dbr['d'], dbr['r']

		ur['u'], ur['r'], br['b'], br['r'], dr['d'], dr['r'], fr['f'], fr['r'],  = \
		fr['f'], fr['r'], ur['u'], ur['r'], br['b'], br['r'], dr['d'], dr['r'] 
		rotate3D("R")


	if face == "R'": # 右面逆时针转
		dfr['f'], dfr['d'], dfr['r'], ufr['f'], ufr['u'], ufr['r'], ubr['b'], ubr['u'], ubr['r'], dbr['b'], dbr['d'], dbr['r'], = \
		ufr['u'], ufr['f'], ufr['r'], ubr['u'], ubr['b'], ubr['r'], dbr['d'], dbr['b'], dbr['r'], dfr['d'], dfr['f'], dfr['r']
		
		ur['u'], ur['r'], fr['f'], fr['r'], dr['d'], dr['r'], br['b'], br['r'],  = \
		br['b'], br['r'], ur['u'], ur['r'], fr['f'], fr['r'], dr['d'], dr['r']
		rotate3D("R'")


	if face == "U": # 顶面顺时针转
		ufr['u'], ufr['f'], ufr['r'], ubr['u'], ubr['b'], ubr['r'], ubl['u'], ubl['b'], ubl['l'], ufl['u'], ufl['f'], ufl['l'],  = \
		ubr['u'], ubr['r'], ubr['b'], ubl['u'], ubl['l'], ubl['b'], ufl['u'], ufl['l'], ufl['f'], ufr['u'], ufr['r'], ufr['f']
		
		ur['u'], ur['r'], uf['u'], uf['f'], ul['u'], ul['l'], ub['u'], ub['b'],  = \
		ub['u'], ub['b'], ur['u'], ur['r'], uf['u'], uf['f'], ul['u'], ul['l']
		rotate3D("U")


	if face == "U'": # 顶面逆时针转
		ubr['u'], ubr['r'], ubr['b'], ubl['u'], ubl['l'], ubl['b'], ufl['u'], ufl['l'], ufl['f'], ufr['u'], ufr['r'], ufr['f'],  = \
		ufr['u'], ufr['f'], ufr['r'], ubr['u'], ubr['b'], ubr['r'], ubl['u'], ubl['b'], ubl['l'], ufl['u'], ufl['f'], ufl['l']

		ur['u'], ur['r'], uf['u'], uf['f'], ul['u'], ul['l'], ub['u'], ub['b'],  = \
	uf['u'], uf['f'], ul['u'], ul['l'], ub['u'], ub['b'], ur['u'], ur['r']
		rotate3D("U'")


	if face == "D": # 底面顺时针转
		dbr['d'], dbr['r'], dbr['b'], dbl['d'], dbl['l'], dbl['b'], dfl['d'], dfl['l'], dfl['f'], dfr['d'], dfr['r'], dfr['f'],  = \
		dfr['d'], dfr['f'], dfr['r'], dbr['d'], dbr['b'], dbr['r'], dbl['d'], dbl['b'], dbl['l'], dfl['d'], dfl['f'], dfl['l']

		dr['d'], dr['r'], df['d'], df['f'], dl['d'], dl['l'], db['d'], db['b'],  = \
		df['d'], df['f'], dl['d'], dl['l'], db['d'], db['b'], dr['d'], dr['r']
		rotate3D("D")


	if face == "D'": # 底面逆时针转
		dfr['d'], dfr['f'], dfr['r'], dbr['d'], dbr['b'], dbr['r'], dbl['d'], dbl['b'], dbl['l'], dfl['d'], dfl['f'], dfl['l'],  = \
		dbr['d'], dbr['r'], dbr['b'], dbl['d'], dbl['l'], dbl['b'], dfl['d'], dfl['l'], dfl['f'], dfr['d'], dfr['r'], dfr['f']

		df['d'], df['f'], dr['d'], dr['r'], db['d'], db['b'], dl['d'], dl['l'],  = \
		dr['d'], dr['r'], db['d'], db['b'], dl['d'], dl['l'], df['d'], df['f']
		rotate3D("D'")


	if face == "L'": # 左面逆时针转
		ufl['u'], ufl['f'], ufl['l'], ubl['u'], ubl['b'], ubl['l'], dbl['d'], dbl['b'], dbl['l'], dfl['d'], dfl['f'], dfl['l'],  = \
		dfl['f'], dfl['d'], dfl['l'], ufl['f'], ufl['u'], ufl['l'], ubl['b'], ubl['u'], ubl['l'], dbl['b'], dbl['d'], dbl['l']

		ul['u'], ul['l'], bl['b'], bl['l'], dl['d'], dl['l'], fl['f'], fl['l'],  = \
		fl['f'], fl['l'], ul['u'], ul['l'], bl['b'], bl['l'], dl['d'], dl['l'] 
		rotate3D("L'")


	if face == "L": # 左面顺时针转
		dfl['f'], dfl['d'], dfl['l'], ufl['f'], ufl['u'], ufl['l'], ubl['b'], ubl['u'], ubl['l'], dbl['b'], dbl['d'], dbl['l'], = \
		ufl['u'], ufl['f'], ufl['l'], ubl['u'], ubl['b'], ubl['l'], dbl['d'], dbl['b'], dbl['l'], dfl['d'], dfl['f'], dfl['l']
		
		ul['u'], ul['l'], fl['f'], fl['l'], dl['d'], dl['l'], bl['b'], bl['l'],  = \
		bl['b'], bl['l'], ul['u'], ul['l'], fl['f'], fl['l'], dl['d'], dl['l']
		rotate3D("L")


	if face == "F": # 前面顺时针转
		ufr['u'], ufr['f'], ufr['r'], dfr['d'], dfr['f'], dfr['r'], dfl['d'], dfl['f'], dfl['l'], ufl['u'], ufl['f'], ufl['l'],  = \
		ufl['l'], ufl['f'], ufl['u'], ufr['r'], ufr['f'], ufr['u'], dfr['r'], dfr['f'], dfr['d'], dfl['l'], dfl['f'], dfl['d']
		
		uf['u'], uf['f'], fl['l'], fl['f'], df['d'], df['f'], fr['r'], fr['f'],  = \
		fl['l'], fl['f'], df['d'], df['f'], fr['r'], fr['f'], uf['u'], uf['f']
		rotate3D("F")


	if face == "F'": # 前面逆时针转
		ufl['l'], ufl['f'], ufl['u'], ufr['r'], ufr['f'], ufr['u'], dfr['r'], dfr['f'], dfr['d'], dfl['l'], dfl['f'], dfl['d'],  = \
		ufr['u'], ufr['f'], ufr['r'], dfr['d'], dfr['f'], dfr['r'], dfl['d'], dfl['f'], dfl['l'], ufl['u'], ufl['f'], ufl['l']
		
		fl['l'], fl['f'], df['d'], df['f'], fr['r'], fr['f'], uf['u'], uf['f'],  = \
		uf['u'], uf['f'], fl['l'], fl['f'], df['d'], df['f'], fr['r'], fr['f']
		rotate3D("F'")


	if face == "B'":	# 后面逆时针转
		ubr['u'], ubr['b'], ubr['r'], dbr['d'], dbr['b'], dbr['r'], dbl['d'], dbl['b'], dbl['l'], ubl['u'], ubl['b'], ubl['l'],  = \
		ubl['l'], ubl['b'], ubl['u'], ubr['r'], ubr['b'], ubr['u'], dbr['r'], dbr['b'], dbr['d'], dbl['l'], dbl['b'], dbl['d']
		
		ub['u'], ub['b'], bl['l'], bl['b'], db['d'], db['b'], br['r'], br['b'],  = \
		bl['l'], bl['b'], db['d'], db['b'], br['r'], br['b'], ub['u'], ub['b']
		rotate3D("B'")


	if face == "B": # 后面顺时针转
		ubl['l'], ubl['b'], ubl['u'], ubr['r'], ubr['b'], ubr['u'], dbr['r'], dbr['b'], dbr['d'], dbl['l'], dbl['b'], dbl['d'],  = \
		ubr['u'], ubr['b'], ubr['r'], dbr['d'], dbr['b'], dbr['r'], dbl['d'], dbl['b'], dbl['l'], ubl['u'], ubl['b'], ubl['l']
		
		bl['l'], bl['b'], db['d'], db['b'], br['r'], br['b'], ub['u'], ub['b'],  = \
		ub['u'], ub['b'], bl['l'], bl['b'], db['d'], db['b'], br['r'], br['b']
		rotate3D("B")



def melanger(nbrDeMoves=25, show=1): #随机打乱方法

	moveList = ["R","R'","L","L'","U","U'","D","D'","F","F'","B","B'"]

	i=0
	for i in range(nbrDeMoves):
		aleatoire = randint(0,11)
		move(moveList[aleatoire], 0)
		if show == 1:
			sys.stdout.write(str(moveList[aleatoire]).upper()+ " ")
	if show == 1:
		print("\n随机打乱魔方!")



def printCube(): #输出所有面的颜色
	print("\n\t" + ubl['u'] + ub['u'] + ubr['u'] + "\n\t" + \
				ul['u'] + u + ur['u'] + "\n\t" + \
				ufl['u'] + uf['u'] + ufr['u'] + "\n" + \

				ubl['l'] + ul['l'] + ufl['l'] + " "	 + ufl['f'] + uf['f'] + ufr['f'] + " "	   + ufr['r'] + ur['r'] + ubr['r'] + " "	   + ubr['b'] + ub['b'] + ubl['b'] + "\n" + \
				bl['l'] + l + fl['l'] + " "			 + fl['f'] + f + fr['f'] + " "			   + fr['r'] + r + br['r'] + " "			   + br['b'] + b + bl['b'] + " " + "\n" + \
				dbl['l'] + dl['l'] + dfl['l'] + " "	  + dfl['f'] + df['f'] + dfr['f'] + " "	  + dfr['r'] + dr['r'] + dbr['r'] + " "	   + dbr['b'] + db['b'] + dbl['b'] + "\n\t" + \

				dfl['d'] + df['d'] + dfr['d'] + "\n\t" + dl['d'] + d + dr['d'] + "\n\t" + dbl['d'] + db['d'] + dbr['d'] + "\n")

	print("=====================================")



def turnCube(show=1): #从右向左中轴转，魔方公式中的Y
	global d, u, f, b, r, l

	# 顶部角块各面的映射变化
	ufr['u'], ufr['f'], ufr['r'], ubr['u'], ubr['b'], ubr['r'], ubl['u'], ubl['b'], ubl['l'], ufl['u'], ufl['f'], ufl['l'],  = \
	ubr['u'], ubr['r'], ubr['b'], ubl['u'], ubl['l'], ubl['b'], ufl['u'], ufl['l'], ufl['f'], ufr['u'], ufr['r'], ufr['f']

	# 顶部棱块各面的映射变化
	ur['u'], ur['r'], uf['u'], uf['f'], ul['u'], ul['l'], ub['u'], ub['b'],  = \
	ub['u'], ub['b'], ur['u'], ur['r'], uf['u'], uf['f'], ul['u'], ul['l']

	# 底部棱块各面的映射变化
	dfr['d'], dfr['f'], dfr['r'], dbr['d'], dbr['b'], dbr['r'], dbl['d'], dbl['b'], dbl['l'], dfl['d'], dfl['f'], dfl['l'],  = \
	dbr['d'], dbr['r'], dbr['b'], dbl['d'], dbl['l'], dbl['b'], dfl['d'], dfl['l'], dfl['f'], dfr['d'], dfr['r'], dfr['f']

	# 底部棱块各面的映射变化
	df['d'], df['f'], dr['d'], dr['r'], db['d'], db['b'], dl['d'], dl['l'],  = \
	dr['d'], dr['r'], db['d'], db['b'], dl['d'], dl['l'], df['d'], df['f']

	# 中间棱块的映射变化
	fl['f'], fl['l'], fr['f'], fr['r'], br['b'], br['r'], bl['b'], bl['l']  = \
	fr['r'], fr['f'], br['r'], br['b'], bl['l'], bl['b'], fl['l'], fl['f']

	# 中心块的映射变化
	f, r, b, l = \
	r, b, l, f

	rotate3D("E")

	if show == 1:
		print("轴转")



def resetCube():

	#中心块
	d   = 'w' # 下是白
	u   = 'y' # 上是黄
	f   = 'r' # 前是红
	b   = 'o' # 后是黄
	r   = 'g' # 右是绿
	l   = 'b' # 左是蓝
	
	#12个棱块和8个角块颜色
	uf = {'u': 'y', 'd': '', 'f': 'r', 'b': '', 'r': '', 'l': ''} 
	ur = {'u': 'y', 'd': '', 'f': '', 'b': '', 'r': 'g', 'l': ''} 
	ub = {'u': 'y', 'd': '', 'f': '', 'b': 'o', 'r': '', 'l': ''} 
	ul = {'u': 'y', 'd': '', 'f': '', 'b': '', 'r': '', 'l': 'b'} 
	df = {'u': '', 'd': 'w', 'f': 'r', 'b': '', 'r': '', 'l': ''} 
	dr = {'u': '', 'd': 'w', 'f': '', 'b': '', 'r': 'g', 'l': ''} 
	db = {'u': '', 'd': 'w', 'f': '', 'b': 'o', 'r': '', 'l': ''} 
	dl = {'u': '', 'd': 'w', 'f': '', 'b': '', 'r': '', 'l': 'b'} 
	fr = {'u': '', 'd': '', 'f': 'r', 'b': '', 'r': 'g', 'l': ''} 
	fl = {'u': '', 'd': '', 'f': 'r', 'b': '', 'r': '', 'l': 'b'} 
	br = {'u': '', 'd': '', 'f': '', 'b': 'o', 'r': 'g', 'l': ''} 
	bl = {'u': '', 'd': '', 'f': '', 'b': 'o', 'r': '', 'l': 'b'} 
		 
	ufr = {'u': 'y', 'd': '', 'f': 'r','b': '', 'r': 'g', 'l': ''} 
	ufl = {'u': 'y', 'd': '', 'f': 'r', 'b': '', 'r': '', 'l': 'b'} 
	ubr = {'u': 'y', 'd': '', 'f': '', 'b': 'o', 'r': 'g', 'l': ''} 
	ubl = {'u': 'y', 'd': '', 'f': '', 'b': 'o', 'r': '', 'l': 'b'} 
	dfr = {'u': '', 'd': 'w', 'f': 'r', 'b': '', 'r': 'g', 'l': ''} 
	dfl = {'u': '', 'd': 'w', 'f': 'r', 'b': '', 'r': '', 'l': 'b'} 
	dbr = {'u': '', 'd': 'w', 'f': '', 'b': 'o', 'r': 'g', 'l': ''} 
	dbl = {'u': '', 'd': 'w', 'f': '', 'b': 'o', 'r': '', 'l': 'b'}



def solveWhiteCross(show=1): #魔方通用解法第一步：底部十字

	if show == 1:
		print("\n构建底面白十字:\n")
	global d, u, f, b, r, l, uf, ur, ub, ul, df, dr, db, dl, fr, fl, br, bl, ufr, ufl, ubr, ubl, dfr, dfl, dbr, dbl#6中心块，12棱块，8角块
	liste = ['r', 'g', 'o', 'b']#颜色

	for i in liste:
		if dr['d'] == 'w' and dr['r'] == i:
			move("R", show)
			move("R", show)
			move("U", show)
			move("F", show)
			move("F", show)

		elif db['d'] == 'w' and db['b'] == i:
			move("B", show)
			move("B", show)
			move("U", show)
			move("U", show)
			move("F", show)
			move("F", show)

		elif dl['d'] == 'w' and dl['l'] == i:
			move("L", show)
			move("L", show)
			move("U'", show)
			move("F", show)
			move("F", show)

		elif fr['f'] == 'w' and fr['r'] == i:
			move("R", show)
			move("U", show)
			move("R'", show)
			move("F", show)
			move("F", show)

		elif fl['f'] == 'w' and fl['l'] == i:
			move("L'", show)
			move("U'", show)
			move("L", show)
			move("F", show)
			move("F", show)

		elif br['b'] == 'w' and br['r'] == i:
			move("R'", show)
			move("U", show)
			move("R", show)
			move("F", show)
			move("F", show)

		elif bl['b'] == 'w' and bl['l'] == i:
			move("L", show)
			move("U'", show)
			move("L'", show)
			move("F", show)
			move("F", show)

		elif uf['u'] == 'w' and uf['f'] == i:
			move("F", show)
			move("F", show)

		elif ur['u'] == 'w' and ur['r'] == i:
			move("U", show)
			move("F", show)
			move("F", show)

		elif ul['u'] == 'w' and ul['l'] == i:
			move("U'", show)
			move("F", show)
			move("F", show)

		elif ub['u'] == 'w' and ub['b'] == i:
			move("U", show)
			move("U", show)
			move("F", show)
			move("F", show)

		elif dr['d'] == i and dr['r'] == 'w':
			move("R", show)
			move("F", show)

		elif db['d'] == i and db['b'] == 'w':
			move("B", show)
			move("D", show)
			move("R", show)
			move("D'", show)

		elif dl['d'] == i and dl['l'] == 'w':
			move("L'", show)
			move("F'", show)

		elif fr['f'] == i and fr['r'] == 'w':
			move("F", show)

		elif fl['f'] == i and fl['l'] == 'w':
			move("F'", show)

		elif br['b'] == i and br['r'] == 'w':
			move("B", show)
			move("U", show)
			move("U", show)
			move("B'", show)
			move("F", show)
			move("F", show)

		elif bl['b'] == i and bl['l'] == 'w':
			move("B'", show)
			move("U", show)
			move("U", show)
			move("B", show)
			move("F", show)
			move("F", show)

		elif uf['u'] == i and uf['f'] == 'w':
			move("U'", show)
			move("R'", show)
			move("F", show)
			move("R", show)

		elif ur['u'] == i and ur['r'] == 'w':
			move("R'", show)
			move("F", show)
			move("R", show)

		elif ul['u'] == i and ul['l'] == 'w':
			move("L", show)
			move("F'", show)
			move("L'", show)

		elif ub['u'] == i and ub['b'] == 'w':
			move("U", show)
			move("R'", show)
			move("F", show)
			move("R", show)

		elif df['d'] == i and df['f'] == 'w':
			move("F'", show)
			move("D", show)
			move("R'", show)
			move("D'", show)
		#end
		turnCube(show)



def solveWhiteCorner(show=1): #魔方通用解法第二步：放置白色角块

	if show == 1:
		print("\n处理白色角块:\n")
	global d, u, f, b, r, l, uf, ur, ub, ul, df, dr, db, dl, fr, fl, br, bl, ufr, ufl, ubr, ubl, dfr, dfl, dbr, dbl
	liste = ["wrg", "wgo", "wob", "wbr"] #  'wrg' 表示白红绿，以此类推

	for j in liste:
		
		if ufl['u'] in j and ufl['f'] in j and ufl['l'] in j:
			move("U'", show)

		elif ubl['u'] in j and ubl['b'] in j and ubl['l'] in j:
			move("U'", show)
			move("U'", show)

		elif ubr['u'] in j and ubr['b'] in j and ubr['r'] in j:
			move("U", show)

		elif dfl['d'] in j and dfl['f'] in j and dfl['l'] in j:
			move("L'", show)
			move("U'", show)
			move("L", show)

		elif dbl['d'] in j and dbl['b'] in j and dbl['l'] in j:
			move("L", show)
			move("U", show)
			move("U", show)
			move("L'", show)

		elif dbr['d'] in j and dbr['b'] in j and dbr['r'] in j:
			move("R'", show)
			move("U", show)
			move("R", show)
			move("U", show)


		if dfr['r'] == 'w' and dfr['d'] in j and dfr['f'] in j:
			move("R", show)
			move("U", show)
			move("R'", show)
			move("U'", show)
			move("R", show)
			move("U", show)
			move("R'", show)

		if dfr['f'] == 'w' and dfr['d'] in j and dfr['r'] in j:
			move("F'", show)
			move("U'", show)
			move("F", show)
			move("U", show)
			move("F'", show)
			move("U'", show)
			move("F", show)

		if ufr['u'] == 'w' and ufr['f'] in j and ufr['r'] in j: 
			move("R", show)
			move("U", show)
			move("U", show)
			move("R'", show)
			move("U'", show)
			move("R", show)
			move("U", show)
			move("R'", show)

		if ufr['f'] == 'w' and ufr['u'] in j and ufr['r'] in j:
			move("U", show)
			move("R", show)
			move("U'", show)
			move("R'", show)

		if ufr['r'] == 'w'and ufr['u'] in j and ufr['f'] in j:
			move("R", show)
			move("U", show)
			move("R'", show)
		
		turnCube(show)

def isFinish():

	global d , u, f, b, r, l, uf, ur, ub, ul, df, dr, db, dl, fr, fl, br, bl , ufr, ufl, ubr, ubl, dfr, dfl, dbr, dbl
	
	if d  == 'w' and \
	u  == 'y' and \
	f  == 'r' and \
	b  == 'o' and \
	r  == 'g' and \
	l  == 'b' and \
	uf == {'u': 'y', 'd': '', 'f': 'r', 'b': '', 'r': '', 'l': ''} and \
	ur == {'u': 'y', 'd': '', 'f': '', 'b': '', 'r': 'g', 'l': ''} and \
	ub == {'u': 'y', 'd': '', 'f': '', 'b': 'o', 'r': '', 'l': ''} and \
	ul == {'u': 'y', 'd': '', 'f': '', 'b': '', 'r': '', 'l': 'b'} and \
	df == {'u': '', 'd': 'w', 'f': 'r', 'b': '', 'r': '', 'l': ''} and \
	dr == {'u': '', 'd': 'w', 'f': '', 'b': '', 'r': 'g', 'l': ''} and \
	db == {'u': '', 'd': 'w', 'f': '', 'b': 'o', 'r': '', 'l': ''} and \
	dl == {'u': '', 'd': 'w', 'f': '', 'b': '', 'r': '', 'l': 'b'} and \
	fr == {'u': '', 'd': '', 'f': 'r', 'b': '', 'r': 'g', 'l': ''} and \
	fl == {'u': '', 'd': '', 'f': 'r', 'b': '', 'r': '', 'l': 'b'} and \
	br == {'u': '', 'd': '', 'f': '', 'b': 'o', 'r': 'g', 'l': ''} and \
	bl == {'u': '', 'd': '', 'f': '', 'b': 'o', 'r': '', 'l': 'b'} and \
	ufr == {'u': 'y', 'd': '', 'f': 'r','b': '', 'r': 'g', 'l': ''} and \
	ufl == {'u': 'y', 'd': '', 'f': 'r', 'b': '', 'r': '', 'l': 'b'} and \
	ubr == {'u': 'y', 'd': '', 'f': '', 'b': 'o', 'r': 'g', 'l': ''} and \
	ubl == {'u': 'y', 'd': '', 'f': '', 'b': 'o', 'r': '', 'l': 'b'} and \
	dfr == {'u': '', 'd': 'w', 'f': 'r', 'b': '', 'r': 'g', 'l': ''} and \
	dfl == {'u': '', 'd': 'w', 'f': 'r', 'b': '', 'r': '', 'l': 'b'} and \
	dbr == {'u': '', 'd': 'w', 'f': '', 'b': 'o', 'r': 'g', 'l': ''} and \
	dbl == {'u': '', 'd': 'w', 'f': '', 'b': 'o', 'r': '', 'l': 'b'}:

		return 1
	else : return 0



def solve2ndCrown(show=1): #魔方通用解法第三步：构建二层皇冠图

	if show == 1:
		print("\n构建下面两层:\n")
	global uf, ur, ub, ul, df, dr, db, dl, fr, fl, br, bl#12棱块
	liste = ['rg', 'go', 'ob', 'br'] #  'rg' 表示红绿，以此类推

	for i in liste: 

		if fl['f'] in i and fl['l'] in i:
			move("F", show)
			move("U", show)
			move("F'", show)
			move("U'", show)
			move("L'", show)
			move("U'", show)
			move("L", show)

		if br['b'] in i and br['r'] in i:
			turnCube(show)
			turnCube(show)
			move("F", show)
			move("U", show)
			move("F'", show)
			move("U'", show)
			move("L'", show)
			move("U'", show)
			move("L", show)
			turnCube(show)
			turnCube(show)

		if bl['b'] in i and bl['l'] in i:
			turnCube(show)
			turnCube(show)
			turnCube(show)
			move("F", show)
			move("U", show)
			move("F'", show)
			move("U'", show)
			move("L'", show)
			move("U'", show)
			move("L", show)
			turnCube(show)

		if fr['r'] is i[0] and fr['f'] in i:
			move("R", show)
			move("U", show)
			move("R'", show)
			move("U'", show)
			move("U'", show)
			move("R", show)
			move("U'", show)
			move("U'", show)
			move("R'", show)
			move("U", show)
			move("F'", show)
			move("U'", show)
			move("F", show)

		if uf['f'] is i[0] and uf['u'] in i:
			move("U", show)
			move("R", show)
			move("U", show)
			move("R'", show)
			move("U'", show)
			move("F'", show)
			move("U'", show)
			move("F", show)

		if uf['u'] is i[0] and uf['f'] in i:
			move("U'", show)
			move("R'", show)
			move("U'", show)
			move("R'", show)
			move("U'", show)
			move("R'", show)
			move("U", show)
			move("R", show)
			move("U", show)
			move("R", show)

		if ur['u'] is i[0] and ur['r'] in i:
			move("R'", show)
			move("U'", show)
			move("R'", show)
			move("U'", show)
			move("R'", show)
			move("U", show)
			move("R", show)
			move("U", show)
			move("R", show)

		if ur['r'] is i[0] and ur['u'] in i:
			move("U", show)
			move("U", show)
			move("R", show)
			move("U", show)
			move("R'", show)
			move("U'", show)
			move("F'", show)
			move("U'", show)
			move("F", show)

		if ub['b'] is i[0] and ub['u'] in i:
			move("U'", show)
			move("R", show)
			move("U", show)
			move("R'", show)
			move("U'", show)
			move("F'", show)
			move("U'", show)
			move("F", show)

		if ub['u'] is i[0] and ub['b'] in i:
			move("U", show)
			move("R'", show)
			move("U'", show)
			move("R'", show)
			move("U'", show)
			move("R'", show)
			move("U", show)
			move("R", show)
			move("U", show)
			move("R", show)

		if ul['l'] is i[0] and ul['u'] in i:
			move("R", show)
			move("U", show)
			move("R'", show)
			move("U'", show)
			move("F'", show)
			move("U'", show)
			move("F", show)

		if ul['u'] is i[0] and ul['l'] in i:
			move("U", show)
			move("U", show)
			move("R'", show)
			move("U'", show)
			move("R'", show)
			move("U'", show)
			move("R'", show)
			move("U", show)
			move("R", show)
			move("U", show)
			move("R", show)

		if fr['f'] is i[0] and fr['r'] in i and show == 1:
			print("棱对正")

		turnCube(show)



def solveYellowCross(show=1): #魔方通用解法第四步：构建黄十字
	if show == 1:
		print("\n构建顶面黄十字:\n")

	global uf, ur, ub, ul

	if uf['u'] != 'y' and ur['u'] != 'y' and ub['u'] != 'y' and ul['u'] != 'y': # 转动使得４个棱块的顶部为黄色
		move("R'", show)
		move("U'", show)
		move("F'", show)
		move("U", show)
		move("F", show)
		move("R", show)

	if uf['u'] != 'y' and  ub['u'] != 'y' and ur['u'] == 'y' and ul['u'] == 'y': # 转动使得４个棱块的顶部为黄色
		move("R'", show)
		move("U'", show)
		move("F'", show)
		move("U", show)
		move("F", show)
		move("R", show)

	if ur['u'] != 'y' and  ul['u'] != 'y' and uf['u'] == 'y' and ub['u'] == 'y':# 转动使得４个棱块的顶部为黄色
		move("U", show)  
		move("R'", show)
		move("U'", show)
		move("F'", show)
		move("U", show)
		move("F", show)
		move("R", show)

	if uf['u'] != 'y' and ur['u'] != 'y' and ub['u'] == 'y' and ul['u'] == 'y': # 转动使得４个棱块的顶部为黄色
		move("R'", show)
		move("U'", show)
		move("F'", show)
		move("U", show)
		move("F", show)
		move("R", show)

	if uf['u'] != 'y' and ur['u'] == 'y' and ub['u'] == 'y' and ul['u'] != 'y': # 转动使得４个棱块的顶部为黄色
		move("U'", show) 
		move("R'", show)
		move("U'", show)
		move("F'", show)
		move("U", show)
		move("F", show)
		move("R", show)

	if uf['u'] == 'y' and ur['u'] == 'y' and ub['u'] != 'y' and ul['u'] != 'y': # 转动使得４个棱块的顶部为黄色
		move("U", show)	
		move("U", show)	
		move("R'", show)
		move("U'", show)
		move("F'", show)
		move("U", show)
		move("F", show)
		move("R", show)

	if uf['u'] == 'y' and ur['u'] != 'y' and ub['u'] != 'y' and ul['u'] == 'y': # 转动使得４个棱块的顶部为黄色
		move("U", show)	
		move("R'", show)
		move("U'", show)
		move("F'", show)
		move("U", show)
		move("F", show)
		move("R", show)

	# 构建十字

	#颜色判断
	loop = 1 # 1表示颜色正确，0表示颜色不正确
	while loop: 
			if uf['f'] == 'r' and ur['r'] == 'g':
				move("U", show)
				move("U", show)

			elif ul['l'] == 'r' and uf['f'] == 'g':
				move("U", show)

			elif ur['r'] == 'r' and ub['b'] == 'g':
				move("U'", show)

			if uf['f'] == 'g' and ur['r'] == 'o':
				move("U", show)
				move("U", show)

			elif ul['l'] == 'g' and uf['f'] == 'o':
				move("U", show)

			elif ur['r'] == 'g' and ub['b'] == 'o':
				move("U'", show)

			if uf['f'] == 'o' and ur['r'] == 'b':
				move("U", show)
				move("U", show)

			elif ul['l'] == 'o' and uf['f'] == 'b':
				move("U", show)

			elif ur['r'] == 'o' and ub['b'] == 'b':
				move("U'", show)

			if uf['f'] == 'b' and ur['r'] == 'r':
				move("U", show)
				move("U", show)

			elif ul['l'] == 'b' and uf['f'] == 'r':
				move("U", show)

			elif ur['r'] == 'b' and ub['b'] == 'r':
				move("U'", show)

			# 魔方公式套路
			move("U", show)
			move("R", show)
			move("U", show)
			move("R'", show)
			move("U", show)
			move("R", show)
			move("U", show)
			move("U", show)
			move("R'", show)

			#通过顶部旋转匹配
			if ul['l'] == 'r' and uf['f'] == 'g' and ur['r'] == 'o' and ub['b'] == 'b':
				move("U'", show)
			if ul['l'] == 'o' and uf['f'] == 'b' and ur['r'] == 'r' and ub['b'] == 'g':
				move("U", show)
			if ul['l'] == 'g' and uf['f'] == 'o' and ur['r'] == 'b' and ub['b'] == 'r':
				move("U", show)
				move("U", show)
			if ul['l'] == 'b' and uf['f'] == 'r' and ur['r'] == 'g' and ub['b'] == 'o':
				loop = 0 # 十字和颜色都正确就退出



def solveFinal(show=1): #魔方公式最后一步：放置好黄色角块
	if show == 1:
		print("\n放置好黄色角块:\n")

	while 1: 

		if  ('r' in ufr.values() and 'g' in ufr.values()) and \
			('b' in ufl.values() and 'r' in ufl.values()) and \
			('g' in ubr.values() and 'o' in ubr.values()) and \
			('b' in ubl.values() and 'o' in ubl.values()):
				break 
		if 'g' in ubr.values() and 'o' in ubr.values(): # 如果上后右角块包含绿或黄
			move("U", show)
			move("U", show)
			move("R", show)
			move("U'", show)
			move("L'", show)
			move("U", show)
			move("R'", show)
			move("U'", show)
			move("L", show)
			move("U'", show)

		elif 'r' in ufr.values() and 'g' in ufr.values():# 如果上前右角块包含红或绿
			move("U", show)
			move("R", show)
			move("U'", show)
			move("L'", show)
			move("U", show)
			move("R'", show)
			move("U'", show)
			move("L", show)

		elif 'b' in ubl.values() and 'o' in ubl.values():# 如果前后右角块包含绿或黄
			move("U'", show)
			move("R", show)
			move("U'", show)
			move("L'", show)
			move("U", show)
			move("R'", show)
			move("U'", show)
			move("L", show)
			move("U", show)
			move("U", show)

		elif 'b' in ufl.values() and 'r' in ufl.values():# 如果上前左角块包含蓝或红
			move("R", show)
			move("U'", show)
			move("L'", show)
			move("U", show)
			move("R'", show)
			move("U'", show)
			move("L", show)
			move("U", show)

		else: # 如无上述对应
			move("U", show)
			move("R", show)
			move("U'", show)
			move("L'", show)
			move("U", show)
			move("R'", show)
			move("U'", show)
			move("L", show)

	while 1:
		if ufr['u'] == 'y': # 如果上前右角块的上面是黄色
			if isFinish(): 
				break 

			move("U'", show) # 去下一块处理

		if ufr['r'] == 'y': # 如果右部角块为黄色
			move("R'", show)
			move("D'", show)
			move("R", show)
			move("D", show)

			move("R'", show)
			move("D'", show)
			move("R", show)
			move("D", show)

		if ufr['f'] == 'y': # 如果前面角块为黄色

			move("R'", show)
			move("D'", show)
			move("R", show)
			move("D", show)

			move("R'", show)
			move("D'", show)
			move("R", show)
			move("D", show)

			move("R'", show)
			move("D'", show)
			move("R", show)
			move("D", show)

			move("R'", show)
			move("D'", show)
			move("R", show)
			move("D", show)


##### 打乱魔方 #####
print("打乱魔方:\n")
melanger() 
printCube() 
print("随机打乱魔方完成!\n")
sleep(3) 


##### 求解基本步骤 #####

if isFinish(): 
	print("执行完成" + str(moveNbr) + " 步!")
	quit()

solveWhiteCross() # 白色十字

if isFinish(): 
	print("执行完成" + str(moveNbr) + " 步!")
	quit()

solveWhiteCorner() # 白色角块

printCube() 

if isFinish(): 
	print("执行完成" + str(moveNbr) + " 步!")
	quit()

solve2ndCrown() # 底部二层

printCube() 

if isFinish(): 
	print("执行完成" + str(moveNbr) + " 步!")
	quit()

solveYellowCross() # 黄十字

printCube() 
if isFinish(): 
	print("执行完成" + str(moveNbr) + " 步!")
	quit()

solveFinal() # 最后一层

printCube() 

if isFinish(): 
	print("执行完成" + str(moveNbr) + " 步!")
	quit()

printCube() 


### 统计测试 ###
#nope = 0
#moveNbrStat = []
#y = 10000
#for x in range (y):
# resetCube ()
# moveNbr = 0
#mix (25, 0)
# solveWhiteCross (0)
# solveWhiteCorner (0)
# solve2ndCrown (0)
# solveYellowCross (0)
# solveFinal (0)
# if not isFinish ():
# print "error"
# moveNbrStat.append (moveNbr)
# #printCube ()
#print (str (y) + "魔方解出的平均步骤为" + str (sum (moveNbrStat) / len (moveNbrStat)))