from pytest_bdd import parsers

@given(
    parsers.cfparse("there are {start:Number} cucumbers",
    extra_types=dict(Number=int)),
    target_fixture="cucumbers",
)
def given_cucumbers(start):
    return dict(start=start, eat=0)