"""
Controller
"""
import sys, os
from flask import make_response, abort
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'core'))
import tool_synonyms
import tool_w2v

def POST_synonyms_similarity(params):
    """
    This function call core tool.

    :param params:  parameters
    :return:        201 on success, 406 on fail
    """
    sent1 = params.get("sent1", None)
    sent2 = params.get("sent2", None)

    if True:
        return tool_synonyms.get_synonyms_similarity(sent1,sent2), 201
    else:
        abort(
            406,
            "Something went wrong",
        )

def POST_w2v_similarity(params):
    """
    This function call core tool.

    :param params:  parameters
    :return:        201 on success, 406 on fail
    """
    sent1 = params.get("sent1", None)
    sent2 = params.get("sent2", None)

    if True:
        return 'unable', 201

    else:
        abort(
            406,
            "Something went wrong",
        )