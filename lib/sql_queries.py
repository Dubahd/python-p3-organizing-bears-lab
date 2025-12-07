
# Returns all female bears with name and age
select_all_female_bears_return_name_and_age = """
    SELECT
        bears.name,
        bears.age
    FROM bears
    WHERE sex='F';
"""

# Returns all bear names in alphabetical order
select_all_bears_names_and_orders_in_alphabetical_order = """
    SELECT
        bears.name
    FROM bears
    ORDER BY name ASC;
"""

# Returns all alive bears with name and age, ordered youngest to oldest
select_all_bears_names_and_ages_that_are_alive_and_order_youngest_to_oldest = """
    SELECT
        bears.name,
        bears.age
    FROM bears
    WHERE alive = 1
    ORDER BY age ASC;
"""

# Returns the oldest bear's name and age
select_oldest_bear_and_returns_name_and_age = """
    SELECT
        bears.name,
        bears.age
    FROM bears
    ORDER BY age DESC
    LIMIT 1;
"""

# Returns the youngest bear's name and age
select_youngest_bear_and_returns_name_and_age = """
    SELECT
        bears.name,
        bears.age
    FROM bears
    ORDER BY age ASC
    LIMIT 1;
"""

# Returns all bears with names starting with 'Mr.'
select_bears_names_starting_with_mr = """
    SELECT
        bears.name
    FROM bears
    WHERE name LIKE 'Mr%';
"""

# Returns all brown bears
select_all_brown_bears_return_name_and_age = """
    SELECT
        bears.name,
        bears.age
    FROM bears
    WHERE color = 'Brown';
"""

# Returns all bears with temperament 'Grumpy'
select_bears_with_temperament_grumpy = """
    SELECT
        bears.name
    FROM bears
    WHERE temperament = 'Grumpy';
"""

# Returns bears with age between 3 and 5
select_bears_with_age_between_3_and_5 = """
    SELECT
        bears.name,
        bears.age
    FROM bears
    WHERE age BETWEEN 3 AND 5;
"""

# Returns count of bears by color
select_bears_by_color_count = """
    SELECT
        color,
        COUNT(*) as count
    FROM bears
    GROUP BY color;
"""

# Returns average age of bears
select_average_age_of_bears = """
    SELECT
        AVG(age) as average_age
    FROM bears;
"""

# Returns bears ordered by name descending
select_all_bears_names_and_orders_in_reverse_alphabetical_order = """
    SELECT
        bears.name
    FROM bears
    ORDER BY name DESC;
"""