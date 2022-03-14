

class Welcome:

    @staticmethod
    def welcome_user(data):
        try:
            # fetch the user data
            user = data.get('name')
            if user == "" or user == "guru":
                response_object = {
                    'status': 'success',
                    'message': 'Successfully logged in.',
                }
                return response_object, 200
            else:
                response_object = {
                    'status': 'fail',
                    'message': 'email or password does not match.'
                }
                return response_object, 401

        except Exception as e:
            print(e)
            response_object = {
                'status': 'fail',
                'message': 'Try again'
            }
            return response_object, 500

    @staticmethod
    def logout_user(data):
        response_object = {
                'status': 'fail',
                'message': 'resp'
                }
        return response_object, 401
