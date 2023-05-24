def handle_exception(mainfunc=None, **kwargs):
    try:

        # Execute the main logic of the Lambda function
        if mainfunc is not None:
            result = mainfunc(**kwargs)

            # Return the result
            return result
    except Exception as e:
        # Handle other exceptions
        if isinstance(e, CustomException):
            print("CustomEx Inst:")
            return e
        else:
            e.__setattr__("message", e.args[0])
            print("Exception Inst:")
            return e


class CustomException(Exception):

    def __init__(self, **kwargs):
        self.message = kwargs['message']
