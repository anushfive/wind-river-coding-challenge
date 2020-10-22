from flask import Flask, request
app = Flask(__name__)


# A Api to encrypt the input string passed in the payload
@app.route('/api/encrypt', methods=['POST'])
def encrypt():
    # Extract the json field with ame Input from request
    input_string = request.json['Input']
    # Check if the input is valid or not. If the input does not have enough length, or is over-sized, then
    # return error response
    if validate_input_string(input_string):
        encrypted_string = encrypt_string(input_string)
        return build_response(input_string, encrypted_string, 'success', 'encryption successful'), 200
    else:
        return build_response(input_string, '', 'failure', 'input should not be empty and should be less '
                                                           'than 30 characters'), 400


# a decryption api to decrypt the provided string input.
@app.route('/api/decrypt', methods=['POST'])
def decrypt():
    # Extract the json field with ame Input from request
    input_string = request.json['Input']
    # Check if the input is valid or not. If the input does not have enough length, or is over-sized, then
    # return error response
    if validate_input_string(input_string):
        decrypted_string = decrypt_string(input_string)
        return build_response(input_string, decrypted_string, 'success', 'decryption successful'), 200
    else:
        return build_response(input_string, '', 'failure', 'input should not be empty and should be less '
                                                           'than 30 characters'), 400


# Health check endpoint to verify if the server is up and running.
@app.route('/api/health', methods=['GET'])
def health():
    return {'health': 'OK'}, 200


# Validate the input string passed. Checks if the string is empty or not. Also check if the string is between lengths
# of 0 and 30. If the validation fails, returns an error response
def validate_input_string(input_string):
    input_string_size = len(input_string)
    if not (input_string.strip() and (0 < input_string_size < 30)):
        return False
    else:
        return True


# A simple function to encrypt a string. Function shifts the characters of the string by 1 and
# returns a new string
def encrypt_string(input_string):
    simple_encrypted_string = ''
    for ip_char in input_string:
        simple_encrypted_string = simple_encrypted_string + chr(ord(ip_char) + 1)
    return simple_encrypted_string


# A simple function to decrypt a string. Function re-shifts the characters of the string by 1 and
# returns the original string
def decrypt_string(input_string):
    simple_decrypted_string = ''
    for ip_char in input_string:
        simple_decrypted_string = simple_decrypted_string + chr(ord(ip_char) - 1)
    return simple_decrypted_string


# An utility function to build the response when required. Returns a response object
def build_response(input_string, output_string, status, message):
    response = {
        'Input': input_string,
        'Output': output_string,
        'Status': status,
        'Message': message
    }
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)

