# Unofficial [DoodStream](https://doodstream.com/join/02i3l9brejix) API

---

## ![https://doodstream.com/join/02i3l9brejix](https://i.doodcdn.com/img/468x60.gif)

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

# Get basic file info
d.file_info("FILE_ID")

# Search videos in your Doodstream account
d.search_videos("YOUR_KEYWORD")

# Rename video filename
d.rename_file("FILE_ID", "NEW_NAME")

# Copy videos from another Doodstream user to your account
d.copy_video("FILE_ID")
```

---

## [![Donate with PayPal](https://raw.githubusercontent.com/stefan-niedermann/paypal-donate-button/master/paypal-donate-button.png)](https://www.paypal.me/wahyubiman)
