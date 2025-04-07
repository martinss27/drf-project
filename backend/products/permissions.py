from rest_framework import permissions # permissions is a module that contains the permissions classes

class IsStaffEditorPermission(permissions.DjangoModelPermissions): # DjangoModelPermissions is a class that checks if the user has the permission to view the model
    perms_map = { # perms_map is a dictionary that maps the HTTP method to the permission
        'GET': ['%(app_label)s.view_%(model_name)s'], # %(app_label)s is the app label of the model and %(model_name)s is the name of the model
        'OPTIONS': [],
        'HEAD': [], 
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'], 
        'PATCH': ['%(app_label)s.change_%(model_name)s'], 
        'DELETE': ['%(app_label)s.delete_%(model_name)s'], 
    }
