import subprocess

Hi = "Empires SMP"
useless_cat_call = subprocess.run(["ddgr"], stdout=subprocess.PIPE, text=True, input=Hi,shell=True)
print(useless_cat_call.stdout)