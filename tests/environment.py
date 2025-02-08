import tempfile
import shutil

def before_scenario(context, scenario):
    context.temp_dir = tempfile.mkdtemp()

def after_scenario(context, scenario):
    shutil.rmtree(context.temp_dir)