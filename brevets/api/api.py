from flask import Flask, request, render_template
from flask_restful import Resource, Api
from pymongo import MongoClient
import os
import csv
from bson.json_util import dumps, loads
from io import StringIO
app = Flask(__name__)
api = Api(app)

client = MongoClient('mongodb://' + os.environ['MONGODB_HOSTNAME'], 27017)
db = client.tododb

def convertToCSV(data):





    # Create a list to hold the CSV rows

    csv_rows = []



    # Iterate over each document in the data

    for document in data:

        distance = document['distance']

        begin_date = document['begin_date']

        begin_time = document['begin_time']

        controls = document['controls']



        # Add the document row with distance, begin_date, and begin_time

        document_row = ['brevets/distance', 'brevets/begin_date', 'brevets/begin_time']

        csv_rows.append(document_row)



        document_row = [distance, begin_date, begin_time]



        # Remove \r and \n characters from each value

        document_row = [str(value).replace('\r', '').replace('\n', '') for value in document_row]



        csv_rows.append(document_row)



        # Iterate over each control in the controls list

        for i, control in enumerate(controls):

            control_row = []



            # Add the control data to the row

            control_row.append(f"brevets/controls/{i}/km")

            control_row.append(control['km'])

            control_row.append(f"brevets/controls/{i}/mi")

            control_row.append(control['mi'])

            control_row.append(f"brevets/controls/{i}/location")

            control_row.append(control['location'])

            control_row.append(f"brevets/controls/{i}/open")

            control_row.append(control['open'])

            control_row.append(f"brevets/controls/{i}/close")

            control_row.append(control['close'])




            # Append the control row to the CSV rows

            csv_rows.append(control_row)



        # Add an empty row between documents

        csv_rows.append([])



    # Create a string buffer to write CSV data

    csv_buffer = StringIO()



    # Write the CSV rows to the buffer

    csv_writer = csv.writer(csv_buffer)

    csv_writer.writerows(csv_rows)



    # Get the CSV data as a string

    csv_data = csv_buffer.getvalue().replace('\r', ' ').replace('\n', ' ')



    return csv_data
def convertToCSVo(data):

    # Create a list to hold the CSV rows

    csv_rows = []



    # Iterate over each document in the data

    for document in data:

        distance = document['distance']

        begin_date = document['begin_date']

        begin_time = document['begin_time']

        controls = document['controls']



        # Add the document row with distance, begin_date, and begin_time

        document_row = ['brevets/distance', 'brevets/begin_date', 'brevets/begin_time']

        csv_rows.append(document_row)



        document_row = [distance, begin_date, begin_time]



        csv_rows.append(document_row)



        # Iterate over each control in the controls list

        for i, control in enumerate(controls):

            control_row = []



            # Add the control data to the row

            control_row.append(f"brevets/controls/{i}/km")

            control_row.append(control['km'])

            control_row.append(f"brevets/controls/{i}/mi")

            control_row.append(control['mi'])

            control_row.append(f"brevets/controls/{i}/location")

            control_row.append(control['location'])

            control_row.append(f"brevets/controls/{i}/open")

            control_row.append(control['open'])

            




            # Append the control row to the CSV rows

            csv_rows.append(control_row)



        # Add an empty row between documents

        csv_rows.append([])



    # Create a string buffer to write CSV data

    csv_buffer = StringIO()



    # Write the CSV rows to the buffer

    csv_writer = csv.writer(csv_buffer)

    csv_writer.writerows(csv_rows)



    # Get the CSV data as a string

    csv_data = csv_buffer.getvalue().replace('\r', ' ').replace('\n', ' ')



    return csv_data


