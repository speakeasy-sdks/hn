# Users
(*users*)

### Available Operations

* [get_user](#get_user) - Get User Details

## get_user

Get User Details

### Example Usage

```python
import test
from test.models import operations

s = test.Test()

req = operations.GetUserRequest(
    id=746869,
)

res = s.users.get_user(req)

if res.user is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [operations.GetUserRequest](../../models/operations/getuserrequest.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |


### Response

**[operations.GetUserResponse](../../models/operations/getuserresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
