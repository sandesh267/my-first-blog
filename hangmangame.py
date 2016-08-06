
import hangman, time
print """
			Folks! Seeing the - lines 
			Now what you have to do !!!!!
			
			 YOU WILL WIN A FRENCH KISS  """
ans = raw_input("Wanna play game ??? preass Y or N  : ")

def play():
	print """Yuhuuu!!!!!!
			Be ready now ! Start guessing 
			Guess the word and win a KISS  
			
			
			"""
	pname = raw_input("Tell me your name : ")
	life  = 10
	print "{} ! You have {} lifes".format(pname,life)
	rand_word = hangman.getword()
	length = len(rand_word)
	
	listis = list('-'*length)
	for i in listis:
		print i, 
	count = 0
	while life > 0 :
		chr = raw_input(" \nenter the letter (between a-z): ")
		indices = hangman.getindices(rand_word,chr)
		if chr in rand_word :
			for a in indices :
				listis[a] = chr
			for i in listis:
				print i,
			count += 1
		else :
			life = life-1
			print "\n{}! what you doing ! lost a life 		Life balance : {}".format(pname, life)
		
		if count == length-4 :
			print "\n\nWell Done {} ! you are doing a great job ! I am feeling nervous you are about to kiss me ".format(pname)
			print '''
					_____Sexy?Sex
					____?Sexy?Sexy
					___y?Sexy?Sexy?
					___?Sexy?Sexy?S
					___?Sexy?Sexy?S
					__?Sexy?Sexy?Se
					_?Sexy?Sexy?Se
					_?Sexy?Sexy?Se
					_?Sexy?Sexy?Sexy?
					?Sexy?Sexy?Sexy?Sexy
					?Sexy?Sexy?Sexy?Sexy?Se
					?Sexy?Sexy?Sexy?Sexy?Sex
					_?Sexy?__?Sexy?Sexy?Sex
					___?Sex____?Sexy?Sexy?
					___?Sex_____?Sexy?Sexy
					___?Sex_____?Sexy?Sexy
					____?Sex____?Sexy?Sexy
					_____?Se____?Sexy?Sex
					______?Se__?Sexy?Sexy
					_______?Sexy?Sexy?Sex'''
		if listis == list(rand_word):
			print """Dude ! Hurrey
						lllll-------------------lllll
						lllll-------------------lllll
						lllll--------0000-------lllll
						lllll-----000---000-----lllll
						lllll-----000---000-----lllll
						lllll-----000---000-----lllll
						lllll--------0000-------lllll
						lllllllllllllllllll-----lllllllllllllllllll 
						lllllllllllllllllll-----lllllllllllllllllll
						
						This is my way of kissing 
						"""
			break
		
	if life == 0 :
			print "game over dude ! Try again :-)"
			print """
						....................../-/) 
						....................,/.//
						.................../..// 
						............./'-/'...'//---' 
						........../'/.../..../....//--\ 
						........('(...'...'.... --~/'...') 
						.........\.................'...../ 
						..........''...\.......... _.'' 
						............\..............( 
						..............\.............\..."""
if ans == 'Y' :
	play()
else :
	print "Hey ! you made me sad !!! "
					
			
