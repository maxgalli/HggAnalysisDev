import os

maindir="/hadoop/cms/store/user/hmei/nanoaod_runII/HHggtautau/"

#print os.listdir(maindir)

mc16={}
mc17={}
mc18={}
data16={}
data17={}
data18={}

allsamples=[]

for subdir in os.listdir(maindir):
  myfiles=os.listdir(maindir+subdir)
  print myfiles[0:1], len(myfiles), maindir+subdir
  if "EGamma_Run2018" in subdir:
    data18[subdir]=maindir+subdir
    allsamples.append(subdir)
    print "data18"
  elif "DoubleEG_Run2017" in subdir:
    data17[subdir]=maindir+subdir
    allsamples.append(subdir)
    print "data17"
  elif "DoubleEG_Run2016" in subdir:
    data16[subdir]=maindir+subdir
    allsamples.append(subdir)
    print "data16"
  elif "Autumn18" in subdir or "Era2018" in subdir:
    mc18[subdir]=maindir+subdir
    allsamples.append(subdir)
    print "mc18"
  elif "Fall17" in subdir or "Era2017" in subdir:
    mc17[subdir]=maindir+subdir
    allsamples.append(subdir)
    print "mc17"
  elif "Summer16" in subdir or "Era2016" in subdir:
    if "20201021" in subdir:
      continue
    mc16[subdir]=maindir+subdir
    allsamples.append(subdir)
    print "mc16"
  else:
    print "BO"
    quit()

print len(mc16), len(mc17), len(mc18), len(data16), len(data17), len(data18)
print len(allsamples)

with open("sa.py", "w") as f:
  
  f.write("mc16={\n")
  keys=sorted(mc16.keys())
  for k in keys:
    f.write("'"+k+"':'"+mc16[k]+"',\n")
  f.write("}\n")

  f.write("mc17={\n")
  keys=sorted(mc17.keys())
  for k in keys:
    f.write("'"+k+"':'"+mc17[k]+"',\n")
  f.write("}\n")  

  f.write("mc18={\n")
  keys=sorted(mc18.keys())
  for k in keys:
    f.write("'"+k+"':'"+mc18[k]+"',\n")
  f.write("}\n")  

  f.write("data16={\n")
  keys=sorted(data16.keys())
  for k in keys:
    f.write("'"+k+"':'"+data16[k]+"',\n")
  f.write("}\n")  

  f.write("data17={\n")
  keys=sorted(data17.keys())
  for k in keys:
    f.write("'"+k+"':'"+data17[k]+"',\n")
  f.write("}\n")  

  f.write("data18={\n")
  keys=sorted(data18.keys())
  for k in keys:
    f.write("'"+k+"':'"+data18[k]+"',\n")
  f.write("}\n")  
    
with open("allsamples.py", "w") as f:
  f.write("allsamples=[\n")
  for k in sorted(allsamples):
    f.write("'"+k+"',\n")
  f.write("]\n")  
