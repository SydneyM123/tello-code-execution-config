import subprocess
import os

working_directory = os.getcwd()

os.chdir("./public")

subprocess.run(["git", "fetch"])

# result = subprocess.run(["git", "diff", "--name-only", "master..remotes/origin/master", "--", "***.py"], stdout=subprocess.PIPE)
# diff = result.stdout.decode("utf-8")

# print("Changed files: ")
# print(diff)

subprocess.run(["git", "pull", "master", "master"])

os.chdir(working_directory)
