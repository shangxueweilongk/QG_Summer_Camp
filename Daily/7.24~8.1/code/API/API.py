import pandas as pd
import requests
import json

url1_qg = 'http://39.98.41.126:31130'


def register(username, password, type='individual'):
    """
    Registration function, the user enters the username and password.
    :param username:User's name(str)
    :param password:User's password(str)
    :param type:User's type(str)
    :return:None
    """
    url = url1_qg + '/users/register'
    post_dict = {'username': username, 'password': password, 'type': type}
    post_dict = json.dumps(post_dict)
    # The agreement with the server
    headers = {'Content-Type': 'application/json'}
    try:
        response = requests.post(url, data=post_dict, headers=headers)
        if response.status_code == 200:
            # status indicates whether the command is successfully executed in the backend
            response = response.json()  # Convert to json format
            if response['code'] == 1:
                print('Register successful.Your username:%s,your username:%s' % (username, password))
            else:
                print("\033[0;31;40m Register unsuccessful!\n may be your username is same as others\033[0m")
        else:
            print("\033[0;31;40m Request unsuccessful!\033[0m")
    except requests.exceptions.RequestException as e:
        print("The request send abnormally：", e)


class USER():
    def __init__(self, username, password):
        """
        Call this class to create an instantiated object,
        and enter the user's name and password to use the following functions
        """
        self.token = None
        url = url1_qg + '/users/login'
        post_dict = {'username': username, 'password': password}
        post_dict = json.dumps(post_dict)
        # The agreement with the server
        headers = {'Content-Type': 'application/json'}
        try:
            response = requests.post(url, data=post_dict, headers=headers)
            if response.status_code == 200:
                response = response.json()  # Convert to json format
                if response['code'] == 1:
                    print('Login success!')
                    # If the username and password are correct, attribute the class
                    self.username = username
                    self.password = password
                    # The user's token
                    self.token = response['data']
                else:
                    print(
                        "\033[0;31;40m Login unsuccessful!\n 1.maybe your username or password isn\'t correct\n 2.maybe this user isn\'t exist "
                        "and you can call register()function to register\033[0m")
            else:
                print("\033[0;31;40m Request unsuccessful!\033[0m")
        except requests.exceptions.RequestException as e:
            print("The request send abnormally：", e)

    def query_user_info(self):
        """
        View personal information（user's ID,user's name,user's type）
        :return:None
        """
        url = url1_qg + '/users/profile'
        post_dict = {}
        post_dict = json.dumps(post_dict)
        headers = {'Content-Type': 'application/json', 'Authorization': self.token}
        try:
            response = requests.get(url, data=post_dict, headers=headers)
            if response.status_code == 200:
                response = response.json()
                # code==1 represents success
                if response['code'] == 1:
                    data = response['data']
                    print('View personal information request succeeded!')
                    print('id       username       user_type')
                    # Read the data for each row, corresponding to the name above
                    print(data['id'], '\t    ', data['username'], '\t   ', data['type'])
                else:
                    print("\033[0;31;40m Query unsuccessful\033[0m")
            else:
                print("\033[0;31;40m Request unsuccessful!\033[0m")
        except requests.exceptions.RequestException as e:
            print("The request send abnormally：", e)

    def user_info_change(self, new_user_name=None, new_user_type=None):
        """
        Modify the user's name and user's type
        :param new_user_name:The user's new name(str)
        :param new_user_type:The user's new type(str)
        :return:None
        """
        if new_user_name is None and new_user_type is None:
            print("\033[0;31;40m The input parameter is missing!\033[0m")
            return
        if new_user_name == self.username:
            print("\033[0;31;40m The name is the same as before!\033[0m")
            return
        url = url1_qg + '/users/profile'
        post_dict = json.dumps({'username': new_user_name, 'type': new_user_type})
        headers = {'Content-Type': 'application/json', 'Authorization': self.token}
        try:
            response = requests.put(url, data=post_dict, headers=headers)
            if response.status_code == 200:
                response = response.json()
                if response['code'] == 1:
                    print("User's information changes successfully!")
                else:
                    print(
                        "\033[0;31;40m User information changes unsuccessfully .\n 1.maybe your username is the same as others.\n"
                        "2.username isn\'t allowed to be same as others\n"
                        "3.username and new_type can\'t be null \n 4.token isn\'t useful \033[0m")
            else:
                print("\033[0;31;40m Request unsuccessful!\033[0m")
        except requests.exceptions.RequestException as e:
            print("The request send abnormally：", e)

    def into_group(self, group_name, group_id=None):
        """
        Join a group
        :param group_name:The name of the group you want to join(str)
        :return:None
        """
        url = url1_qg + '/groups/join'
        post_dict = {'groupName': group_name}
        post_dict = json.dumps(post_dict)
        headers = {'Content-Type': 'application/json', 'Authorization': self.token, 'id': group_id}
        try:
            response = requests.post(url, data=post_dict, headers=headers)
            if response.status_code == 200:
                response = response.json()
                if response['code'] == 1:
                    print('you have succeed entry group %s' % group_name)
                else:
                    print("\033[0;31;40m Unsuccessful!\n 1.your group_name may be false\n 2.maybe you have already joined "
                          "this group %s\033[0m" % group_name)
            else:
                print("\033[0;31;40m Request unsuccessful!\033[0m")
        except requests.exceptions.RequestException as e:
            print("The request send abnormally：", e)

    def out_group(self, group_name, group_id=None):
        """
        Exit a group
        :param group_name:The name of the group you want to quit(str)
        :param group_id:The ID of the group you want to quit(int)
        :return:None
        """
        url = url1_qg + '/groups/quit'
        post_dict = {'groupName': group_name, 'groupId': group_id}
        post_dict = json.dumps(post_dict)
        headers = {'Authorization': self.token, 'Content-Type': 'application/json'}
        try:
            response = requests.delete(url, data=post_dict, headers=headers)
            if response.status_code == 200:
                response = response.json()
                if response['code'] == 1:
                    print('Quit %s group successful!' % group_name)
                else:
                    print("\033[0;31;40m Quit %s group unsuccessful!\n 1.maybe your group_name may be false \n"
                          " 2.maybe you haven\'t join %s group\n"
                          " 3.you are the owner of this group %s\033[0m" % (group_name, group_name, group_name))
            else:
                print("\033[0;31;40m Request unsuccessful!\033[0m")
        except requests.exceptions.RequestException as e:
            print("The request send abnormally：", e)

    def invite_connect(self, relativeUsername, group_id, group_name):
        """
        Initiates a connection request to a specified user in a specified group
        :param relativeUsername:The specified user's name(str)
        :param group_id:The specified group's ID(int)
        :param group_name:The specified group's name(str)
        :return:
        """
        url = url1_qg + '/users/apply'
        post_dict = {'groupName': group_name, 'id': group_id, 'relativeUsername': relativeUsername}
        post_dict = json.dumps(post_dict)
        headers = {'Authorization': self.token, 'Content-Type': 'application/json'}
        try:
            response = requests.put(url, data=post_dict, headers=headers)
            if response.status_code == 200:
                response = response.json()
                if response['code'] == 1:
                    print('Connecting invite have send to %s successful! please wait for confirm' % relativeUsername)
                else:
                    print("\033[0;31;40m Unsuccessful!\n 1.maybe your group_name,group_id,relative_username is wrong"
                          "\n 2.maybe you have connected with user %s so don\'t need to invite again\033[0m" % relativeUsername)
            else:
                print("\033[0;31;40m Request unsuccessful!\033[0m")
        except requests.exceptions.RequestException as e:
            print("The request send abnormally：", e)

    def agree_connect(self, group_id, applicant_name):
        """
        Agree to connection requests from other users
        :param group_id:The group's ID to which the user belongs(int)
        :param applicant_name:Name of the application user(str)
        :return:None
        """
        url = url1_qg + '/users/processApplication'
        post_dict = {'groupId': str(group_id), 'objectName': applicant_name, 'operate': '1'}
        post_dict = json.dumps(post_dict)
        headers = {'Authorization': self.token, 'Content-Type': 'application/json'}
        try:
            response = requests.post(url, data=post_dict, headers=headers)
            if response.status_code == 200:
                response = response.json()
                if response['code'] == 1:
                    print('You have succeed building connection with user \'%s\' in group \'%s\'' % (applicant_name, group_id))
                else:
                    print("\033[0;31;40m Unsuccessful!\n 1.maybe your group_id or applicant_name is wrong\033[0m")
            else:
                print("\033[0;31;40m Request unsuccessful!\033[0m")
        except requests.exceptions.RequestException as e:
            print("The request send abnormally：", e)

    def disagree_connect(self, group_id, applicant_name):
        """
        Reject requests from other users
        :param group_id: The group's ID to which the user belongs(int)
        :param applicant_name:Name of the application user(str)
        :return:None
        """
        url = url1_qg + '/users/processApplication'
        post_dict = {'groupId': str(group_id), 'objectName': applicant_name, 'operate': '2'}
        post_dict = json.dumps(post_dict)
        headers = {'Authorization': self.token, 'Content-Type': 'application/json'}
        try:
            response = requests.post(url, data=post_dict, headers=headers)
            if response.status_code == 200:
                response = response.json()
                if response['code'] == 1:
                    print('You have refused building connection with user \033[0;31;40m \'%s\' \033[0m in group \'%s\'' % (applicant_name, group_id))
                else:
                    print("\033[0;31;40m Unsuccessful!\n 1.maybe your group_id or applicant_name is wrong\033[0m")
            else:
                print("\033[0;31;40m Request unsuccessful!\033[0m")
        except requests.exceptions.RequestException as e:
            print("The request send abnormally：", e)

    def upload_file(self, filepath, group_id, noise_rank, resource_name):
        """
        Upload data,the data type for each group is different. You need to specify which group the data of this type is applicable to
        :param filepath:File path(str).Only csv files are supported
        :param group_id:The specified group's ID(int)
        :param noise_rank:Noise level.The range is greater than or equal to 0 and less than 3(int)
        :param resource_name:The name of this data(str)
        :return:None
        """
        if filepath[-3:] != "csv" and filepath[-3:] != "CSV":
            print("\033[0;31;40m Incorrect file format!\033[0m")
            return

        if noise_rank > 3 and noise_rank >= 0:
            print("\033[0;31;40m Incorrect noise_rank!\033[0m")
            return

        url = url1_qg + '/resource'
        data = pd.read_csv(filepath)
        final_list = []
        # The data is uploaded in the format of dictionary and list
        for i in data.keys():
            tmp = {i: data[i].values.tolist()}
            final_list.append(tmp)
        post_dict = {'data': final_list, 'groupId': group_id, 'noiseLevel': noise_rank, 'resourceName': resource_name}
        post_dict = json.dumps(post_dict)
        headers = {'Authorization': self.token, 'Content-Type': 'application/json'}
        try:
            response = requests.put(url, headers=headers, data=post_dict)
            if response.status_code == 200:
                response = response.json()
                if response['code'] == 1:
                    print('File upload successful!')
                else:
                    print("\033[0;31;40m File upload unsuccessful!\033[0m")
            else:
                print("\033[0;31;40m Request unsuccessful!\033[0m")
        except requests.exceptions.RequestException as e:
            print("The request send abnormally：", e)

    def calculate(self, method, group_id, resources_name, resource_weights, data):
        """
        Data operation, the user can choose to operate with a user in a group, which operation to perform, difference or mean
        :param method:You need to enter 0 or 1.0 means mean division operation, 1 means difference operation.(int)
        :param group_id:The specified group's ID(int)
        :param resources_name:The data's name(str)
        :param resource_weights:Weight of each group of data.See example file for specific format requirements(list)
        :param data:Data to be calculated.See example file for specific format requirements(list)
        :return:Two-dimensional array
        """
        url = url1_qg + '/resource/forward/operation'
        post_dict = {'algorithmId': method, 'groupId': group_id, 'resourceNames': resources_name, 'resourceWeights': resource_weights,
                     'username': self.username,'data': data}
        post_dict = json.dumps(post_dict)
        headers = {'Authorization': self.token,  'Content-Type': 'application/json'}
        try:
            response = requests.post(url, headers=headers, data=post_dict)
            if response.status_code == 200:
                response = response.json()
                if response['code'] == 1:
                    print('Calculate successful!  Your calculate result are as follow')
                    return response['data']['result_data']
                else:
                    print(
                        "\033[0;31;40m Calculate unsuccessful! \n 1.maybe you haven\'t upload the data\n 2.maybe your group_id or relative_user_name is "
                        "wrong!\033[0m")
            else:
                print("\033[0;31;40m Request unsuccessful!\033[0m")
        except requests.exceptions.RequestException as e:
            print("The request send abnormally：", e)

    def query_groups_ranking(self, page, size):
        """
        Query the ranking of a group in a specified range
        :param page:Queries the group before the page of a table in the database(int)
        :param size:Check out the top few.If you set size=3, you'll see the top 3 groups(int)
        :return:None
        """
        url = url1_qg + '/groups/{0}/{1}'.format(page, size)
        post_dict = {'currentPage': page, 'pageSize': size}
        post_dict = json.dumps(post_dict)
        headers = None
        try:
            response = requests.get(url, data=post_dict, headers=headers)
            if response.status_code == 200:
                response = response.json()
                if response['code'] == 1:
                    print('Query successful!')
                    print('Page:%s,\t  ,Size:%s' % (page, size))
                    for i in response['data']['data']:
                        print(i)
                else:
                    print("\033[0;31;40m Query unsuccessful!\n 1.page is out of index or size is out of index\033[0m")
            else:
                print("\033[0;31;40m Request unsuccessful!\033[0m")
        except requests.exceptions.RequestException as e:
            print("The request send abnormally：", e)

    def query_group_detail(self, group_name):
        """
        Query information about a specified group
        :param group_name:The specified group's name(str)
        :return:None
        """
        url = url1_qg + '/groups/detail'
        post_dict = {'groupName': group_name}
        post_dict = json.dumps(post_dict)
        headers = {'Content-Type': 'application/json'}
        try:
            response = requests.post(url, data=post_dict, headers=headers)
            if response.status_code == 200:
                response = response.json()
                if response['code'] == 1:
                    print('Query successful!')
                    print('Group %s information as follow!')
                    print(response['data'])
                else:
                    print("\033[0;31;40m Query failed!\n 1.maybe this group_name %s is wrong\033[0m" % group_name)
            else:
                print("\033[0;31;40m Request unsuccessful!\033[0m")
        except requests.exceptions.RequestException as e:
            print("The request send abnormally：", e)

    def create_group(self, group_name, data_dimension, description, resource_format=None):
        """
        Create a group
        :param group_name: The group's name(str)
        :param data_dimension: The dimension of each point in the data of this group(int)
        :param description: A description of the group(str)
        :return:None
        """
        url = url1_qg + '/groups'
        post_dict = {'groupName': group_name, 'dimension': data_dimension, 'description': description,
                     'resourceFormat': resource_format}
        post_dict = json.dumps(post_dict)
        headers = {'Authorization': self.token, 'Content-Type': 'application/json'}
        try:
            response = requests.post(url, data=post_dict, headers=headers)
            if response.status_code == 200:
                response = response.json()
                if response['code'] == 1:
                    print('Create group %s successfully!\n here is the information of your groups %s' % (
                        group_name, description))
                else:
                    print(
                        "\033[0;31;40m Create group %s unsuccessfully! \n 1.this groups have been existing\033[0m" % group_name)
            else:
                print("\033[0;31;40m Request unsuccessful!\033[0m")
        except requests.exceptions.RequestException as e:
            print("The request send abnormally：", e)

    def cancel_connect(self, relativeUsername, group_id, group_name):
        """
        Cancel the permission of the specified users of the specified group to use their own data
        :param relativeUsername:The specified user's name(str)
        :param group_id:The specified group's ID(int)
        :param group_name:The specified group's name(str)
        :return:None
        """
        url = url1_qg + '/users/apply'
        post_dict = {'groupName': group_name, 'relativeUsername': relativeUsername, 'id': group_id}
        post_dict = json.dumps(post_dict)
        headers = {'Authorization': self.token, 'Content-Type': 'application/json'}
        try:
            response = requests.delete(url, data=post_dict, headers=headers)
            if response.status_code == 200:
                response = response.json()
                if response['code'] == 1:
                    print('You have cancelled the connect between you and user %s' % relativeUsername)
                else:
                    print(
                        "\033[0;31;40m Unsuccessful! maybe your relativeUsername or group_id or group_name is wrong.\033[0m")
            else:
                print("\033[0;31;40m Request unsuccessful!\033[0m")
        except requests.exceptions.RequestException as e:
            print("\033[0;31;40m The request send abnormally：\033[0m", e)

    def query_my_groups(self):
        """
        View the groups I joined
        :return: None
        """
        url = url1_qg + '/groups'
        post_dict = {}
        post_dict = json.dumps(post_dict)
        headers = {'Authorization': self.token, 'Content-Type': 'application/json'}
        try:
            response = requests.get(url, data=post_dict, headers=headers)
            if response.status_code == 200:
                response = response.json()
                if response['code'] == 1:
                    print('Query your groups successful! your groups are as follow.')
                    for i in response['data']:
                        print(i)
                else:
                    print("\033[0;31;40m Unsuccessful! maybe you haven\'t joined any groups!\033[0m")
            else:
                print("\033[0;31;40m Request unsuccessful!\033[0m")
        except requests.exceptions.RequestException as e:
            print("\033[0;31;40m The request send abnormally：\033[0m", e)

    def change_group_info(self, group_id, new_group_name=None, new_description=None):
        """
        Example Modify the group name and description.Only the group owner is eligible
        :param group_id:The original group's ID(int)
        :param new_group_name:The original group's new name(str)
        :param new_description:The original group's new description(str)
        :return:None
        """
        if new_group_name is None and new_description is None:
            print("\033[0;31;40m The input parameter is missing!\033[0m")
            return

        url = url1_qg + '/groups'
        post_dict = {'id': group_id, 'groupName': new_group_name, 'description': new_description}
        post_dict = json.dumps(post_dict)
        headers = {'Authorization': self.token, 'Content-Type': 'application/json'}
        try:
            response = requests.put(url, data=post_dict, headers=headers)
            if response.status_code == 200:
                response = response.json()
                if response['code'] == 1:
                    print('Change group information successfully!')
                else:
                    print(
                        "\033[0;31;40m Unsuccessful!\n 1.maybe your group_id is wrong\n 2.maybe you are not the owner of this group\033[0m")
            else:
                print("\033[0;31;40m Request unsuccessful!\033[0m")
        except requests.exceptions.RequestException as e:
            print("\033[0;31;40m The request send abnormally：\033[0m", e)

    def destroy_group(self, group_name, group_id=None):
        """
        Destroy the group. Only the group owner is eligible
        :param group_name:The specified group's name(str)
        :param group_id:The specified group's ID(int)
        :return:None
        """
        url = url1_qg + '/groups'
        post_dict = {'id': group_id, 'groupName': group_name}
        post_dict = json.dumps(post_dict)
        headers = {'Authorization': self.token, 'Content-Type': 'application/json'}
        try:
            response = requests.delete(url, data=post_dict, headers=headers)
            if response.status_code == 200:
                response = response.json()
                if response['code'] == 1:
                    print('Destroy group %s successfully!' % group_name)
                else:
                    print(
                        "\033[0;31;40m Unsuccessful!\n 1.maybe your group_id is wrong\n 2.maybe you are not the owner of this group\033[0m")
            else:
                print("\033[0;31;40m Request unsuccessful!\033[0m")
        except requests.exceptions.RequestException as e:
            print("\033[0;31;40m The request send abnormally：\033[0m", e)

    def message(self, group_id):
        """
        View requests sent to me by others, who rejected me and agreed to wait for the message
        :param group_id:The specified group's ID(int)
        :return:None
        """
        url = url1_qg + '/users/readMessages'
        post_dict = {'groupId': group_id}
        post_dict = json.dumps(post_dict)
        headers = {'Authorization': self.token, 'Content-Type': 'application/json'}
        try:
            response = requests.post(url, data=post_dict, headers=headers)
            if response.status_code == 200:
                response = response.json()
                if response['code'] == 1:
                    print('Look through message successfully!')
                    data = response['data']
                    if data == None:
                        print('NO MESSAGE!')
                    for i in range(len(data)):
                        if data[i]['status'] == '0':
                            print(' \033[0;31;40m %s \033[0m  Waiting for you to deal with his invite!' % data[i]['username'])
                        elif data[i]['status'] == '1':
                            print(' \033[0;31;40m %s \033[0m  Had agreed your connection' % data[i]['username'])
                        elif data[i]['status'] == '2':
                            print(' \033[0;31;40m %s \033[0m Had rejected your connection!' % data[i]['username'])
                else:
                    print(
                        "\033[0;31;40m No message\033[0m")
            else:
                print("\033[0;31;40m Request unsuccessful!\033[0m")
        except requests.exceptions.RequestException as e:
            print("\033[0;31;40m The request send abnormally：\033[0m", e)
