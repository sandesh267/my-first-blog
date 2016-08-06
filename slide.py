
a = [1,2,3,4,5,6,7,8,0]
while True :
	print a[0],a[1],a[2], '\n', a[3],a[4],a[5], '\n',a[6],a[7],a[8]
	mov = int(raw_input('Enter the number to replace zero : '))
	pos_zero = a.index(0)
	pos_mov  = a.index(mov)
	if (((pos_zero == 0) and ((pos_mov == 1) or (pos_mov == 3))) or 
	 ((pos_zero == 1) and ((pos_mov == 0) or (pos_mov == 2)  or (pos_mov == 4))) or 
	 ((pos_zero == 2) and ((pos_mov == 1) or (pos_mov == 5))) or 
	 ((pos_zero == 3) and ((pos_mov == 0) or (pos_mov == 4)  or (pos_mov == 6))) or
	 ((pos_zero == 4) and ((pos_mov == 1) or (pos_mov == 3)  or (pos_mov == 7) or (pos_mov == 7))) or
	 ((pos_zero == 5) and ((pos_mov == 2) or (pos_mov == 4)  or (pos_mov == 8))) or
	 ((pos_zero == 6) and ((pos_mov == 3) or (pos_mov == 7))) or
	 ((pos_zero == 7) and ((pos_mov == 4) or (pos_mov == 6) or (pos_mov == 8))) or
	 ((pos_zero == 8) and ((pos_mov == 5) or (pos_mov == 7)))) : 
		a[pos_zero], a[pos_mov] = a[pos_mov], a[pos_zero]

	else :
		continue