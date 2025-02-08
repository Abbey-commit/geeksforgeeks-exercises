from behave import given, when, then
from pathlib import Path
from textwrap import dedent
import subprocess
import shlex

@given(u'an HTML page "{filename}"')
def step_impl(context, filename):
    context.path = Path(filename)
    context.path.write_text(dedent(context.text))
    context.add_cleanup(context.path.unlink)

@when(u'we run the html extract command')
def step_impl(context):
    command = [
        'python', 'src/acquire.py',
        '--o', 'quartet',
        '--page', '$URL',
        '--caption', "Ascombe's quartet"
    ]
    url = f"file://{str(context.path.absolute())}"
    command[command.index('$URL')] = url
    print(shlex.join(command))
    result = subprocess.run(command, capture_output=True, text=True)
    context.output = result.stdout

@then(u'log has INFO line with "{line}"')
def step_impl(context, line):
    assert line in context.output

@then(u'log has INFO line with "count: {count}"')
def step_impl(context, count):
    assert f"count: {count}" in context.output