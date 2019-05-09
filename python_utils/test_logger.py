from logger import Logger

logger = Logger()


class TestLogger(object):
    def test_logger(self, capfd):
        # logger.info('my_info_message')
        # assert 'my_info_message' in capfd.readouterr()
        # logger.info('my_info_message_2', extra={'custom_field': 'my_custom_info'})
        logger.warning('my_warning_message')
        # assert 'my_warning_message' in capfd.readouterr().out
        logger.warning('my_warning_message_2', extra={'custom_field': 'my_custom_warning'})
        # assert 'my_warning_message_2' in capfd.readouterr().out
        # assert 'my_custom_warning' in capfd.readouterr().out
        logger.error('my_error_message')
        # assert 'my_error_message' in capfd.readouterr().out
        logger.error('my_error_message_2', extra={'custom_field': 'my_custom_error'})
        # assert 'my_error_message_2' in capfd.readouterr().out
        # assert 'my_custom_error' in capfd.readouterr().out
