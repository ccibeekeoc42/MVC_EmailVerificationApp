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

    def retrieve(self):
        try:
            # retreiving from the model
            self.model.retrieve()
            self.retrieved_email = self.model.retrieved_email

            # show success message
            self.view.show_success(
                f'The email {self.retrieved_email} retrieved')
        except FileNotFoundError:
            self.view.show_error(f'No email saved in database.')
        finally:
            return self.retrieved_email
