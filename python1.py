
##https://raw.githubusercontent.com/racaljk/hosts/master/hosts
#0 准备工作:从github 获取更新的host文件 保存到githost
import requests
res = requests.get("https://raw.githubusercontent.com/racaljk/hosts/master/hosts")
savefile = open("githost","wb")
savefile.write(res.content)
savefile.close() 
print ("[status]:"+"get host from github finished !! "  +"(https://raw.githubusercontent.com/racaljk/hosts/master/hosts)")

#1 从本地host文件中截取前半部分内容
import os
# desk = "C:\\Users\\chen\\Desktop"
# temppath = os.path.join(desk,"temp")
temp = open("temp",'w')
file = open("host")
ant = "# Modified hosts start"

while 1:
    line = file.readline()

    if ant in line:
        print("[status]:"+"put first part to temp")
        break
        pass
    temp.write(line)
    if not line:
        break
    pass # do something
file.close()
temp.close()

#2 将githost文件中start 和end 中间部分内容追加到temp后面

#1. 按行读取文件(截取star和end中间部分内容)
start = "# Modified hosts start"
end = "# Modified hosts end"
file = open("githost")
flag = 0

temp = open("temp",'a+')
timetap = "# Last updated:"
update = ""
while 1:
    line = file.readline()

    if timetap in line: #保存更新时间
    	update = line.replace(timetap,"Last updated").replace("\n","")
    	# temp.write(line)
    	pass
    if start in line:#设置标记位 词行以后所有内容都追加到temp 中
    	flag = 1
    	pass

    if flag == 1:
    	temp.write(line)
    	pass
    if not line:
        break
    pass # do something
file.close()
temp.close()
print("[status]:"+"add new host part to temp")
print("[status]:"+update)


# 3. 删除老的文件 host  将temp 命名为 host
pwd = os.getcwd()
githost_path = os.path.join(pwd,"githost")
os.remove(githost_path)
host_path = os.path.join(pwd,"host")
# os.remove(host_path)

temp_path = os.path.join(pwd,"temp")

# host_path = os.path.join(pwd,"host")
os.remove(host_path)
os.rename(temp_path,host_path)

print("[status]:"+"udpate host successfull>>"+host_path)
