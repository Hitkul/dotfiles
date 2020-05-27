
from subprocess import check_output

items = check_output("gcalcli --refresh remind 30 'echo %s'", shell=True).rstrip()
items = items.split("\n")
if len(items)>1:
    st = items[0]+" | "+items[1]
elif items[0]=='':
    st = "Nothing Upcoming"
else:
    st = items[0]
print(st)
