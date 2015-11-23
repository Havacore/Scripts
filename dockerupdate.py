from subprocess import Popen, PIPE
import re

def main():
	p1 = Popen(["docker", "ps"], stdout=PIPE)
	i = 0
	containerId = ""
	for line in p1.stdout:
		if i is 1:
			containerId = line
		i += 1

	containerId = containerId[:12]

	Popen(["docker", "build", "-t", "ws-proxy", "."])
	Popen(["docker", "kill", containerId], stdout=PIPE)
	p2 = Popen(["docker", "run", "-d", "-p", "80:80", "ws-proxy"], stdout=PIPE)
	for line in p2.stdout:
		new_process = line
	print new_process

	Popen(["docker", "logs", "-f", new_process], stdout=PIPE)

if __name__ == "__main__":
    main()
