# For Reviewers

## Overview
This document outlines important points that reviewers should keep in mind when evaluating the Risk Management project. The project handles the creation, updating, and retrieval of risk data using a JSON-based storage method. It does not require a database and operates entirely in-memory (or via a JSON file).

## JSON file Used:
The JSON file is used to persist risk data between server runs, as Django's default behavior doesn't retain data without a connected database, making the JSON file a lightweight solution for temporary storage.

## Key Points to Review

1. **Title and Description Check for Creating or Updating a Risk**:
   - When creating a new risk or updating an existing one, it checks if a risk with the same `title` and `description` already exists.
   - If a risk with the same `title` and `description` is found, its `state` will be updated to the new state provided in the request. Otherwise, a new risk will be created.
   - This logic is implemented in the `check_and_create_risk()` function.

2. **Handling Invalid State**:
   - The state of a risk is validated against a predefined list of valid states: `['open', 'closed', 'accepted', 'investigating']`.
   - If an invalid state is provided, the API will return an error message with a list of valid states.

3. **Error Handling**:
   - If there is an issue with the request body (like missing required fields or invalid JSON), the system will return a clear error message with a `400 Bad Request` status.
   - If a risk cannot be found by its `id`, the system will return a `404 Not Found` response.

4. **File Storage (JSON)**:
   - Risks are stored in a JSON file (`risks.json`), which is read and written by the system. If the file does not exist, it is created when the first risk is added.
   - The application will automatically load risks from this file and save changes back to it.




## Common Issues and Fixes

### **Unapplied Migrations Warning**

While running the application, you might encounter the following error message:
## You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions. Run 'python manage.py migrate' to apply them.



- **What does this mean?**
  This error occurs because Django is trying to apply migrations related to database tables, which is typically needed when using a database.
  
- **Can I ignore this?**
  Yes. Since this project does not use a database (it stores data in a JSON file), you can ignore this warning. The migrations do not affect the core functionality of this project because it does not rely on Django's database ORM.

  You can safely proceed with the review and testing of the project as long as the API functionality works as expected.

---
Please ensure that you verify the following:
- Ensure the correct functionality of the API endpoints.
- Confirm that the logic for checking and updating risks works correctly when the same `title` and `description` are provided.
- Validate that the file handling (loading and saving risks) operates correctly without using a database.


### **Error: That port is already in use.**
While running the application, you might encounter the following error message:
## Error: That port is already in use.
While compiling may be you are trying to `python manage.py runserver 8080` but this erro comes in , means already the comman is executed adn you would have closed the terminal.
* * Solution:
- lsof -i:8080 (lists all the process on the port )
- kill -9 <PID> (to kill the process and free up the port)


