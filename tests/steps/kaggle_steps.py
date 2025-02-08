from behave import given, when, then
import subprocess
import shlex

@given(u'proper keys are in "kaggle.json"')
def step_impl(context):
    # Assume kaggle.json is already present and valid
    pass

@when(u'we run the kaggle download command')
def step_impl(context):
    command = [
        'python', 'src/acquire.py',
        '-o', 'output_directory',
        '-k', 'kaggle.json',
        '--zip', 'carlmcbrideellis/data-anscombes-quartet'
    ]
    result = subprocess.run(command, capture_output=True, text=True)
    context.output = result.stdout

@then(u'log has INFO line with "Dataset downloaded to"')
def step_impl(context):
    assert "Dataset downloaded to" in context.output