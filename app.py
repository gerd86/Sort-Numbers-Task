import json
import timeit
import collections

from flask import Flask, render_template, request, flash, redirect

from sort_number import Sort
from sort_db import Sort_DB

app = Flask(__name__)
app.config['SECRET_KEY'] = 'GDtfDCFYjD'

db = Sort_DB("sorted_lists.s3db")
db.create_tb()

@app.route('/', methods=["POST", "GET"])
def index():

    if request.method == "POST":
        form_data = request.form
        # TODO Write a validation expression that accepts negative numbers
        # TODO Should return warning if message doesn't contain any numbers
        valid_exp = all(x.isdigit() or x.isspace() for x in form_data['message'])
        if not valid_exp:
            flash('Please enter only numeric characters!')
            return redirect('/')
        print(form_data)
        # init sort class with form data
        num_list = Sort(form_data['message'])
        # do appropriate sort based upon chosen order
        if form_data['sort-order'] == 'ascending':
            sort = num_list.sort_number_ascending()
        else:
            sort = num_list.sort_number_descending()
        sorted_string = ' '.join(sort)
        time_of_op = timeit.timeit(lambda: sort)

        db.add_record(form_data['sort-order'], sorted_string, str(time_of_op))
        return render_template('index.html', sorted_list=sorted_string, sort_order=form_data['sort-order'].title(),
                               time_of_sort=f'Sorted in {time_of_op} seconds.')
    return render_template('index.html')

@app.route('/to_json/', methods=['POST', 'GET'])
def to_json():
    rows = db.fetch_records()
    objects_list = []
    for row in rows:
        d = collections.OrderedDict()
        d['id'] = row[0]
        d['sort_order'] = row[1]
        d['sorted_list'] = row[2]
        d['sort_time'] = row[3]
        objects_list.append(d)
    j = json.dumps(objects_list)
    with open('data.json', 'w') as outfile:
        outfile.write(j)
    return render_template('index.html', success_msg='JSON File has successfully exported!')





if __name__ == '__main__':
    app.run()
