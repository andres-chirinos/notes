import requests

PACKAGE_LIST_PATH = '/api/3/action/package_list'
PACKAGE_SHOW_PATH = '/api/3/action/package_show?id={id}'

def get_package_list(baseurl, package_list_path=PACKAGE_LIST_PATH):
    url = baseurl+package_list_path
    try:
        response = requests.get(url)
        data = response.json()
    except Exception as e:
        print('An error occurred: %s' % e)
        return None
    return data["result"]

class CKAN:
    def __init__(self, baseurl):
        self.baseurl = baseurl
        self.package_list = get_package_list(baseurl)
        pass

    def __str__(self):
        return str(self.baseurl)

    def get_package_list(self):
        return self.package_list

    def get_package(self, package_id):
        return Package(self.baseurl, package_id)

class Package:
    def __init__(self, baseurl, package_id, package_show_path=PACKAGE_SHOW_PATH):
        self.baseurl = baseurl
        self.package_id = package_id
        self.package_show_path = package_show_path
        self.metadata = self.get_package_show()
        pass

    def __str__(self):
        return str(self.package_id)

    def get_package_show(self):
        url = baseurl+self.package_show_path.format(id=self.package_id)
        try:
            response = requests.get(url)
            data = response.json()
        except Exception as e:
            print('An error occurred: %s' % e)
            return None
        return data["result"]

    def get_resourses(self):
        resources = self.metadata["resources"]
        return resources

class Resource:
    def __init__(self, baseurl, resource_id):
        self.baseurl = baseurl
        self.resource_id = resource_id
        self.metadata = self.get_resource_show()
        pass

    def __str__(self):
        return str(self.resource_id)

    def get_resource_show(self):
        url = baseurl+self.resource_show_path.format(id=self.resource_id)
        try:
            response = requests.get(url)
            data = response.json()
        except Exception as e:
            print('An error occurred: %s' % e)
            return None
        return data["result"]

    def get_data(self):
        url = baseurl+self.metadata["url"]
        try:
            response = requests.get(url)
            data = response.json()
        except Exception as e:
            print('An error occurred: %s' % e)
            return None
        return data

if __name__ == '__main__':
    baseurl = 'https://datos.gob.bo'
    package_list = get_package_list(baseurl)
    id = package_list[0]
    package = Package(baseurl, id, PACKAGE_SHOW_PATH)
    print(package.get_resourses())