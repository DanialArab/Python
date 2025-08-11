
apply vs applymap in Pandas:

1. apply()

Works on a Series (one column) or a DataFrame (multiple columns).

If used on a Series, it passes each value to your function.

If used on a DataFrame, it passes an entire row or column at a time (depending on axis).

When to use:

You want to apply a function to each column as a whole or each row as a whole.

Example:

      # Apply to each column
      df.apply(sum, axis=0)  
      
      # Apply to each row
      df.apply(lambda row: row['col1'] + row['col2'], axis=1)  
      
2. applymap()

Works only on DataFrames.

Always applies the function element-wise to each cell in the DataFrame.

When to use:

You want to run a function on every single value in selected columns or the whole DataFrame.

Example:


      df.applymap(lambda x: x.strip().lower() if isinstance(x, str) else x)

Rule of thumb:

Per value → applymap()

Per row or per column → apply()

On one column only → apply() (because a Series doesn’t have applymap)

