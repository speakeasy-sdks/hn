# Stories

### Available Operations

* [get_item](#get_item) - Get User Details
* [get_stories](#get_stories) - Get latest story IDs

## get_item

Get User Details

### Example Usage

```python
import test
from test.models import operations

s = test.Test()

req = operations.GetItemRequest(
    item_id=715190,
)

res = s.stories.get_item(req)

if res.story is not None:
    # handle response
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [operations.GetItemRequest](../../models/operations/getitemrequest.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |


### Response

**[operations.GetItemResponse](../../models/operations/getitemresponse.md)**


## get_stories

Get latest story IDs

### Example Usage

```python
import test


s = test.Test()


res = s.stories.get_stories()

if res.get_stories_200_application_json_integers is not None:
    # handle response
```


### Response

**[operations.GetStoriesResponse](../../models/operations/getstoriesresponse.md)**

