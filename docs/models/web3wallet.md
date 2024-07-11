# Web3Wallet


## Fields

| Field                                                                                   | Type                                                                                    | Required                                                                                | Description                                                                             | Example                                                                                 |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `object`                                                                                | [models.Web3WalletObject](../models/web3walletobject.md)                                | :heavy_check_mark:                                                                      | String representing the object's type. Objects of the same type share the same value.<br/> | web3_wallet                                                                             |
| `web3_wallet`                                                                           | *str*                                                                                   | :heavy_check_mark:                                                                      | N/A                                                                                     | 0x123456789abcdef                                                                       |
| `verification`                                                                          | [Nullable[models.Web3WalletVerification]](../models/web3walletverification.md)          | :heavy_check_mark:                                                                      | N/A                                                                                     | {<br/>"status": "verified",<br/>"strategy": "web3_metamask_signature",<br/>"nonce": "nonce_value"<br/>} |
| `created_at`                                                                            | *int*                                                                                   | :heavy_check_mark:                                                                      | Unix timestamp of creation<br/>                                                         | 1609459200                                                                              |
| `updated_at`                                                                            | *int*                                                                                   | :heavy_check_mark:                                                                      | Unix timestamp of creation<br/>                                                         | 1609459200                                                                              |
| `id`                                                                                    | *Optional[str]*                                                                         | :heavy_minus_sign:                                                                      | N/A                                                                                     | wallet_id_123                                                                           |