from all_imports import *
from main_router import *

if not os.path.exists('logs'):
    os.makedirs('logs')
    

app = Flask(__name__)

# Configurations
app.config.from_object(Config)

# Registering blueprints
app.register_blueprint(host)

logging.basicConfig(
    filename='logs/server.log', 
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
    )

if __name__ == '__main__':
    app.run(debug=True)