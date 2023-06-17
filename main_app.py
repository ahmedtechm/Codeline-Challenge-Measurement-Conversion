from flask import Flask, request, jsonify

app = Flask(__name__)


def convert_measurements(input_string):
    measurements = input_string.split(',')
    total_values = []

    for measurement in measurements:
        values = measurement.split(' ')
        total = 0

        for value in values:
            try:
                num = float(value)
                total += num
            except ValueError:
                pass

        total_values.append(total)

    return total_values


@app.route('/convert', methods=['POST'])
def convert():
    data = request.get_json()
    input_string = data['input_string']
    result = convert_measurements(input_string)
    return jsonify({'result': result})


if __name__ == '__main__':
    app.run()
