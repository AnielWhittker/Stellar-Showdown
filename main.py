import streamlit as st
import time
import readFile as r
import mergeSort as ms
import selectionSort as ss
import bubbleSort as bsort
import shellSort as shs
import timSort as ts
import quickSort as qs
import heapSort as hs
import bogoSort as bogo
import bitonicSort as bitSort
import math
import sortingCodes as sc
import base64
import runAllSorts as ras

# reads the readme file and stores it in a string
with open("README.md", "r") as file:
  readme = file.read()

# takes in an imge file and sets it as the background image
def background(imageFile):
  with open(imageFile, "rb") as imageFile:
    encodedString = base64.b64encode(imageFile.read())
  st.markdown(
  f"""
  <style>
  .stApp {{
    background-image: url(data:image/{"jpg"};base64,{encodedString.decode()});
    background-size: cover
  }}
  </style>
  """,
  unsafe_allow_html=True
  )

def main():
  st.set_page_config(layout="wide")
  # list that stores the star objects
  # I used session state becuse otherwise there is no way to keep track of what has happend before
  if "sorting_list" not in st.session_state:
    st.session_state.sorting_list = r.list

  background("image.jpg") # add background image

  # title and subheader
  st.sidebar.title("Stellar Showdown")
  st.sidebar.subheader("******using the HYG Database of 120,000 Stars******")

  if 'star_range' not in st.session_state:
    st.session_state.star_range = (0, 119614)
  if 'slider_moved' not in st.session_state:
    st.session_state.slider_moved = False
  if 'input_changed' not in st.session_state:
    st.session_state.input_changed = False
  if 'pressed_run_all' not in st.session_state:
    st.session_state.pressed_run_all = False

  star_range = st.sidebar.slider(
    'adjust range of stars',
    0, 119614, st.session_state.star_range
  )

  input_range = st.sidebar.number_input(
    "manually enter range of stars", 
    min_value=0, 
    max_value=119614, 
    value=st.session_state.star_range[1],
    step=1, 
    key="range"
  )

  if star_range != st.session_state.star_range:
    st.session_state.slider_moved = True
    st.session_state.star_range = star_range
    st.session_state.input_range = star_range[1]
    input_range = star_range[1]

  if input_range != st.session_state.star_range[1]:
    st.session_state.input_changed = True
    st.session_state.star_range = (0, input_range)
    star_range = (0, input_range)

  if st.session_state.slider_moved:
    st.sidebar.write('range:', star_range)
    st.session_state.slider_moved = False
  elif st.session_state.input_changed:
    st.sidebar.write('range:', (0, input_range))
    st.session_state.input_changed = False
  else:
    st.sidebar.write('range:', star_range)


  # checks if button pressed is in the session state, 
  # if not it adds it and sets it to False, similar with sort resul
  if "button_pressed" not in st.session_state:
    st.session_state.button_pressed = False
  if "sort_result" not in st.session_state:
    st.session_state.sort_result = None

  # adds the choices buttons
  choice1 = st.sidebar.radio("Sort stars by", ["Distance from Earth", "Temperature"])
  choice2 = st.sidebar.radio("Which Sorting algorithm?",
                     ["Merge Sort", "Selection Sort", "Bubble Sort", "Shell Sort", "Quick Sort", "TimSort", "Heap Sort", 
                      "Bogo Sort", "Bitonic Sort"])
  
  # dictionary for report
  if "usedAlgorithimDist" not in st.session_state or "usedAlgorithimTemp" not in st.session_state:
    st.session_state.usedAlgorithimDist = {}
    st.session_state.usedAlgorithimTemp = {}

  # it sets button presed to True in the session state
  if st.sidebar.button("Sort"):
    st.session_state.button_pressed = True
  st.sidebar.write("(press reset before pressing sort again)")

  if "run_sortsTemp" not in st.session_state or "run_sortsDist" not in st.session_state:
    st.session_state.run_sortsTemp = {}
    st.session_state.run_sortsDist = {}
  
  listRun = r.list[0:16385]
  if st.sidebar.button("Run all sorts"):
    st.session_state.pressed_run_all = True
    st.session_state.run_sortsTemp = ras.runAllSorts(listRun, "temp")
    st.session_state.run_sortsDist = ras.runAllSorts(listRun, "distance")
  st.sidebar.write("Takes a couple minutes to run all sorts")
  
  string_temp = ""
  string_dist = ""
  if st.session_state.pressed_run_all:
    for key, value in st.session_state.run_sortsTemp.items():
      string_temp += key + " Algorithm took: " + value + " seconds" + ", sorted 16,384 stars\n"
    for key, value in st.session_state.run_sortsDist.items():
      string_dist += key + " Algorithm took: " + value + " seconds" + ", sorted 16,384 stars\n"
    st.subheader("Sort by distance, all sorts")
    st.code(string_dist)
    st.subheader("Sort by temperature, all sorts")
    st.code(string_temp)

  # if button pressed is True, it will run the sorting algorithm selected
  #  and sets the result( string of time it took) to the session state, sets button pressed to False in state
  if st.session_state.button_pressed and st.session_state.sort_result is None:
    st.session_state.sorting_list = r.list[star_range[0]:star_range[1]]
    list = st.session_state.sorting_list
    
    if choice1 == "Distance from Earth" and choice2 == "Merge Sort":
      start = time.time()
      ms.mergeSortDistance(st.session_state.sorting_list, 0, len(list) - 1)
      end = time.time()
      st.session_state.usedAlgorithimDist[choice2] = str("{:.4f}".format(end - start))
      st.session_state.sort_result = choice2 + " Algorithm took: " + str(
        "{:.4f}".format(end - start)) + " seconds"
      st.session_state.button_pressed = False

    elif choice1 == "Temperature" and choice2 == "Merge Sort":
      start = time.time()
      ms.mergeSortTemperature(st.session_state.sorting_list, 0, len(list) - 1)
      end = time.time()
      st.session_state.usedAlgorithimTemp[choice2] = str("{:.4f}".format(end - start))
      st.session_state.sort_result = choice2 + " Algorithm took: " + str(
        "{:.4f}".format(end - start)) + " seconds"
      st.session_state.button_pressed = False
    
    elif choice1 == "Distance from Earth" and choice2 == "Selection Sort":
      start = time.time()
      ss.selectionSortDist(st.session_state.sorting_list)
      end = time.time()
      st.session_state.usedAlgorithimDist[choice2] = str("{:.4f}".format(end - start))
      st.session_state.sort_result = choice2 + " Algorithm took: " + str(
        "{:.4f}".format(end - start)) + " seconds"
      st.session_state.button_pressed = False
    
    elif choice1 == "Temperature" and choice2 == "Selection Sort":
      start = time.time()
      ss.selectionSortTemp(st.session_state.sorting_list)
      end = time.time()
      st.session_state.usedAlgorithimTemp[choice2] = str("{:.4f}".format(end - start))
      st.session_state.sort_result = choice2 + " Algorithm took: " + str(
        "{:.4f}".format(end - start)) + " seconds"
      st.session_state.button_pressed = False
    
    elif choice1 == "Distance from Earth" and choice2 == "Bubble Sort":
      start = time.time()
      st.session_state.sorting_list = bsort.bubbleSortDist(st.session_state.sorting_list)
      end = time.time()
      st.session_state.usedAlgorithimDist[choice2] = str("{:.4f}".format(end - start))
      st.session_state.sort_result = choice2 + " Algorithm took: " + str(
        "{:.4f}".format(end - start)) + " seconds"
      st.session_state.button_pressed = False
    
    elif choice1 == "Temperature" and choice2 == "Bubble Sort":
      start = time.time()
      st.session_state.sorting_list = bsort.bubbleSortTemp(st.session_state.sorting_list)
      end = time.time()
      st.session_state.usedAlgorithimTemp[choice2] = str("{:.4f}".format(end - start))
      st.session_state.sort_result = choice2 + " Algorithm took: " + str(
        "{:.4f}".format(end - start)) + " seconds"
      st.session_state.button_pressed = False
    
    elif choice1 == "Distance from Earth" and choice2 == "Shell Sort":
      start = time.time()
      st.session_state.sorting_list = shs.shellSortDistance(st.session_state.sorting_list)
      end = time.time()
      st.session_state.usedAlgorithimDist[choice2] = str("{:.4f}".format(end - start))
      st.session_state.sort_result = choice2 + " Algorithm took: " + str(
        "{:.4f}".format(end - start)) + " seconds"
      st.session_state.button_pressed = False
    
    elif choice1 == "Temperature" and choice2 == "Shell Sort":
      start = time.time()
      st.session_state.sorting_list = shs.shellSortTemp(st.session_state.sorting_list)
      end = time.time()
      st.session_state.usedAlgorithimTemp[choice2] = str("{:.4f}".format(end - start))
      st.session_state.sort_result = choice2 + " Algorithm took: " + str(
        "{:.4f}".format(end - start)) + " seconds"
      st.session_state.button_pressed = False
    
    elif choice1 == "Distance from Earth" and choice2 == "Quick Sort":
      start = time.time()
      st.session_state.sorting_list = qs.quickSortDistance(st.session_state.sorting_list)
      end = time.time()
      st.session_state.usedAlgorithimDist[choice2] = str("{:.4f}".format(end - start))
      st.session_state.sort_result = choice2 + " Algorithm took: " + str(
        "{:.4f}".format(end - start)) + " seconds"
      st.session_state.button_pressed = False
    
    elif choice1 == "Temperature" and choice2 == "Quick Sort":
      start = time.time()
      st.session_state.sorting_list = qs.quickSortTemp(st.session_state.sorting_list)
      end = time.time()
      st.session_state.usedAlgorithimTemp[choice2] = str("{:.4f}".format(end - start))
      st.session_state.sort_result = choice2 + " Algorithm took: " + str(
        "{:.4f}".format(end - start)) + " seconds"
      st.session_state.button_pressed = False

    elif choice1 == "Distance from Earth" and choice2 == "TimSort":
      start = time.time()
      st.session_state.sorting_list = ts.timSortDist(st.session_state.sorting_list)
      end = time.time()
      st.session_state.usedAlgorithimDist[choice2] = str("{:.4f}".format(end - start))
      st.session_state.sort_result = choice2 + " Algorithm took: " + str(
        "{:.4f}".format(end - start)) + " seconds"
      st.session_state.button_pressed = False

    elif choice1 == "Temperature" and choice2 == "TimSort":
      start = time.time()
      st.session_state.sorting_list = ts.timSortTemp(st.session_state.sorting_list)
      end = time.time()
      st.session_state.usedAlgorithimTemp[choice2] = str("{:.4f}".format(end - start))
      st.session_state.sort_result = choice2 + " Algorithm took: " + str(
        "{:.4f}".format(end - start)) + " seconds"
      st.session_state.button_pressed = False
    
    elif choice1 == "Distance from Earth" and choice2 == "Heap Sort":
      start = time.time()
      hs.heapSortDist(st.session_state.sorting_list)
      end = time.time()
      st.session_state.usedAlgorithimDist[choice2] = str("{:.4f}".format(end - start))
      st.session_state.sort_result = choice2 + " Algorithm took: " + str(
        "{:.4f}".format(end - start)) + " seconds"
      st.session_state.button_pressed = False
    
    elif choice1 == "Temperature" and choice2 == "Heap Sort":
      start = time.time()
      hs.heapSortTemp(st.session_state.sorting_list)
      end = time.time()
      st.session_state.usedAlgorithimTemp[choice2] = str("{:.4f}".format(end - start))
      st.session_state.sort_result = choice2 + " Algorithm took: " + str(
        "{:.4f}".format(end - start)) + " seconds"
      st.session_state.button_pressed = False
    
    elif choice1 == "Distance from Earth" and choice2 == "Bogo Sort":
      start = time.time()
      st.session_state.sorting_list = bogo.bogoSortDistance(st.session_state.sorting_list)
      end = time.time()
      st.session_state.usedAlgorithimDist[choice2] = str("{:.4f}".format(end - start))
      st.session_state.sort_result = choice2 + " Algorithm took: " + str(
        "{:.4f}".format(end - start)) + " seconds"
      st.session_state.button_pressed = False
    
    elif choice1 == "Temperature" and choice2 == "Bogo Sort":
      start = time.time()
      st.session_state.sorting_list = bogo.bogoSortTemp(st.session_state.sorting_list)
      end = time.time()
      st.session_state.usedAlgorithimTemp[choice2] = str("{:.4f}".format(end - start))
      st.session_state.sort_result = choice2 + " Algorithm took: " + str(
        "{:.4f}".format(end - start)) + " seconds"
      st.session_state.button_pressed = False
    
    elif choice1 == "Distance from Earth" and choice2 == "Bitonic Sort":
      # checks if the length of the list is a power of 2
      if math.log2(len(list)) % 2 == 0:
        start = time.time()
        bitSort.bitonicSortDist(st.session_state.sorting_list, 0, len(list), 1)
        end = time.time()
        st.session_state.usedAlgorithimDist[choice2] = str("{:.4f}".format(end - start))
        st.session_state.sort_result = choice2 + " Algorithm took: " + str(
          "{:.4f}".format(end - start)) + " seconds"
        st.session_state.button_pressed = False
      else:
        st.sidebar.write("Please enter a power of 2 as the range")
        st.session_state.button_pressed = False
    
    elif choice1 == "Temperature" and choice2 == "Bitonic Sort":
      # checks if the length of the list is a power of 2
      if math.log2(len(list)) % 2 == 0:
        start = time.time()
        bitSort.bitonicSortTemp(st.session_state.sorting_list, 0, len(list), 1)
        end = time.time()

        st.session_state.usedAlgorithimTemp[choice2] = str("{:.4f}".format(end - start))
        st.session_state.sort_result = choice2 + " Algorithm took: " + str(
          "{:.4f}".format(end - start)) + " seconds"
        st.session_state.button_pressed = False
      else:
        st.sidebar.write("Please enter a power of 2 as the range")
        st.session_state.button_pressed = False

  # displays the result string and code to screen if result is not None
  if st.session_state.sort_result is not None:
    st.sidebar.write(st.session_state.sort_result)
  
  # show code of currently selected algorithm
  if st.sidebar.checkbox("Show code"):
    st.header("Python Code for " + choice2 + " Algorithm")
    if choice2 == "Merge Sort":
      st.code(sc.mergeSort, language="python")
    elif choice2 == "Selection Sort":
      st.code(sc.selectionSort, language="python")
    elif choice2 == "Bubble Sort":
      st.code(sc.bubbleSort, language="python")
    elif choice2 == "Shell Sort":
      st.code(sc.shellSort, language="python")
    elif choice2 == "Quick Sort":
      st.code(sc.quickSort, language="python")
    elif choice2 == "TimSort":
      st.code(sc.timSort, language="python")
    elif choice2 == "Heap Sort":
      st.code(sc.heapSort, language="python")
    elif choice2 == "Bogo Sort":
      st.code(sc.bogoSort, language="python")
    elif choice2 == "Bitonic Sort":
      st.code(sc.bitonicSort, language="python")
  
  # if tthe button is pressed, it will display the top 25 and bottom 26 stars in the list
  if st.sidebar.checkbox("Show stars"):
    st.header("Stars by " + choice1)
    stringStars = ""
    starsToShow = 0
    list = st.session_state.sorting_list

    if len(list) < 25:
      starsToShow = len(list)
    else:
      starsToShow = 26
    
    st.subheader("Top " + str(starsToShow-1) + " stars")

    for j in range(len(list) - 1, len(list) - starsToShow, -1):
      temperature = str("{:.5f}".format(st.session_state.sorting_list[j].temperature))
      # if the color index was empty, therfore set to 0, set to "N/A"
      if temperature == str(4600 * ((1 / 1.7) + (1 / 0.62))):
        temperature = "N/A"
      stringStars += "Star " + str(st.session_state.sorting_list[j].star_id) + ":" + " Distance from Earth, " + str("{:.5f}".format(st.session_state.sorting_list[j].distance)) + " light-years. Temperature " + temperature + " Kelvin" + "\n"
    st.code(stringStars)

    st.subheader("Bottom " + str(starsToShow) + " stars")

    stringStars = ""
    for j in range(0, starsToShow):
      temperature = str("{:.5f}".format(st.session_state.sorting_list[j].temperature))
      # if the color index was empty, therfore set to 0, set to "N/A"
      if temperature == str(4600 * ((1 / 1.7) + (1 / 0.62))):
        temperature = "N/A"
      stringStars += "Star " + str(st.session_state.sorting_list[j].star_id) + ":" + " Distance from Earth, " + str("{:.5f}".format(st.session_state.sorting_list[j].distance)) + " light-years. Temperature " + temperature + " Kelvin" + "\n"
    st.code(stringStars)
  
  # it adds the report dictionary keys and values to a string
  string_dist = ""
  if len(st.session_state.usedAlgorithimDist) > 0:
    for key, value in st.session_state.usedAlgorithimDist.items():
      string_dist += key + " Algorithm took: " + value + " seconds" + "\n"

  string_temp = ""
  if len(st.session_state.usedAlgorithimTemp) > 0:
    for key, value in st.session_state.usedAlgorithimTemp.items():
      string_temp += key + " Algorithm took: " + value + " seconds" + "\n"

  # Show the report
  if st.sidebar.checkbox("Show report"):
    if len(st.session_state.usedAlgorithimDist) == 0 and len(st.session_state.usedAlgorithimTemp) == 0:
      st.sidebar.write("No sorting has been done yet")
    else:
      st.header("Report")
      st.subheader("Sort by distance")
      st.code(string_dist)
      st.subheader("Sort by temperature")
      st.code(string_temp)

  # reset button
  if st.sidebar.button("Reset"):
    st.session_state.sort_result = None
    if "sorting_list" in st.session_state:
      del st.session_state.sorting_list
    st.session_state.pressed_run_all = False
    st.session_state.run_sortsTemp = {}
    st.session_state.run_sortsDist = {}
    st.experimental_rerun()
  
  # credits
  st.sidebar.write("---")
  st.sidebar.write("Created by: The Stellar Coders")
  st.sidebar.write("Neema Owji, Maxwell Evans, and Aniel Whittker Melian")

  # about button
  if "about" not in st.session_state:
    st.session_state.about = False
    st.session_state.text = st.empty()

  if st.sidebar.button("about"):
    st.session_state.about = not st.session_state.about

  if st.session_state.about:
    # Add text
    st.session_state.text = st.write("#" + readme)
  else:
    # Remove text
    st.session_state.text = st.empty()

if __name__ == "__main__":
  main()


# stock image from, https://www.pexels.com/photo/milky-way-illustration-1169754/
# used to create background image main.py
