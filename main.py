import streamlit as st
import time
import readFile as r
import mergeSort as ms
import sortingCodes as sc
import base64


def background(imageFile):
  with open(imageFile, "rb") as imageFile:
    encoded_string = base64.b64encode(imageFile.read())
  st.markdown(
  f"""
  <style>
  .stApp {{
    background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
    background-size: cover
  }}
  </style>
  """,
  unsafe_allow_html=True
  )

def main():
  # list that stores the star objects
  list = r.list
  background('image.jpg') # add background image

  st.sidebar.title("Stellar Showdown")
  st.sidebar.subheader("******using the HYG Database of 120,000 Stars******")

  # I used session state becuse otherwise there is no way to keep track of what has happend before, which is important as I do not want the sorting to run again if ano  other action is performed, like prssing show stars

  # checks if button pressed is in the session state, if not it adds it and sets it to False, similar with sort resul
  if "button_pressed" not in st.session_state:
    st.session_state.button_pressed = False
  if "sort_result" not in st.session_state:
    st.session_state.sort_result = None

  # adds the choices buttons
  choice1 = st.sidebar.radio("Sort stars by", ["Distance from Earth", "Temperature"])
  choice2 = st.sidebar.radio("Which Sorting algorithm?",
                     ["Merge Sort", "Bogo Sort", "Random Sort", "Shell Sort"])

  # it sets button presed to True in the session state
  if st.sidebar.button("Sort"):
    st.session_state.button_pressed = True

  # if button pressed is True, it will run the sorting algorithm(TODO) and sets the result( string of time it took) to the session state, sets button pressed to False in state
  if st.session_state.button_pressed and st.session_state.sort_result is None:
    if choice1 == "Distance from Earth" and choice2 == "Merge Sort":
      start = time.time()
      ms.mergeSortDistance(list, 0, len(list) - 1)
      end = time.time()
      st.session_state.sort_result = choice2 + " Algorithm took: " + str(
        "{:.4f}".format(end - start)) + " seconds"
      st.session_state.button_pressed = False

    elif choice1 == "Temperature" and choice2 == "Merge Sort":
      start = time.time()
      ms.mergeSortTemperature(list, 0, len(list) - 1)
      end = time.time()
      st.session_state.sort_result = choice2 + " Algorithm took: " + str(
        "{:.4f}".format(end - start)) + " seconds"
      st.session_state.button_pressed = False

  # displays the result string and code to screen if result is not None
  if st.session_state.sort_result is not None:
    st.sidebar.write(st.session_state.sort_result)
    st.sidebar.write("")
  
  # show code
  if st.sidebar.checkbox("Show code"):
    st.write("C++ Code for " + choice2 + " Algorithm")
    if choice2 == "Merge Sort":
      st.code(sc.mergeSort, language="cpp")

  # if tthe button is pressed, it will display the last 25 stars in the list
  if st.sidebar.checkbox("Show stars"):
    st.write("")
    st.header("Stars by " + choice1)
    for j in range(len(list) - 1, len(list) - 26, -1):
      temperature = str("{:.5f}".format(list[j].temperature))
      # if the color index was empty, therfore set to 0, set to "N/A"
      if temperature == str(4600 * ((1 / 1.7) + (1 / 0.62))):
        temperature = "N/A"
      st.subheader("Star " + str(j + 1) + ":" + " Distance from Earth, " +
               str("{:.5f}".format(list[j].distance)) +
               " light-years. Temperature " + temperature + " Kelvin")

  if st.sidebar.button("Reset"):
    st.session_state.sort_result = None
    list = r.list
    st.experimental_rerun()


if __name__ == "__main__":
  main()


# stock image from, https://www.pexels.com/photo/milky-way-illustration-1169754/
# used to create background image main.py