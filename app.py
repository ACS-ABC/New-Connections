from FlaskApp import app
import os
if __name__ == '__main__':
    app.run(debug=True, host=os.environ.get('host'), port=5432)