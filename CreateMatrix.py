import math
def CreateMatrix(filename):
  def _EucDist(x1, y1, x2, y2):
    x_sq = (x1 - x2) * (x1 - x2) 
    y_sq = (y1 - y2) * (y1 - y2)
    dist = math.sqrt(x_sq + y_sq)
    return dist

  file = open(filename)
  x_coords = []
  y_coords = []
  mat = []
  for i in file:
    line_num, x_coord, y_coord = i.split(" ")
    x_coords.append(x_coord)
    y_coords.append(y_coord)
  for i in range(len(x_coords)):
    line_mat = []
    for j in range(len(x_coords)):
      dist = _EucDist(int(x_coords[i]), int(y_coords[i]), int(x_coords[j]), int(y_coords[j]))
      line_mat.append(dist)
    mat.append(line_mat)
  return mat