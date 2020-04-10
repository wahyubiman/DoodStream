import requests
import re
import sys

class DoodStream:
    '''Python doodstream api wrapper from official https://doodstream.com/api
    
    all method below return dict that contain info'''
    
    base_url = "https://doodstream.com/api/"
    
    def __init__(self, api_key):
        '''init doodstream
        Args:
            api_key (str): api key from doodstream'''
        self.api_key = api_key
        
    
    def req(self, url):
        '''requests to api
        
        Args:
            url (str): api url
            
        Return:
            (dict): output dic from requests url'''
        try:
            r = requests.get(url)
            response = r.json()
            if response['msg'] == "Wrong Auth":
                sys.exit("Invalid API key, please check your API key")
            else:
                return response
        except ConnectionError as e:
            sys.exit(f"ERROR : {e}")

    def account_info(self):
        '''Get basic info of your account'''
        url = f"{self.base_url}account/info?key={self.api_key}"
        return self.req(url)
        
    def account_reports(self):
        '''Get reports of your account'''
        url = f"{self.base_url}account/stats?key={self.api_key}"
        return self.req(url)
        
    def local_upload(self, path):
        '''Upload from local storage
        
        Args:
            path (str): path to file
        '''
        url = f"{self.base_url}upload/server?key={self.api_key}"
        url_for_upload = self.req(url)['result']
        post_data = {"api_key": self.api_key}
        filename = path.split("/")[-1]
        post_files = {"file": (filename, open(path, "rb"))}
        up = requests.post(url_for_upload, data=post_data, files=post_files)
        st = re.findall(r'name="st">(.*?)</text' , str(up.text))
        fn = re.findall(r'name="fn">(.*?)</text' , str(up.text))
        if st[0] == "OK":
            return {"status": st[0], "file_id": fn[0], "file_url": f"https://doodstream.com/d/{fn[0]}"}
        else:
            raise TypeError(f"unsupported video format {filename}, please upload video with mkv, mp4, wmv, avi, mpeg4, mpegps, flv, 3gp, webm, mov, mpg & m4v format")
        
    def remote_upload(self, direct_link):
        '''Upload files using direct links
        
        Args:
            direct_link (str): direct link video for upload
        '''
        url = f"{self.base_url}upload/url?key={self.api_key}&url={direct_link}"
        return self.req(url)
        
    def file_info(self, file_id):
        '''Get basic file info
        
        Args:
            file_id (str): doodstream video file id
        '''
        url = f"{self.base_url}file/info?key={self.api_key}&file_code={file_id}"
        return self.req(url)
        
    def search_videos(self, search_keyword):
        '''Search your videos
        
        Args:
            search_keyword (str): video keyword to search
        '''
        url = f"{self.base_url}search/videos?key={self.api_key}&search_term={search_keyword}"
        return self.req(url)
        
    def rename_file(self, file_id, title):
        '''rename file
        
        Args:
            file_id (str): doodstream video file id
            title (str): new name for renamed video file'''
        url = f"https://doodstream.com/api/file/rename?key={self.api_key}&file_code={file_id}&title={title}"
        return self.req(url)
        
    def copy_video(self, file_id):
        '''Copy video to your account
        
        Args:
            file_id (str): doodstream video file id'''
        url = f"{self.base_url}file/clone?key={self.api_key}&file_code={file_id}"
        return self.req(url)
    