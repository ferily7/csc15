import urllib.request 
import json

def main():

  weatherURL = "http://api.openweathermap.org/data/2.5/weather?q="
  runAgain = "Yes"

  while runAgain == "Yes":
    #Initializing variables
    city = input("Please enter a city: ")
    metric = input("Please enter a weather metric: ")
    json_input = urllib.request.urlopen(weatherURL+city).read()
    decoded = json_input.decode('utf-8')
    data = json.loads(decoded)
    tempData = data['main']
    tempData = str(tempData)
    tempList = tempData.split(", ")
    found = False
    i = 0

    #Finding the word temp in the list
    while found == False and i < len(tempList):
      if "'temp'" in tempList[i]:
        found = True
        tempStr = tempList[i]
      else:
        i += 1

    #Splits the list when temp is found
    if found == True:
      tempList2 = tempStr.split(": ")
      tempNum = tempList2[1]

      #Gets rid of the "}" if present
      if "}" in tempNum:
        tempNum2 = tempNum.split("}")
        tempNum = float(tempNum2[0])
      else:
        tempNum = float(tempList2[1])

    #Converting Kelvin to the metric the user enters    
    if metric == "C":
      tempNum = int(tempNum - 272.15)
    else:
      tempNum = int(9/5*(tempNum - 273) + 32)

    #Prints results
    print("The weather in", city, "is", tempNum, metric)

    #Asks the user if they want to search another city
    runAgain = input("Enter another city? ")
    if runAgain == "No":
      print("Thank you for visiting openweathermap.org!")
    
main()
