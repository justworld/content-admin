import logging

def other_exception_handler(e, event, context):
    """
    未处理异常处理
    :param e:
    :param event:
    :param context:
    :return:
    """
    logging.info('{}, {}, {}'.format(e, event, context))
