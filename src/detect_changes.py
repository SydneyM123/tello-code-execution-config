import subprocess
import os


working_directory = os.getcwd()

os.chdir("./public")

subprocess.run(["git", "fetch"])

print("Changed Python files: ")
result = subprocess.run(["git", "diff", "--name-only", "master..remotes/origin/master", "--", "***.py"], stdout=subprocess.PIPE)
print(result.stdout.decode("utf-8"))

subprocess.run(["git", "pull", "origin", "master"])

os.chdir(working_directory)
