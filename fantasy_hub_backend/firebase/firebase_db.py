import sys
import json
import firebase_admin # type: ignore
from firebase_admin import credentials # type: ignore
from firebase_admin import db # type: ignore

TRADE_VALS_DIR = '../trade_values/'

def load_json(file):
    json_file = TRADE_VALS_DIR + file
    try:
        with open(json_file, 'r') as f:
            trade_values = json.load(f)
        print('Successfully loaded file: ', json_file)
    except FileNotFoundError as file_err:
        print('File {} not found!'.format(file), file_err)
        sys.exit(1)
    except Exception as err:
        print('Another error has occured: ', err)
        sys.exit(1)
    return trade_values

def main(argv):
    # Handle invalid number of arguments
    if len(argv) != 1:
        print("Arguments must be in form: firebase_db.py <file_name>")
        sys.exit(1)
    # Fetch the service account key JSON file contents
    with open('fb-admin-key.json') as f: admin_key = json.load(f)
    cred = credentials.Certificate(admin_key)
    # Initialize the app with admin privileges
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://fantasy-hub-c58bf-default-rtdb.firebaseio.com/'
    })
    # As an admin, the app has access to read and write all data, regradless of Security Rules
    ref = db.reference('/')
    values_ref = ref.child('trade_values')
    try:
        values_ref.set(load_json(argv[0]))
        print('Successfully loaded to Firebase Realtime Database.')
    except Exception as err:
        print('Error in saving to Firebase DB: ', err)

if __name__ == '__main__':
    main(sys.argv[1:])
