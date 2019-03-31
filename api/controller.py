# -*- coding: utf-8 -*-

import sys, os
from flask import make_response, abort
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'core'))
import knowledge_methods
import corpus_methods

def POST_synonyms_similarity(params):
    """
    This function call core tool.

    :param params:  parameters
    :return:        201 on success, 406 on fail
    """
    sent1 = params.get("sent1", None)
    sent2 = params.get("sent2", None)

    result = knowledge_methods.similarity_sentences(sent1,sent2)

    if result is not None:
        return result, 201
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

    result = corpus_methods.similarity_sentences(sent1,sent2)

    if result is not None:
        return result, 201
    else:
        abort(
            406,
            "Something went wrong",
        )