<!-- Start SDK Example Usage [usage] -->
```python
import test
from test.models import operations

s = test.Test()

req = operations.GetItemRequest(
    item_id=454948,
)

res = s.stories.get_item(req)

if res.story is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage [usage] -->