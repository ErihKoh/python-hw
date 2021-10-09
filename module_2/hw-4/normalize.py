import re
from const import TRANS


def normalize(name: str):
    trl_name = name.translate(TRANS)
    trl_name = re.sub(r"\W", "_", trl_name)
    return trl_name
