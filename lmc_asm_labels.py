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
labels = {}
output = []
MAXMEM = 1000

def handle_commands(cmdline):
	if not cmdline[0] in commands.keys():
		print "Error, unknown command %s" % cmdline[0]
		print "Line was: %s", ' '.join(cmdline)
		exit(1)
	if len(cmdline) > 1:
		try:
			mem = int(cmdline[1])
			if mem > MAXMEM - 1:
				raise ValueError
		except ValueError:
			print "Error, invalid memory address %s" % cmdline[1]
	else:
		if cmdline[0] in nomem_cmds:
			pass
		else:
			print "Error, command %s needs memory address" % cmdline[0]
			exit(1)
	print cmdline
	
f = ""
if (len(argv) > 2):
	try:
		f = open(argv[1], "r")
	except:
		print "Error, file", argv[1], "could not be opened"
		exit(1)

for line in f:
	line = line.strip()
	cmds = line.split(" ")
	print cmds

	if not cmds[0].lower() in commands.keys():
		output.append(handle_label(cmds))
		continue
	else:
		cmds[0] = cmds[0].lower()
		output.append(handle_command(cmds))
