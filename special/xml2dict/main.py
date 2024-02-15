import json

import xmltodict

o = xmltodict.parse(
    """
<e attr="test" another="test2">
    <as>
        <a attr="test">content</a>
        <a attr="test"><mm></mm><nn></nn></a>
        <a>text</a>
    </as>

    <nums>
        123
    </nums>
</e>
"""
)

r = json.dumps(o, indent=4)  # '{"e": {"a": ["text", "text"]}}'
print(r)
