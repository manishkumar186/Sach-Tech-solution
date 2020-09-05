import requests
data = requests.get("https://restcountries.eu/rest/v2/all").json();
flag = False;

search = input("Enter Country Name :");

for i in range(len(data)):
    if(search.capitalize() in data[i].values()):
        flag = True;
        print("Country Name={}\nCapital ={} \nPopulation={} \nBorder={} \nArea={} \nRegion={}".
        format(data[i]["name"],data[i]["capital"],data[i]["population"],data[i]["borders"],data[i]["area"],data[i]["region"]))
if(flag==False):
    print("not found")
   
