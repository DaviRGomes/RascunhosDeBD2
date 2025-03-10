import pprint
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')

db = client['dbworld']

paises = db.paises


results = paises.find()

# for aux in results:
#     pprint.pprint(aux)


newdoc = {
    "Name": "Madagascar",
    "quantBixo": {
        "Pinguin": 15,
        "Lemore": 20
    }
}

results = db.bixosPaises.insert_one(newdoc)

if results.acknowledged:
    print("DOCUMENTO FOI METIDO")
else:
    print("DOCUMENTO PRECISA DO AZULZINHO")

results = paises.find({"Nome": "Madagascar"})
print(*results)