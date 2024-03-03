

import numpy as np
import sys
import os
import utils

DATA_DIR = "data"
# loading data: file_list, vertex, mean, std
#def obj2npy(label="male"):
#    
#  OBJ_DIR = os.path.join(DATA_DIR, "obj")
#  
#  obj_file_dir = os.path.join(OBJ_DIR, label)
##  print("File directory = ",obj_file_dir)
#  file_list = os.listdir(obj_file_dir)
#
#  # load original data
#  vertex = []
#  for i, obj in enumerate(file_list):
#    sys.stdout.write('\r>> Converting %s body %d\n'%(label, i))
#    sys.stdout.flush()
#    f = open(os.path.join(obj_file_dir, obj), 'r')
#    j = 0
#    for line in f:
#      if line[0] == '#':
#        continue
#      elif "v " in line:
#        line.replace('\n', ' ')
#        tmp = list(map(float, line[1:].split()))
#        vertex.append(tmp)
#        j += 1
#      else:
#        break
# 
#  vertex = np.array(vertex).reshape(len(file_list), utils.V_NUM, 3)#utils.V_NUM
##  print("Vertex are of type = ",type(vertex)) 
##  print("vertex = ",vertex)
#
#  return vertex


        
 
# read control  points(CP) from text file
def convert_cp():
    
  f = open(os.path.join(DATA_DIR, 'customBodyPoints.txt'), "r")

  tmplist = []
  cp = []
  for line in f:
    if '#' in line:
      if len(tmplist) != 0:
        cp.append(tmplist)
        tmplist = []
    elif len(line.split()) == 1:
      continue
    else:
      tmplist.append(list(map(float, line.strip().split())))
  cp.append(tmplist)


  return cp


# calculate measure data from given vertex by control points
def calc_measure(cp, vertex,height):#, facet):
  measure_list = []
  
  for measure in cp:
#    print("#########################",measure)  
#    print("@@@@@@@@@@@@")

    length = 0.0
    p2 = vertex[int(measure[0][1]), :]

    for i in range(0, len(measure)):#1
      p1 = p2
      if measure[i][0] == 1:
        p2 = vertex[int(measure[i][1]), :]  
        
      elif measure[i][0] == 2:
        p2 = vertex[int(measure[i][1]), :] * measure[i][3] + \
        vertex[int(measure[i][2]), :] * measure[i][4]
#        print("if 2 Measurement",int(measure[i][1]))
        
      else:
        p2 = vertex[int(measure[i][1]), :] * measure[i][4] + \
          vertex[int(measure[i][2]), :] * measure[i][5] + \
          vertex[int(measure[i][3]), :] * measure[i][6]
      length += np.sqrt(np.sum((p1 - p2)**2.0))

    measure_list.append(length * 100)# * 1000
  
  measure_list = float(height)*(measure_list/measure_list[0])
  #print("measure list = ",float(height)*(measure_list/measure_list[0])) 
  measure_list[8] = measure_list[8] * 0.36#reducing the error in measurement added due to unarranged vertices
  measure_list[3] = measure_list[3] * 0.6927
#  print("measure list = ",float(height)*(measure_list/measure_list[0]))
#  measure_list = float(height)*(measure_list/measure_list[0])
  return np.array(measure_list).reshape(utils.M_NUM, 1)


##added code: extract body measurements given a .obj model in data.
def extract_measurements(height, vertices,sex):
  genders = [sex]
  measure = []
  for gender in genders:
    # generate and load control point from txt to npy file
    cp = convert_cp()

#    vertex = obj2npy(gender)[0]
    #calculte + convert
    measure = calc_measure(cp, vertices, height)

    # Round up measurements
    measure = np.around(measure, decimals=2)  # Round to 2 decimal places


    #give body measurements one by one
    for i in range(0, utils.M_NUM):
      print("%s: %.2f" % (utils.M_STR[i], measure[i]))


    face_path = './src/tf_smpl/smpl_faces.npy'
    faces = np.load(face_path)
    obj_mesh_name = 'test.obj'
    with open(obj_mesh_name, 'w') as fp:
        for v in vertices:
            fp.write( 'v %f %f %f\n' % ( v[0], v[1], v[2]) )
        for f in faces: # Faces are 1-based, not 0-based in obj files
            fp.write( 'f %d %d %d\n' %  (f[0] + 1, f[1] + 1, f[2] + 1) )

        
    print("Model Saved...")

    
    waist = np.round(measure[1])
    chest = np.round(measure[3])
    shoulder_width = np.round(measure[8])
    hips = np.round(measure[9])

    print(waist)
    print(chest)
       
    if hips / shoulder_width < 0.95 or hips / chest < 0.95:
      print("Body Shape: Inverted Triangle")
    elif hips/shoulder_width > 1.05 and hips/chest > 1.05:
      print("Body Shape: Pear")
    elif hips == chest == shoulder_width:
      print("Body Shape: Athletic")
    elif chest > waist and chest > hips and waist / chest < 0.75 and hips / chest > 0.75:
      print("Body Shape: Hourglass")
    elif hips <= shoulder_width * 1.05 and hips <= chest * 1.05:
      print("Body Shape: Rectangle")
    elif hips * 1.05 < chest:
        print("Body Shape: Apple")
    elif hips > chest and hips > shoulder_width:
      print("Body Shape: Spoon")   
    elif hips > shoulder_width and waist > chest:
      print("Body Shape: Diamond")

    if sex == "male":
      if chest >= 86 and chest <=91 and waist >=71 and waist <=76:
        print("Size: S")
      elif chest >= 91 and chest <=96 and waist >=76 and waist <=80:
        print("Size: S")
      elif chest >= 96 and chest <=101 and waist >=80 and waist <=86:
        print("Size: M")
      elif chest >= 101 and chest <=106 and waist >=86 and waist <=91:
        print("Size: L") 
      elif chest >=106 and chest <=111 and waist >=91 and waist <=96:
        print("Size: XL")
      elif chest >= 111 and chest <=117 and waist >=96 and waist <=106:
        print("Size: XXL")
      elif chest >= 119 and chest <=126 and waist >=106 and waist <=113:
        print("Size: XXXL")
      else:
        print("Unknown")

    elif sex == "female":
      if chest >= 81 and chest <=84 and waist >=63 and waist <=66:
        print("Size: XS")
      elif chest >=85 and chest <=88 and waist >=67 and waist <=70:
        print("Size: S") 
      elif chest >=89 and chest <=92 and waist >=71 and waist <=74:
        print("Size: M")   
      elif chest >=93 and chest <=97 and waist >=75 and waist <=78:
        print("Size: L")  
      elif chest >=98 and chest <=103 and waist >=79 and waist <=83:
        print("Size: XL")  
      elif chest >=104 and chest <=110 and waist >=84 and waist <=88:
        print("Size: XXL")
      elif chest >=111 and chest <=118 and waist >=89 and waist <=94:
        print("Size: XXXL")
      else:
        print("") 


#if __name__ == "__main__":
#  extract_measurements()
  
