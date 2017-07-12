# send-loadtests

Load tests for [Firefox Send](https://github.com/mozilla/send).

## Uploading files:

The following example will upload a local file named "./package.json" with a custom `X-File-Metadata` HTTP header. Note that the nested `id` attribute must be a [24-character hex string](https://github.com/mozilla/send/blob/52173bf6e79c35fbba7e3493fae94ebf9d53b4c0/server/server.js#L240-L242):

```sh
$ http -f POST https://send.stage.mozaws.net/upload 'X-File-Metadata:{"aad":"ff00", "id":"123456789012345678901234", "filename":"foo.txt"}' file@./package.json
```

### Output:

```
HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 110
Content-Security-Policy: default-src 'self'; connect-src 'self' https://sentry.prod.mozaws.net https://www.google-analytics.com https://ssl.google-analytics.com; img-src 'self' https://www.google-analytics.com https://ssl.google-analytics.com; script-src 'self' https://ssl.google-analytics.com; style-src 'self' https://code.cdn.mozilla.net; font-src 'self' https://code.cdn.mozilla.net; form-action 'none'; frame-ancestors 'none'; object-src 'none'
Content-Security-Policy: default-src: 'none'; report_uri /__cspreport__
Content-Type: application/json; charset=utf-8
Date: Wed, 12 Jul 2017 22:23:12 GMT
ETag: W/"6e-bvGsSQB4y3AFKQqSCwNJoamYHKY"
Public-Key-Pins: max-age=86400; pin-sha256="WoiWRyIOVNa9ihaBciRSC7XHjliYS9VwUGOIud4PB18="; pin-sha256="r/mIkG3eEpVdm+u/ko/cwxzOMo1bk4TyHIlByibiA5E="; pin-sha256="YLh1dUR9y6Kja30RrAn7JKnbQG/uEtLMkBgFF2Fuihg="; pin-sha256="sRHdihwgkaib1P1gxX8HFszlD+7/gTfNvuAybgLPNis=";
X-Content-Security-Policy: default-src 'self'; connect-src 'self' https://sentry.prod.mozaws.net https://www.google-analytics.com https://ssl.google-analytics.com; img-src 'self' https://www.google-analytics.com https://ssl.google-analytics.com; script-src 'self' https://ssl.google-analytics.com; style-src 'self' https://code.cdn.mozilla.net; font-src 'self' https://code.cdn.mozilla.net; form-action 'none'; frame-ancestors 'none'; object-src 'none'
X-Content-Type-Options: nosniff
X-DNS-Prefetch-Control: off
X-Download-Options: noopen
X-Frame-Options: SAMEORIGIN
X-WebKit-CSP: default-src 'self'; connect-src 'self' https://sentry.prod.mozaws.net https://www.google-analytics.com https://ssl.google-analytics.com; img-src 'self' https://www.google-analytics.com https://ssl.google-analytics.com; script-src 'self' https://ssl.google-analytics.com; style-src 'self' https://code.cdn.mozilla.net; font-src 'self' https://code.cdn.mozilla.net; form-action 'none'; frame-ancestors 'none'; object-src 'none'
X-XSS-Protection: 1; mode=block

{
    "delete": "f5731ecd6edd1e0237d5",
    "id": "e903b0a8f1",
    "url": "https://send.stage.mozaws.net/download/e903b0a8f1/"
}
```

## Downloading files:

If you want to **download** the freshly uploaded file, you can use the [/assets/download/:id](https://github.com/mozilla/send/blob/52173bf6e79c35fbba7e3493fae94ebf9d53b4c0/server/server.js#L109) route. For example, given the following `id` from the JSON response above, you can use the following URL (instead of the returned `url` with `/download/:id`):

```
https://send.stage.mozaws.net/assets/download/:id/
```
