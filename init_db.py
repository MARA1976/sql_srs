import io

import pandas as pd
import duckdb

# Connect to the database
con = duckdb.connect(database="data/exercises_sql_tables.duckdb", read_only=False)

# Define the DataFrame
data = {
    "theme": ["cross_Joins", "Windows Functions"],
    "exercise_name": ["beverages_and_food", "simple_window"],
    "tables": [["beverages", "food_items"], ["simple_window"]],
    "last_reviewed": ["1970-01-01", "1970-01-01"],
}
memory_state_df = pd.DataFrame(data)

# Create and populate the memory_state table
con.execute("CREATE TABLE IF NOT EXISTS memory_state AS SELECT * FROM memory_state_df")

# ------------------------------------------------------------------------
# CROSS JOINS EXERCISES
# ------------------------------------------------------------------------
CSV = """
beverages,price
orange juice,2.5
Expresso,2
Tea,3
"""
beverages = pd.read_csv(io.StringIO(CSV))
con.execute("CREATE TABLE IF NOT EXISTS beverages AS SELECT * FROM beverages")

CSV2 = """
food_item, food_price
cookie juice,2.5
chocolatine,3
muffin,3
"""

food_items = pd.read_csv(io.StringIO(CSV2))


# ANSWER_STR = """
# SELECT * FROM beverages
# CROSS JOIN food_items
# """

con.execute("CREATE TABLE IF NOT EXISTS food_items AS SELECT * FROM food_items")