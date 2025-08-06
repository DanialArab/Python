- Regex Pattern Explanation

        \b           # Word boundary (ensures we're matching whole words/emails)
        [\w.-]+      # One or more of: word characters (a-z, A-Z, 0-9, _), dot (.), or hyphen (-)
        @            # Literal '@' symbol
        [\w.-]+      # Again, one or more of word characters, dots, or hyphens (domain name)
        \.           # A literal dot '.'
        \w+          # One or more word characters (like com, org, net)
        \b           # Word boundary
- To solve the problem of validating a US phone number in the format (XXX) XXX-XXXX, we use a regular expression (regex) to match that exact structure.     
        
        pattern = r'^\(\d{3}\) \d{3}-\d{4}$'


        ( : literal opening parenthesis

        123 : exactly 3 digits

        ) : literal closing parenthesis

        A space

        456 : exactly 3 digits

        - : hyphen

        7890 : exactly 4 digits