def material_prompt():
    return """
Analyze the given construction image and identify:
1. Construction materials used
2. Location in structure
3. Estimated usage
4. Possible function

Return output in structured JSON format.
"""

def documentation_prompt():
    return """
Analyze the construction site image and generate:
1. Completed structural elements
2. Materials used
3. Construction methods
4. Planned next phases

Return professional documentation format.
"""

def bridge_prompt():
    return """
Analyze the bridge image and identify:
1. Beams
2. Columns
3. Trusses
4. Structural observations
5. Engineering challenges

Return detailed structured analysis.
"""
