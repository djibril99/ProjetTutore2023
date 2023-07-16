import streamlit as st
from model.views import DataVisualizer

def main():
    # Create an instance of the DataVisualizer class
    visualizer = DataVisualizer()
    
    # Run the data visualization
    visualizer.run()

if __name__ == '__main__':
    main()
