def displayPage(python_file):
    directory = 'templates/mealdiary.html'
    html = open(directory, "w+")
    # Creates HTML page with updated logs
    html.write("""{% extends 'base.html' %}

{% block content %}
    <body class="m-3" style="background-repeat: inherit; background-size: cover; height: 100%" 
    background="/static/meal_background.jpg">
        <div class="container center rounded" style="background:lightgray; width: 100%; border: solid 2px black">
            <h2>Meal Log</h2>
            A food diary is a daily log of what you eat and drink each day. The diary helps you and your doctor understand 
            your eating habits. It can help you realize what you consume. <b> Press 'Add Meal' to enter a log. </b>
            <hr>
            <!-- Button trigger modal -->
            <button type="button" class="btn btn-success" data-bs-toggle="modal" data-bs-target="#newLog">
                Add Meal
            </button>

            <!-- Modal -->
            <div class="modal fade" id="newLog" tabindex="-1" aria-labelledby="newLogLabel" aria-hidden="true">
                <div class="modal-dialog">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title" id="newLog">
                                Add Meal
                            </h5>
                            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                        </div>

                        <!-- Form -->
                        <form id="mealForm" method="post">
                            <div class="modal-body">
                                <!-- Sourced from: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/date -->
                                <label for="formDate" class="col-form-label"><b>Date</b></label><br>
                                <input type="date" id="formDate" name="inputDate" class="form-control" form="mealForm"
                                       value="2022-01-01" min="2022-01-01" max="3000-01-01"><br><br>

                                <label for="inputTime" class="col-form-label"><b>Time</b></label><br>
                                <div class="d-inline-flex">
                                    <div id="inputTime" class="input-group" style="width: 60%">
                                        <input type="number" name="inputHour" class="form-control" style="width: 10%"
                                               form="mealForm" min="1" max="12" step="1" placeholder="00" aria-label="Hour"
                                               required>
                                        <span class="input-group-text"><b>:</b></span>
                                        <input type="number" name="inputMinute" class="form-control" style="width: 10%"
                                               form="mealForm" min="0" max="59" step="1" placeholder="00" aria-label="Minute"
                                               required>
                                    </div>
                                    &nbsp
                                    <select id="formPeriod" name="inputPeriod" class="form-select"
                                            style="width: 35%; display: inline-block"
                                            form="mealForm" aria-label="Period Select" required>
                                        <option selected value="">Select</option>
                                        <option value="am">a.m.</option>
                                        <option value="pm">p.m.</option>
                                    </select>
                                </div>
                                <br><br>

                                <label for="formDescription" class="col-form-label"><b>Description</b></label>
                                <textarea id="formDescription" name="inputMeal" class="form-control" form="mealForm"
                                          aria-label="Textarea" required></textarea>
                            </div>
                            <div class="modal-footer">
                                <button type="button" class="btn btn-danger" data-bs-dismiss="modal">Cancel</button>
                                <button type="submit" class="btn btn-success" form="mealForm">Submit</button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
            <br><br>

            <!-- Table -->
            <form id="optionForm" method="post">
                <table class="table table-success table-hover table-sm table-bordered">
                    <thead>
                        <tr>
                            <th scope="col" style="width: 10%">Date</th>
                            <th scope="col" style="width: 10%">Time</th>
                            <th scope="col" style="width: 70%">Description</th>
                            <th scope="col" style="width: 10%">Options</th>
                        </tr>
                    </thead>
                    <tbody>""")
    html.close()

    # Creates a table row/column for each log
    logs = python_file
    for i in range(len(logs)):
        date = logs[i]["Date"]
        time = logs[i]["Time"]
        meal = logs[i]["Meal"]
        add_logs = open(directory, "a")
        add_logs.write(f"""
                        <tr>
                            <td>{date}</td>
                            <td>{time}</td>
                            <td class="text-break">{meal}</td>
                            <td>
                                <div class="btn-group" role="group" aria-label="Option Buttons">
                                    <button type="submit" name="edit" value="{i}" class="btn btn-primary btn-sm" disabled 
                                    >Edit</button> 
                                    <button type="submit" name="clone" value="{i}" class="btn btn-primary btn-sm" disabled 
                                    >Clone</button> 
                                    <button type="submit" name="delete" value="{i}" class="btn btn-danger btn-sm" disabled 
                                    >Delete</button>
                                </div> 
                            </td>
                        </tr> """)
        add_logs.close()

    # Completes HTML page
    add_end = open(directory, "a")
    add_end.write("""
                    </tbody>
                </table>
            </form>
        </div>
    </body>
{% endblock %}""")
    add_end.close()
