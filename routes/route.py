from controllers.home import home_route 
from controllers.login import login_route 
from controllers.admin import admin_route
from controllers.deputy import deputy_route
from controllers.cleaner import cleaner_route
from controllers.police import police_route
from controllers.chef import chef_route
from controllers.adminDash import adminDash_route
from controllers.staffDetails import staffDetails_route
from controllers.prisonerInfo import prisonerInfo_route
from controllers.request import request_route

def register_routes(app):
    home_route(app)
    login_route(app)
    admin_route(app)
    deputy_route(app)
    cleaner_route(app)
    police_route(app)
    chef_route(app)
    adminDash_route(app)
    staffDetails_route(app)
    prisonerInfo_route(app)
    request_route(app)
    
 # End