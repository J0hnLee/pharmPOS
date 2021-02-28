"""Web Server Gateway Interface"""

##################
# FOR PRODUCTION
####################
from .src.resfulAPI import app

if __name__ == "__main__":
    ####################
    # FOR DEVELOPMENT
    ####################
    app.run(host='0.0.0.0', debug=True)