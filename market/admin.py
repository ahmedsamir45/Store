from flask import Blueprint
from flask_admin.contrib.sqla import ModelView
from flask_admin import AdminIndexView

from market import bcrypt
from flask_login import current_user

admin_page=Blueprint("admin_page",__name__)


class UserModelView(ModelView):
    def on_model_change(self, form, model, is_created):
        if hasattr(form, 'password') and form.password.data:
            model.password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

    def is_accessible(self):
        return current_user.is_authenticated and current_user.id == 1
        # return True


class MyModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.id == 1
        # return True


class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.id == 1
        # return True
    

