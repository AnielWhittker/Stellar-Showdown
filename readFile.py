import csv


# class that curenctly can store the star id,  distance, and temperature of the star, also makes the conversions to kelvin and light-years
class Star:

  def __init__(self, star_id, distance, temperature):
    self.star_id = star_id
    self.distance = float(distance) * 3.262
    self.temperature = 4600 * ((1 / (0.92 * float(temperature) + 1.7)) +
                               (1 / (0.92 * float(temperature) + 0.62)))


list = []
# reads the csv file and stores the temperature and distance on a star object in the list
with open("hygxyz.csv", "r") as file:
  reader = csv.reader(file)
  next(reader)
  for line in reader:
    # this is for data validation for if the color index is empty
    if line[16] == "":
      line[16] = 0
    star = Star(line[0], line[9], line[16])
    list.append(star)

print(len(list))
