"""
Controller
"""
from flask import make_response, abort
# import core/tool_synonyms

def compute(params):
    """
    This function call core tool.

    :param params:  parameters
    :return:        201 on success, 406 on fail
    """
    sent1 = params.get("sent1", None)
    sent2 = params.get("sent2", None)

    if True:
        return 0.42, 201

    else:
        abort(
            406,
            "Something went wrong",
        )