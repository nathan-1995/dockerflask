from flask import Flask
from datetime import datetime
import uuid

instance_id = uuid.uuid4().hex

app = Flask(__name__)


@app.route("/")
def index():
        
        return f"Instance ID: {instance_id} hello world"
        
        




if __name__ == "__main__":
    app.run(debug=True)