from flask import Flask, render_template, render_template_string
import redis

app = Flask(__name__)

# Connect to the FarGen DB Redis DB.
redis_connection = redis.Redis(host='fargen-db', port=6379, db=0, decode_responses=True)

@app.route('/runinfo')
def runinfo():
    # Fetch all records about runs from the database.
    runinfo_dict = dict()  # Dictionary to store all information retrieved from DB.
    cursor = 0
    while True:
        # Get keys for run IDs and update DB cursor.
        cursor, results = redis_connection.scan(cursor, match='run_id:*')

        for db_key in results:
            # Get all fields in hash table corresponding to current key.
            fields = redis_connection.hgetall(db_key)

            # Get the run ID.
            run_id = fields['run_id']

            # Store all info.
            runinfo_dict[run_id] = fields

        if cursor == 0:
            break

    return render_template('runinfo.html', runinfo_dict=runinfo_dict)

@app.route('/runinfo/demux-report/<run_id>')
def demux_report(run_id):
    # Use the run ID to obtain the record in the database.
    html_path = redis_connection.hget('run_id:' + run_id, 'demux-report')
    # Read the HTML file source.
    with open(html_path) as fid:
        source = fid.read()
        # Render the HTML from string.
        return render_template_string(source)

