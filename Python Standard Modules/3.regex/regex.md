- Regex Pattern Explanation

        \b           # Word boundary (ensures we're matching whole words/emails)
        [\w.-]+      # One or more of: word characters (a-z, A-Z, 0-9, _), dot (.), or hyphen (-)
        @            # Literal '@' symbol
        [\w.-]+      # Again, one or more of word characters, dots, or hyphens (domain name)
        \.           # A literal dot '.'
        \w+          # One or more word characters (like com, org, net)
        \b           # Word boundary
