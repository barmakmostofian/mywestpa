import sys
import re
import h5py


MinIter = int(sys.argv[1])
MaxIter = int(sys.argv[2])
TargetBinVal = float(sys.argv[3])
EventStartVal = float(sys.argv[4])
dt = float(sys.argv[5])

DataIn = h5py.File("west.h5", 'r')


TraceIter = []
TraceSeg  = []

for i in range(MinIter,MaxIter+1) :
   ITER = "{0:08}".format(i)
   SegNum = int(DataIn["/iterations/iter_"+ITER+"/pcoord"].shape[0])

   for j in range(SegNum) :
      if float(DataIn["/iterations/iter_"+ITER+"/pcoord"].value[j][1]) < TargetBinVal :
         TraceIter.append(i)
         TraceSeg.append(j)


AllTimes = []
AllWeights = []

for i in range(len(TraceIter)) :
   FileIn = open("Traces/traj_"+str(TraceIter[i])+"_"+str(TraceSeg[i])+"_trace.txt")
   for line in reversed(FileIn.readlines()):
      Words = line.rstrip().split()
      if float(Words[5]) < TargetBinVal :
         EndIter = int(Words[0])
         EndWeight = float(Words[2])
      if float(Words[5]) > EventStartVal :
         BegIter = int(Words[0]) 
         break
   AllTimes.append((EndIter-BegIter)*dt)
   AllWeights.append(EndWeight)



FileOut = open("Events_"+str(EventStartVal)+".dat", 'w')
print>>FileOut, "Event duration\t weight\n"
for i in range(len(AllTimes)) :
   print>>FileOutAll, AllTimes[i], "\t", AllWeights[i]
FileOut.close()



