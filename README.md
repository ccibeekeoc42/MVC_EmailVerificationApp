# MVC_EmailVerificationApp

In this repo, we explore using the MVC design pattern in building an email verification app using tkinter in python. Please enjoy!

### Software, Tools, and prerequisits

1. A trused programming IDE.
2. Basic python programing.
3. Basic Tkinter package knowledge.

### Intro To Model-View-Controller (MVC) Design Pattern

The MVC pattern allows the programmer to seperate concerns by dividing and application into three main components: model, view, and controller. This structure enables the code to be more maintainable by seperating focus for each of the components.

<img
  src="chart.png"
  alt="Alt text"
  title="Optional title"
  style="display: block; align: center; margin: 0 auto; max-width: 180px">

- **The Model**: this component is responsible for handeling the data/ state of the application. it typically sends and/or retrieves the data to/from the storage/ database. The model could have a bi-dirrectional connection to the Controller as it recieves commands from the controller oh how to handle the data.

- **The Controller**: this is the link between the Model and the View. it sends commands to update the state of the model based on actions from the View. it has a bi-directional connection to the View as it can also update the state of the view based on the model.

- **The View**: this is the component that faces the end user/ client. it is the user interface that represents the model as it has logic to display data. The view typically communicates with the controller directly.

### Intro To Model-View-Controller (MVC) Design Pattern

- **The Model Class**: Below are the steps to build the model.
  - The model class recieves the email data as input to the constructor.
  - Then uses getter and setter properties to get and set the email respectively.
    - The setter first uses regular expressions to check that the email provided matches a standard pattern.
    - if the pattern is correct, it sets the email variable correctly.
    - if the pattern is NOT correct, it throws a ValueError of an invalid email address.
- The model class also implements the logic to talk to the database (storage) by saving the provided email into a txt file.

- **The View Class**: Below are the steps to build the view.

###### Credits: https://www.pythontutorial.net/tkinter/tkinter-mvc/#:~:text=The%20MVC%20design%20pattern%20allows,especially%20when%20the%20application%20grows.
