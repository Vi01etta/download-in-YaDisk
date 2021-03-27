import requests

TOKEN = ' '


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def _get_link(self, disk_file_path):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        params = {'path': disk_file_path, 'overwrite': 'true'}
        headers = {'Content-Type': 'application/json', 'Authorization': TOKEN}
        response = requests.get(url, headers=headers, params=params)
        return response.json()


    def upload_file_to_disk(self, disk_file_path, filename):
        href = self._get_link(disk_file_path=disk_file_path).get('href', '')
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("УРА")


if __name__ == '__main__':
    yandex_disk = YaUploader(token=TOKEN)
    print(yandex_disk.upload_file_to_disk('netology/file.txt', 'file.txt'))