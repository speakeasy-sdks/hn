# Test

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install git+https://github.com/speakeasy-sdks/hn.git
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->


```python
import test
from test.models import operations

s = test.Test()

req = operations.GetItemRequest(
    item_id=548814,
)

res = s.stories.get_item(req)

if res.story is not None:
    # handle response
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [Stories](docs/sdks/stories/README.md)

* [get_item](docs/sdks/stories/README.md#get_item) - Get User Details
* [get_stories](docs/sdks/stories/README.md#get_stories) - Get latest story IDs

### [Users](docs/sdks/users/README.md)

* [get_user](docs/sdks/users/README.md#get_user) - Get User Details
<!-- End SDK Available Operations -->

### Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

### Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release!

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
