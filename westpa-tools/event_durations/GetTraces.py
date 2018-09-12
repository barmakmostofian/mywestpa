import sys
import os
import h5py


MinIter = int(sys.argv[1])
MaxIter = int(sys.argv[2])
TargetBinVal = float(sys.argv[3])

DataIn = h5py.File("./west.h5", 'r')

CWD = os.getcwd()
os.mkdir("Traces")
os.chdir("Traces")


TraceIter = []
TraceSeg  = []

for i in range(MinIter,MaxIter+1) :
   ITER = "{0:08}".format(i)
   SegNum = int(DataIn["/iterations/iter_"+ITER+"/pcoord"].shape[0])

   for j in range(SegNum) :
      if float(DataIn["/iterations/iter_"+ITER+"/pcoord"].value[j][1]) < TargetBinVal :
          TraceCommand = "w_trace -W ../west.h5 "+str(i)+":"+str(j)+" -o trajs_"+str(i)+":"+str(j)+".h5"
          os.system(TraceCommand)


os.chdir(CWD)


