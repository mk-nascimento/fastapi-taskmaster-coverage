from unittest.mock import Mock, patch

from sqlalchemy.orm import Session

from taskmaster.core.database import get_session


def test_get_session():
    mock_engine = Mock()
    mock_session = Mock(spec=Session)

    with patch('taskmaster.core.database.create_engine', return_value=mock_engine):
        with patch('taskmaster.core.database.Session', return_value=mock_session):
            session = next(get_session())

            assert isinstance(session, Session)
