#app/dtos/response_standard.py
# This file formats every response.
# THESE ARE THE STRUCTURED RESPONSES THAT THE API SHOULD HAVE. IN THIS FORMAT,
# THEY'RE SIMPLY CALLED WITH ONE PARAMETER, THE RESPONSE BEFORE SENDING. THE REST IS OPTIONAL.

# THIS RESPONSE IS USED FOR SUCCESS
def format_success_response(data, message="Success", code=200):
    response = {
        "status": "success",
        "data": data,
        "message": message,
        "code": code
    }
    return response

# THIS RESPONSE IS USED FOR CREATION
def format_success_created_response(data, message="Created", code=201):
    response = {
        "status": "success",
        "data": data,
        "message": message,
        "code": code
    }
    return response

# THIS RESPONSE IS USED FOR UPDATES
def format_updated_response(data, message="Updated", code=200):
    response = {
        "status": "success",
        "data": data,
        "message": message,
        "code": code
    }
    return response

# THIS RESPONSE IS USED FOR DELETIONS
def format_deleted_response(message="Deleted", code=204):
    response = {
        "status": "success",
        "data": None,  # Usually, no data is sent back for deletions
        "message": message,
        "code": code
    }
    return response

# THIS IS FOR ERRORS
def format_error_response(message, code=500):
    response = {
        "status": "error",
        "data": None,
        "message": message,
        "code": code
    }
    return response