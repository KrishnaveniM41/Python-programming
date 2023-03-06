import pytube

url=input("Enter the vedio url: ")
path=input("Enter the path of storage: ")
pytube.YouTube(url).streams.get_highest_resolution().download(path)
print("Downloaded!!!!!!")