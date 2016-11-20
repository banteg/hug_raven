from unittest.mock import MagicMock

import hug
import pytest
from app import api
from hug_raven import Sentry


def test_handler_captures_exceptions():
    sentry = Sentry(api, client=MagicMock())

    with pytest.raises(ZeroDivisionError):
        hug.test.get(api, '/0')

    assert sentry.client.captureException.called
