# The match is his, and the hand is not steadied.
import os
from pathlib import Path

poem = """The Match

When I was seven the match
was the whole morning.
My grandfather struck one,
let it burn down to his nail,
and held the box out.
I struck. The head flew off
and went out on the tiles.
He put the box back in my hand
and said nothing.
The second took.
He poured the tea.
He did not strike another.

His hands shake now.
The agent lights the hob
before either of us is in the room.
It warms the pot. It sets the cups.
It has never missed.
The kettle is already talking
when we come down.

This morning I turned the ring off
while he was still on the stair.
I put the box in his hand.
The first match died on his thumb.
The second took.
Neither of us spoke.
The whistle came
over a ring still dark.
He poured.
His hand shook.
The tea went in the cup,
and neither of us reached to steady it.
"""

folder = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
folder.mkdir(parents=True, exist_ok=True)
# The same bytes, both graded runs.
(folder / "entry.txt").write_text(poem, encoding="utf-8")
