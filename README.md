# Unofficial DoodStream API
---
![doodstream logo](https://i.doodcdn.com/img/logo-s.png)
---
Unofficial python api wrapper from [doodstream api](https://doodstream/api).
DoodStream is a video hosting service were you can upload videos, share & make money.
### Feature
- HLS Streaming
- Unlimited Storage
- Faster Encoding
- Subtitles Support
- Premium bandwidth
> Supported host for remote upload :
> - [Google Drive](https://drive.google.com)
> - Fembed.com
> - Gounlimited.to
> - Clipwatching.com
> - Vidoza.net
> - Mp4upload.com
> - Vidlox.me
> 
> Max remote upload slot : 40

More detail [Click Me](https://doodstream.com/)

---

## Install
```bash
pip install doodstream
```
---

## Usage

You can use this as python module or via terminal

### Use as python module
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

### Use via terminal
set your doodstream api key first
```bash
export DOODSTREAM_API=you_key_here
```
- Check doodstream account info
```bash
doodstream account
```

- Check doodstream account reports
```bash
doodstream reports
```

- Upload video file from local storage
```bash
doodstream upload PATH_TO_YOUR_VIDEO
```

- Upload video from direct links
```bash
doodstream remote DIRECT_VIDEO_LINK
```

- Get basic file info,
```bash
doodstream info FILE_ID
```

- Search videos in your Doodstream account
```bash
doodstream search YOUR_KEYWORD
```

- Rename video filename 
```bash
doodstream rename FILE_ID NEW_NAME
```

- Copy videos from another Doodstream user to your account
```bash
doodstream copy FILE_ID
```

> to get "FILE_ID" just remove https://doodstream.com/d/ or https://dood.watch/d/ from your video link share.
> ex : https://doodstream.com/d/FILE_ID
---