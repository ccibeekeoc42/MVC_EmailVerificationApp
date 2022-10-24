class Controller:

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def save(self, email):
        '''Save the email'''
        try:
            # save the model
            self.model.email = email
            self.model.save()

            # show success message
            self.view.show_success(f'The email {email} saved!')
        except ValueError as error:
            # show error message
            self.view.show_error(error)
