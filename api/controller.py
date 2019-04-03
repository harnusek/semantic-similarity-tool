# -*- coding: utf-8 -*-

import sys, os
from flask import make_response, abort
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'core'))
import knowledge_methods
import corpus_methods

def POST_knowledge_similarity(params):
    """
    This function call core tool.

    :param params:  parameters
    :return:        201 on success, 406 on fail
    """
    sent_1 = params.get("sent_1", None)
    sent_2 = params.get("sent_2", None)
    use_stop = params.get("use_stop", True)
    use_pos = params.get("use_pos", False)
    use_lem = params.get("use_lem", False)
    result = knowledge_methods.similarity_sentences(sent_1,sent_2, use_stop, use_pos, use_lem)
    if result is not None:
        return result, 201
    else:
        abort(
            406,
            "Something went wrong",
        )

def POST_corpus_similarity(params):
    """
    This function call core tool.

    :param params:  parameters
    :return:        201 on success, 406 on fail
    """
    sent_1 = params.get("sent_1", None)
    sent_2 = params.get("sent_2", None)
    use_stop = params.get("use_stop", True)
    use_pos = params.get("use_pos", False)
    use_lem = params.get("use_lem", False)
    result = corpus_methods.similarity_sentences(sent_1,sent_2, use_stop, use_pos, use_lem)
    if result is not None:
        return result, 201
    else:
        abort(
            406,
            "Something went wrong",
        )