def convertToCSVc(data):

    # Create a list to hold the CSV rows

    csv_rows = []



    # Iterate over each document in the data

    for document in data:

        distance = document['distance']

        begin_date = document['begin_date']

        begin_time = document['begin_time']

        controls = document['controls']



        # Add the document row with distance, begin_date, and begin_time

        document_row = ['brevets/distance', 'brevets/begin_date', 'brevets/begin_time']

        csv_rows.append(document_row)



        document_row = [distance, begin_date, begin_time]





        csv_rows.append(document_row)



        # Iterate over each control in the controls list

        for i, control in enumerate(controls):

            control_row = []



            # Add the control data to the row

            control_row.append(f"brevets/controls/{i}/km")

            control_row.append(control['km'])

            control_row.append(f"brevets/controls/{i}/mi")

            control_row.append(control['mi'])

            control_row.append(f"brevets/controls/{i}/location")

            control_row.append(control['location'])

            control_row.append(f"brevets/controls/{i}/close")

            control_row.append(control['close'])




            # Append the control row to the CSV rows

            csv_rows.append(control_row)



        # Add an empty row between documents

        csv_rows.append([])



    # Create a string buffer to write CSV data

    csv_buffer = StringIO()



    # Write the CSV rows to the buffer

    csv_writer = csv.writer(csv_buffer)

    csv_writer.writerows(csv_rows)



    # Get the CSV data as a string

    csv_data = csv_buffer.getvalue().replace('\r', ' ').replace('\n', ' ')



    return csv_data

class listAll(Resource):
	def get(self, type="JSON"):
		num = request.args.get('top', default=-1, type=int)
		
		if num == -1:
			data = db.tododb.find({}, {'_id': 0,'distance': 1,'begin_date': 1,'begin_time':1,'controls':1})
		else:
			data = db.tododb.find({}, {'_id': 0,'distance': 1,'begin_date': 1,'begin_time':1,'controls':1}).limit(num)

		if type == "csv":
			data = convertToCSV(data)
		else:
			data = {'brevets':loads(dumps(data))}
		return data

class listOpenOnly(Resource):

    def get(self, type="JSON"):

        num = request.args.get('top', default=-1, type=int)



        if num == -1:

            data = db.tododb.find({}, {'_id': 0, 'distance': 1, 'begin_date': 1, 'begin_time': 1, 'controls': 1})

        else:

            data = db.tododb.find({}, {'_id': 0, 'distance': 1, 'begin_date': 1, 'begin_time': 1, 'controls': 1}).limit(num)



        results = []



        for document in data:

            distance = document['distance']

            begin_date = document['begin_date']

            begin_time = document['begin_time']

            controls = document['controls']

            document_result = {

                "distance": distance,

                "begin_date": begin_date,

                "begin_time": begin_time,

                "controls": []

            }



            for control in controls:

                control_result = {
                    "km": control['km'],
					"mi": control['mi'],
                    "location": control['location'],

                    "open": control['open']

                }

                document_result["controls"].append(control_result)



            results.append(document_result)



        if type == "csv":

            data = convertToCSVo(results)

        else:

            data = {'brevets':results}



        return data
class listCloseOnly(Resource):

    def get(self, type="JSON"):

        num = request.args.get('top', default=-1, type=int)



        if num == -1:

            data = db.tododb.find({}, {'_id': 0, 'distance': 1, 'begin_date': 1, 'begin_time': 1, 'controls': 1})

        else:

            data = db.tododb.find({}, {'_id': 0, 'distance': 1, 'begin_date': 1, 'begin_time': 1, 'controls': 1}).limit(num)



        results = []



        for document in data:

            distance = document['distance']

            begin_date = document['begin_date']

            begin_time = document['begin_time']

            controls = document['controls']

            document_result = {

                "distance": distance,

                "begin_date": begin_date,

                "begin_time": begin_time,

                "controls": []

            }



            for control in controls:

                control_result = {

                    "km": control['km'],

                    "mi": control['mi'],

                    "location": control['location'],

                    "close": control['close']

                }

                document_result["controls"].append(control_result)



            results.append(document_result)



        if type == "csv":

            data =  convertToCSVc(results)

        else:

            data = {'brevets': results}



        return data

# Create routes
# Another way, without decorators
api.add_resource(listAll, '/listAll', '/listAll/', '/listAll/<string:type>')
api.add_resource(listOpenOnly, '/listOpenOnly', '/listOpenOnly/', '/listOpenOnly/<string:type>')
api.add_resource(listCloseOnly,'/listCloseOnly', '/listCloseOnly/', '/listCloseOnly/<string:type>')

# Run the application
if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)