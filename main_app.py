from flask import Flask, request, jsonify

app = Flask(__name__)


def convert_measurements(input_string):
    measurements = input_string.split(',')
    result = []
    for measurement in measurements:
        count = ""
        values = []
        for char in measurement:
            if char.isdigit():
                count += char
            else:
                if count != "":
                    values.append(int(count))
                    count = ""
                if char.isalpha():
                    value = ord(char.lower()) - ord('a') + 1
                    values.append(value)
        if count != "":
            values.append(int(count))
        result.append(sum(values))
    return result


@app.route('/')
def convert_measurements_api():
    input_string = request.args.get('convert-measurements')
    if input_string:
        try:
            result = convert_measurements(input_string)
            return jsonify({'result': result})
        except Exception as e:
            return jsonify({'error': str(e)})
    else:
        return jsonify({'error': 'Missing query parameter "convert-measurements"'})


if __name__ == '__main__':
    app.run()
