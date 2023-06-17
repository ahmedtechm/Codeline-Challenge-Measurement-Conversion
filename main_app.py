from flask import Flask, request, jsonify

app = Flask(__name__)


def convert_measurement_string(measurement_string):
    packages = measurement_string.split(',')  # Split measurement string into packages
    converted_packages = []

    for package in packages:
        package_values = []
        count = ""

        for char in package:
            if char == 'z':
                break  # Terminate decoding if non-'z' character is encountered

            if char.isdigit():
                count += char
            else:
                if count:
                    package_values.append(int(count))
                    count = ""

                value = ord(char) - ord('a') + 1  # Convert char to numeric value
                package_values.append(value)

        if count:
            package_values.append(int(count))

        total_value = sum(package_values)
        converted_packages.append(total_value)

    return converted_packages


@app.route('/conversion', methods=['GET'])
def convert_measurements():
    measurement_string = request.args.get('convert-measurements', '')

    if not measurement_string:
        return jsonify({'error': 'Measurement string not provided.'}), 400

    try:
        converted_packages = convert_measurement_string(measurement_string)
        return jsonify({'converted_packages': converted_packages})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run()
