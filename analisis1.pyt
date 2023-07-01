import csv
import json
import couchdb
 couch = couchdb.Server('http://admin:admin@25.4.21.117:5984')
    db=couch['movies']
    
    def csv_to_json(csv_file):
        with open(csv_file,'r', encoding='utf-8')ass file:
            reader=csv.DictReader(file)
            for row in reader:
                json_data {}
                for key,value in row.items():
                    json_data[key]=value
                json_data['autor']='Andrew Brandon Washington Ariana Nataly'
                doc_id=json_data['Name']
                db.seve(json_data)
#Ejemplo de uso
csv_file='imb_movies.csv'
csv_to_json(csv_file)

