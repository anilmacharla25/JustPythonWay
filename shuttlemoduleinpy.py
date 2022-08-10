#moving files from one loction to other location
import shutil 
path="C:\\Users\\AM\\Desktop\\my_folder1\\clickhere2.PNG"
dest="‪C:\\Users\\AM\\Desktop\\1"
path=path.strip("‪u202a")
dest=dest.strip("‪u202a")
shutil.move(path,dest)
