"""doodstream cli"""
import click
import os
import sys
from doodstream import DoodStream

api = os.environ.get("DOODSTREAM_API")
d = DoodStream(api)


@click.group()
def main():
    """Doodstream free video hosting cli"""
    if api == None or len(api) == 0:
        print("Please set doodstream api key in environment variable first")
        print("$ export DOODSTREAM_API=your_key_here")
        sys.exit()


@main.command()
def account():
    """show basic account info"""
    data = d.account_info()["result"]
    print("#" * 10 + " Account Info " + "#" * 10)
    print(f"Email : {data['email']}")
    print(f"Balance : ${data['balance']}")
    print(f"Used Storage : {int(int(data['storage_used'])/1024)} MB")
    print(f"Storage Left : {data['storage_left']}")
    print(f"Premium Expire : {data['premim_expire']}")
    print("#" * 40)


@main.command()
def reports():
    """show account report"""
    report = d.account_reports()["result"]
    print("#" * 10 + " Account Reports " + "#" * 10)
    for data in report:
        print(f">>> {data['day']} <<<")
        print(f"Download : {data['downloads']}")
        print(f"View : {data['views']}")
        print(f"Profit View : ${data['profit_views']}")
        print(f"Referral : {data['refs']}")
        print(f"Profit Referral : ${data['profit_refs']}")
        print(f"Profit Total : ${data['profit_total']}")
        print("")
    print("#" * 40)


@main.command()
@click.argument("path", type=click.Path(exists=True))
def upload(path):
    """upload from local storage"""
    try:
        u = d.local_upload(path)
        print("#" * 10 + " Local Upload " + "#" * 10)
        print(f"Status : {u['status']}")
        print(f"Video ID : {u['result'][0]['filecode']}")
        print(f"Video Url : {u['result'][0]['download_url']}")
        print("#" * 40)
    except TypeError:
        print(f"Unsopported video format for {str(path).split('/')[-1]}")
        print(
            "Supported video format : mkv, mp4, wmv, avi, mpeg4, mpegps, flv, 3gp, webm, mov, mpg, m4v"
        )
        sys.exit()


@main.command()
@click.argument("direct_link")
def remote(direct_link):
    """upload from direct link"""
    if "http://" in direct_link or "https://" in direct_link:
        r = d.remote_upload(direct_link)
        print("#" * 10 + " Remote Upload " + "#" * 10)
        print(f"Status : {r['msg']}")
        print(f"File ID : {r['result']['filecode']}")
        print("")
        print(
            "Please see your doodstream remote upload dashboard for further information"
        )
        print("#" * 40)
    else:
        print("#" * 10 + " Remote Upload " + "#" * 10)
        print("\nPlease add http:// or https:// in link\n")
        print("#" * 40)


@main.command()
@click.argument("file_id")
def info(file_id):
    """show file info"""
    info = d.file_info(file_id)
    if info["status"] == 400:
        print(info["msg"])
        sys.exit()
    print("#" * 10 + " File Info " + "#" * 10)
    for i in info["result"]:
        if "Not found or not your file" in str(i["status"]):
            print("\nVideo Not found or not your file\n")
        else:
            print(f"Title : {i['title']}")
            print(f"Uploaded : {i['uploaded']}")
            print(f"Length : {i['length']}")
            print(f"View : {i['views']}")
            print(f"Last View : {i['last_view']}")
            print(f"Single Image : {i['single_img']}")
            print(f"Splash Image : {i['splash_img']}")
            print(f"Protected Download : https://dood.watch{i['protected_dl']}")
            print(f"Protected Embed : https://dood.watch{i['protected_embed']}")
            print(f"Public Url : https://dood.watch/d/{file_id}")
    print("#" * 40)


@main.command()
@click.argument("keyword")
def search(keyword):
    """search videos"""
    s = d.search_videos(keyword)
    print("#" * 10 + " Search Videos " + "#" * 10)
    if len(s["result"]) == 0:
        print("\nNot Found !!!\n")
    else:
        for result in s["result"]:
            print("-" * 40)
            print(f"Title : {result['title']}")
            print(f"Uploaded : {result['uploaded']}")
            print(f"Length : {result['length']}")
            print(f"View : {result['views']}")
            print(f"Single Image : {result['single_img']}")
            print(f"Splash Image : {result['splash_img']}")
            print(f"Public Url : https://dood.watch/d/{result['file_code']}")
    print("#" * 40)


@main.command()
@click.argument("file_id")
@click.argument("new_title")
def rename(file_id, new_title):
    """rename video title"""
    print("#" * 10 + " Rename Videos " + "#" * 10)
    r = d.rename_file(file_id, new_title)
    if r["status"] == 200:
        print("\nSuccess\n")
    elif r["status"] == 403:
        print(f"{r['msg']}")
    elif r["status"] == 400:
        print("Invalid file id")
    print("#" * 40)


@main.command()
@click.argument("file_id")
def copy(file_id):
    """copy doodstream video to your account"""
    c = d.copy_video(file_id)
    print("#" * 10 + " Copy Videos " + "#" * 10)
    if "OK" in c["msg"]:
        print("Success")
        print(f"File Id : {c['result']['filecode']}")
        print(f"Video Url : {c['result']['url']}")
    else:
        print("")
        print(c["msg"])
        print("")
    print("#" * 40)


"""
if __name__ == '__main__':
    main()
"""
