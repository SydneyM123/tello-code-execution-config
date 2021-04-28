import subprocess
import os

working_directory = os.getcwd()

os.chdir("./public")

subprocess.run(["git", "fetch"])

result = subprocess.run(["git", "diff", "--name-only", "master..remotes/origin/master", "--", "***.py"], stdout=subprocess.PIPE)

print("Changed files: ")
diff = result.stdout.decode("utf-8")

subprocess.run(["git", "pull", "origin", "master"])

os.chdir(working_directory)
