

import re



pat = re.compile(r"[о]")

pat2 = "({})".format(re.sub(pat, "[оауяыи]", "каро"))

print(pat2)



