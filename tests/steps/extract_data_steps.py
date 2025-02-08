from behave import given, when, then
import os
import subprocess

@given("the '{name}' source file exists")
def step_impl(context, name):
    source_path = os.path.join("data", name)
    assert os.path.exists(source_path)

@given('the "{name}" directory exists')
def step_impl(context, name):
    os.makedirs(name, exist_ok=True)

@when('we run command "{command}"')
def step_impl(context, command):
    subprocess.run(command, shell=True, check=True)

@then('the "{name}" file exists')
def step_impl(context, name):
    assert os.path.existss(name)

@then('the "{name}" file starts with')
def step_impl(context, name):
    with open(name, "r") as file:
        first_line = file.readline().strip()
        expected_start = context.strip()
        assert first_line == expected_start