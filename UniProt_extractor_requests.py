import requests
import re

# set up the API URL and query parameters
url = "https://www.uniprot.org/uniprot/"
params = {
    "format": "tab",
    "query": "organism:9606 AND reviewed:yes AND gene:p53 AND annotation:(type:modified)"
}

# make the request and get the response
response = requests.get(url, params=params)

print(response)
print(type(response))

# # parse the response into a list of dictionaries
# data = []
# for line in response.content.decode().split("\n"):
#     if not line.startswith("#"):
#         data.append(dict(zip(response.content.decode().split("\n")[0].split("\t"), line.split("\t"))))

# # print the results
# for row in data:
#     print(row["Entry"], row["Protein names"], row["Gene names"], row["Feature"])
