from sys import argv

memory = 1000 * [0]
inbox = ""
outbox = ""
accumulator = 0
prog_counter = 0
operation = ["", 0]
neg_flag = False

def get_op(value):
	op = value / 1000
	mem = value % 1000
	
	operations = [
			["hlt", -1],
			["add", mem],
			["sub", mem],
			["sta", mem],
			["", -1],
			["lda", mem],
			["bra", mem],
			["brz", mem],
			["brp", mem],
			["inp", mem],
			["out", mem]
			]

	if op == 9:
		if mem == 1:
			return ["inp", mem]
		elif mem == 2:
			return ["out", mem]
		else:
			return ["", -1]

	return operations[op]

def get_input():
	global accumulator, inbox
	accumulator = int(raw_input("INBOX: ").split(' ')[0])
	inbox = accumulator

def put_output():
	global accumulator, outbox
	print "OUTPUT:", accumulator
	output = accumulator

def exec_cycle():
	global accumulator, memory, inbox, outbox, prog_counter, operation

	while True:
		if (prog_counter > 999):
			prog_counter = prog_counter % 1000
		
		operation = get_op(memory[prog_counter])

		if operation[0] == "":
			print "Error in program at", prog_counter
			exit(1)

		prog_counter += 1

		if operation[0] == "add":
			accumulator = (accumulator + memory[operation[1]]) % 1000
		elif operation[0] == "sub":
			accumulator = (accumulator - memory[operation[1]])
			if (accumulator < 0):
				accumulator = 1000 - accumulator
				neg_flag = True
			else:
				neg_flag = False
		elif operation[0] == "sta":
			memory[operation[1]] = accumulator
		elif operation[0] == "lda":
			accumulator = memory[operation[1]]
		elif operation[0] == "inp":
			get_input()
		elif operation[0] == "out":
			put_output()
		elif operation[0] == "bra":
			prog_counter = operation[1]
		elif operation[0] == "brz":
			print "dicks"
			if accumulator == 0:
				prog_counter = operation[1]
		elif operation[0] == "brp":
			if accumulator >= 0 and not neg_flag:
				prog_counter = operation[1]
		elif operation[0] == "hlt":
			break

		neg_flag = False

		#print "mem:", memory
		#print "prog:", prog_counter
		#print "accm:", accumulator

if (len(argv) > 1):
	try:
		f = open(argv[1], "r")
	except:
		print "Error, file", argv[1], "could not be opened"
		exit(1)
	line = f.readline()
	line.strip()
	cmds = line.split(" ")
	for i in xrange(len(cmds)):
		memory[i] = int(cmds[i])
	exec_cycle()
else:
	print "Usage:", argv[0], "<memory to load>"
	print "Contents of the file are numbers corresponding to Little Man"
	print "Computer commands separated by space."
	print "Eg: 1001 1001 00"
	exit(0)
