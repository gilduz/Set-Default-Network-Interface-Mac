import subprocess
import copy
import StringIO

commandList = "networksetup -listnetworkserviceorder"
commandSet = "sudo networksetup -ordernetworkservices "

outputList = subprocess.Popen(commandList, shell=True, stdout=subprocess.PIPE).stdout.read()

s = StringIO.StringIO(outputList)

devicesList = []
newDeviceOrder = []

for idx, line in enumerate(s):
    if line[0] == '(' and line[2] == ')':
        devicesList.append(line[4:-1])

print "Current Default Adapter: " + devicesList[0]
for idx, device in enumerate(devicesList):
    print '[' + str(idx) + '] ' + device

selection = input("Set default adapter: ")
selectedID = int(selection)

newDeviceOrder = copy.deepcopy(devicesList)

newDeviceOrder[0] = devicesList[selectedID]
newDeviceOrder[selectedID] = devicesList[0]

for idx, device in enumerate(newDeviceOrder):
    commandSet += '"' + device + '" '

outputSet = subprocess.Popen(commandSet, shell=True, stdout=subprocess.PIPE).stdout.read()
