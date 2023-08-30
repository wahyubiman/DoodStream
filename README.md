# Unofficial [DoodStream](https://doodstream.com/join/02i3l9brejix) API

---

## ![https://doodstream.com/join/02i3l9brejix](https://i.doodcdn.com/img/468x60.gif)

[![Downloads](https://static.pepy.tech/badge/doodstream)](https://pepy.tech/project/doodstream)

DoodStream is a video hosting service were you can upload videos, share & make money.

Don't have account? register [here](https://doodstream.com/join/02i3l9brejix).

### Features

- HLS Streaming
- Unlimited Storage
- Faster Encoding
- Subtitles Support
- Premium bandwidth
- [Supported host for remote upload](https://help.doodstream.com/en/article/supported-remote-hosts-1fy5vnn/)

More detail [Click Me](https://doodstream.com/api)

---

## Install

```bash
pip install doodstream
```

---

## Usage

```python
from doodstream import DoodStream

d = DoodStream("YOUR_API_KEY")

# Check doodstream account info
d.account_info()

# Check doodstream account reports
d.account_reports()

# Upload video file from local storage
d.local_upload("PATH_TO_YOUR_VIDEO")

# Upload video from direct links
d.remote_upload("DIRECT_VIDEO_LINK")

# list all available method
help(DoodStream)

# please refer to https://doodstream.com/api-docs
```

---

#### **Note : Please update to v1.x, all the v0.x are out to date**

---

## [![Donate with PayPal](https://raw.githubusercontent.com/stefan-niedermann/paypal-donate-button/master/paypal-donate-button.png)](https://www.paypal.me/wahyubiman)
