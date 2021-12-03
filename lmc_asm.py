from sys import argv

commands = {
		"add": 1000,
		"sub": 2000,
		"sta": 3000,
		"lda": 5000,
		"bra": 6000,
		"brz": 7000,
		"brp": 8000,
		"inp": 9001,
		"out": 9002,
		"dat": 0,
		"hlt": 0,
		}
nomem_cmds = ["inp","out","hlt"]
output = []

class NoMemGiven(Exception):
	def __str__(self):
		return repr(self.value)

if (len(argv) > 2):
	try:
		f = open(argv[1], "r")
	except:
		print "Error, file", argv[1], "could not be opened"
		exit(1)

	for line in f: 
		line = line.strip()
		if line == "":
			continue
		if line[0] == ";":
			continue
		cmds = line.split(" ")

		try:
			cmd = cmds[0].lower()
			if len(cmds) > 1:
				mem = int(cmds[1])
				if mem > 999:
					raise ValueError
				output.append(str(commands[cmd] + mem))
			else:
				if cmd in nomem_cmds:
					output.append(str(commands[cmd]))
				else:
					raise NoMemGiven
		except KeyError, e:
			print "No such command '%s' in line: %s" % (cmd, line)

			exit(1)
		except NoMemGiven:
			print "Command '%s' needs memory address in line: %s" % (cmd, line)
			exit(1)
		except ValueError:
			print "Incorrect memory address in line: %s" % (line)
			exit(1)

	try:
		o = open(argv[2], "w")
		o.write(' '.join(output))
	except Exception, e:
		print "Couldn't open file %s" % argv[2]
		print e

else:
	print "Usage:", argv[0], "<file to assemble> <output>"
	exit(2)
