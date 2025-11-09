"""
Demo Vulnerable Application

This app intentionally uses outdated packages with known CVEs
"""

from flask import Flask, request, render_template_string
import yaml

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Vulnerable Demo App</h1>
    <p>This application uses packages with known security vulnerabilities:</p>
    <ul>
        <li>Flask 2.0.1 - CVE-2023-30861</li>
        <li>PyYAML 5.3.1 - CVE-2020-14343</li>
        <li>Jinja2 2.11.3 - CVE-2024-22195</li>
    </ul>
    <p><strong>DO NOT use in production!</strong></p>
    """

@app.route('/parse', methods=['POST'])
def parse_yaml():
    """Vulnerable YAML parsing endpoint"""
    data = request.data
    # UNSAFE: PyYAML 5.3.1 allows arbitrary code execution
    parsed = yaml.load(data, Loader=yaml.FullLoader)
    return f"Parsed: {parsed}"

if __name__ == '__main__':
    app.run(debug=True)
