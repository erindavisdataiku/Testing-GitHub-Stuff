# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
flight_data = dataiku.Dataset("flight_data")
flight_data_df = flight_data.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

flight_data_prepared_df = flight_data_df # For this sample code, simply copy input to output


# Write recipe outputs
flight_data_prepared = dataiku.Dataset("flight_data_prepared")
flight_data_prepared.write_with_schema(flight_data_prepared_df)
