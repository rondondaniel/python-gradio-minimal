# Python Gradio Minimal

A minimal dashboard application built with Gradio to visualize and filter demographic data.

## Overview

This application demonstrates how to create a simple yet effective dashboard using Gradio. It visualizes randomly generated demographic data (height, weight, age, city) and allows users to filter the data interactively.

## Features

- **Interactive Filters**: Filter data by city and maximum age
- **Visualizations**:
  - Scatter plot showing the relationship between weight and height
  - Line plot showing the relationship between age and height
- **Real-time Updates**: All visualizations update instantly when filters are changed

## Installation

1. Clone this repository:
```bash
git clone git@github.com:rondondaniel/python-gradio-minimal.git
cd python-gradio-minimal
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the dashboard application:

```bash
python gradio_dashboard.py
```

The application will launch a local web server, typically at http://127.0.0.1:7860, where you can interact with the dashboard.

## Dependencies

- gradio
- pandas
- numpy

## License

MIT

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
