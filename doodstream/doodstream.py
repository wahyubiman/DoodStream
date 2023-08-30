import requests
import re
import sys
from typing import Optional


class DoodStream:
    """Python doodstream api wrapper from official https://doodstream.com/api"""

    def __init__(self, api_key: str, base_url="https://doodapi.com/api/"):
        """
        init

        Args:
            api_key (str): api key from doodstream
            base_url (str, optional): base api url. Defaults to "https://doodapi.com/api/".
        """
        self.api_key = api_key
        self.base_url = base_url

    def _req(self, url: str) -> dict:
        """requests to api

        Args:
            url (str): api url

        Return:
            (dict): output dict from requests url"""
        try:
            r = requests.get(url)
            response = r.json()
            if response["msg"] == "Wrong Auth":
                Exception("Invalid API key, please check your API key")
            else:
                return response
        except ConnectionError as e:
            Exception(e)

    def account_info(self) -> dict:
        """
        Get basic info of your account

        Returns:
            dict: response
        """
        url = f"{self.base_url}account/info?key={self.api_key}"
        return self._req(url)

    def account_reports(
        self,
        last: Optional[str] = None,
        from_date: Optional[str] = None,
        to_date: Optional[str] = None,
    ) -> dict:
        """
        Get reports of your account (default last 7 days)

        Args:
            last (Optional[str], optional): Last x days report. Defaults to None.
            from_date (Optional[str], optional): From date - YYYY-MM-DD. Defaults to None.
            to_date (Optional[str], optional): To date - YYYY-MM-DD. Defaults to None.

        Returns:
            dict: response
        """
        url = f"{self.base_url}account/stats?key={self.api_key}"
        if last != None:
            url += f"&last={last}"
        if from_date != None:
            url = f"&from_date={from_date}"
        if to_date != None:
            url = f"&to_date={to_date}"
        url = f"{self.base_url}account/stats?key={self.api_key}"
        return self._req(url)

    def dmca_list(
        self, per_page: Optional[int] = None, page: Optional[int] = None
    ) -> dict:
        """
        Get DMCA reported files list (500 results per page)

        Args:
            per_page (Optional[int]): Results per page (default 500). Defaults to None.
            page (Optional[int], optional): Pagination. Defaults to None.

        Returns:
            dict: response
        """
        url = f"{self.base_url}dmca/list?key={self.api_key}"
        if per_page != None:
            url += f"&per_page={per_page}"
        if page != None:
            url += f"&page={page}"
        return self._req(url)

    def local_upload(self, path):
        """Upload from local storage

        Args:
            path (str): path to file
        """
        url = f"{self.base_url}upload/server?key={self.api_key}"
        url_for_upload = self._req(url)["result"]
        post_data = {"api_key": self.api_key}
        filename = path.split("/")[-1]
        post_files = {"file": (filename, open(path, "rb"))}
        res = requests.post(url_for_upload, data=post_data, files=post_files).json()
        if res["msg"] == "OK":
            return res
        else:
            raise TypeError(
                f"unsupported video format {filename}, please upload video with mkv, mp4, wmv, avi, mpeg4, mpegps, flv, 3gp, webm, mov, mpg & m4v format"
            )

    def copy_video(self, file_code: str, fld_id: Optional[str] = None) -> dict:
        """
        Copy / Clone your's or other's file

        Args:
            file_code (str): File code
            fld_id (Optional[str], optional): Folder ID (to copy inside the folder). Defaults to None.

        Returns:
            dict: response
        """
        url = f"{self.base_url}file/clone?key={self.api_key}&file_code={file_id}"
        if fld_id != None:
            url += f"&fld_id={fld_id}"
        return self._req(url)

    def remote_upload(
        self,
        direct_link: str,
        fld_id: Optional[str] = None,
        new_title: Optional[str] = None,
    ) -> dict:
        """
        Upload files using direct links

        Args:
            direct_link (str): URL to upload
            fld_id (Optional[str], optional): To upload inside a folder. Defaults to None.
            new_title (Optional[str], optional): To set new title. Defaults to None.

        Returns:
            dict: response
        """
        url = f"{self.base_url}upload/url?key={self.api_key}&url={direct_link}"
        if fld_id != None:
            url += f"&fld_id={fld_id}"
        if new_title != None:
            url += f"&new_title={new_title}"
        return self._req(url)

    def remote_upload_list(self) -> dict:
        """
        Remote Upload List & Status

        Returns:
            dict: response
        """
        url = f"{self.base_url}urlupload/list?key={self.api_key}"
        return self._req(url)

    def remote_upload_status(self, file_code: str) -> dict:
        """
        Remote Upload Status

        Args:
            file_code (str): File code of the file

        Returns:
            dict: response
        """
        url = (
            f"{self.base_url}urlupload/status?key={self.api_key}&file_code={file_code}"
        )
        return self._req(url)

    def remote_upload_slots(self) -> dict:
        """
        Get total & used remote upload slots

        Returns:
            dict: response
        """
        url = f"{self.base_url}urlupload/slots?key={self.api_key}"
        return self._req(url)

    def remote_upload_action(
        self,
        restart_errors: bool,
        clear_errors: Optional[bool] = None,
        clear_all: Optional[bool] = None,
        delete_code: Optional[str] = None,
    ) -> dict:
        """
        Perform various actions on remote upload

        Args:
            restart_errors (bool): Restart all errors
            clear_errors (Optional[bool], optional): Clear all errors. Defaults to None.
            clear_all (Optional[bool], optional): Clear all. Defaults to None.
            delete_code (Optional[str], optional): Delete a transfer, pass file_code. Defaults to None.

        Returns:
            dict: response
        """
        url = f"{self.base_url}urlupload/actions?key={self.api_key}&restart_errors={restart_errors}"
        if clear_errors != None:
            url += f"&clear_errors={clear_errors}"
        if clear_all != None:
            url += f"&clear_all={clear_all}"
        if delete_code != None:
            url += f"&delete_code={delete_code}"
        return self._req(url)

    def create_folder(self, name: str, parent_id: Optional[str] = None) -> dict:
        """
        Create a folder

        Args:
            name (str): Name of the folder
            parent_id (Optional[str], optional): Parent folder ID. Defaults to None.

        Returns:
            dict: response
        """
        url = f"{self.base_url}folder/create?key={self.api_key}&name={name}"
        if parent_id != None:
            url += f"&parent_id={parent_id}"
        return self._req(url)

    def rename_folder(self, fld_id: str, name: str) -> dict:
        """
        Rename folder

        Args:
            fld_id (str): Folder ID
            name (str): New name of the folder

        Returns:
            dict: response
        """
        url = f"{self.base_url}folder/rename?key={self.api_key}&fld_id={fld_id}&name={name}"
        return self._req(url)

    def list_files(
        self,
        page: Optional[int] = None,
        per_page: Optional[int] = None,
        fld_id: Optional[str] = None,
    ) -> dict:
        """
        List all files

        Args:
            page (Optional[int], optional): Pagination. Defaults to None.
            per_page (Optional[int], optional): Max videos per page. Defaults to None.
            fld_id (Optional[str], optional): Videos inside a folder. Defaults to None.

        Returns:
            dict: response
        """
        url = f"{self.base_url}file/list?key={self.api_key}"
        if page != None:
            url += f"&page={page}"
        if per_page != None:
            url += f"&per_page={per_page}"
        if fld_id != None:
            url += f"&fld_id={fld_id}"
        return self._req(url)

    def file_status(self, file_code: str) -> dict:
        """
        Check status of your file

        Args:
            file_code (str): File code

        Returns:
            dict: response
        """
        url = f"{self.base_url}file/check?key={self.api_key}&file_code={file_code}"
        return self._req(url)

    def file_info(self, file_code):
        """
        Get file info

        Args:
            file_code (_type_): File code

        Returns:
            _type_: response
        """
        url = f"{self.base_url}file/info?key={self.api_key}&file_code={file_code}"
        return self._req(url)

    def file_image(self, file_code: str) -> dict:
        """
        Get file splash, single or thumbnail image

        Args:
            file_code (str): File code

        Returns:
            dict: response
        """
        url = f"{self.base_url}file/image?key={self.api_key}&file_code={file_code}"
        return self._req(url)

    def file_rename(self, file_code: str, title: str) -> dict:
        """
        Rename your file

        Args:
            file_code (str): File code
            title (str): New file name

        Returns:
            dict: response
        """
        url = f"{self.base_url}file/rename?key={self.api_key}&file_code={file_code}&title={title}"
        return self._req(url)

    def file_search(self, search_term: str) -> dict:
        """
        Search your files

        Args:
            search_term (str): Search term

        Returns:
            dict: response
        """
        url = (
            f"{self.base_url}search/videos?key={self.api_key}&search_term={search_term}"
        )
        return self._req(url)
