from airflow.plugins_manager import AirflowPlugin
from flask import Blueprint, request
from flask_appbuilder import expose, BaseView as AppBuilderBaseView
from my_task import MyTask #this is our usecase py file
from wtforms import Form, StringField
from airflow.www.app import csrf

#  Blueprint record operations to be executed later when you register them on an application
bp = Blueprint(
               "test_plugin",
               __name__,
               template_folder="templates", # registers airflow/plugins/templates as a Jinja template folder
               static_folder="static",
               static_url_path="/static/test_plugin",
               )

class FilterForm(Form):
    param1 = StringField('param1')
    param2 = StringField('param2')
    param3 = StringField('param3')
    param4 = StringField('param4')

# Each view is a Flask blueprint that will be created for you automatically by the framework. 
class TestAppBuilderBaseView(AppBuilderBaseView):
    default_view = "test"
    #this method gets the view as localhost:/testappbuilderbaseview/
    @expose("/", methods=['GET', 'POST'])
    @csrf.exempt # if we don’t want to use csrf
    def test(self):
        form = FilterForm(request.form)
        if request.method == 'POST' and form.validate():
            #Here we are calling our usecase functions
            my_task_output = MyTask(
                   form.param1.data, 
                   form.param2.data,
                   form.param3.data, 
                   form.param4.data
            )
            df = my_task_output.my_function()
            return df
        return self.render_template("test.html", form = form)

v_appbuilder_view = TestAppBuilderBaseView()
v_appbuilder_package = {
    "name": "Test View", # this is the name of the link displayed
    "category": "Test Plugin", # This is the name of the tab under which we have our view
    "view": v_appbuilder_view
}

class AirflowTestPlugin(AirflowPlugin):
    name = "test_plugin"
    flask_blueprints = [bp]
    appbuilder_views = [v_appbuilder_package]