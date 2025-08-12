import os
import subprocess

# os.system("ls")   exercise 1

# subprocess.run(["ls"])    exercise 2

# subprocess.run(["ls", "-l"])  exercise 3

# subprocess.run(["ls", "-l", "README.md"]) exercise 4

# exercise 5
# command = "uname"
# commandArgument = "-a"
# print(f'Gathering System Information with Command: {command} {commandArgument}')
# subprocess.run([command, commandArgument])

# exercise 6
command = "ps"
commandArgument = "-X"
print(f'Gathering System Information with Command: {command} {commandArgument}')
subprocess.run([command, commandArgument])

