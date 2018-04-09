from behave import given, then

from player import Player


@given('new player')
def step_impl(context):
    context.p = Player()

@then('it should have {attr}')
def step_impl(context, attr):
    assert hasattr(context.p, attr)