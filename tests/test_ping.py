from pytest import fixture, mark
from pytest_mock import MockerFixture
from src import PingRoute


class TestPing():

    @fixture
    def target(self, mocker: MockerFixture) -> PingRoute:
        yield PingRoute(mocker.MagicMock)

    def test_ping_should_succeed(
        self,
        mocker: MockerFixture,
        target: PingRoute
    ) -> None:
        # Arrange
        expected_result = 'Pong'
        mock = mocker.MagicMock(
            return_value=None
        )
        target._logger = mock

        # Act
        result = target.get()

        # Assert
        assert result == expected_result
